import os
import sys
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class WebScraper:
    """
    A generic web scraper class using Selenium.
    """

    def __init__(self, output_dir: str, script_name: str):
        """
        Initializes the WebScraper.

        :param output_dir: The directory to save screenshots to.
        :param script_name: The name of the script running the scraper.
        """
        self.output_dir = output_dir
        self.script_name = script_name
        self.driver = self._init_driver()

    @staticmethod
    def _init_driver() -> WebDriver:
        """
        Initializes the Firefox WebDriver.

        :return: The initialized WebDriver instance.
        """
        print("Initializing the Firefox WebDriver...")
        options = Options()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)
        print("WebDriver initialized successfully.")
        return driver

    def attempt_navigation(self, url: str):
        """
        Attempts to navigate to a given URL.
        It will always take a screenshot, whether the page loads or not,
        and then quits the driver.

        :param url: The URL to navigate to.
        """
        try:
            # Attempt to navigate to the provided URL
            print(f"Navigating to {url}")
            self.driver.get(url)
            print(f"Successfully navigated to {url}")

        finally:
            print("Navigation attempt finished. Taking a screenshot and closing the driver.")
            self._save_screenshot()
            self.driver.quit()
            print("WebDriver closed.")

    def _save_screenshot(self):
        """
        Saves a screenshot of the current page with a timestamp and script name prefix.
        """
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        screenshot_name = f"{self.output_dir}/{self.script_name}_screenshot_{timestamp}.png"
        self.driver.save_screenshot(screenshot_name)
        print(f"Screenshot saved as {screenshot_name}")


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

    scraper = WebScraper(scraper_output_dir, script_name)
    scraper.attempt_navigation("http://nowhere.nowhere/")


if __name__ == "__main__":
    main()
