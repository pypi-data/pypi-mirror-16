# coding=utf-8

import tornado.gen

from .db import db


class QuerySet(object):

    def __init__(self, model):
        self.model = model
        self.cursor = db[self.model.__collection__]
        self.items = []

    def __getattr__(self, attribute):
        return getattr(self.cursor, attribute)

    @tornado.gen.coroutine
    def construct(self, items):
        constructed = []

        for item in items:
            instance = self.model(**item)
            yield instance.construct()
            constructed.append(instance)

        return constructed

    @tornado.gen.coroutine
    def next(self):
        if (yield self.cursor.fetch_next):
            item = self.cursor.next_object()
            instance = (yield self.construct([item]))[0]

            raise tornado.gen.Return(instance)
        else:
            raise tornado.gen.Return(None)

    @tornado.gen.coroutine
    def filter(self, **query):
        cursor = db[self.model.__collection__]
        self.cursor = cursor.find(query)
        raise tornado.gen.Return(self)

    @tornado.gen.coroutine
    def first(self):
        (yield self.filter()).limit(1).sort('_id', 1)
        raise tornado.gen.Return((yield self.next()))

    @tornado.gen.coroutine
    def last(self):
        (yield self.filter()).limit(1).sort('_id', -1)
        raise tornado.gen.Return((yield self.next()))

    @tornado.gen.coroutine
    def all(self, length=None):
        if length:
            items = yield self.cursor.to_list(length)
            self.items = yield self.construct(items)
            raise tornado.gen.Return(self.items)

        while True:
            item = yield self.next()

            if item:
                self.items.append(item)
            else:
                break

        raise tornado.gen.Return(self.items)

    @tornado.gen.coroutine
    def __getitem__(self, sliced):
        if self.items:
            raise tornado.gen.Return(self.items[sliced])

        if isinstance(sliced, slice):
            if sliced.start is not None and sliced.stop is not None:
                self.cursor.skip(sliced.start)
                instances = yield self.all(sliced.stop - sliced.start)
                raise tornado.gen.Return(instances)
            elif sliced.start is not None:
                self.cursor.skip(sliced.start)
            elif sliced.stop is not None:
                self.cursor.limit(sliced.stop)
        else:
            data = yield self.all()
            raise tornado.gen.Return(data[sliced])

        raise tornado.gen.Return(self)
