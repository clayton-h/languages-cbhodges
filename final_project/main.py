from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service  # Import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Setup Edge options
edge_options = Options()
edge_options.add_argument("--headless")  # Runs Edge in headless mode

# Use WebDriver Manager to manage the Edge driver
# The EdgeChromiumDriverManager().install() returns the path to the edge driver executable as a string
# The Service class is used to create a service with that path
driver = webdriver.Edge(service=Service(
    EdgeChromiumDriverManager().install()), options=edge_options)

url = "http://quotes.toscrape.com/js/"

# Use the browser to get the URL
driver.get(url)

# Use WebDriverWait instead of time.sleep()
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.text")))

# Now that the necessary elements are visible, get the final HTML
final_html = driver.page_source
driver.quit()

# Use Beautiful Soup to parse the final HTML
soup = BeautifulSoup(final_html, 'html.parser')

# Now you can find elements as if it's a static page
quotes = soup.find_all('span', class_='text')
for quote in quotes:
    print(quote.text)
