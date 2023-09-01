#!/usr/bin/env python3

import os
import shutil
from pathlib import Path

""" Delete virtual environment if exist and recreate it """
base_path = Path(os.getcwd() + "/venv")
if base_path.exists() and base_path.is_dir():
    print("Delete virtual environment...")
    shutil.rmtree(base_path)

""" Create virtual environment """
print("Create virtual environment...")
os.system("python3 -m venv venv")

""" Activate virtual environment and install required python packages """
print("Install packages...")
os.system(". venv/bin/activate && pip install -r requirements.txt")

# Commands
print(
    "** Commands to download video **\n\n"
    "source venv/bin/activate\n"
    "python download.py\n"
    "Enter the YouTube video URL: https://www.youtube.com/xxxxxxxxxxx"
)
