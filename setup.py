from distutils.core import setup

setup(
    name = "PocketWhale",
    url = "https://github.com/Glinek/PocketWhale",
    packages = ["PocketWhale"],
    install_requires = [
        "textual",
        "pyfiglet",
        "rich",
        "geocoder",
        "datetime",
        "distro", 
        "requests"   
    ],
    entry_points = {
        "console_scripts": [
            "PW = PocketWhale.PW:pw",
        ],
    }
)
