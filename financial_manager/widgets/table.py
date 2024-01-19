import kivy
kivy.require('2.3.0') # Check this line

from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from pandas import DataFrame    # Check if is better to create a parser
    
class Table(GridLayout):
    '''
    This class serves as a base for a widget, if a iter is passed
    it converts it into a table widget with the given iter.
    Now we're using pandas to make the table, but it may change on the future
    '''
    def __init__(self, *args, **kwargs):
        super(Table, self).__init__(**kwargs)

        if args:
            self.raw_table = DataFrame(args[0]) # any iter that can be converted into a table
            self.cols = self.raw_table.shape[1]
            self.create_table()

    def create_table(self):
        for column in self.raw_table.columns:
            self.add_widget(Label(text = str(column), bold = True))

        for index, row in self.raw_table.iterrows():
            for value in row:
                self.add_widget(Label(text=str(value)))
    
    def add_row(self, row):
        for value in row:
            self.add_widget(Label(text=str(value)))
