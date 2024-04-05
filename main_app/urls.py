from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # django's convention is to use a trailing / for
    # the routE
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name="index"),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    # CBV's expect the params to be called pk (convention), which is short for primary key,
    # which is another for id
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),

]
