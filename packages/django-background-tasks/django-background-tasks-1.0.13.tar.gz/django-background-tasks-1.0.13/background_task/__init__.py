__version__ = '1.0.13'


def background(*arg, **kw):
    from background_task.tasks import tasks
    return tasks.background(*arg, **kw)
