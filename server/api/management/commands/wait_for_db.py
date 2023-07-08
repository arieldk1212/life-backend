import time
from django.db.utils import OperationalError 
from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2OpError

class Command(BaseCommand):

  def handle(self, *args, **options):
    self.stdout.write('Waiting for database...')
    db_up = False
    while db_up is False:
      try:
        self.check(databases=['default'])
        db_up = True
      except (OperationalError, Psycopg2OpError):
        self.stdout.write('Database Unavailable, Waiting for database...')
        time.sleep(1)

    self.stdout.write(self.style.SUCCESS('Database Available.'))