from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated
from .models import *
from .permissions import *
# Create your views here.


class BooksView(ListCreateAPIView):

    queryset=Book.objects.all()
    serializer_class=BookSerializer
   


class BookDetails(RetrieveUpdateDestroyAPIView):

    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=[IsOwnerOrReadOnly]