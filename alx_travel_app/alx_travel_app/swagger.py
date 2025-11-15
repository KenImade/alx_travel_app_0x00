import environ
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

env = environ.Env()

schema_view = get_schema_view(
    openapi.Info(
        title="ALX Travel API",
        default_version="v1",
        description="API documentation for ALX Travel",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
