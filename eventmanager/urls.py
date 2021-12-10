from django.urls import path

from . import views

urlpatterns = [
    path('',views.EventAPIView.as_view()),
    path('<str:day>',views.EventDetail.as_view()),
    path('<int:pk>/<str:day>',views.EventDelete.as_view())
    # path('delete/<str:pk>',views.EventDetail.as_view())

    
    ]