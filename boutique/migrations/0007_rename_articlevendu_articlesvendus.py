# Generated by Django 5.1.5 on 2025-02-08 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("boutique", "0006_articlevendu_article_vendu"),
        ("wagtailcore", "0094_alter_page_locale"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="ArticleVendu",
            new_name="ArticlesVendus",
        ),
    ]
