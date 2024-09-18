from django.contrib import admin
from django.urls import path
from api.views import StudentAPI  # Import the StudentAPI class-based view

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin route
    path('studentapi/', StudentAPI.as_view(), name='student_api'),  # Use .as_view() to handle requests
]
