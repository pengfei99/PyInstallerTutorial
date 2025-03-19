from casd_hub.resources import get_icon_path, get_config


def test_get_icon_path():
    icon_path = get_icon_path("bouclier.ico")
    print(icon_path)

def test_get_config():
    icon_path = get_config()
    print(icon_path)