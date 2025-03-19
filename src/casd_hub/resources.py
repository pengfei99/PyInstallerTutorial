import importlib.resources

def get_icon_path(icon_name:str):
    """Retrieve the full path of an icon from the assets folder inside the package"""
    return str(importlib.resources.files("casd_hub.assets") / icon_name)

def get_config():
    """
    This function returns the config dict
    :return:
    """
