import nltk
import random

from nltk.corpus import names

from django.contrib.auth.models import User
from niteabout.apps.main.models import UserProfile

def run():
    name_list = ([name for name in names.words('male.txt')] +
                 [name for name in names.words('female.txt')])
    random.shuffle(name_list)
    for name in name_list[:16]:
        user = User.objects.create(username=name,
                                   password="asdf",
                                   email="test@niteabout.com")
        prof = UserProfile.objects.create(auth=user)
