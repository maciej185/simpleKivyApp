from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput    
from kivy.uix.button import Button
import kivy
from pkg_resources import PkgResourcesDeprecationWarning

class KivyApp(App):
    def build(self):
        return MyGrid()

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
   
        self.rows = 2

        self.frame = GridLayout()   #gorny frame
        self.frame.cols = 2

        self.frame1 = GridLayout()  #frame z labelka i polem tekstowym
        self.frame1.rows = 2

        self.tekst = Label(text = "Podaj swoje imię i nazwisko")
        self.frame1.add_widget(self.tekst)

        self.pole_tekstowe = TextInput()
        self.frame1.add_widget(self.pole_tekstowe)

        self.frame.add_widget(self.frame1)
        self.okno = Label(text = " ")
        self.frame.add_widget(self.okno)
        self.add_widget(self.frame)

        self.click = Button(text = "Submit")  
        self.click.bind(on_press = self.pressed)
        self.add_widget(self.click)


    # obsluga zdazenia klikniecia w przycisk
    def pressed(self, instance):
        imie = self.pole_tekstowe.text
        self.pole_tekstowe.text = ""   #czysczenie pola tekstowego
        self.okno.text = imie    #printowanie inputu w labelce w prawym gornym rogu

if __name__ == "__main__":
    KivyApp().run()