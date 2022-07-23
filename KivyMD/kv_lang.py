from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDScreen:

    MDIconButton:
        icon: "language-python"
        pos_hint: {"center_x": .5, "center_y": .9}

    MDFlatButton:
        text: "MDFlatButton"
        theme_text_color: "Custom"
        text_color: 0, 0, 1, 1
        pos_hint: {"center_x": .5, "center_y": .8}    

    MDRaisedButton:
        text: "MDRaisedButton"
        md_bg_color: 0, 0, 1, 1            
        pos_hint: {"center_x": .5, "center_y": .7}    

    MDRectangleFlatButton:
        text: "MDRectangleFlatButton"
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
        line_color: 0, 0, 1, 1    
        pos_hint: {"center_x": .5, "center_y": .6}   

    MDRectangleFlatIconButton:
        icon: "android"
        text: "MDRectangleFlatIconButton"
        theme_text_color: "Custom"
        text_color: 0, 0, 1, 1
        line_color: 0, 0, 1, 1
        theme_icon_color: "Custom"
        icon_color: .2, .8, .2, 1       
        pos_hint: {"center_x": .5, "center_y": .5}    

    MDRoundFlatButton:
        text: "MDRoundFlatButton"
        text_color: 0, 1, 0, 1  
        pos_hint: {"center_x": .5, "center_y": .4}     

    MDFillRoundFlatIconButton:
        text: "MDFillRoundFlatIconButton"
        icon: "android"
        md_bg_color: 0, 0, 1, 1            
        pos_hint: {"center_x": .5, "center_y": .3}                                         

'''


class Example(MDApp):
    def build(self):
        return Builder.load_string(KV)


Example().run()