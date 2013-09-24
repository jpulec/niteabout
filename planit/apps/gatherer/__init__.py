import logging

logger = logging.getLogger(__name__)


def init_scheduler():

    import django_rq
    import tasks
    from collections import defaultdict
    import datetime

    scheduler = django_rq.get_scheduler('default')

    jobs = scheduler.get_jobs()

    functions = defaultdict(lambda: list())

    map(lambda x: functions[x.func].append(x.meta.get('interval')), jobs)

    now = datetime.datetime.now()

    def schedule_once(func, interval):
        if not func in functions or not interval in functions[func] or len(functions[func]) > 1:
            map(scheduler.cancel, filter(lambda x: x.func==func, jobs))
            scheduler.schedule(now, func, interval=interval)
    schedule_once(tasks.google_scrape, interval=1800)


init_scheduler()
