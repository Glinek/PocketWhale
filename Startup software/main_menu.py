from pyfiglet import Figlet
from rich.panel import Panel
from textual.widget import Widget
from datetime import datetime
from rich.style import Style
from rich.align import Align
import distro
import geocoder
import os
import platform
import socket
import random
import requests
#list of random words 
WORDS = ("Have a nice day", "Always be creative", "100% not orginal", 
"This code is a mess", "MINECRAFT <3",  "Miau", "Started in: was never tested",
"Cyberdeck.cafe", "test 01", "tested on Kali linux", "Everything is wrong", 
"Don't trust me", "Safe to use on plane", "?"
)
word = random.choice(WORDS)
#location from ip adress
g = geocoder.ip('me')
#time
t = os.popen('uptime -p').read()[:-1]
#i have no idea
class Action():
    def __init__(self, handler: str, execString: str):
        self.handler = handler
        self.execString = execString
#main menu
class Menu(Widget):
    menuEntries: dict[str, dict[str, Action]] = {
        "": {"key": "e", "text": "", "action": Action("textual", "quit")}
    }
    def __init__(self, small: bool = False):

        super().__init__()
        self.small = small
    def render(self):
        if self.small:
            font_title = Figlet(font="smslant")
        else:
            font_title = Figlet(font="slant")
        content = font_title.renderText("PocketWhale")
        return Panel(
            content, 
            style="white",
            border_style=Style(color="cyan")
            )
#info on left side
class Arc(Widget):
    Title="Test"
    def render(self):  
        a = "\n Archietcture: "
        a += f"{platform.architecture()[0]}\n" 
        a += f" OS: {platform.system()}\n"
        a += f" Distribution: {distro.name()}\n" 
        a += f" User: {os.getlogin()}\n"
        a += f" IP: {socket.gethostbyname(socket.gethostname())} \n"
        a += f" Started in: {t}\n\n\n"
        a += f" Weather in: {g.city}\n"
        url = 'https://wttr.in/{}?format=_Weather:%C\n+Temperatue:%t\n+Wind:%w\n+Precipitation:%p\n+Pressure:%P\n+Time_zone:%Z'.format(g.city)
        res = requests.get(url)
        a += f"{res.text}"        
        return Panel(
        a, 
        title="Info",
        style="white", 
        border_style=Style(color="cyan")
        )         
#clock
class Clock(Widget):
    def on_mount(self):
        self.set_interval(1, self.refresh)
    def render(self):
        time = datetime.now().strftime("%c")
        return Align.center(time, vertical="middle", style="cyan")
#Main info + weather
class Main(Widget):
    def render(self):
        a = f"Hi {os.getlogin()}\n\n"
        a += f"PocketWhale program was made to give u most important info on startup\n\n"
        a += f"Localization is taken from ip adress, precipitation is in mm/3 hours\n\n"
        a += f"press E to EXIT"
        return Panel(
            a, 
            style="white",
            border_style=Style(color="cyan")
            )
#random 
class Word(Widget):
    def render(self):
        a = f"{word}"  
        return Align.center(a,  
            style="bold white"
            )