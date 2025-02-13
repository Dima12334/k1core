import os
from django.core.asgi import get_asgi_application
from starlette.staticfiles import StaticFiles

"""
Settings
"""
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")


"""
Django settings
"""
django_app = get_asgi_application()


"""
FastAPI settings
"""
from fastapi import FastAPI, APIRouter
from users.routers import user_router, auth_router
from blocks.routers.block import block_router
from providers.routers.provider import provider_router

fastapi_app = FastAPI()

# routers
api_v1_router = APIRouter(prefix="/api/v1")
api_v1_router.include_router(provider_router, tags=["providers"], prefix="/providers")
api_v1_router.include_router(block_router, tags=["blocks"], prefix="/blocks")
api_v1_router.include_router(user_router, tags=["users"], prefix="/users")
api_v1_router.include_router(auth_router, tags=["auth"], prefix="/auth")

fastapi_app.include_router(api_v1_router)

# to mount Django
fastapi_app.mount("/django", django_app)
fastapi_app.mount("/static", StaticFiles(directory="static"), name="static")
