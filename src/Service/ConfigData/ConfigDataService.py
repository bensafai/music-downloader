import os.path
import yaml


class ConfigDataService:
    def __init__(self):
        self.config_path = './config.yml'
        self.client_name = ''

    def get_config(self):
        config_data = False
        file_exists = os.path.isfile(self.config_path)
        if file_exists:
            with open(self.config_path) as file:
                config_file = yaml.full_load(file)
                config_data = config_file[self.client_name]
        return config_data