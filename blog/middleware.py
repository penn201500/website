# -*- coding:UTF-8 -*-
import json

from django.shortcuts import render
from rest_framework import status
from django.utils.deprecation import MiddlewareMixin


class ApiMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if response.status_code == status.HTTP_403_FORBIDDEN:
            return render(request, 'blog/403.html', locals())

        if response.status_code == status.HTTP_400_BAD_REQUEST:
            return render(request, 'blog/400.html', locals())

        if response.status_code == status.HTTP_404_NOT_FOUND:
            return render(request, 'blog/404.html', locals())

        if response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR:
            return render(request, 'blog/500.html', locals())

