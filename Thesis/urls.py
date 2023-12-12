from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.manage, name='Manage'),
    path('AddThesis/', views.AddThesis, name='AddThesis'),
    # path('Message/',views.Message,name='Message'),
    path('Search/',views.Search_by_Name,name='Search_by_Name'),
    path('Search_by_Area/',views.Search_by_Area,name='Search_by_Area'),
    path('Search_by_Tech/',views.Search_by_Tech_used,name='Search_by_Tech_used'),
    path('List/',views.ListThesis,name='List'),
    path('Remove/',views.Remove,name='Remove'),
    path('RemoveThesis/<tname>/',views.RemoveThesis,name='RemoveThesis'),
    path('Report/',views.Report,name='Report'),
    
    
    
]
