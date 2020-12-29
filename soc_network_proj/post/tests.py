import time
import random
import configparser

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient


from core.models import User
from post.models import Post
from .helpers import gen_random_sentence, gen_random_post_body


class AutomatedBotTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        # Start automated bot and preparatory operations
        print('Start Automated Bot...')
        # Create DRF APIClient
        cls.client = APIClient()
        time.sleep(2)
        print('Reading config file...')
        time.sleep(2)
        # Reading configuration from config.ini
        config = configparser.ConfigParser()
        try:
            config.read('../config.ini')
            cls.users_count = int(config['Automated Bot']['number_of_users'])
            cls.posts_per_user = int(config['Automated Bot']['max_posts_per_user'])
            cls.likes_per_user = int(config['Automated Bot']['max_likes_per_user'])
            print('Reading configuration file was completed successfully')
        except (configparser.Error, KeyError):
            print('There was an error during reading config file. Using default values...')
            time.sleep(2)
            cls.users_count = 5
            cls.posts_per_user = 3
            cls.likes_per_user = 5
        print(f'Number of users to create: {cls.users_count}')
        print(f'Number of posts per user to create: {cls.posts_per_user}')
        print(f'Number of likes per user: {cls.likes_per_user}')
        print('Preparatory operations were executed successfully')
        super(AutomatedBotTests, cls).setUpClass()

    def test_automated_bot(self):
        print('User creation, signin and posts creation operations are performing...')
        time.sleep(2)
        for i in range(self.users_count):
            # Signup
            signup_data = {'email': f'user{i}@example.com', 'password': f'user123{i}',
                           'password_repeat': f'user123{i}'}
            signup_response = self.client.post('/api/v1/accounts/create/', signup_data, format='json')
            # Signin for create posts
            if signup_response.status_code == status.HTTP_201_CREATED:
                print(f'User with email {signup_data["email"]} was created successfully')
                signup_data.pop('password_repeat')
                signin_response = self.client.post('/api/v1/token/', signup_data, format='json')
                # Posts create
                if signin_response.status_code == status.HTTP_200_OK:
                    print(f'User with email {signup_data["email"]} was signin successfully')
                    access_token = signin_response.data['access']
                    self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
                    for k in range(self.posts_per_user):
                        post_create_response = self.client.post('/api/v1/post/create/',
                                                                {'title': gen_random_sentence(random.randint(5, 10)),
                                                                 'body': gen_random_post_body(random.randint(5, 10))},
                                                                format='json')
                        if post_create_response.status_code == status.HTTP_201_CREATED:
                            print('Post was created successfully')
                        else:
                            print('Failed to create post')
                else:
                    print(f'Failed to signin user with email {signup_data["email"]}')
            else:
                print(f'Failed to create user with email {signup_data["email"]}')
        print('User creation, signin and posts creation operations was performed')

        print('Posts like operations are performing...')
        time.sleep(2)
        # Signin for posts like
        for i in range(self.users_count):
            signin_data = {'email': f'user{i}@example.com', 'password': f'user123{i}'}
            signin_response = self.client.post('/api/v1/token/', signin_data, format='json')
            if signin_response.status_code == status.HTTP_200_OK:
                print(f'User with email {signin_data["email"]} was signin successfully')
                access_token = signin_response.data['access']
                self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
                user = User.objects.get(email=signin_data['email'])
                not_own_posts = Post.objects.exclude(owner=user)
                for k in range(self.likes_per_user):
                    random_post = random.choice(not_own_posts)
                    post_like_response = self.client.post(f'/api/v1/post/{random_post.id}/like/',
                                                          {'action': 'like'}, format='json')
                    not_own_posts = not_own_posts.exclude(pk=random_post.id)
                    if post_like_response.status_code == status.HTTP_202_ACCEPTED:
                        print('Post was liked successfully')
                    else:
                        print('Failed to like post')
            else:
                print(f'Failed to signin user with email {signin_data["email"]}')
        print('Posts like operations are performed')

        # Final operations and shutdown automated bot
        print('Shutdown Automated bot...')
        time.sleep(2)
        print('Users were created: ', User.objects.count())
        print('Posts were created: ', Post.objects.count())
        posts_likes = 0
        for post in Post.objects.all():
            posts_likes += len(post.users_liked.all())
        print('Number of posts likes: ', posts_likes)
        time.sleep(2)
        print('Automated bot was turned off')
















