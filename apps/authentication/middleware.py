# myapp/middleware.py

from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings


class LogoutRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path != reverse(settings.LOGOUT_REDIRECT_URL):
            return redirect(settings.LOGOUT_REDIRECT_URL)

        response = self.get_response(request)
        return response
