
from distutils.core import setup
import py2exe
from requests_html import HTMLSession
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

setup(zipfile=None,
      options={"py2exe": {"bundle_files": 1}},
      console=["sniper_bot.py"])