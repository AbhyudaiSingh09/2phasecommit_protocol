import yaml

class ConfigLoader:
    def __init__(self):
        self.file_path = 'config.yaml'

    def _load_config(self):
        with open(self.file_path, "r") as config_file:
            return yaml.safe_load(config_file)

    def upload_master_config(self):
        config = self._load_config()
        return config['Master']['M1']

    def upload_config_Node_P1(self):
        config = self._load_config()
        return config['Nodes']['P1']

    def upload_config_Node_P2(self):
        config = self._load_config()
        return config['Nodes']['P2']

    def upload_client_config(self):
        config = self._load_config()
        return config['Client']['C1']

    def upload_keywords(self):
        with open("keywords.yaml", "r") as keywords_file:
            keywords = yaml.safe_load(keywords_file)
            return keywords['keywords']
