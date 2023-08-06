from __future__ import unicode_literals

from sqlbag import raw_execute
from schemainspect import get_inspector
from .changes import Changes
from .statements import Statements


class Migration(object):
    def __init__(self, s_from, s_target):
        self.s_from = s_from
        self.s_target = s_target

        self.changes = Changes(None, None)
        self.inspect_from()
        self.inspect_target()
        self.statements = Statements()

    def clear(self):
        self.statements = Statements()

    def inspect_from(self):
        self.changes.i_from = get_inspector(self.s_from)

    def inspect_target(self):
        self.changes.i_target = get_inspector(self.s_target)

    def apply(self):
        for stmt in self.statements:
            raw_execute(self.s_from, stmt)

        self.inspect_from()
        safety_on = self.statements.safe
        self.clear()
        self.set_safety(safety_on)

    def add(self, statements):
        self.statements += statements

    def add_sql(self, sql):
        self.statements += Statements([sql])

    def set_safety(self, safety_on):
        self.statements.safe = safety_on

    def add_all_changes(self):
        self.add(self.changes.enums(creations_only=True, modifications=False))

        self.add(self.changes.sequences(creations_only=True))

        self.add(self.changes.views(drops_only=True))
        self.add(self.changes.functions(drops_only=True))

        self.add(self.changes.extensions())
        self.add(self.changes.schema())

        self.add(self.changes.views(creations_only=True))
        self.add(self.changes.functions(creations_only=True))

        self.add(self.changes.sequences(drops_only=True))
        self.add(self.changes.enums(drops_only=True, modifications=False))

    @property
    def sql(self):
        return self.statements.sql
