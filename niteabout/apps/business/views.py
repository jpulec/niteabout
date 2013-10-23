from django.views.generic import TemplateView


class BusinessView(TemplateView):
    template_name = "business/main.html"

class BusinessPush(TemplateView):
    template_name = "business/push.html"

    def post(self, request, *args, **kwargs):
        pass
