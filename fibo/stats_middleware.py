import time
from django.utils.deprecation import MiddlewareMixin


class StatsMiddleware(MiddlewareMixin):



    def __call__(self, request):
        "Calculate and output the page generation duration"
        # Get the start time from the request and calculate how long
        # the response took.
        request.start_time = time.time()
        response = self.get_response(request)
        duration = time.time() - request.start_time

        # Add the header.
        response["X-Page-Generation-Duration-ms"] = int(duration * 1000)
        return response