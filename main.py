import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.graphics import Color, Line
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import NumericProperty, ObjectProperty
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy_deps import sdl2, glew
import json, time, glob, random
import datetime as dt
from math import cos, sin, pi
from pathlib import Path
Window.size = (400, 500)
Window.clearcolor = (0.502, 0.502, 0.502, 1)

Builder.load_file("main.kv")

class OpeningScreen(Screen):
    def calculator(self):
        self.manager.transition.direction = "left"
        self.manager.current = "calculator_screen"
    
    def clock(self):
        self.manager.transition.direction = "left"
        self.manager.current = "clock_screen"

    def converter(self):
        self.manager.transition.direction = "left"
        self.manager.current = "converter_screen"

    def journal(self):
        self.manager.transition.direction = "left"
        self.manager.current = "journal_screen" 

class CalculatorScreen(Screen):
    def back(self):
        self.manager.transition.direction = "right"
        self.manager.current = "opening_screen"
    
    def reverse(self, s):
        try:   
            return str(-float(s))
        except ValueError:
            return "Error"

    def percent(self, s):
        try:   
            return str(float(s)/100)
        except ValueError:
            return "Error"

    def calculate(self, s):
        if s: 
            try: 
                return str(eval(s)) 
            except Exception: 
                return "Error"
        
class ClockUpdate(Label):
    pass

class ClockLabel(Label):
    def __init__(self, **kwargs):
        super(ClockLabel, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1)

    def update(self, *args):
        self.text = str(time.asctime())

class ClockScreen(Screen):
    def back(self):
        self.manager.transition.direction = "right"
        self.manager.current = "opening_screen"

"""
create a test.py to add a running clock-face above the digital clock
class Ticks(Widget):
    def __init__(self, **kwargs):
        super(Ticks, self).__init__(**kwargs)
        self.bind(pos = self.update_clock)
        self.bind(size = self.update_clock)
        Clock.schedule_interval(self.update_clock, 1)
        self.update_clock()

    def update_clock(self, *args):
        self.canvas.clear()
        with self.canvas:
            curtime = dt.datetime.now()
            Color(0.2, 0.5, 0.2)
            Line(points=[self.center_x, self.center_y, 
                            self.center_x+0.8*self.r*sin(pi/30*curtime.second), 
                            self.center_y+0.8*self.r*cos(pi/30*curtime.second)], 
                            width=1, cap="round")
            Color(0.3, 0.6, 0.3)
            Line(points=[self.center_x, self.center_y, 
                            self.center_x+0.7*self.r*sin(pi/30*curtime.minute), 
                            self.center_y+0.7*self.r*cos(pi/30*curtime.minute)], 
                            width=2, cap="round")
            Color(0.4, 0.7, 0.4)
            curhour = curtime.hour*60 + curtime.minute
            Line(points=[self.center_x, self.center_y, 
                            self.center_x+0.5*self.r*sin(pi/360*curhour), 
                            self.center_y+0.5*self.r*cos(pi/360*curhour)], 
                            width=3, cap="round")
"""

