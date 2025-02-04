# Django management command to load initial data via fixtures,
# code taken from the WagtailBakerydemo:
# https://github.com/wagtail/bakerydemo/blob/main/bakerydemo/base/management/commands/load_initial_data.py

from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, **options):
        call_command(
            "dumpdata --natural-foreign --indent 2 -e auth.permission "
            "-e contenttypes -e wagtailcore.GroupCollectionPermission "
            "-e wagtailimages.rendition -e images.rendition -e sessions "
            "-e wagtailsearch.indexentry -e wagtailsearch.sqliteftsindexentry "
            "-e wagtailcore.referenceindex -e wagtailcore.pagesubscription "
            "> fixtures/demo.json",
            verbosity=0,
        )

        print("Awesome. Your bakery data is exported!")  # noqa: T201
