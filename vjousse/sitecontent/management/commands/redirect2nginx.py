from django.core.management.base import BaseCommand, CommandError
from django.contrib.redirects.models import Redirect

class Command(BaseCommand):
    help = 'Print nginx redirections'

    def handle(self, *args, **options):
        for redirect in Redirect.objects.all():
            self.stdout.write('rewrite ^%s$ %s permanent;' % (redirect.old_path, redirect.new_path))
