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
    path("submissions/", SubmissionList.as_view(), name="submission"),
    path("response/", ResponseList.as_view(), name="response"),
    #path("writtenres/", WrittenResponseList.as_view(), name="written response"),
    path("multiplechoicequestion/", MultipleChoiceQuestionList.as_view(), name="multiple question"),
    path("writtenquestion/", WrittenQuestionList.as_view(), name="written question"),

]
#will all the data be sent through one submission