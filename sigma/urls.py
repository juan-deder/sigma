from django.http import HttpResponse
from django.urls import path
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from graphene_django.views import GraphQLView


@ensure_csrf_cookie
def csrf_cookie(request):
    return HttpResponse()


urlpatterns = [
    path('csrf-cookie', csrf_cookie),
    path('graphql', csrf_exempt(GraphQLView.as_view())), #r remove csrf_exempt
]
