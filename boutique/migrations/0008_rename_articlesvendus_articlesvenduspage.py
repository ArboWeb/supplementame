# Generated by Django 5.1.5 on 2025-02-08 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("boutique", "0007_rename_articlevendu_articlesvendus"),
        ("wagtailcore", "0094_alter_page_locale"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="ArticlesVendus",
            new_name="ArticlesVendusPage",
        ),
    ]
