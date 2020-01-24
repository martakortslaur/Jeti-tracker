from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm
from django.conf import settings
from django.utils import timezone
from features.models import Feature
import stripe

stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    if request.method == "POST":
    
        payment_form = MakePaymentForm(request.POST)

        if payment_form.is_valid():

            cart = request.session.get('cart', {})
            total = 0

            for id, quantity in cart.items():
                feature = get_object_or_404(Feature, pk=id)
                total += quantity * 5

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            
            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('upvote_feature'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            messages.error(
                request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
    
    return render(request, "checkout.html", {"payment_form": payment_form,
                                            "publishable": settings.STRIPE_PUBLISHABLE})