class ConverterScreen(Screen):
    def __init__(self, *args, **kwargs):
        super(ConverterScreen, self).__init__(*args, **kwargs)

    def back(self):
        self.manager.transition.direction = "right"
        self.manager.current = "opening_screen"

    def type_release_clicked(self):
        self.ids.unitType.text = "Metric Type:"
        self.dropdown = DropDown()
        convert_type = ['Temperature', 'Length', 'Mass', 'Volume']
        for item in convert_type:
            btn = Button(text = item, size_hint_y=None, height=20)
            btn.bind(on_release = lambda btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)
            self.ids.unitType.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.ids.unitType, 'text', x))
        return
    
    def unit1_release_clicked(self, type):
        self.ids.unit1.text = "Unit 1:"
        self.dropdown = DropDown()
        if type == "Temperature":
            unit_list = ["Celcius", "Fahrenheit", "Kelvin"]
        elif type == "Length":
            unit_list = ["Miles", "Meters", "Kilometers", "Feet", "Inches", "Yards"]
        elif type == "Mass":
            unit_list = ["Grams", "Kilograms", "Pounds", "Ounces", "Tons"]
        elif type == "Volume":
            unit_list = ["Liters", "Milliliters", "Fluid ounces", "Cups", "Pints", "Quarts", "Tablespoons", "Teaspoons"]
        else:  
            unit_list = []
        for item in unit_list:
            btn = Button(text = item, size_hint_y=None, height=20)
            btn.bind(on_release = lambda btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)
            self.ids.unit1.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.ids.unit1, 'text', x))
        return

    def unit2_release_clicked(self, type):
        self.ids.unit2.text = "Unit 2:"
        self.dropdown = DropDown()
        if type == "Temperature":
            unit_list = ["Celcius", "Fahrenheit", "Kelvin"]
        elif type == "Length":
            unit_list = ["Miles", "Meters", "Kilometers", "Feet", "Inches", "Yards"]
        elif type == "Mass":
            unit_list = ["Grams", "Kilograms", "Pounds", "Ounces", "Tons"]
        elif type == "Volume":
            unit_list = ["Liters", "Milliliters", "Fluid ounces", "Cups", "Pints", "Quarts", "Tablespoons", "Teaspoons"]
        else:  
            unit_list = []
        for item in unit_list:
            btn = Button(text = item, size_hint_y=None, height=20)
            btn.bind(on_release = lambda btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)
            self.ids.unit2.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.ids.unit2, 'text', x))
        return
    
    def converter(self, u1, u2, val):
        try:
            val = float(val)
        except ValueError:
            return 'Invalid input.'
        result = 0

        if val == 0:
            return '0'

        if u1 == "Celcius":
            result = val * 1
        elif u1 == "Fahrenheit":
            result = (val - 32) * 5/9
        elif u1 == 'Kelvin':
            result = val - 273.15
        elif u1 == 'Miles':
            result = val / 1609.34
        elif u1 == 'Meters':
            result = val * 1
        elif u1 == 'Kilometers':
            result = val * 1000
        elif u1 == 'Feet':
            result = val / 3.281
        elif u1 == 'Inches':
            result = val / 38.37
        elif u1 == 'Yards':
            result = val / 1.094
        elif u1 == 'Grams':
            result = val * 1
        elif u1 == 'Kilograms':
            result = val * 1000
        elif u1 == 'Pounds':
            result = val * 454.592
        elif u1 == "Ounces":
            result = val * 28.35
        elif u1 == "Tons":
            result = val * 907185
        elif u1 == 'Liters':
            result = val * 1
        elif u1 == 'Milliliters':
            result = val / 1000
        elif u1 == 'Fluid ounces':
            result = val / 33.814
        elif u1 == 'Cups':
            result = val / 4.227
        elif u1 == 'Pints':
            result = val / 2.113
        elif u1 == 'Quarts':
            result = val / 1.057
        elif u1 == 'Tablespoons':
            result = val / 67.628
        elif u1 == 'Teaspoons':
            result = val / 203
        else:
            result = val

        if u2 == "Celcius":
            return str(result * 1)
        elif u2 == "Fahrenheit":
            return str(result * 9/5 + 32)
        elif u2 == 'Kelvin':
            return str(result + 273.15)
        elif u2 == 'Miles':
            return str(result * 1609.34)
        elif u2 == 'Meters':
            return str(result * 1)
        elif u2 == 'Kilometers':
            return str(result / 1000)
        elif u2 == 'Feet':
            return str(result * 3.281)
        elif u2 == 'Inches':
            return str(result * 38.37)
        elif u2 == 'Yards':
            return str(result * 1.094)
        elif u2 == 'Grams':
            return str(result * 1)
        elif u2 == 'Kilograms':
            return str(result / 1000)
        elif u2 == 'Pounds':
            return str(result / 454.592)
        elif u2 == "Ounces":
            return str(result / 28.35)
        elif u2 == "Tons":
            return str(result / 907185)
        elif u2 == 'Liters':
            return str(result * 1)
        elif u2 == 'Milliliters':
            return str(result * 1000)
        elif u2 == 'Fluid ounces':
            return str(result * 33.814)
        elif u2 == 'Cups':
            return str(result * 4.227)
        elif u2 == 'Pints':
            return str(result * 2.113)
        elif u2 == 'Quarts':
            return str(result * 1.057)
        elif u2 == 'Tablespoons':
            return str(result * 67.628)
        elif u2 == 'Teaspoons':
            return str(result * 203)
        else:
            return('Invalid input.')

class JournalScreen(Screen):
    def back(self):
        self.manager.transition.direction = "right"
        self.manager.current = "opening_screen"

    def new_screen(self):
        self.manager.transition.direction = "left"
        self.manager.current = "new_screen"

    def exist_screen(self):
        self.manager.transition.direction = "left"
        self.manager.current = "existing_screen"

class NewJournalScreen(Screen):
    def submit(self, title, text):
        if title == "":
            pass
        else:
            with open("journal.json") as file:
                data = json.load(file)

            data[title] = {'title': title, 'text': text, 'last_update': dt.datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
            
            with open("journal.json", 'w') as file:
                json.dump(data, file)

        self.manager.transition.direction = "right"
        self.manager.current = "journal_screen"
    
    def cancel(self):
        self.manager.transition.direction = "right"
        self.manager.current = "journal_screen"

class ExistingScreen(Screen):
    def __init__(self, *args, **kwargs):
        super(ExistingScreen, self).__init__(*args, **kwargs)
        
    def create_scrollview(self):
        self.ids.exist_id.text = "Select note:"
        self.dropdown = DropDown()
        with open("journal.json") as file:
            data = json.load(file)
        title_list = [*data.keys()]
        for t in title_list:
            btn = Button(text = t, size_hint_y=None, height=20)
            btn.bind(on_release = lambda btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)
            self.ids.exist_id.bind(on_release = self.dropdown.open)
        self.dropdown.bind(on_select = lambda instance, x: setattr(self.ids.exist_id, 'text', x))
        return

    def publish_title(self, t):
        with open("journal.json") as file:
            data = json.load(file)
        try:
            return data[t]['title']
        except KeyError:
            return ''

    def publish_text(self, t):
        with open("journal.json") as file:
            data = json.load(file)
        try:
            return data[t]['text']
        except KeyError:
            return ''

    def back(self):
        self.manager.transition.direction = "right"
        self.manager.current = "journal_screen"

    def submit(self, title, text):
        if title == "":
            pass
        else:
            with open("journal.json") as file:
                data = json.load(file)

            data[title] = {'title': title, 'text': text, 'last_update': dt.datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
            
            with open("journal.json", 'w') as file:
                json.dump(data, file)

        self.manager.transition.direction = "right"
        self.manager.current = "journal_screen"
    
    def cancel(self):
        self.manager.transition.direction = "right"
        self.manager.current = "journal_screen"

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()