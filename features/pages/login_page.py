# from selenium.webdriver.common.by import By
# from selenium.webdriver.remote.webdriver import WebDriver

# class LoginPage:
#     def __init__(self, driver: WebDriver):
#         self.driver = driver
#         self.username_input = (By.ID, "username")
#         self.password_input = (By.ID, "password")
#         self.login_button = (By.ID, "login-button")

#     def open(self, url):
#         self.driver.get(url)

#     def login(self, username, password):
#         self.driver.find_element(*self.username_input).send_keys(username)
#         self.driver.find_element(*self.password_input).send_keys(password)
#         self.driver.find_element(*self.login_button).click()

#     def get_title(self):
#         return self.driver.title
