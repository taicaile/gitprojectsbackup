"""to load config file"""
import os
import logging
import yaml

__all__ = ['config']

logging.basicConfig(level=logging.INFO)

CONFIG_FILE = "config.yaml"
if os.path.isfile(CONFIG_FILE):
    with open(CONFIG_FILE, 'r', encoding="utf-8") as file:
        config = yaml.load(file, yaml.Loader)
