# -*- coding:UTF-8 -*-
from django.shortcuts import render
from rest_framework import status
from django.utils.deprecation import MiddlewareMixin


class ApiMiddleware(MiddlewareMixin):
    @staticmethod
    def process_response(request, response):
        if response.status_code == status.HTTP_403_FORBIDDEN:
            return render(response, 'blog/403.html', locals())

        if response.status_code == status.HTTP_400_BAD_REQUEST:
            return render(response, 'blog/400.html', locals())

        if response.status_code == status.HTTP_404_NOT_FOUND:
            return render(response, 'blog/404.html', locals())

        if response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR:
            return render(response, 'blog/500.html', locals())

        return response

