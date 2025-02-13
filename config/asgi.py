import os
from django.core.asgi import get_asgi_application
from starlette.staticfiles import StaticFiles

"""
Settings
"""
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')


"""
Django settings
"""
django_app = get_asgi_application()


"""
FastAPI settings
"""
from fastapi import FastAPI
from users.routers import user_router, auth_router
from blocks.routers.block import block_router
from providers.routers.provider import provider_router

fastapi_app = FastAPI()

fastapi_app.include_router(provider_router, tags=["providers"], prefix="/providers")
fastapi_app.include_router(block_router, tags=["blocks"], prefix="/blocks")
# routers
fastapi_app.include_router(user_router, tags=["users"], prefix="/users")
fastapi_app.include_router(auth_router, tags=["auth"], prefix="/auth")

# to mount Django
fastapi_app.mount("/django", django_app)
fastapi_app.mount("/static", StaticFiles(directory="static"), name="static")
