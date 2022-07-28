from kivy.uix.button import Button
from kivy.core.window import Window

class HLButton(Button):

    def __init__(self, *args, **kwargs):
        super(HLButton, self).__init__(*args, **kwargs)

        self.bc_hovering = (.25, .45, 1, 1) 
        self.bc = (.25, .4, .95, 1)   

        self.background_normal = ""        
        self.background_color = self.bc  

        Window.bind(mouse_pos=self.pos_check)

    def pos_check(self, inst, pos):
        if self.collide_point(*pos):
            # hovering
            self.background_color = self.bc_hovering
        else:
            # not hovering
            self.background_color = self.bc