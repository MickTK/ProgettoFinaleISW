# classe di test
import unittest

from django.test import TestCase

# framework
from selenium import webdriver

from test.test_login import TestLogin

if __name__ == '__main__':
    # Inizializza il browser
    driver = webdriver.Chrome()

    # Inizializza il runner dei test
    test_runner = unittest.TextTestRunner()

    # Esegue i test
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestLogin))

    result = test_runner.run(suite)

    # Chiudi il browser
    driver.quit()