from kivy.app import App
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex

class minhaApp(App):
    def build(self):
        return Label(text='olá SENAI', font_size=100, font_name='Arial',color=get_color_from_hex)

    
    if __name__ == "__main__":
        minhaApp().run()