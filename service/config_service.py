from configs.config_reader import ConfigManager


class ConfigService:
    instance = None

    def __init__(self):
        self.confManger = ConfigManager.get_instance()
        ConfigService.instance = self

    def getConfig(self, key: str):
        return self.confManger.get_val(key)

    @staticmethod
    def getInstance():
        if ConfigService.instance is None:
            ConfigService()
        return ConfigService.instance
