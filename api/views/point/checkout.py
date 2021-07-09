import math

import stripe
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from accounts.models import CustomUser


stripe.api_key = settings.STRIPE_SECRET_KEY


@api_view(['POST'])
@permission_classes([AllowAny])
def test_payment(request):
    test_payment_intent = stripe.PaymentIntent.create(
        amount=1000, currency='jpy',
        payment_method_types=['card'],
        receipt_email='test@example.com')
    return Response(status=status.HTTP_200_OK, data=test_payment_intent)


@api_view(['POST'])
def save_stripe_info(request):
    data = request.data
    name = data['name']
    email = data['email']
    payment_method_id = data['payment_method_id']

    customer_data = stripe.Customer.list(email=email).data

    if len(customer_data) == 0:
        customer = stripe.Customer.create(
            name=name, email=email, payment_method=payment_method_id)
    else:
        customer = customer_data[0]

    try:
        stripe.PaymentIntent.create(
            customer=customer,
            payment_method=payment_method_id,
            currency='jpy',
            amount=math.ceil(data['amount']*1.038),
            confirm=True
        )
    except Exception:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': '決済に失敗しました'})

    user = CustomUser.objects.get(email=email)
    user.own_point = user.own_point + data['amount']
    user.save()
    return Response(status=status.HTTP_200_OK,
                    data={'message': 'Success'})
