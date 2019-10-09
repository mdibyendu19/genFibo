import time
from django.utils.deprecation import MiddlewareMixin



class StatsMiddleware(MiddlewareMixin):

    def process_request(self, request):
        "Store the start time when the request comes in."
        request.start_time = time.time()

    def process_response(self, request, response):
        "Calculate and output the page generation duration"
        # Get the start time from the request and calculate how long
        # the response took.
        duration = time.time() - request.start_time

        # Add the header.
        response["X-Page-Generation-Duration-ms"] = int(duration * 1000)
        response.content = response.content+b" <div class=\"mt-4 text-center\" style=\"position: absolute;top: 50%;left: 65%;-moz-transform: translateX(-50%) translateY(-45%);-webkit-transform: translateX(-50%) translateY(-45%);transform: translateX(-50%) translateY(-45%);\">Time taken "+str.encode(response["X-Page-Generation-Duration-ms"]) + b" ms</p>"
        return response