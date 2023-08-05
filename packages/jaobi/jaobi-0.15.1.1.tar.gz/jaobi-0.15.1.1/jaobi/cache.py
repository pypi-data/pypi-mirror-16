# -*- coding: utf-8 -*-

from copy import copy
import json
from pyrocumulus.conf import settings
from pyrocumulus.web.applications import PyroApplication, URLSpec
from pyrocumulus.web.handlers import TemplateHandler
from tornado import gen
from jaobi.models import ContentConsumption


class _SizedConsumptionCache:

    def __init__(self):
        self.cache = []
        self.cache_size = settings.CONSUMPTION_CACHE_SIZE
        self.lock = None

    @gen.coroutine
    def add(self, obj):
        """Adds a ContentConsumption to the cache queue."""

        # wierd bug. somethimes a consumer arrives here with id == None.
        consumer = obj.consumer
        if consumer.id is None:
            yield consumer.save()

        self.cache.append(obj)

        if len(self.cache) >= self.cache_size and not self.lock:
            try:
                self.lock = 'lóqui'
                to_insert = copy(self.cache)
                self.cache = []
                yield self.insert(to_insert)
            finally:
                self.lock = None

    @gen.coroutine
    def insert(self, obj_list):
        yield ContentConsumption.objects.insert(obj_list)


sized_cache = _SizedConsumptionCache()


def get_cache(cache_type='sized'):
    return sized_cache


# Here a simple app to show the size of the cache queue
# Mainly used for testing and debugging
class SpyHandler(TemplateHandler):

    def get(self):
        mydict = {'size': len(sized_cache.cache),
                  'locked': bool(sized_cache.lock)}
        self.write(json.dumps(mydict))


spy = URLSpec('/cache/spy$', SpyHandler)
spyapp = PyroApplication([spy])
