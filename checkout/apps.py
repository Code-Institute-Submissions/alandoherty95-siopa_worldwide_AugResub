from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        """
        Updates order total when a line item is saved or deleted
        """
        import checkout.signals
