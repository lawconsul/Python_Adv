import logging
from functools import wraps
import time

logger = logging.getLogger('controllers')


def logged(log_format):
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            result = func(request, *args, **kwargs)
            logger.debug(
                log_format % {'name': func.__name__, 'request': request, 'args': args, 'kwargs': kwargs, 'result': result}
            )
            return result
        return wrapper
    return decorator


def freeze(log_format, time_sleep):
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            result = func(request, *args, **kwargs)
            Start = time.ctime()
            time.sleep(time_sleep)
            End = time.ctime()
            logger.debug(
                log_format % {'Start': Start, 'End': End, 'Sleep': time_sleep, 'args': args, 'kwargs': kwargs}
            )
            return result
        return wrapper
    return decorator