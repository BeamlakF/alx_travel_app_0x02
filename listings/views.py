from django.shortcuts import render
from rest_framework import viewsets
from .models import Listing, Booking, Payment
from .serializers import ListingSerializer, BookingSerializer

class ListingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Listing instances.
    Provides: list, create, retrieve, update, destroy
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Booking instances.
    Provides: list, create, retrieve, update, destroy
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

