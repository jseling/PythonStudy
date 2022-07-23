from kivy.app import App
from kivy.uix.treeview import TreeView
from kivy.uix.treeview import TreeViewLabel


class Test(App):
    def build(self):
        tv = TreeView()
        n1 = tv.add_node(TreeViewLabel(text='Item 1'))
        tv.add_node(TreeViewLabel(text='SubItem 1'), n1)
        tv.add_node(TreeViewLabel(text='SubItem 2'), n1)
        return tv

Test().run()