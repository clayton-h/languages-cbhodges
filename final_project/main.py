# Automates a headless browser (no GUI)
# to scrape content from websites formatted with JavaScript
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Scrapes static HTML web content
from bs4 import BeautifulSoup

# Setup Edge options
edge_options = Options()
edge_options.add_argument("--headless")  # Runs Edge in headless mode

# Use WebDriver Manager to manage the Edge driver
# The EdgeChromiumDriverManager().install() returns the path to the edge driver executable as a string
# The Service class is used to create a service with that path
driver = webdriver.Edge(service=Service(
    EdgeChromiumDriverManager().install()), options=edge_options)

# http://quotes.toscrape.com/js/ #HTML
url = "https://www.webscraper.io/test-sites/e-commerce/allinone"

# Use the browser to get the URL
driver.get(url)

# Use WebDriverWait instead of time.sleep()
# to wait for JavaScript to load
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, ".thumbnail")))  # span.text #HTML

# Now that the necessary elements are visible, get the final HTML
final_html = driver.page_source
driver.quit()

# Use Beautiful Soup to parse the final HTML
soup = BeautifulSoup(final_html, 'html.parser')

# # Now you can find elements as if it's a static page (HTML)
# quotes = soup.find_all('span', class_='text')
# for quote in quotes:
#     print(quote.text)

# Find elements containing products; adjust the selectors to match the site structure
# For example, this will find all the 'div' elements with the class 'caption'
products = soup.find_all('div', class_='caption')
for product in products:
    # You might find the name of the product in an 'a' tag with a 'title' attribute
    name = product.find('a', {'title': True}).get(
        'title', 'No title attribute')
    # Prices might be found in an 'h4' tag with class 'price'
    price = product.find('h4', class_='price').text
    print(f'Product Name: {name}, Price: {price}')
