from django.contrib import admin
from dogs.models import Dog, Category

@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'birthday',)
    list_filter = ('category',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)