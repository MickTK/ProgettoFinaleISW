from selenium.webdriver.common.by import By

class Home:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def logout(self):
        logout_button = self.driver.find_element(By.ID, "logout")
        logout_button.click()
        
class Home_utente(Home):
    def __init__(self, driver):
        url = "http://127.0.0.1:8000/home/"
        super().__init__(driver, url)
        
    def logout(self):
        logout_button = self.driver.find_element(By.ID, "logout")
        logout_button.click()    

class Home_amministratore(Home):
    def __init__(self, driver):
        url = "http://127.0.0.1:8000/Home_amministratore/"
        super().__init__(driver, url)
    
    def logout(self):
        logout_button = self.driver.find_element(By.ID, "logout")
        logout_button.click()