from src.app   		import Application
from src.menu  		import Menu
from src.clock 		import Clock
from src.torch 		import Torch
from src.weather	import Weather
from src.settings 	import Settings
from PIL   			import Image
import time
import threading

class Main(threading.Thread):
    def __init__(self, adress, port, username):
        self.adress = adress
        self.port = port
        self.username = username
        threading.Thread.__init__(self)
    
    def run(self):
        app=Application(self.adress, self.port, self.username)
        app.getPinConfig("src/config/pinout.json")
        app.getConfig("src/config/config.json")
        pic=Image.open('src/images/pic.png')
        app.setImg(pic)
        app.sendImg()
        time.sleep(4)
        app.newImg()
        app.setText((10,0),"GBROS", 255,app.getFonts()[1])
        app.setText((32,32),"V 0.1", 255,app.getFonts()[1])
        app.sendImg()
        time.sleep(2)
        applications=[["CLOCK", Clock(app)],["TORCH", Torch(app)],["WEATHER", Weather(app)],["SETTINGS",Settings(app)]]
        menu=Menu(app, applications)
        applications[0][1].run(menu)


Main("0.0.0.0",1234,"gaber").run()

