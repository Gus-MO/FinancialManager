import kivy
kivy.require('2.3.0') # Check this line

# Kivy Widgets
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

# Inner Project imports
from database.manage import DataBase
from database.create import create_database

# General imports
from pathlib import Path

class MainScreen(GridLayout):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        #self.cols = 3
        self.add_widget(Label(text='0'))
        self.add_widget(Label(text='1'))
        self.add_widget(Label(text='2'))

        self.add_widget(TextInput())
        self.add_widget(TextInput())

class Manager(App):

    def build(self):
        return MainScreen() # returns a widet

if __name__ == '__main__':
    # Check Database
    if not Path('').joinpath('financial_manager/database/manager.db').resolve().exists():
        print('Database Not Found.')
        print('Creating...')
        create_database()

    Manager().run()