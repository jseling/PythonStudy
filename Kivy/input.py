# https://kivy.org/doc/stable/api-kivy.uix.textinput.html

# https://stackoverflow.com/questions/47581333/kivy-how-to-trigger-event-by-text-change
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class Test(App):
    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)

        self.textinput = TextInput(text='Hello world')
        self.label = Label()

    def on_click_meu_button(instance, value):
        instance.label.text = instance.textinput.text  

    def build(self):
        box = BoxLayout(orientation='vertical')
        button = Button(text='Botão 1')
        button.bind(on_press=self.on_click_meu_button)

        box.add_widget(self.label)
        box.add_widget(self.textinput)        
        box.add_widget(button)

        return box      

Test().run()