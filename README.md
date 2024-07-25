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