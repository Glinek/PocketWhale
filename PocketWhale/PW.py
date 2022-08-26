import distro, os, platform, socket, random, requests, subprocess, shutil
from textual.app import App
from textual.widgets import *
from pyfiglet import Figlet
from rich.panel import Panel
from textual.widget import Widget
from datetime import datetime
from rich.style import Style
from rich.align import Align
#city
with open('City.txt', 'w') as f:
    f.write("katowice")
f = open('City.txt', 'r')
content = f.read()
#list of random words 
WORDS = ("Have a nice day", "Always be creative", "100% not orginal", 
"This code is a mess", "MINECRAFT <3",  "Miau", "Started in: was never tested",
"Cyberdeck.cafe", "test 01", "tested on Kali linux", "Everything is wrong", 
"Don't trust me", "Safe to use on plane", "?", "hi", "Servus!", "Tiger my friend", "Siemka", "hola",
"Why by Sabrina Carpenter", "made within 24h", "made by Glinek", "Mikołów", "Your data is not safe")
word = random.choice(WORDS)
#disk storage
total, used, free = shutil.disk_usage(__file__)
ff = round(free /1024 /1024 /1024)
tt = round(total /1024 /1024 /1024)
uu = round(used /1024 /1024 /1024)
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
        return Panel(content, style="white", border_style=Style(color="cyan"))
#info on left side
class Arc(Widget):
    Title="Test"
    def render(self):  
        a = " Basic info:\n "
        a += f"Architecture: {platform.architecture()[0]}\n OS: {platform.system()}\n Distribution: {distro.name()}\n" 
        a += f" User: {os.getlogin()}\n IP: {socket.gethostbyname(socket.gethostname())} \n Started in: {t}\n\n"
        a += f" Disk space:\n Used: {uu} GB\n Free: {ff} GB\n\n"
        a += f" Weather forecast for: {content}\n"
        url = 'https://wttr.in/{}?format= Weather: %C\n+Temperatue: %t\n+Wind: %w\n+Precipitation: %p\n+Pressure: %P\n+Time_zone: %Z'.format(content)
        res = requests.get(url)
        a += f"{res.text}"        
        return Panel(a, title="Info", style="white", border_style=Style(color="cyan"))         
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
        a += f"PocketWhale program was made to give u most important info on startup\n"
        a += f"To change place for which weather is displaying run city.py\n"
        a += f"Precipitation is in mm/3 hours\n\n" 
        a += f"press E to EXIT\n\n\033[1;33;40m{word}"
        return Panel(a, style="white", border_style=Style(color="cyan"))
#main app 
class Pocketwhale(App):
    def __init__(
        self,
        screen: bool = True,
        driver_class = None,
        log: str = "",
        log_verbosity: int = 1,
        title: str = "Glinek",
    ):
        super().__init__(screen, driver_class, log, log_verbosity, title)
        self.small = False
    async def on_mount(self):
        await self.view.dock(Arc(self.small), edge="left", size=40)
        await self.view.dock(Clock(self.small), edge="top", size=1)
        await self.view.dock(Menu(self.small), edge="top", size=8)
        await self.view.dock(Main(self.small), edge="top")
    async def on_key(self, event):
        for item in Menu.menuEntries.values():
            if item["key"] == event.key:
                if item["action"].handler == "textual":
                    await self.action(item["action"].execString)
                if item["action"].handler == "system":
                    proc = subprocess.Popen(item["action"].execString.split(" "))
                    proc.wait()
                    self.refresh()
#idfk            
if __name__ == "__main__":
    Pocketwhale().run(title="GLINEK")
