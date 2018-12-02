from django.contrib import admin

# Register your models here.

from .models import Question, Choice, Category, News


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['Name']


admin.site.register([Question, Choice])
admin.site.register(Category, CategoryAdmin)
admin.site.register(News)


