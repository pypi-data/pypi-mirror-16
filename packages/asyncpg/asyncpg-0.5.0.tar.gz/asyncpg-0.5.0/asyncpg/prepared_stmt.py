# Copyright (C) 2016-present the ayncpg authors and contributors
# <see AUTHORS file>
#
# This module is part of asyncpg and is released under
# the Apache 2.0 License: http://www.apache.org/licenses/LICENSE-2.0


import json

from . import cursor
from . import exceptions


class PreparedStatement:

    __slots__ = ('_connection', '_state', '_query', '_last_status')

    def __init__(self, connection, query, state):
        self._connection = connection
        self._state = state
        self._query = query
        state.attach()
        self._last_status = None

    def get_query(self):
        return self._query

    def get_statusmsg(self):
        if self._last_status is None:
            return self._last_status
        return self._last_status.decode()

    def get_parameters(self):
        self.__check_open()
        return self._state._get_parameters()

    def get_attributes(self):
        self.__check_open()
        return self._state._get_attributes()

    def cursor(self, *args, prefetch=None, timeout=None):
        self.__check_open()
        return cursor.CursorFactory(self._connection, self._query,
                                    self._state, args, prefetch,
                                    timeout)

    async def explain(self, *args, analyze=False):
        query = 'EXPLAIN (FORMAT JSON, VERBOSE'
        if analyze:
            query += ', ANALYZE) '
        else:
            query += ') '
        query += self._state.query

        if analyze:
            # From PostgreSQL docs:
            # Important: Keep in mind that the statement is actually
            # executed when the ANALYZE option is used. Although EXPLAIN
            # will discard any output that a SELECT would return, other
            # side effects of the statement will happen as usual. If you
            # wish to use EXPLAIN ANALYZE on an INSERT, UPDATE, DELETE,
            # CREATE TABLE AS, or EXECUTE statement without letting the
            # command affect your data, use this approach:
            #     BEGIN;
            #     EXPLAIN ANALYZE ...;
            #     ROLLBACK;
            tr = self._connection.transaction()
            await tr.start()
            try:
                data = await self._connection.fetchval(query, *args)
            finally:
                await tr.rollback()
        else:
            data = await self._connection.fetchval(query, *args)

        return json.loads(data)

    async def fetch(self, *args, timeout=None):
        self.__check_open()
        protocol = self._connection._protocol
        data, status, _ = await protocol.bind_execute(
            self._state, args, '', 0, True, timeout)
        self._last_status = status
        return data

    async def fetchval(self, *args, column=0, timeout=None):
        self.__check_open()
        protocol = self._connection._protocol
        data, status, _ = await protocol.bind_execute(
            self._state, args, '', 1, True, timeout)
        self._last_status = status
        if not data:
            return None
        return data[0][column]

    async def fetchrow(self, *args, timeout=None):
        self.__check_open()
        protocol = self._connection._protocol
        data, status, _ = await protocol.bind_execute(
            self._state, args, '', 1, True, timeout)
        self._last_status = status
        if not data:
            return None
        return data[0]

    def __check_open(self):
        if self._state.closed:
            raise exceptions.InterfaceError('prepared statement is closed')

    def __del__(self):
        self._state.detach()
        self._connection._maybe_gc_stmt(self._state)
