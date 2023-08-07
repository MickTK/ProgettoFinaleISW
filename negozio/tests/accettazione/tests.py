from django.test import TestCase

from selenium import webdriver

from selenium.webdriver.common.keys import Keys 
import time 
import os

# from login_test import login_test
from registrazione_test import registrazione_test
from logout_test import logout_test

registrazione_test()

time.sleep(6)

# login_test()

time.sleep(6)

logout_test()


time.sleep(20)  # tot secondi prima della chiusura del browser



