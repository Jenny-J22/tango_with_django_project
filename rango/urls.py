from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
	path('', views.index, name='index'),
	#path('admin/', admin.site.urls),
	
	path('about/', views.about, name='about'),
]
