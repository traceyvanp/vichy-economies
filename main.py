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

# Find username and password fields and enter data
username_field = driver.find_element(By.CSS_SELECTOR, "#usr_mail")
print(username_field)
#password_field = driver.find_element(By.CSS_SELECTOR, "#passwd")


#username_field.send_keys('thomas.van-puyvelde@axereal-elevage.com')
#password_field.send_keys('FeedAx2024')

# Submit the form
#password_field.send_keys(Keys.RETURN)

# Wait for login to complete
#time.sleep(5)  # Adjust based on your network speed and website response time

# Now navigate to the secured page
#driver.get('https://www.feed-alliance.fr/index.php?option=com_faweb&innerview=terme&innerlayout=main#')

# Extract the page content
#secured_page_content = driver.page_source

# Parse with BeautifulSoup
#from bs4 import BeautifulSoup
#secured_page_soup = BeautifulSoup(secured_page_content, 'html.parser')

# Do your scraping here
#print(secured_page_soup.prettify())

# Close the browser
#driver.quit()
