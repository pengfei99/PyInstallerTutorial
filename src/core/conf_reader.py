import configparser
import os

from app.conf.constant import CONFIG_FILE_PATH


def read_config():
    conf_file = "/tmp/config.cfg"
    if os.path.exists(CONFIG_FILE_PATH):
        conf_file = CONFIG_FILE_PATH
    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Read the configuration file
    config.read(conf_file)

    # Accessing values
    db_host = config.get('database', 'host')
    db_port = config.getint('database', 'port')
    db_username = config.get('database', 'username')
    db_password = config.get('database', 'password')

    server_host = config.get('server', 'host')
    server_port = config.getint('server', 'port')

    log_level = config.get('logging', 'level')
    log_file = config.get('logging', 'file')

    # Print values
    print(f"Database Host: {db_host}")
    print(f"Database Port: {db_port}")
    print(f"Database Username: {db_username}")
    print(f"Server Host: {server_host}")
    print(f"Server Port: {server_port}")
    print(f"Logging Level: {log_level}")
    print(f"Logging File: {log_file}")
