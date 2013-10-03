import logging
from planit.apps.gatherer.tasks import parse_openstreetmap, scrape_fandango, scrape_onconnect

logger = logging.getLogger(__name__)


def init_scheduler():

    import django_rq
    import tasks
    from collections import defaultdict
    import datetime

    scheduler = django_rq.get_scheduler('default')

    jobs = scheduler.get_jobs()

    functions = defaultdict(lambda: list())

    map(lambda x: functions[(x.func, x.args)].append(x.meta), jobs)

    now = datetime.datetime.now()

    def schedule_once(func, func_args, *args, **kwargs):
        if not (func, func_args) in functions or not args in functions[(func, func_args)] or not kwargs in functions[(func, func_args)] or len(functions[(func, func_args)]) > 1:
            map(scheduler.cancel, filter(lambda x: (x.func, x.args)==(func, func_args), jobs))
            scheduler.schedule(now, func, func_args, *args, **kwargs)

    schedule_once(parse_openstreetmap, ('planit/osm/madison.osm.bz2',), interval=60*24*7, timeout=-1)
    schedule_once(scrape_onconnect, ("53703",), interval=60*24*7, timeout=-1)
    #schedule_once(scrape_fandango, ("53703",), interval=60*24*7, timeout=-1)

init_scheduler()
