import logging
import requests
import clearbit

from django.conf import settings

from .models import User, ClearBitProfile
from soc_network_proj.celery import app


logger = logging.getLogger('user')


@app.task()
def clearbit_enrichment_task(user_id):
    user = User.objects.get(pk=user_id)
    clearbit.key = settings.CLEARBIT_API_KEY
    try:
        response = clearbit.Enrichment.find(email=user.email)
    except requests.exceptions.RequestException:
        logger.warning(f'An error occurred while performing the clearbit enrichment for user {user_id}')
    else:
        if response:
            if 'pending' in response:
                pass
            else:
                clearbit_data = {}
                if 'person' in response:
                    clearbit_data['clearbit_id'] = response['person']['id']
                    clearbit_data['clearbit_full_name'] = response['person']['name']['fullName']
                    clearbit_data['clearbit_given_name'] = response['person']['name']['givenName']
                    clearbit_data['clearbit_family_name'] = response['person']['name']['familyName']
                if 'company' in response:
                    clearbit_data['clearbit_comp_id'] = response['company']['id']
                    clearbit_data['clearbit_comp_name'] = response['company']['name']
                    clearbit_data['clearbit_comp_legal_name'] = response['company']['legalName']
                    clearbit_data['clearbit_comp_domain'] = response['company']['domain']
                ClearBitProfile.objects.create(user=user, **clearbit_data)
                user.clearbit_enriched = True
                user.save()
                logger.info(f'Successfully completed clearbit enrichment for user {user_id}')


@app.task()
def hunter_verify_task(user_id):
    user = User.objects.get(pk=user_id)
    query_params = {'email': user.email, 'api_key': settings.EMAIL_HUNTER_API_KEY}
    try:
        response = requests.get(settings.EMAIL_HUNTER_API_ENDPOINT, params=query_params)
    except requests.exceptions.RequestException:
        logger.warning(f'An error occurred while performing the hunter verify for user {user_id}')
    else:
        if response.status_code == 200:
            response = response.json()
            if response['data']['status'] not in ('invalid', 'disposable', 'unknown'):
                user.hunter_verified = User.HUNTER_VALID
            else:
                user.hunter_verified = User.HUNTER_NOT_VALID
            user.save()
            logger.info(f'Successfully completed hunter verify for user {user_id}')
        else:
            logger.warning(f'An error occurred while performing the hunter verify for user {user_id}')