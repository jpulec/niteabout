from django.views.generic import TemplateView
from django.views.generic.edit import FormView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth import login

from niteabout.apps.business.forms import BusinessSignupForm, BusinessUpdateForm
from niteabout.apps.business.models import Business

class BusinessView(FormView):
    template_name = "business/main.html"
    form_class = BusinessSignupForm
    success_url = "/"

    def form_valid(self, form):
        form.instance.backend = 'django.contrib.auth.backends.ModelBackend'
        self.object = form.save()
        login(self.request, self.object)
        return super(BusinessView, self).form_valid(form)

class BusinessProfile(UpdateView):
    context_object_name = "business"
    model = Business
    form_class = BusinessUpdateForm

    def get(self, request, *args, **kwargs):
        pk = kwargs.pop('pk', None)
        try:
            business = Business.objects.get(id=pk, owner__organization_user__user=request.user)
            return super(BusinessProfile, self).get(request, *args, **kwargs)
        except Business.DoesNotExist:
            self.object = self.get_object()
            return self.render_to_response(self.get_context_data(business=self.object))

    def post(self, request, *args, **kwargs):
        pk = kwargs.pop('pk', None)
        try:
            business = Organization.objects.get(id=pk, owner__organization_user__user=request.user)
            super(BusinessProfile, self).post(request, *args, **kwargs)
        except Business.DoesNotExist as e:
            logger.exception(e)

class BusinessPush(TemplateView):
    template_name = "business/push.html"
