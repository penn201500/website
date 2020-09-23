# -*- coding:UTF-8 -*-
import json
from rest_framework import status
from django.utils.deprecation import MiddlewareMixin


class ApiMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        message = ""
        code = 1

        if response.status_code == status.HTTP_403_FORBIDDEN:
            code = 4
            message = "您没有执行此操作的权限，请联系管理员获取相应的权限。"

        if response.status_code == status.HTTP_400_BAD_REQUEST and not message:
            message = "缺少必要的请求参数或参数错误"
            code = 2

        if response.status_code == status.HTTP_404_NOT_FOUND:
            message = "Page Not Found"
            code = 2

        response.content = json.dumps({
            "code": code,
            "message": message,
        })
        return response
