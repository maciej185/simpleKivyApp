from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput    
from kivy.uix.button import Button
import kivy
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.graphics import Rectangle
from kivy.graphics import Color

class KivyApp(App):
    def build(self):
        return MyGrid()

class MyGrid(Widget):
    pass

class Touch(Widget):

    #btn = ObjectProperty(None)
    def on_touch_down(self, touch):
        print("mouse down ", touch)
        #self.btn.opacity = 0.5
    def on_touch_up(self, touch):
        print("mouse up ", touch)
        #self.btn.opacity = 1
    def on_touch_move(self, touch):
        print("mouse move ", touch)
    

if __name__ == "__main__":
    KivyApp().run()