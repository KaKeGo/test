from django.contrib import admin

from .models import (
    MeMe, MeMeFilters, Category
)

# Register your models here.


admin.site.register([MeMe, Category, MeMeFilters])
