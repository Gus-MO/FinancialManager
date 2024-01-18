import kivy
kivy.require('2.3.0') # Check this line

# Kivy Widgets
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# Inner Project imports
from database.manage import DataBase

# General imports
from pathlib import Path


class MainScreen(GridLayout):

    def __init__(self, data_base,**kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.data_base = data_base

        #self.cols = 3
        self.add_widget(Label(text='Name'))
        self.add_widget(Label(text='Value'))

        btn = Button(text='Insert')
        self.add_widget(btn)

        btn.bind(on_press=self.insert_callback)

        self.name_input = TextInput()
        self.value_input = TextInput()
        self.add_widget(self.name_input)
        self.add_widget(self.value_input)

    def insert_callback(self, instance):
        self.data_base.insert(self.name_input.text, self.value_input.text)
        return 

class Manager(App):
    def __init__(self, data_base, **kwargs):
        super(Manager, self).__init__(**kwargs)

    def build(self):
        return MainScreen(data_base) # returns a widget

if __name__ == '__main__':
    # Creats a DataBase instance and connects to the given database
    data_base = DataBase('manager')

    Manager(data_base).run()