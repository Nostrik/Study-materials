from django.core.exceptions import PermissionDenied
from time import sleep, time
from datetime import datetime


class FilterIPMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        allowed_ips = ['127.0.0.1']
        ip = request.META.get('REMOTE_ADDR')
        if ip not in allowed_ips:
            raise PermissionDenied

        response = self.get_response(request)

        return response


class DelayMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        sleep(0)
        response = self.get_response(request)

        return response


class CountIPMiddleware:

    time_memory = []
    time_now = 0
    n = 0

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if len(self.time_memory) == 0:
            self.time_memory.append({ip: time()})
            print(self.time_memory)
        else:
            for ip_dict in self.time_memory:
                if ip in ip_dict:
                    # print('ip find!', f'time is - {ip_dict[ip]}')
                    self.time_now = time()
                    time_check = self.time_now - ip_dict[ip]
                    # print('elapsed time since request -', time_check)
                    ip_dict[ip] = self.time_now
                    if time_check <= self.n:
                        # print('RAISE EXCEPTION!!')
                        raise PermissionDenied

        response = self.get_response(request)

        return response

