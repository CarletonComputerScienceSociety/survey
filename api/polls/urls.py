from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from .views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Polls API",
        default_version="v1",
        description="tbd",
        terms_of_service="(Top Be Updated)",  # To be Changed
        contact=openapi.Contact(email="contact@ccss.com"),  # To be Changed
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path(
        "poll/<id>",
        PollDetails.as_view(),
        name="poll-details",
    ),
    path(
        "poll/statistics/<id>",
        PollStatistics.as_view(),
        name="poll-statistics",
    ),
]
