from django.utils.timezone import datetime
from .models import Log


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        time = datetime.now()
        ip = request.META.get('REMOTE_ADDR')
        user_agent = request.META.get('HTTP_USER_AGENT')
        accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE')

        Log.objects.create(
            timestamp=time,
            ip=ip,
            user_agent=user_agent,
            accept_language=accept_language
        )

        return response