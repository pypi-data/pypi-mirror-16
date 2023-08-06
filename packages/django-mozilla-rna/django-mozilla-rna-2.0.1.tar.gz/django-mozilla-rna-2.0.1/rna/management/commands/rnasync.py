from django.conf import settings
from django.core.management import BaseCommand

from synctool.functions import sync_data

from rna.utils import get_last_modified_date


DEFAULT_RNA_SYNC_URL = 'https://nucleus.mozilla.org/rna/sync/'


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-u', '--url',
                            default=getattr(settings, 'RNA_SYNC_URL', DEFAULT_RNA_SYNC_URL),
                            help='Full URL to RNA Sync endpoint')
        parser.add_argument('-c', '--clean', action='store_true',
                            help='Delete all RNA data before sync.')

    def handle(self, *args, **options):
        sync_data(url=options['url'],
                  clean=options['clean'],
                  last_modified=get_last_modified_date(),
                  api_token=None)
