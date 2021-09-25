import json


class ConfigManager:
    instance = None

    def __init__(self):
        self.data = None
        with open("configs/configs.json") as json_file:
            self.data = json.load(json_file)
        ConfigManager.instance = self

    def get_header(self):
        return ["tenants", self.data["current_tenant"]]

    def get_val(self, key: str):
        keys = key.split(".")
        keys = self.get_header() + keys
        res = self.data
        for k in keys:
            if res[k] is not None:
                res = res[k]
            else:
                return ""
        return res

    @staticmethod
    def get_instance():
        if ConfigManager.instance is None:
            ConfigManager()
        return ConfigManager.instance
