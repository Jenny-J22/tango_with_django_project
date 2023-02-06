from django.contrib import admin
from rango.models import Category, Page

# Register your models here.

class ChoiceInline(admin.TabularInline):
	model = Page


class CategoryAdmin(admin.ModelAdmin):
	
	fieldsets = [
		(None,		{'fields': ['name']}),
		('info',	{'fields': ['views', 'likes']}),
	]
	inlines = [ChoiceInline]
	list_display = ('name', 'views', 'likes')



class PageAdmin(admin.ModelAdmin):
	
	fieldsets = [
		(None,		{'fields': ['category']}),
		('info',	{'fields': ['title', 'url', 'views']}),
	]
	list_display = ('title', 'category', 'url')





admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)

