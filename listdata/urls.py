from django.urls import path
from listdata import views

urlpatterns = [
    path('',views.index,name='index'),
]
urlpatterns += [
        path('data/', views.DataListView.as_view(), name='datos'),
        ]
urlpatterns += [
        path('data/<int:pk>',views.DataListDetailView.as_view(),\
             name='datos-detail')
        ]
urlpatterns += [
        path('search/', views.FileSearchView.as_view(), name='search'),
        ]