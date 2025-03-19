
from pathlib import Path
import sys
import tomllib
from importlib import resources

def get_base_path():
    # get path when release with pyinstaller
    #
    if hasattr(sys, '_MEIPASS'):
        base_path = Path(sys._MEIPASS)
    else:
        base_path = resources.files("casd_hub")
    return base_path

def get_icon_path(icon_name:str):
    """Retrieve the full path of an icon from the assets folder inside the package"""
    base_path = get_base_path()
    icon_relative_path = Path.joinpath(base_path, "assets")
    icon_path = Path.joinpath(icon_relative_path, icon_name)
    return icon_path.as_posix()

def get_config():
    """
    This function returns the config dict
    :return:
    """
    base_path = get_base_path()
    with resources.as_file(base_path / "config.toml") as config_path:
       config = tomllib.loads(config_path.read_text(encoding="utf-8"))
       return config

def get_app_title():
    config = get_config()
    return config["ui"]["app_title"]
