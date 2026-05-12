from django.shortcuts import render
from .models import Payment

def payment_page(request):
    if request.method == "POST":
        card_number = request.POST.get("card_number")

        last4 = card_number[-4:]

        Payment.objects.create(
            card_last4=last4
        )

        return render(request, "success.html")

    return render(request, "payment.html")