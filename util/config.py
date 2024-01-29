###
# This is Rich config file
###
from os import environ
from dotenv import load_dotenv
from util.exception import RichConfigNotFound, RichConfigError
import yaml

load_dotenv()


class RichConf:

    def __init__(self):
        self.conf = self.parse_conf()

    def get_conf_path(self):
        config_path = environ.get("RICH_CONF_PATH", None)
        if not config_path:
            raise RichConfigNotFound("Cannot fount any value from `RICH_CONF_PATH` environment Please Set it")

        return config_path

    def parse_conf(self):
        with open(self.get_conf_path()) as f:
            try:
                return yaml.safe_load(f)
            except Exception as e:
                raise RichConfigError(f"error parsing {Exception}")
