#!/usr/bin/env python

from photo import Photo
import pymongo

def retry(num_tries, exceptions):
    def decorator(func):
        def f_retry(*args, **kwargs):
            for i in range(num_tries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    continue
        return f_retry
    return decorator


# Retry on AutoReconnect or Timeout exception, maximum 3 times
retry_mongo = retry(3, (pymongo.errors.AutoReconnect,
                        pymongo.errors.ServerSelectionTimeoutError))

