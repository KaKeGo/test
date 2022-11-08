from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Contact
from .serializer import (
    ContactSerializer,
)
# Create your views here.


@api_view(['GET'])
def contact_list_view(request):
    contact = Contact.objects.all()
    if not contact.exists:
        return Response({'message': 'Somethin went wrong'})
    serializer = ContactSerializer(contact, mant=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
