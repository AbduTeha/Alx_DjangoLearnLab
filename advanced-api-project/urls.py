from django.urls import path, include

urlpatterns = [
    # other URL patterns here
    path('api/', include('api.urls')),
]