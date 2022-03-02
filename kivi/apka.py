from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput    
from kivy.uix.button import Button
import kivy
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class KivyApp(App):
    def build(self):
        return MyGrid()

class MyGrid(Widget):
    imie = ObjectProperty(None)
    pass

    def pressed(self):
        self.imie.text = "" #czyszcenie okna z inputem
        

if __name__ == "__main__":
    KivyApp().run()