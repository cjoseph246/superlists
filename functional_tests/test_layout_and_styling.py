
from functional_tests.base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):
    
    def test_layout_and_styling(self):
        # Chuck goes to the home page
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)
        
        # He notices the input box is nicely centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2, 512, delta=5
        )
    
        # He starts a new list and sees the input is nicely centered there too
        inputbox.send_keys('testing\n')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2, 512, delta=5
        )
