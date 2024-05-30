# Now navigate to the secured page
driver.get('https://www.feed-alliance.fr/index.php?option=com_faweb&innerview=terme&innerlayout=main#')

# Extract the page content
secured_page_content = driver.page_source

# Parse with BeautifulSoup
from bs4 import BeautifulSoup
secured_page_soup = BeautifulSoup(secured_page_content, 'html.parser')

# Do your scraping here
soup = secured_page_soup.prettify()