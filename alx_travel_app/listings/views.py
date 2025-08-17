from django.shortcuts import render
from rest_framework import viewsets
from .models import Listing, Booking, Payment
from .serializers import ListingSerializer, BookingSerializer
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .models import Payment

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



class InitiatePaymentView(APIView):
    def post(self, request):
        booking_reference = request.data.get("booking_reference")
        amount = request.data.get("amount")
        email = request.data.get("email")

        # Create payment record
        payment = Payment.objects.create(
            booking_reference=booking_reference,
            amount=amount,
            status="Pending"
        )

        headers = {
            "Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}",
            "Content-Type": "application/json",
        }

        data = {
            "amount": str(amount),
            "currency": "ETB",
            "email": email,
            "tx_ref": f"{booking_reference}_{payment.id}",
            "callback_url": "http://localhost:8000/api/payments/verify/",  # adjust later
        }

        response = requests.post("https://api.chapa.co/v1/transaction/initialize",
                                 headers=headers, json=data)

        if response.status_code == 200:
            result = response.json()
            payment.transaction_id = result["data"]["tx_ref"]
            payment.save()
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)

class VerifyPaymentView(APIView):
    def get(self, request):
        tx_ref = request.query_params.get("tx_ref")

        headers = {
            "Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}",
        }

        response = requests.get(f"https://api.chapa.co/v1/transaction/verify/{tx_ref}",
                                headers=headers)

        if response.status_code == 200:
            result = response.json()
            try:
                payment = Payment.objects.get(transaction_id=tx_ref)
                if result["data"]["status"] == "success":
                    payment.status = "Completed"
                else:
                    payment.status = "Failed"
                payment.save()
            except Payment.DoesNotExist:
                return Response({"error": "Payment not found"}, status=404)

            return Response(result, status=200)
        return Response(response.json(), status=400)
