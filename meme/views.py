from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .models import (
    MeMe, Category, MeMeFilters
)

from .serializer import (
    MeMeSerializer, MeMeDetailsSerializer, MeMeCreateSerializer, MeMeUpdateSerializer,
    MeMeFilterSerializer, MeMeFilterCreateSerializer, MeMeFilterUpdateSerializer,
    CategorySerializer, CategoryCreateSerializer, CategoryUpdateSerializer,
)

# Create your views here.


@api_view(['GET'])
def meme_list_view(request):
    meme = MeMe.objects.all()
    if not meme.exists:
        return Response({'message': 'Something want wrong or memes not avaible'})
    serializer = MeMeSerializer(meme, many=True)
    context = {
        'meme': serializer.data,
    }
    return Response(context, status=status.HTTP_200_OK)

@api_view(['GET'])
def meme_detail_view(request, pk):
    meme = MeMe.objects.filter(id=pk)
    if not meme.exists:
        return Response({'Message': 'Something went wrong or meme not exist'})
    serializer = MeMeDetailsSerializer(meme, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def meme_create_view(request):
    serializer = MeMeCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        meme = serializer.save()
        return Response({'Success': "MeMe {} was created".format(
            meme.title
        )}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MeMe_Update_View(APIView):
    def get(self, request, pk):
        meme = MeMe.objects.filter(id=pk)
        serializer = MeMeSerializer(meme, many=True)
        return Response(serializer.data)
    
    def put(self, request, pk, *args, **kwargs):
        meme = MeMe.objects.filter(id=pk)
        serializer = MeMeUpdateSerializer(meme, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, {'Success': 'MeMe {} was updated successfully'.format(
                serializer.title
            )}, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

class MeMe_Delete_View(APIView):
    def get(self, request, pk):
        meme = MeMe.objects.filter(id=pk)
        serializer = MeMeDetailsSerializer(meme, many=True)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        meme = MeMe.objects.filter(id=pk).delete()
        return Response(status=status.HTTP_200_OK)
        

@api_view(['GET'])
def category_list_view(request):
    category = Category.objects.all()
    if not category.exists:
        return Response({'message': 'Something want wrong or category not avaible'})
    serializer = CategorySerializer(category, many=True)
    context = {
        'category': serializer.data,
    }
    return Response(context, status=status.HTTP_200_OK)

@api_view(['POST'])
def category_create_view(request):
    serializer = CategoryCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        category = serializer.save()
        return Response({'Success': 'Category {} was created'.format(
            category.title
        )}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def memefilters_list_view(request):
    mamefilters = MeMeFilters.objects.all()
    if not mamefilters.exists:
        return Response({'message': 'Something went wrong or memefiters not avaible'})
    serializer = MeMeFilterSerializer(mamefilters, many=True)
    context = {
        'memefilters': serializer.data,
    }
    return Response(context, status=status.HTTP_200_OK)

@api_view(['POST'])
def memefilters_create_view(request):
    serializer = MeMeFilterCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        memefilter = serializer.save()
        return Response({'Success': 'Filter for MeMe {} was added'.format(
            memefilter.title
        )}, status=status.HTTP_201_CREATED)
