from niteabout.apps.beerpong.models import Match, Round, Team, Tournament

from niteabout.apps.main.models import UserProfile

def run():
    profs = UserProfile.objects.all()
    count = 0
    for player1, player2 in zip(profs[0::2], profs[1::2]):
        team = Team.objects.create(player1=player1, player2=player2, name="Team " + unicode(count))
        count += 1
    teams = Team.objects.all()
    round = Round.objects.get(number=1)
    for home, away in zip(teams[0::2], teams[1::2]):
        match = Match.objects.create(round=round, match_type="n", home=home, away=away)

