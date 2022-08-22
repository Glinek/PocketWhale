from textual.app import App
from textual.widgets import *
import os
import subprocess
from main_menu import Menu, Arc, Clock, Main, Word

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
        await self.view.dock(Main(self.small), edge="top", size=os.get_terminal_size().lines-12)
        await self.view.dock(Word("input field"), edge="bottom", size=2)

    async def on_key(self, event):
        for item in Menu.menuEntries.values():
            if item["key"] == event.key:
                if item["action"].handler == "textual":
                    await self.action(item["action"].execString)
                if item["action"].handler == "system":
                    proc = subprocess.Popen(item["action"].execString.split(" "))
                    proc.wait()
                    self.refresh()
            
if __name__ == "__main__":
    Pocketwhale().run(title="GLINEK")
