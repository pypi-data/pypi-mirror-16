"""Ein Modul für die Verwendung des Eingabe-Ausgabe-Moduls für den Raspberry
Pi.

Es besteht aus der Hauptklasse EAModul, die für die Ansteuerung vorgesehen
ist. Hierfür existieren verschiedene Demos, die von der Kommandozeile aus
aufgerufen werden können:

  $ python3 -m eapi.hw

Mit Hilfe der Klasse DimmbaresEAModul können die LEDs auf dem Board gedimmt
werden.
"""


# Versuche, die Bibliothek für GPIO-Pins zu laden. Wenn dies scheitert, wird 
# ein Dummy verwendet.
try:
    import RPi.GPIO as GPIO
except ImportError:
    import eapi.GPIODummy as GPIO


class EAModul:
    """Die Klasse EAModul hilft bei der Ansteuerung eines Eingabe-Ausgabe-Moduls
    für den Raspberry Pi. Es besteht aus drei LED und zwei Tastern."""

    LED_ROT = 0
    LED_GELB = 1
    LED_GRUEN = 2

    def __init__(self, pin_taster0=29, pin_taster1=31,
                 pin_led_rot=33, pin_led_gelb=35, pin_led_gruen=37):
        """
        Die PINs des Moduls werden konfiguriert.

        Pins der LED werden als Ausgänge, und Pins der Taster als Eingänge
        konfiguriert. Wenn keine PINS angegeben werden, werden die PINs
        oberhalb des GND Pins links unten verwendet.

        >>> from eapi.hw import EAModul

        >>> ea = EAModul()
        >>> ea.cleanup()
        """
        GPIO.setmode(GPIO.BOARD)

        self._taster = [pin_taster0, pin_taster1]
        GPIO.setup(self._taster, GPIO.IN)

        self._leds = [pin_led_rot, pin_led_gelb, pin_led_gruen]
        GPIO.setup(self._leds, GPIO.OUT)

    def taster_gedrueckt(self, num=0):
        """
        Liest den Wert des Tasters mit der gegebenen Nummer aus und gibt den
        Wert zurück. Eine einfache Verwendung könnte wie folgt aussehen:

        >>> from eapi.hw import EAModul
        >>> import time

        >>> ea_modul = EAModul()
        >>> while not ea_modul.taster_gedrueckt(1):
        ...   ea_modul.schalte_led(EAModul.LED_ROT, 1)
        ...   time.sleep(0.2)
        ...   ea_modul.schalte_led(EAModul.LED_ROT, 0)
        >>> ea_modul.cleanup()
        """
        if 0 <= num < len(self._taster):
            if GPIO.input(self._taster[num]):
                return True
            else:
                return False
        else:
            raise ValueError(
                "Falsche Tasternummer. Muss zwischen 0 und {ln} liegen.".format(
                    ln=len(self._taster) - 1))

    def schalte_led(self, led_farbe, an_aus):
        """Schalte die LED mit der gegebenen Nummer ein (1) oder aus (0).

        Der Wert für led_farbe ist LED_ROT, LED_GELB oder LED_GRUEN.

        Eine einfache Verwendung könnte wie folgt aussehen:

        >>> from eapi.hw import EAModul

        >>> ea_modul = EAModul()
        >>> ea_modul.schalte_led(EAModul.LED_ROT, 1)
        >>> ea_modul.schalte_led(EAModul.LED_GELB, 0)
        >>> ea_modul.schalte_led(EAModul.LED_GRUEN, 1)
        >>> ea_modul.cleanup()
        """

        if 0 <= led_farbe < len(self._leds):
            if an_aus == 1 or an_aus == 0:
                GPIO.output(self._leds[led_farbe], an_aus)
            else:
                raise ValueError("Wert für an_aus muss 0 oder 1 sein.")
        else:
            raise ValueError("Falsche LED-Farbe.")

    def taster_event_registrieren(self, taster_nr, methode):
        """Registriere eine Methode, die bei Betätigung ausgeführt wird.

        Die übergebene Methode muss ein Argument haben und wird mit der
        Pin-Nur des Tasters aufgerufen, sobald der Taster gedrückt oder
        losgelassen wird. Eine einfache Verwendung könnte wie folgt aussehen:

        >>> from eapi.hw import EAModul

        >>> def taster0_gedrueckt(pin):
        ...  print("Taster 0 wurde gedrückt.")

        >>> ea_modul = EAModul()
        >>> ea_modul.taster_event_registrieren(0, taster0_gedrueckt)
        >>> ea_modul.cleanup()
        """
        if taster_nr < 0 or taster_nr >= len(self._taster):
            raise ValueError("Falsche Taster Nummer." + taster_nr)

        GPIO.add_event_detect(self._taster[taster_nr], GPIO.BOTH)
        GPIO.add_event_callback(self._taster[taster_nr], methode)

    def cleanup(self):
        """Setzt alle Pins des Pi wieder in den Ausgangszustand.

        >>> from eapi.hw import EAModul
        >>> ea = EAModul()
        >>> ea.cleanup()
        """
        GPIO.cleanup()


