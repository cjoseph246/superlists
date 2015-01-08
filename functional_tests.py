
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Chuck heard about a brand new to-do app.  He goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                         inputbox.get_attribute('placeholder'),
                         'Enter a to-do item'
                         )

        # He types "Learn TDD testing" into a text box
        inputbox.send_keys('Learn TDD testing')

        # When he hits enter, the page updates, and now the pages lists
        # "1: Learn TDD testing" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
                        any(row.text == '1: Learn TDD testing' for row in rows)
                        )

        # There is still a text box inviting him to add another item.
        # He enters "Buy a testing goat"
        self.fail('Finish the test!')

# The page updates again, and now shows both items on his list

# Chuck wonders whether the site will remember his list. Then he sees
# that the site has generated a unique URL for him -- some explanatory
# text to that effect.

# She visits that URL - his to-do list is still there.

# Satisfied, he goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')