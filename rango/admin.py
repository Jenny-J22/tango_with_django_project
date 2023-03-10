from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile 


# Register your models here.

class ChoiceInline(admin.TabularInline):
	model = Page


class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}



class PageAdmin(admin.ModelAdmin):
	
	fieldsets = [
		(None,		{'fields': ['category']}),
		('info',	{'fields': ['title', 'url', 'views']}),
	]
	list_display = ('title', 'category', 'url')





admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
