from distutils.core import setup
import py2exe
from time import sleep
from pushbullet import PushBullet
import cv2
import getpass
import os

setup(zipfile=None,
      options={"py2exe": {"bundle_files": 1}},
      windows=["pushbullet_inicioPC.py"])
