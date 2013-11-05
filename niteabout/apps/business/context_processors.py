from niteabout.apps.business.models import Business 


def add_business(request):
    return {'business': Business.objects.get(organization_users__user=request.user)}

