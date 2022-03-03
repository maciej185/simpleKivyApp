from kivy.app import App
from kivy.core.window import Window   
import kivy
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import ListProperty
from kivy.graphics import Ellipse, Line
from kivy.graphics import Color

#making the window white
Window.clearcolor = (1,1,1,1)

class KivyApp(App):
    def build(self):
        return MyGrid()

class MyGrid(Widget):

    color = ListProperty((1, 1, 1, 1))

    btn = ObjectProperty(None)
    tekst = ObjectProperty(None)
    
    def pressed(self, canvass):
        global Window
        self.tekst1 = self.tekst
        self.btn.text = ""
        canvass.clear()

    def lifted(self):
        self.btn.text = self.tekst1
    
    def increase(self, canvass):
        canvass.d += 1

    def decrease(self, canvass):
        canvass.d -= 1

class Touch(Widget):

    color = ListProperty((1, 1, 1, 1))
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)
        self.d = 5

    def on_touch_down(self, touch):
        print("mouse down ", touch)
        x = touch.pos[0]
        y = touch.pos[1]
        self.canvas.add(Color(rgba=(0,0,0,1)))
        self.canvas.add(Ellipse(segments = 5, pos = (x - self.d/2,y-self.d/2), size = (self.d,self.d)))
        self.canvas.ask_update()
    def on_touch_up(self, touch):
        print("mouse up ", touch)
        
    def on_touch_move(self, touch):
        x = touch.pos[0]
        y = touch.pos[1]
        self.canvas.add(Color(rgba=(0,0,0,1)))
        self.canvas.add(Ellipse(segments = 5, pos = (x - self.d/2,y - self.d/2), size = (self.d,self.d)))
        print("mouse move ", touch)
    
if __name__ == "__main__":
    KivyApp().run()