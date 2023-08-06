"""Ein Modul, das die Eingabe-Ausgabe-Module für den Raspberry Pi
netzwerkfähig macht.

Der Server kann mit folgenden Zeilen einfach erstellt werden:

>>> from eapi.net import EAModulServer
>>> easerver = EAModulServer("localhost", 9999)

Anschließend wird er mit einem Aufruf gestartet.

  easerver.serve_forever()

Ebenso kann der Server über die Kommandozeile mit dem folgenden Befehl
gestartet werden.

  $ python3 -m eapi.net startserver

Nun wartet der Server auf dem Port 9999 auf UDP-Pakete. Ein an den Server
gesendeter Request besteht aus genau drei Bytes - für jede LED ein Byte: erst
rot, dann gelb zuletzt grün. Der Wert des Bytes gibt in Prozent (0-100) die
Helligkeit der LED an. Werte außerhalb dieses Bereiches werden ignoriert.

Mit Netcat und echo können drei Bytes einfach an einen Testserver wie folgt
gesendet werden:

  $ echo -en '\\x02\\x64\\x00' | nc -4u localhost 9999

Hex 2 (\\x02) entspricht dem Hexwert 2. Mit der Option -e wird eine
Escapesequenz verschickt, die Option -n besagt, dass kein Zeilenumbruch
gesendet werden soll - also nur die angegebenen Bytes. Die Option -4 von nc
sendet ein IPv4-Paket, das als UDP-Paket (-u) verschickt werden soll.

Das Modul enthält auch einen einfachen Konsolenclient, der über die Konsole
gestartet werden kann:

  $ python3 -m eapi.net startclient

"""

import socket
import socketserver
from eapi.hw import EAModul


class EAModulUDPHandler(socketserver.BaseRequestHandler):
    """Ein Handler für UDP requests an den EAModulServer."""

    # eamodul als Klassenattribut, da für jeden Request auf den Server
    # eine neue Handlerinstanz erzeugt wird.
    eamodul = None

    def handle(self):
        """Der UDP-Handler bearbeitet UDP-Requests gemäß der Modulbeschreibung 
        (s.o.)."""

        # statisches Modul initaisieren, falls noch nicht geschehen
        if EAModulUDPHandler.eamodul is None:
            EAModulUDPHandler.eamodul = EAModul()

        # Der Request besteht aus einem Tupel aus Daten und Socket des
        # Senders. Wir greifen die Daten heraus.
        data = self.request[0]

        # Erwarte mindestens drei Bytes im Request
        # Für jede LED ein Byte (rot, gelb, grün)
        if len(data) < 3:
            return

        if 0 <= data[0] <= 100:
            EAModulUDPHandler.eamodul.schalte_led(EAModul.LED_ROT, data[0]/100)
        if 0 <= data[1] <= 100:
            EAModulUDPHandler.eamodul.schalte_led(EAModul.LED_GELB, data[1]/100)
        if 0 <= data[2] <= 100:
            EAModulUDPHandler.eamodul.schalte_led(EAModul.LED_GRUEN, data[2]/100)


class EAModulServer(socketserver.UDPServer):
    """Ein UDPServer für ein EA-Modul.

    Ein an den Server gesendeter Request wird vom EAModulUDPHandler
    verarbeitet.
    """

    def __init__(self, host, port, eamodul=None):
        """Starte einen Server auf dem angegebnen hostname, oder IP-Adresse - 
        lokale Server können hier auch 'localhost' als Name verwenden.

        Über den Parameter eamodul kann ein EAModul übergeben werden. Wird
        kein Modul übergeben, wird ein Standardmodul selbst erstellt.
        """

        super().__init__((host,port), EAModulUDPHandler)

        if eamodul:
            EAModulUDPHandler.eamodul = eamodul


class EAModulClient:
    """Client, um auf den EAModulServer zuzugreifen.

    Der Client kann mit der Angabe eines Hostnamens oder einer IP-Adresse
    gestartet werden.

    >>> from eapi.net import EAModulClient
    >>> client = EAModulClient('localhost', 9999)

    Nun kann er über mit dem Server kommunizieren und die dortigen LEDs
    ansteuern.

    >>> client.sende(100, 0, 100)
    >>> client.sende(50, 0, 30)
    """

    def __init__(self, servername, serverport):
        """Starte den Client für einen laufenden Server.

        Der angegebene servername ist eine IP-Adresse oder ein Domainname -
        für ein lokal laufenden Server kann auch localhost verwendet
        werden. Mit serverport wird die Portnummer angegeben, über die der
        Server ansprechbar ist.
        """
        self.servername = servername
        self.serverport = serverport
        self.client = socket.socket(socket.AF_INET,  # Address Family Internet
                                    socket.SOCK_DGRAM)  # UDP

    def sende(self, rot, gelb, gruen):
        """Sende an den Server die Information, welche LEDs an- bzw. 
        ausgeschaltet werden sollen.

        Die Werte für rot, gelb und grün müssen zwischen 0 und 100 liegen.
        """

        # Standardwerte auf 255 festelgen -> werden ignoriert.
        data = [255, 255, 255]
        if 0 <= rot <= 100:
            data[0] = rot
        if 0 <= gelb <= 100:
            data[1] = gelb
        if 0 <= gruen <= 100:
            data[2] = gruen

        self.client.sendto(bytes(data), (self.servername, self.serverport))


# Main
#
if __name__ == "__main__":
    import sys

    if len(sys.argv) >= 2:
        __hostname = input("Hostname (Enter für localhost):")
        if __hostname == '':
            __hostname = 'localhost'
        __port = input("Port (Enter für 9999):")
        if __port == '':
            __port = '9999'

        if sys.argv[1] == "startserver":
            print("Starte Server auf", __hostname, "auf Port", __port)
            __easerver = EAModulServer(__hostname, int(__port))
            __easerver.serve_forever()

        elif sys.argv[1] == "startclient":
            print("Starte Client")
            __client = EAModulClient(__hostname, int(__port))

            print("""
            Welche LEDs sollen angeschaltet werden? Gib drei Werte zwischen 
            0 und 100 ein (getrennt durch Leerzeichen: erst rot, dann gelb, 
            dann grün)
            Beispiel: 65 100 0 schaltet gelb an, grün aus, rot leuchtet mit 
            halber Helligkeit.
            'q' beendet das Programm""")

            while True:
                __eingabe = input()                    
                if __eingabe == 'q':
                    exit(0)
                try:
                    __seingabe = __eingabe.split(' ')
                    __rot = int(__seingabe[0])
                    __gelb = int(__seingabe[1])
                    __gruen = int(__seingabe[2])
                    __client.sende(__rot, __gelb, __gruen)

                except IndexError:
                    print("Eingabe fehlerhaft. Erwarte genau drei Zahlen zwischen 0 und 100.")
                    print("Bitte wiederholen!")
                    
    else:
        print("Befehl angeben: startserver oder startclient")
