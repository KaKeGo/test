from rest_framework import serializers

from .models import(
    MeMe, Category, MeMeFilters
)


class MeMeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MeMe
        fields = [
            'id', 'title', 'img', 'upvotes', 'downvotes', 'category',
            'filters', 'create_on', 'updated_on'
        ]

class MeMeCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MeMe
        fields = [
            'title', 'img', 'category', 'filters'
        ]
    
class MeMeDetailsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MeMe
        fields = [
            'id', 'title', 'img'
        ]
        
class MeMeUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MeMe
        fields = [
            'title'
        ]

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = [
            'id', 'title'
        ]
        
class CategoryCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['title']
                
class CategoryUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['title']
        
class MeMeFilterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MeMeFilters
        fields = [
            'id', 'title'
        ]

class MeMeFilterCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MeMeFilters
        fields = ['title']

        
class MeMeFilterUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['title']
