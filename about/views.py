from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .models import About
from .serializer import (
    AboutSerializer
)

# Create your views here.


@api_view(['GET'])
def about_list_view(request):
    about = About.objects.all()
    if not about.exists:
        return Response({'message': 'Something went wrong'})
    serializer = AboutSerializer(about, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
