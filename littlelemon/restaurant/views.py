from django.shortcuts import render
import rest_framework
from rest_framework import generics, permissions, viewsets
from .serializers import MenuSerializer, BookingSerializer
from .models import Menu, Booking

def index(request):
    return render(request, 'index.html', {})


# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated] 