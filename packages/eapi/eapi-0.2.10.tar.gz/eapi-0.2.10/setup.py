import setuptools


# gemäß der Beschreibung von
# https://packaging.python.org/distributing/
# Weitere Hinweise stehen in dem Buch "Expert Python Programming" in 
# Kapitel 5.
#
setuptools.setup(
    name="eapi",
    url="https://github.com/pintman/ea_rpi_modul",
    version="0.2.10",
    description="Modul zur Ansteuerung eines EA-Moduls fuer den Raspberry Pi.",
    long_description="Ein Modul zu Ansteuerung eines Eingabe-Ausgabe-Moduls fuer den Raspberry. Fuer die Ausgabe dienen LEDs und fuer die Eingabe Taster. Es kommt im Bildungsbereich zum Einsatz.",
    author="Marco Bakera",
    author_email="pintman@bakera.de",
    packages=setuptools.find_packages(),
    classifiers=[ # gemäß https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Natural Language :: German",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Education",
        "Topic :: System :: Hardware",
    ])


# Ein Release kann wie folgt erstellt werden
# python3 setup.py sdist

# Mit dem folgenden Befehl kann ein neues Release veröffentlicht werden
# python3 setup.py sdist upload

# Damit der Upload klappt, muss eine Datei ~/.pypirc mit Zugangsdaten für ein
# Account bei PyPi vorhanden sein. Der Inhalt der Datei könnte wie folgt aussehen:
#
#[distutils]
#index-servers=pypi
#
#[pypi]
#repository = https://upload.pypi.io/legacy/
#username = mein_username
#password = mein_passwort

