from django.http import HttpResponse


class StripeWH_Handler:
    """Handles Stripe webhooks to notify
    application when an event happens"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handles a generic or unknown webhook events
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
