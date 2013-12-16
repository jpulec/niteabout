from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

import stripe

from niteabout.apps.events.models import Event

class EventView(DetailView, FormView):
    template_name = "events/event.html"
    model = Event
    context_object_name = "event"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        stripe.api_key = "sk_test_mfZIJyxJSBs9pMLDdGs4IG2r"
        token = request.POST['stripeToken']

        try:
            charge = stripe.Charge.create(
                            amount=self.object.cost, # amount in cents, again
                            currency="usd",
                            card=token,
                            description="payinguser@example.com"
                        )
        except stripe.CardError as e:
            pass
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('signup_done')
