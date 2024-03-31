import unittest
import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class TestATGConnection(unittest.TestCase):

    def test_connection(self):
        logging.info("Starting ATG connection test...")
        url = "https://atg.world"

        try:
            logging.info("Attempting to connect to ATG website...")
            response = requests.get(url, timeout=5)  # Set a timeout
            response.raise_for_status()  # Raise an exception for error status codes

            logging.info("Connection successful!")
            self.assertTrue(True)  # Test passes

        except requests.exceptions.RequestException as e:
            logging.error("Connection failed: {}".format(e))
            self.fail("Website connection failed.")


if __name__ == '__main__':
    unittest.main()
