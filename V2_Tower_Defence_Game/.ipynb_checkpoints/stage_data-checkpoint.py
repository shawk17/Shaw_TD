import ast  # For safely parsing strings as Python objects
import os

class Stages:
    def __init__(self, saves_directory = './Saves'):
        self.saves_directory = saves_directory
        self.stages = self.read_in_stages()
        print(self.stages)
        

    def read_in_stages(self):
        stages = []
        for file_name in os.listdir(self.saves_directory):
            if file_name.endswith('.atd'):
                file_path = os.path.join(self.saves_directory, file_name)
                with open(file_path, 'r') as file:
                    file_content = file.read()
                    try:
                        file_stage = ast.literal_eval(file_content)
                        if isinstance(file_stage, dict):
                            stages.append(file_stage)
                        else:
                            print(f'skipping file {file_name}: not a dictionary')
                    except Exception as e:
                        print(f'Error reading file {file_name}: {e}')
        return stages
                        
                        
        
# Each Dictionary in the list is a level
# Each list says how many of each level and guy you want (No more than 4 levels currently, can add more)
# Curret enemies are: regular, dash, strong, speed, armored, and constant