class DimmbaresEAModul(EAModul):
    """Ein Erweiterung der Klasse EAModul, die dimmbare LEDs unterstüzt.

    Im Unterschied zum EAModul können über die Klasse DimmbaresEAModul die LEDs
    mit Hilfe von PWM in der Helligkeit reguliert werden. Hierbei wurde die
    Methode schalte_led so angepasst, dass sie nun auch Werte zwischen 0.0 und
    1.0 annehmen kann.

    >>> from eapi.hw import DimmbaresEAModul
    >>> ea = DimmbaresEAModul()
    >>> ea.schalte_led(EAModul.LED_ROT, 0.5)
    >>> ea.schalte_led(EAModul.LED_GELB, 0.8)
    >>> ea.schalte_led(EAModul.LED_GRUEN, 0.2)
    """

    def __init__(self, pin_taster0=29, pin_taster1=31,
                 pin_led_rot=33, pin_led_gelb=35, pin_led_gruen=37):
        """
        Die PINs des Moduls werden konfiguriert.

        Pins der LED werden als Ausgänge, und Pins der Taster als Eingänge
        konfiguriert. Wenn keine PINS angegeben werden, werden die PINs
        oberhalb des GND Pins links unten verwendet.

        >>> from eapi.hw import DimmbaresEAModul

        >>> ea = DimmbaresEAModul()
        >>> ea.cleanup()
        """
        super().__init__(pin_taster0, pin_taster1,
                         pin_led_rot, pin_led_gelb, pin_led_gruen)

        # Für jede LED wird ein PWM bereitgestellt, ueber den die LED
        # gedimmt werden kann
        self.__pwms = [
            GPIO.PWM(pin_led_rot, 50),
            GPIO.PWM(pin_led_gelb, 50),
            GPIO.PWM(pin_led_gruen, 50)
            ]
        for pwm in self.__pwms:
            pwm.start(0)

    def schalte_led(self, led_farbe, helligkeit):
        """Schalte die LED mit der gegebenen Nummer ein (1) oder aus (0).

        Der Wert für led_farbe ist LED_ROT, LED_GELB oder LED_GRUEN.

        Wenn für helligkeit eine Kommazahl zwischen 0 und 1 angegeben
        wird, lässt sich die LED dimmen: ein Wert von 0.5 lässt die
        LED nur mit halber Kraft leuchten.

        Eine einfache Verwendung könnte wie folgt aussehen:

        >>> from eapi.hw import DimmbaresEAModul

        >>> ea_modul = DimmbaresEAModul()
        >>> ea_modul.schalte_led(EAModul.LED_ROT, 1)
        >>> ea_modul.schalte_led(EAModul.LED_GELB, 0)
        >>> ea_modul.schalte_led(EAModul.LED_GRUEN, 0.5)
        >>> ea_modul.cleanup()
        """

        if 0 <= led_farbe < len(self._leds):
            if 0 <= helligkeit <= 1:
                # LED dimmen
                pwm = self.__pwms[led_farbe]
                pwm.ChangeDutyCycle(helligkeit*100)

            else:
                raise ValueError("Wert für Helligkeit muss zwischen 0 und 1 liegen.")
        else:
            raise ValueError("Falsche LED-Farbe.")


def demo_led_taster():
    """
    Ein einfaches Demoprogramm, um die LED und Taster auf dem Board zu prüfen.
    """
    import time

    input(
        """
        Die rote und grüne LED blinken abwechselnd. Gleichzeitig kann über
        den einen Taster die gelbe LED an- und ausgeschaltet werden. Der
        andere Taster beendet das Programm, wenn er länger gedrückt wird.
        (Enter)
        """)

    ea_modul = EAModul()

    def __taster0_gedrueckt(pin):
        global ea_modul
        ea_modul.schalte_led(EAModul.LED_GELB, ea_modul.taster_gedrueckt(0))

    ea_modul.taster_event_registrieren(0, __taster0_gedrueckt)

    try:
        while not ea_modul.taster_gedrueckt(1):
            ea_modul.schalte_led(EAModul.LED_ROT, 1)
            time.sleep(0.2)
            ea_modul.schalte_led(EAModul.LED_ROT, 0)
            time.sleep(0.2)

            ea_modul.schalte_led(EAModul.LED_GRUEN, 1)
            time.sleep(0.5)
            ea_modul.schalte_led(EAModul.LED_GRUEN, 0)
            time.sleep(0.2)

    except KeyboardInterrupt:
        ea_modul.cleanup()
    finally:
        ea_modul.cleanup()


def demo_dimmen():
    """Demoprogramm, um die Dimmen-Funktionalität zu prüfen."""

    import time

    input(
        "Alle LEDs werden 0.0 auf 1.0 gedimmt und dann von 1.0 auf 0.0 (Enter)")
    dim_ea_modul = DimmbaresEAModul()
    for i in range(100):
        dim_ea_modul.schalte_led(EAModul.LED_ROT, i / 100)
        dim_ea_modul.schalte_led(EAModul.LED_GELB, i / 100)
        dim_ea_modul.schalte_led(EAModul.LED_GRUEN, i / 100)
        time.sleep(0.05)
    for i in range(100):
        dim_ea_modul.schalte_led(EAModul.LED_ROT, 1 - i / 100)
        dim_ea_modul.schalte_led(EAModul.LED_GELB, 1 - i / 100)
        dim_ea_modul.schalte_led(EAModul.LED_GRUEN, 1 - i / 100)
        time.sleep(0.05)

    dim_ea_modul.cleanup()


def main():
    """Hauptprogramm, das beim Starten des Moduls ausgeführt wird."""
    __command = input("Befehl angeben: demo_led_taster demo_dimmen: ")
    if __command == "demo_dimmen":
        demo_dimmen()

    elif __command == "demo_led_taster":
        demo_led_taster()


if __name__ == "__main__":
    main()
