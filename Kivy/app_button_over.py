from button_hover import HLButton
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.metrics import dp

class Test(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        button = HLButton(text='Botão 1',pos_hint={"center_x": 0.5, "center_y": 0.5},size_hint=(None, None), size=(dp(110), dp(35)))
        label = Label(text='Texto 1')
        box.add_widget(label)        
        box.add_widget(button)
        return box

Test().run()