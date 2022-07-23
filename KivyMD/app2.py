from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.button import MDIconButton
from kivymd.uix.button import MDFlatButton

class MainApp(MDApp):
    def build(self):
        screen = Screen()
        screen.add_widget(
            MDIconButton(
                icon="language-python",
                pos_hint={"center_x": 0.5, "center_y": 0.9},
            )
        )

        screen.add_widget(
            MDFlatButton(
                text="MDFlatButton",
                pos_hint={"center_x": 0.5, "center_y": 0.8},
            )
        )        

        screen.add_widget(
            MDRectangleFlatButton(
                text="MDRectangleFlatButton",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )        

        return screen


MainApp().run()