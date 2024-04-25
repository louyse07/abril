from kivy.app import App
from kivy.uix.button import Button

def botao_pressionado(instance):
    print("botão pressionado!")

class MinhaApp(App):
    def build(self):
        bnt = Button(text='Clique Aqui')
        bnt.bind(on_press=botao_pressionado)
        return bnt
    
if __name__ == "__main__":
    MinhaApp().run()
    