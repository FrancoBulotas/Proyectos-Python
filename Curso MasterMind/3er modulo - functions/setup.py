from distutils.core import setup
import py2exe
import re
import os
from pathlib import Path
from time import sleep
from random import randrange
import sqlite3
import glob


setup(zipfile=None,
      options={"py2exe": {"bundle_files": 1}},
      windows=["joder_amigos.py"])
