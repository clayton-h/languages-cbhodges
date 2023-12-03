import requests
from selenium import webdriver
""" Automates a headless browser (no GUI)
    to scrape dynamic JavaScript web content
"""
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
""" Scrapes static HTML web content
"""


# Function to parse static HTML content
def parse_static_html(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract content as needed, for example, quotes
    quotes = soup.find_all('span', class_='text')
    for quote in quotes:
        print(quote.text)


# Function to parse dynamic JavaScript content
def parse_dynamic_content(url):
    # Setup Edge options and run Edge in headless mode
    edge_options = Options()
    edge_options.add_argument("--headless")

    # Use WebDriver Manager to manage the Edge driver
    driver = webdriver.Edge(service=Service(
        EdgeChromiumDriverManager().install()), options=edge_options)

    # Use the browser to get the URL
    driver.get(url)

    # Use the WebDriverWait function instead of time.sleep()
    # to wait for dynamic content to load
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".thumbnail")))

    # Now that the necessary elements are visible,
    # get the final HTML
    final_html = driver.page_source
    driver.quit()

    # Use Beautiful Soup to parse the final HTML
    soup = BeautifulSoup(final_html, 'html.parser')
    products = soup.find_all('div', class_='caption')

    # Find elements containing products and print them
    for product in products:
        name = product.find('a', {'title': True}).get(
            'title', 'No title attribute')
        price = product.find('h4', class_='price').text
        print(f'Product Name: {name}, Price: {price}')


# Main function to decide which parsing function to use
def main(url, is_dynamic):
    if is_dynamic:
        print("JAVASCRIPT")
        parse_dynamic_content(url)
    else:
        parse_static_html(url)


# Example usage
main("http://quotes.toscrape.com", is_dynamic=False)
# main("https://www.webscraper.io/test-sites/e-commerce/allinone", is_dynamic=True)
