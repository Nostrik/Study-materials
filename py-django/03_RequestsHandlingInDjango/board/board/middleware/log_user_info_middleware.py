from django.core.exceptions import PermissionDenied
import datetime


class UserInfoMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        req_method = request.META.get('REQUEST_METHOD')
        req_url = request.META.get('PATH_INFO')
        log_str = f'[{datetime.datetime.now()}] IP: {ip} Method_HTTP: {req_method} URL: {req_url}'
        print(log_str)
        with open('log_test.txt', 'a') as log_file:
            log_file.write(log_str + '\n')
        response = self.get_response(request)

        return response
