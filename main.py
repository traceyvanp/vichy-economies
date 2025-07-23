from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup

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
time.sleep(10) 


# Submit the form
connection_button.send_keys(Keys.ENTER)

# Wait for login to complete
time.sleep(10)

# Now navigate to the secured page
driver.get('https://www.feed-alliance.fr/index.php?option=com_faweb&innerview=terme&innerlayout=main#')

# navigate to livre d'achats from achats dropdown
achats_link = driver.find_element(By.LINK_TEXT, "Achats")
achats_link.click()
time.sleep(5)

#navigate to livre d'achats
livres_link = driver.find_element(By.LINK_TEXT, "Livres d'achats")
livres_link.click()
time.sleep(5)

#navigate to usine
usine_button = driver.find_element(By.XPATH, "*//span[normalize-space()='TELLUS USINES']")
usine_button.click()
time.sleep(5)

#navigate to synthese
synthese_button = driver.find_element(By.XPATH, "*//span[normalize-space()='synthèse']")
synthese_button.click()
time.sleep(5)

# Extract the page content
secured_page_content = driver.page_source

# Parse with BeautifulSoup
secured_page_soup = BeautifulSoup(secured_page_content, 'html.parser')
secured_page_soup.prettify()

# Initialize an empty list to hold the data
data = []

# Find all element headers
headers = secured_page_soup.find_all('h1')
#num_elements = len(headers)

# Iterate over each header
for header in headers:
    # Get the text of the current header
    header_text = header.get_text()  
    
    # Find the next 'tr' elements after the header
    header_row = header.find_next('tr', class_='header_fa')
    price_row = header_row.find_next('tr', class_='bold prix_prev')

    # Extract dates from the header row
    dates = header_row.find_all('td', class_='borduredroite_bas centrer')
    date_texts = [date.get_text() for date in dates]
    
    # Extract prices from the price row
    prices = price_row.find_all('td', class_='borduredroite_bas centrer')
    est_prices = price_row.find_all('td', class_='borduredroite_bas centrer prix_estimes')
    #combine the current and forecast prices
    combined_prices = prices + est_prices
    price_texts = [price.get_text() for price in combined_prices]

    # Combine the data for the current header
    today = datetime.today().strftime('%Y-%m-%d')
    for date, price in zip(date_texts, price_texts):
        data.append({
            'Header': header_text,
            'Date': date,
            'Price': price,
            'LastModifiedDate': today
        })

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

#Export DataFrame to CSV
filename = 'tellus_data.csv'
df.to_csv(filename, index=False)

# Close the browser
driver.quit()

