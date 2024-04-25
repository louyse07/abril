from kivy.app import App
from kivy.uix.button import button 
from kivy.utils import get_color_from_hex

class MyApp(App):
    def build(self):
        return button(text='clique aqui', background_color=get_color_from_hex('#3498db'))
    
    if __name__ == "__main__":
        MinhaApp().run()
        