"""
ASGI config for untitled3 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from .websocket import websocket_applciation

# Здесь нужно изменить название вашего проекта !!! а именно vshop
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vshop.settings')  # vshop

django_application = get_asgi_application()  # application


async def application(scope, receive, send):
    if scope['type'] == 'http':
        # Let Django handle HTTP requests
        await django_application(scope, receive, send)
    elif scope['type'] == 'websocket':
        # We'll handle Websocket connections here
        # pass
        await websocket_applciation(scope, receive, send)
    else:
        raise NotImplementedError(f"Unknown scope type {scope['type']}")