from django.apps import apps
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError, ProgrammingError
from django_autoshard import models


class Command(BaseCommand):
    help = 'Create shards databases'

    def add_arguments(self, parser):
        parser.add_argument('--list', '-l', action='store_true', default=False,
                            help='Show a list of all the constraints that will be dropped')

    def handle(self, *args, **options):
        for connection in connections.all():
            with connection.cursor() as cursor:
                for model in apps.get_models():
                    if issubclass(model, models.ShardedModel):
                        continue
                    self.run(connection, cursor, model, **options)

    def run(self, connection, cursor, model, **options):
        try:
            constraints = dict()
            for key, val in cursor.db.introspection.get_constraints(cursor, model._meta.db_table).items():
                if issubclass(model, models.ShardRelatedModel):
                    if val['foreign_key'] is not None and val['foreign_key'][0] == get_user_model()._meta.db_table:
                        continue
                    elif val['foreign_key'] is not None:
                        constraints[key] = val

                else:
                    if val['foreign_key'] is not None and val['foreign_key'][0] == get_user_model()._meta.db_table:
                        constraints[key] = val
        except ProgrammingError:
            return

        if len(constraints) == 0:
            f = self.style.MIGRATE_HEADING('[{}] No constraints defined for {}.'.format(connection.alias, str(model)))
            self.stdout.write(f)
            return

        for key, val in constraints.items():
            db_table, _ = val['foreign_key']

            sql = cursor.db.SchemaEditorClass.sql_delete_fk % dict(
                table=model._meta.db_table,
                name=key
            )
            if options.get('list'):
                f = self.style.MIGRATE_HEADING('{}'.format(sql))
                self.stdout.write(f)
                continue

            try:
                f = self.style.MIGRATE_HEADING('[{}] Executing {}'.format(connection.alias, sql))
                self.stdout.write(f)

                cursor.execute(sql)
                f = self.style.MIGRATE_HEADING('[{}] Done.\n'.format(connection.alias))
                self.stdout.write(f)
            except OperationalError as e:
                f = self.style.MIGRATE_HEADING('[{}] Failed: {}.\n'.format(connection.alias, str(e)))
                self.stdout.write(f)
