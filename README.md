# PyInstaller

## Why we need PyInstaller for a python application?

When you deploy your python application on a new machine. You probably have to do something like this:

- Download and install a specific version of Python
- Set up pip
- Set up a virtual environment
- Get a copy of your code
- Install dependencies

If the application requires other dependencies (e.g. spark jars), you may need extra steps for it to work. 

**PyInstaller** abstracts these details from the user by finding all your dependencies and bundling them together. 
Your users won’t even know they’re running a Python project because the Python Interpreter itself is bundled into 
your application. Goodbye complicated installation instructions!

## To build your app with pyinstaller

The official doc for pyinstller is [here](https://pyinstaller.org/en/v4.1/index.html)

### Prepare the entry point of your application

**pyinstaller** requires `an entry point` of your application to build the `.exe`. By convention, we create a `main.py`
in the root path of the package. 

The below code is an example of `main.py`. 

```python
import sys

from PyQt6.QtWidgets import QApplication
from casd_hub.ui import SecureHubWidget


def main():
    app = QApplication(sys.argv)
    window = SecureHubWidget()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
```

> Before building the `.exe`, make sure the `main.py` works properly

### Prepare the resource which you want to include 

This step is the most tricky step. Because all the resources(e.g. logo.png, config.toml, etc.) in your application may
not work anymore. There are three points you need to pay attention:
- By default, non-code resources are not included in the `.exe` bundle. You need to prepare a list of all resources
   which you want to include.
- Use a `path determinator` for all resources to get path. Because `PyInstaller` extracts files into a `temporary directory (_MEIPASS)` when running a 
bundled `.exe`. The path of the resources may not be the same between the `.exe` and your project
- Don't try to edit resources (e.g. config.toml) in the `temporary directory (_MEIPASS)`, you will get Permission denied error. 


In below example, we show how to use `hasattr(sys, '_MEIPASS')` to detect if the code is run by `PyInstaller` or 
`classic python virtual env`. Then we use different approach to get the resources path

```python

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

```


> I still have the **Permission denied error** with `config.toml`, even I use read-only method.
> 

### Build with command line options (Not recommended)

```shell
# install pyinstaller bin
pip install pyinstaller

# go to project
cd C:\Users\PLIU\Documents\git\PyInstallerTutorial

pyinstaller --onefile --windowed --icon=C:/Users/PLIU/Documents/git/PyInstallerTutorial/src/casd_hub/assets/bouclier.ico ./src/casd_hub/main.py

pyinstaller --onefile --windowed --add-data "src/casd_hub/assets;assets" --add-data "src/casd_hub/conf;conf" --icon=C:/Users/PLIU/Documents/git/PyInstallerTutorial/src/casd_hub/assets/bouclier.ico ./src/casd_hub/__main__.py

```

The explanation of option:
- `onefile`: one single bundle `.exe`.
- `windowed`: do not open a console, only the app window
- `icon`: provide a custom icon for the `.exe`
- `add-data`: include extra resources into the `.exe`

The complete option list can be found [here](https://pyinstaller.org/en/v4.1/usage.html). Click on the `General Options`
button to view them, if you can see them.

> By default, the generated `.exe` is located in `./dist`
> 
### Build with .spec config file (Recommended)

With the command line option, you need to type a lot of things for each build. To avoid this, you can specify all the
build options in one `.spec` file. Then you run the below command to do the build.

```shell
pyinstaller main.spec
```

> You can find the complete doc of the `.spec` in [here](https://pyinstaller.org/en/v4.1/spec-files.html)

Below is an example of the main.spec

```python
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

from PyInstaller.utils.hooks import collect_data_files

a = Analysis(
    ['src\\casd_hub\\main.py'],
    pathex=[],
    binaries=[],
    datas=[('src/casd_hub/assets', 'assets'), ('src/casd_hub/config.toml', 'config.toml')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='casd_secure_hub',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\PLIU\\Documents\\git\\PyInstallerTutorial\\src\\casd_hub\\assets\\bouclier.ico'],
)

```