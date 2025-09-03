import os
import random
import sys
import time
from datetime import datetime

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class DuckDuckGoScraper:
    """
    A class to scrape DuckDuckGo for a given search term.
    """

    def __init__(self, output_dir: str, script_name: str):
        """
        Initializes the DuckDuckGoScraper.

        :param output_dir: The directory to save screenshots to.
        """
        self.output_dir = output_dir
        self.script_name = script_name
        self.driver = self._init_driver()

    @staticmethod
    def _init_driver() -> WebDriver:
        """
        Initializes the Firefox WebDriver.

        :return: The initialized WebDriver.
        """
        print("Initializing the Firefox WebDriver...")
        options = Options()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)
        print("WebDriver initialized successfully.")
        return driver

    def search(self, search_term: str):
        """
        Searches DuckDuckGo for the given search term.

        :param search_term: The term to search for.
        """
        try:
            print(f"Navigating to https://duckduckgo.com/")
            self.driver.get('https://duckduckgo.com/')
            self._wait_random_time()

            print(f"Searching for '{search_term}'...")
            self._send_keys((By.XPATH, "//input[@id='searchbox_input']"), search_term)
            self._wait_random_time()

            self._get_element((By.XPATH, "//button[@aria-label='Search']")).click()
            self._wait_random_time()
            print("Search successful.")

        finally:
            self._save_screenshot()
            self.driver.quit()
            print("WebDriver closed.")

    def _send_keys(self, locator: tuple[str, str], text: str, timeout: int = 10):
        """
        Finds an element and sends keys to it.

        :param locator: The locator of the element.
        :param text: The text to send.
        :param timeout: The maximum time to wait for the element.
        """
        print(f"Sending keys '{text}' to element {locator}...")
        element = self._get_element(locator, timeout)
        element.send_keys(text)

    def _get_element(self, locator: tuple[str, str], timeout: int = 10) -> WebElement:
        """
        Finds and returns an element.

        :param locator: The locator of the element.
        :param timeout: The maximum time to wait for the element.
        :return: The found WebElement.
        """
        print(f"Getting element {locator}...")
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(ec.visibility_of_element_located(locator))
        return element

    def _get_optional_element(self, locator: tuple[str, str], timeout: int = 10) -> WebElement | None:
        """
        Finds and returns an element if it exists, otherwise returns None.

        :param locator: The locator of the element.
        :param timeout: The maximum time to wait for the element.
        :return: The found WebElement or None.
        """
        try:
            return self._get_element(locator, timeout)
        except TimeoutException:
            return None

    def _save_screenshot(self):
        """
        Saves a screenshot of the current page with a timestamp and script name prefix.
        """
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        screenshot_name = f"{self.output_dir}/{self.script_name}_screenshot_{timestamp}.png"
        self.driver.save_screenshot(screenshot_name)
        print(f"Screenshot saved as {screenshot_name}")

    @staticmethod
    def _wait_random_time(min_milliseconds: int = 500, max_milliseconds: int = 1500):
        """
        Waits for a random amount of time.

        :param min_milliseconds: The minimum time to wait in milliseconds.
        :param max_milliseconds: The maximum time to wait in milliseconds.
        """
        random_duration = random.uniform(min_milliseconds, max_milliseconds) / 1000
        print(f"Waiting for {random_duration:.2f} seconds...")
        time.sleep(random_duration)


def main():
    """
    Main function to run the scraper.
    """
    print("Starting the web scraping process...")
    scraper_output_dir = os.getenv('SCRAPER_OUTPUT_DIR')
    if not scraper_output_dir:
        raise ValueError("SCRAPER_OUTPUT_DIR environment variable not set.")

    # Get the name of the current script without the .py suffix
    script_name, _ = os.path.splitext(os.path.basename(sys.argv[0]))

    scraper = DuckDuckGoScraper(scraper_output_dir, script_name)
    scraper.search("Python Selenium Example")


if __name__ == "__main__":
    main()
