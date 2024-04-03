from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='home'),
	# django's convention is to use a trailing / for 
	# the routE
	path('about/', views.about, name='about'),
	path('finches/', views.finches_index, name="index"),
	path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
]