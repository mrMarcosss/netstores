import os
import time
import datetime
from django.conf import settings


class RequestLogMiddleware(object):
    def __init__(self):
        self.log_fn = os.path.join(settings.BASE_DIR, 'requests.log')

    def process_request(self, request):
        self.start_time = time.time()

    def process_response(self, request, response):
        with open(self.log_fn, 'a') as f:
            f.write('[{dt}] {method} {url} ~ {t:.5f}\n'.format(
                dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                method=request.method,
                url=request.build_absolute_uri(),
                t=(time.time() - self.start_time)
            ))
        return response