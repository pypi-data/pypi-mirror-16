# -*- coding: utf-8 -*-

from mamonsu.lib.plugin import Plugin
from .pool import Pooler


class Xlog(Plugin):

    TriggerLagMoreThen = 360

    def run(self, zbx):
        # recovery
        result = Pooler.query('select pg_is_in_recovery()')
        if str(result[0][0]) == 't' or str(result[0][0]) == 'True':
            lag = Pooler.query('select extract(epoch from now() \
                - pg_last_xact_replay_timestamp())')
            zbx.send('pgsql.replication_lag[sec]', lag[0][0])
        else:
            # xlog location
            result = Pooler.query("select pg_xlog_location_diff\
                (pg_current_xlog_location(),'0/00000000')")
            zbx.send('pgsql.wal.write[]', result[0][0])

    def items(self, template):
        return template.item({
            'name': 'PostgreSQL: streaming replication lag in seconds',
            'key': 'pgsql.replication_lag[sec]'
        }) + template.item({
            'name': 'PostgreSQL: wal write speed',
            'key': 'pgsql.wal.write[]',
            'units': Plugin.UNITS.bytes,
            'delta': Plugin.DELTA.speed_per_second
        })

    def graphs(self, template):
        result = template.graph({
            'name': 'PostgreSQL write-ahead log generation speed',
            'items': [
                {'color': 'CC0000',
                    'key': 'pgsql.wal.write[]'}]})
        result += template.graph({
            'name': 'PostgreSQL replication lag in second',
            'items': [
                {'color': 'CC0000',
                    'key': 'pgsql.replication_lag[sec]'}]})
        return result

    def triggers(self, template):
        return template.trigger({
            'name': 'PostgreSQL streaming lag to high '
            'on {HOSTNAME} (value={ITEM.LASTVALUE})',
            'expression': '{#TEMPLATE:pgsql.replication_lag[sec].last'
            '()}&gt;' + str(self.TriggerLagMoreThen)
        })
