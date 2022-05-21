import time

from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "https://webscraper.io/test-sites/e-commerce/allinone"


def get_driver():
    time.sleep(3)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")

    driver = webdriver.Remote(
    command_executor='http://headless_chrome:3000/webdriver',
        options=chrome_options,
    )
    return driver


def main():
    driver = get_driver()
    driver.get(URL)
    driver.implicitly_wait(10)

    products = driver.find_elements(By.XPATH, '//div[@class="col-sm-4 col-lg-4 col-md-4"]')
    
    for product in products:
        product_title = product.find_element(By.XPATH, './/a[@class="title"]').text
        product_price = product.find_element(By.XPATH, './/h4[@class="pull-right price"]').text
        product_description = product.find_element(By.XPATH, './/p[@class="description"]').text
        product_reviews_count = product.find_element(By.XPATH, './/div[@class="ratings"]').text

        print(product_title, product_price, product_description)


if __name__ == '__main__':
    main()