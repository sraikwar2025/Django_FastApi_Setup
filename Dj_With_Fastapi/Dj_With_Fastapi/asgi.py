"""
ASGI config for Dj_With_Fastapi project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Dj_With_Fastapi.settings')

# application = get_asgi_application()


import os
from django.core.asgi import get_asgi_application
from fastapi.middleware.wsgi import WSGIMiddleware
from fastApi_app.main import app as fastApi_app
from starlette.middleware.cors import CORSMiddleware
from starlette.routing import Mount
from starlette.applications import Starlette

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Dj_With_Fastapi.settings')

application = get_asgi_application()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Dj_With_Fastapi.settings')

# Django ASGI application
django_asgi_app = get_asgi_application()

# Apply CORS middleware
fastApi_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create ASGI application
application = Starlette(
    routes=[
        Mount("/api", app=fastApi_app),
        Mount("/", app=WSGIMiddleware(django_asgi_app)),
    ]
)