from django.shortcuts import redirect

from social.pipeline.partial import partial

import logging

from niteabout.apps.main.models import UserProfile

logger = logging.getLogger(__name__)

@partial
def require_profile(strategy, details, user=None, is_new=False, *args, **kwargs):
    if user and hasattr(user, "user_profile") and user.user_profile:
        return
    elif not details.get('user_profile'):
        if strategy.session_get('saved_profile'):
            details['user_profile'] = strategy.session_pop('saved_profile')
        else:
            return redirect('require_profile')

def associate_profile(strategy, details, uid, user=None, profile=None, *args, **kwargs):
    if user and not profile:
        try:
            profile = UserProfile.objects.create(auth=user, **details['user_profile'])
        except Exception as e:
            logger.exception(e)
        else:
            return {'profile': profile,
                    'user': profile.auth}
