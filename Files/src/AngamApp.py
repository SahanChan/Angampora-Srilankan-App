from kivy.app import App
from kivy.uix.label import Label

class AngamApp(App):
    def build(self):
        print("Hello World")
        return Label(text='Angampora\nIn Development',font_size='20sp')

if __name__=='__main__':
    AngamApp().run()
