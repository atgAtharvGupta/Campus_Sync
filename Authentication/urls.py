from django.urls import path
from . import views

app_name = 'Authentication'

urlpatterns = [
    path('login/', views.loginAuth, name='Login'),
    path('register/', views.registerAuth, name='Register'),
    path('logout/', views.logoutAuth, name='Logout'),
    # Make sure these URLs match what's referenced in the JS
    path('get-course/', views.get_course, name='GetCourse'),
    path('get-branch/', views.get_branch, name='GetBranch'),
    path('get-semester/', views.get_semester, name='GetSemester'),
]
