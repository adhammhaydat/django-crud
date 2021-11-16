from django.urls import path
from .views import (SnackCreateView,
                    SnackDeleteView,
                    SnackListDetail,
                    SnackListView,
                    SnackUpdatView)
urlpatterns = [
    path('',SnackListView.as_view(),name = 'snack_view'),
    path('<int:pk>/',SnackListDetail.as_view(),name = 'list'),
    path('create/',SnackCreateView.as_view(),name = 'create'),
    path('<int:pk>/update/',SnackUpdatView.as_view(), name = 'update'),
    path('<int:pk>/delete/',SnackDeleteView.as_view(), name = 'delete'),
    
]                    