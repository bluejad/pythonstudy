import sys
from django.views.debug import technical_500_response
from django.conf import settings
from django.http import HttpResponse

class UserBasedExceptionMiddleware(object):
    def process_request(self, request):
        if request.user.is_superuser:
            return HttpResponse("lalalalalalallllllllllllllllll")
            # return technical_500_response(request, *sys.exc_info())