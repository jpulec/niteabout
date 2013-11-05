from niteabout.apps.business.models import Business


def add_business(request):
    if request.user.is_authenticated():
        return {'businesses': Business.objects.filter(organization_users__user=request.user)}
    return {}

