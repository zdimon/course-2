from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_is_title_ok(self):
        self.browser.get('http://localhost:8081')
        self.assertIn('Welcome', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()
