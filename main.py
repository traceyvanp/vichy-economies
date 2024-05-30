from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Path to ChromeDriver
driver_path = '/usr/local/bin/chromedriver'  # Ensure chromedriver is installed and the path is correct

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless Chrome

# Setup Chrome driver
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the login page
driver.get('https://www.feed-alliance.fr/index.php?option=com_faweb&innerview=activation')

# Find the required elements
username_field = driver.find_element(By.XPATH, "*//*[@id='usr_mail']")
password_field = driver.find_element(By.XPATH, "*//*[@id='passwd']")
#relative XPATH //input[@id='btn_login']
connection_button = driver.find_element(By.XPATH, "*//*[@id='btn_login']")
#print(username_field)
#print(password_field)

#set the key values
username_field.send_keys('thomas.van-puyvelde@axereal-elevage.com')
password_field.send_keys('FeedAx2024')

# Submit the form
connection_button.send_keys(Keys.ENTER)

# Wait for login to complete
time.sleep(10)  # Adjust based on your network speed and website response time

# Now navigate to the secured page
driver.get('https://www.feed-alliance.fr/index.php?option=com_faweb&innerview=terme&innerlayout=main#')

# navigate to livre dachats from achats dropdown
#relative XPATH //a[@data-options="menu:'#menu_achats'"]//span[@class='m-btn-downarrow']
achats_link = driver.find_element(By.XPATH, "*//*[@class='m-btn-downarrow']")
achats_link.click()
time.sleep(5)
#relative XPATH //div[@onclick="openLayout('achats', 'couvertures_main', 'facontent')"]//div[@class='menu-text']//a[@href='#']
action = "openLayout('achats', 'couvertures_main', 'facontent')"
livres_link = driver.find_element(By.XPATH, "*//div[@onclick=" + action + "]//div[@class='menu-text']//a[@href='#']")
livres_link.click()
time.sleep(5)

#navigate to usine
#relative XPATH //span[normalize-space()='AXEREAL ELEVAGE USINES']
usine_button = driver.find_element(By.XPATH, "*//span[normalize-space()='AXEREAL ELEVAGE USINES']")
usine_button.click()
time.sleep(5)

#navigate to synthese
#relative XPATH //span[normalize-space()='synthèse']
synthese_button = driver.find_element(By.XPATH, "*//span[normalize-space()='synthèse']")

# Give the next page some time to load if necessary
time.sleep(10)

# Extract the page content
secured_page_content = driver.page_source

# Parse with BeautifulSoup
from bs4 import BeautifulSoup
secured_page_soup = BeautifulSoup(secured_page_content, 'html.parser')
secured_page_soup.prettify()

'''
# Find all elements with the specified classes
elements_borduredroit_bas = secured_page_soup.find_all(class_='borduredroit_bas')
elements_borduredroit_bas_centrer = secured_page_soup.find_all(class_='borduredroit_bas_centrer')

# Combine the results if you need both in one list
all_elements = elements_borduredroit_bas + elements_borduredroit_bas_centrer

# Print the content of each element found
for element in all_elements:
    print(element)


# Do your scraping here
#print(secured_page_soup.prettify())

# Find all elements with the specified classes
#secured_page_soup.find_all(class_="borduredroit_bas")
#secured_page_soup.find_all("td", "borduredroit_bas")
secured_page_soup.find_all("a")

elements_borduredroit_bas_centrer = secured_page_soup.find_all(class_="borduredroite_bas centrer ")

# Combine the results if you need both in one list
all_elements = elements_borduredroit_bas + elements_borduredroit_bas_centrer

# Print the content of each element found
for element in all_elements:
    print(element)

# Close the browser
#driver.quit()
'''

