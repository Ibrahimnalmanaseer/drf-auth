from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('books',BooksView.as_view(),name='books'),
    path('books/<pk>',BookDetails.as_view(),name='book'),
    path('api-auth/', include('rest_framework.urls'))
]
