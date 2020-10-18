from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout

class ImageButton(ButtonBehavior, Image):
    def on_press(self):
        print ('pressed')

class MyApp(App):
    def build(self):
        return FloatLayout()


MyApp().run()
