Simple project that imitates social network based on Django and Django REST framework.

The project consists of two small apps: 
core (declaring custom user model and apiview for create(signup) users) 
and post(declaring post model and views for create, retrieve and like/unlike posts).
"Run" app exists to run the frontend as a staticfiles.

As database Postgresql 10 is used.

Clearbit.com and hunter.io are used for enrichment and email verify user respectively on signup with Celery tasks,
so users signup without valid status from hunter.io is possible.

JWT authentication is realized with djangorestframework-simplejwt package.

Vue.js 2 with vuex are used as frontend library.

Automated bot is realized with DRF APIClient(tests.py in post module).

