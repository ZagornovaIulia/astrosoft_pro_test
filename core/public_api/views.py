import time
from rest_framework.response import Response
from rest_framework.views import APIView

class PublicApiView(APIView):
    def get(self, request):
        return Response({'ts': time.time()})
