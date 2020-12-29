import random
import configparser

from rest_framework.test import APILiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver

from .helpers import gen_random_sentence, gen_random_post_body


class SeleniumAutomatedBotTests(APILiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        config = configparser.ConfigParser()
        try:
            config.read('../config.ini')
            cls.users_count = int(config['Automated Bot']['number_of_users'])
            cls.posts_per_user = int(config['Automated Bot']['max_posts_per_user'])
            cls.likes_per_user = int(config['Automated Bot']['max_likes_per_user'])
        except (configparser.Error, KeyError):
            cls.users_count = 5
            cls.posts_per_user = 3
            cls.likes_per_user = 5

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_selenium_automated_bot(self):
        # SignUp and Create Posts
        for i in range(self.users_count):
            # SignUp
            self.selenium.get('http://localhost:8080/signup')
            email_input = self.selenium.find_element_by_id('email')
            email_input.send_keys(f'user{i}@example.com')
            password_input = self.selenium.find_element_by_id('password')
            password_input.send_keys(f'user123{i}')
            password_repeat_input = self.selenium.find_element_by_id('password_repeat')
            password_repeat_input.send_keys(f'user123{i}')
            self.selenium.find_element_by_id('submit').click()
            # SignIn
            self.selenium.get('http://localhost:8080/signin')
            email_input = self.selenium.find_element_by_id('email')
            email_input.send_keys(f'user{i}@example.com')
            password_input = self.selenium.find_element_by_id('password')
            password_input.send_keys(f'user123{i}')
            self.selenium.find_element_by_id('submit').click()
            # Posts Create
            for k in range(self.posts_per_user):
                self.selenium.find_element_by_id('create').click()
                title_input = self.selenium.find_element_by_id('title')
                title_input.send_keys(gen_random_sentence(random.randint(5, 10)))
                body_input = self.selenium.find_element_by_id('body')
                body_input.send_keys(gen_random_post_body(random.randint(5, 10)))
                self.selenium.find_element_by_id('submit').click()
            self.selenium.find_element_by_id('logout').click()

        # SignIn and Like Posts
        for j in range(self.users_count):
            # SignIn
            self.selenium.get('http://localhost:8080/signin')
            email_input = self.selenium.find_element_by_id('email')
            email_input.send_keys(f'user{i}@example.com')
            password_input = self.selenium.find_element_by_id('password')
            password_input.send_keys(f'user123{i}')
            self.selenium.find_element_by_id('submit').click()
            self.selenium.get('http://localhost:8080/posts/all')
            # Like
            links = self.selenium.find_elements_by_css_selector('td p a')
            for n in range(self.posts_per_user):
                links[n].click()
                self.selenium.find_element_by_id('like').click()
                self.selenium.back()
            self.selenium.find_element_by_id('logout').click()