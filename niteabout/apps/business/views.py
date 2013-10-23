from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth import login

from niteabout.apps.business.forms import BusinessSignupForm

class BusinessView(FormView):
    template_name = "business/main.html"
    form_class = BusinessSignupForm
    success_url = "/"

    def form_valid(self, form):
        form.instance.backend = 'django.contrib.auth.backends.ModelBackend'
        self.object = form.save()
        login(self.request, self.object)
        return super(BusinessView, self).form_valid(form)


class BusinessPush(TemplateView):
    template_name = "business/push.html"
