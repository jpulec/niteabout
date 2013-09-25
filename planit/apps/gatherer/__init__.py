import logging
from planit.apps.gatherer.models import PLACE_TYPES

logger = logging.getLogger(__name__)


def init_scheduler():

    import django_rq
    import tasks
    from collections import defaultdict
    import datetime

    scheduler = django_rq.get_scheduler('default')

    jobs = scheduler.get_jobs()

    functions = defaultdict(lambda: list())

    map(lambda x: functions[(x.func, x.args)].append(x.meta.get('interval')), jobs)

    now = datetime.datetime.now()

    def schedule_once(func, args, interval):
        if not (func, args) in functions or not interval in functions[(func, args)] or len(functions[(func, args)]) > 1:
            map(scheduler.cancel, filter(lambda x: (x.func, x.args)==(func, args), jobs))
            scheduler.schedule(now, func, args, interval=interval)
    for type_, type_name in PLACE_TYPES:
        schedule_once(tasks.google_scrape, (type_,), interval=86400)


init_scheduler()
