from distutils.core import setup

setup(
    name = "PocketWhale",
    url = "https://github.com/Glinek/PocketWhale",
    packages = ["Startup software"],
    install_requires = [
        "textual",
        "pyfiglet",
        "rich",
        "geocoder",
        "datetime",
        "distro", 
        "os", 
        "platform", 
        "socket", 
        "random", 
        "requests",
        "subprocess",
        "shutil"
    ],
    entry_points = {
        "console_scripts": [
            "ecofetch = cd ~/Pocketwhale/ python PW.py",
        ],
    }
)