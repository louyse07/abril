from kivy.app import App
from kivy.uix.label import Label

class minhaApp(App):
    def build(self):
        return Label(text="olá SENAI")
    
    if __name__ == "__main__":
        minhaApp().run()
        