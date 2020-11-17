"""
WSGI config for cdk_test project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import awsgi

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cdk_test.settings')

application = get_wsgi_application()

def lambda_handler(event, context):
        return awsgi.response(application, event, context, base64_content_types={"image/png"})
