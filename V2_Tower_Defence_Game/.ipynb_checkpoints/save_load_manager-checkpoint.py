import pickle
import os
import easygui

class SaveLoadClass:
    def __init__(self, folder = 'Saves', file_extension = '.td'):
        self.folder = folder
        self.file_extension = file_extension

    def save_data(self, data, name=None):
        if not name:
            name = self.get_file_name()
        data_file = open(f'{self.folder}/{name}{self.file_extension}', "wb")
        pickle.dump(data, data_file)

    def load_data(self, name):
        data_file = open(name, "rb")
        return pickle.load(data_file)

    def get_file_name(self):
        return easygui.enterbox('Input file name: ', title='AHHHHHH', default='your_name')
        