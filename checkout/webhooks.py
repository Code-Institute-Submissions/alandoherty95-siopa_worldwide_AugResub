from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWH_Handler

import stripe

@require_POST
@csrf_exempt
def webhook(request):
    """Listens for Stripe webhooks"""
    # Setup Stripe webhooks
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Gets webhook data and verifies the signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Handles invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Handles invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # Sets up a webhook handler
    handler = StripeWH_Handler(request)

    # Maps webhook events to relevant handler functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }

    # Gets the webhook type from Stripe
    event_type = event['type']
    # If event handler exists, get it from the event map
    event_handler = event_map.get(event_type, handler.handle_event)

    # Calls the event handler with the event
    response = event_handler(event)
    return response
