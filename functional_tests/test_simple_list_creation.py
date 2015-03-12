
from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Chuck heard about a brand new to-do app.  He goes
        # to check out its homepage
        self.browser.get(self.server_url)

        # He notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'), 'Enter a to-do item'
        )

        # He types "Learn TDD testing" into a text box
        inputbox.send_keys('Learn TDD testing')

        # When he hits enter, the page updates, and now the pages lists
        # "1: Learn TDD testing" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        chuck_list_url = self.browser.current_url
        self.assertRegex(chuck_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Learn TDD testing')

        # There is still a text box inviting him to add another item.
        # He enters "Buy a testing goat"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy a testing goat')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on his list
        self.check_for_row_in_list_table('1: Learn TDD testing')
        self.check_for_row_in_list_table('2: Buy a testing goat')
       
        ##### Now a new user, Jim, comes along to the site. #####
        
       
        ## We use a new browser session to make sure that no information of
        ## Chuck's is coming through from cookies etc
        self.browser.quit()
        time.sleep(2)
        self.browser = webdriver.Firefox()
        time.sleep(2)
        
        # Jim visits the home page. There is no sign of Chuck's list
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Learn TDD testing', page_text)
        self.assertNotIn('testing goat', page_text)
        
        # Jim starts a new list by entering a new item.  He is less
        # interesting than Chuck...
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        
        # Jim gets his own unique URL
        jim_list_url = self.browser.current_url
        self.assertRegex(jim_list_url, '/lists/.+')
        self.assertNotEqual(jim_list_url, chuck_list_url)
        
        # Again, there is no trace of Chuck's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Learn TDD testing', page_text)
        self.assertIn('Buy milk', page_text)

        # Satisfied, they both go back to sleep
