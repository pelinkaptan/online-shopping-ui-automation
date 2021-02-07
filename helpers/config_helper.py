import yaml
from pathlib import Path


class ConfigHelper:

    def config_load(self):
        path = Path(__file__).parent / "../config.yaml"
        with path.open() as file:
            config = yaml.load(file, Loader=yaml.Loader)
            return config
