from rest_framework import generics
from .serializers import *

class EmailView(generics.CreateAPIView):
    serializer_class=EmailSerializer
    queryset=Email.objects.all()
    