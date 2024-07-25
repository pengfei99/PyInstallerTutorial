import os

from setuptools import setup, find_packages

# Read the long description from the README.md file
with open(os.path.join(os.path.dirname(__file__), 'README.md'), 'r', encoding='utf-8') as fh:
    README = fh.read()
app_name = "casd"
setup(
    name="data-convertor",
    version="1.0.0",
    author="Pengfei Liu",
    description="Read the latest Real Python tutorials",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/realpython/reader",
    author_email="info@realpython.com",
    license="MIT",
    classifiers=[
         'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pyspark", "pandas", "PyQt6", "python-dotenv"
    ],
    entry_points={"console_scripts": [f"{app_name}=app.__main__:main"]},
)
