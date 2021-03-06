# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-20 06:56
from __future__ import unicode_literals

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="Entry",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "state",
                    models.IntegerField(
                        choices=[(0, "Unread"), (1, "Read"), (2, "Saved")], default=0
                    ),
                ),
                (
                    "expires",
                    models.DateTimeField(
                        blank=True, help_text="When the entry should expire", null=True
                    ),
                ),
                ("title", models.TextField(blank=True)),
                ("content", models.TextField(blank=True)),
                (
                    "date",
                    models.DateTimeField(
                        help_text="When this entry says it was published"
                    ),
                ),
                ("author", models.TextField(blank=True)),
                (
                    "url",
                    models.TextField(
                        blank=True,
                        help_text="URL for the HTML for this entry",
                        validators=[django.core.validators.URLValidator()],
                    ),
                ),
                (
                    "comments_url",
                    models.TextField(
                        blank=True,
                        help_text="URL for HTML comment submission page",
                        validators=[django.core.validators.URLValidator()],
                    ),
                ),
                (
                    "guid",
                    models.TextField(
                        blank=True,
                        help_text="GUID for the entry, according to the feed",
                    ),
                ),
            ],
            options={"verbose_name_plural": "entries", "ordering": ("-date",)},
        ),
        migrations.CreateModel(
            name="Feed",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.TextField(help_text="Published title of the feed")),
                (
                    "feed_url",
                    models.TextField(
                        help_text="URL of the RSS feed",
                        validators=[django.core.validators.URLValidator()],
                        verbose_name="Feed URL",
                    ),
                ),
                (
                    "text",
                    models.TextField(
                        blank=True,
                        help_text="Custom title for the feed - defaults to feed title above",
                        verbose_name="Custom title",
                    ),
                ),
                (
                    "site_url",
                    models.TextField(
                        help_text="URL of the HTML site",
                        validators=[django.core.validators.URLValidator()],
                        verbose_name="Site URL",
                    ),
                ),
                (
                    "added",
                    models.DateTimeField(
                        auto_now_add=True, help_text="Date this feed was added"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="A feed will become inactive when a permanent error occurs",
                    ),
                ),
                (
                    "check_frequency",
                    models.IntegerField(
                        blank=True,
                        help_text="How often to check the feed for changes, in minutes",
                        null=True,
                    ),
                ),
                (
                    "last_updated",
                    models.DateTimeField(
                        blank=True,
                        help_text="Last time the feed says it changed",
                        null=True,
                    ),
                ),
                (
                    "last_checked",
                    models.DateTimeField(
                        blank=True,
                        help_text="Last time the feed was checked",
                        null=True,
                    ),
                ),
                (
                    "next_check",
                    models.DateTimeField(
                        blank=True,
                        help_text="When the next feed check is due",
                        null=True,
                    ),
                ),
                (
                    "error",
                    models.CharField(
                        blank=True, help_text="When a problem occurs", max_length=255
                    ),
                ),
                (
                    "count_unread",
                    models.IntegerField(
                        default=0, help_text="Cache of number of unread items"
                    ),
                ),
                (
                    "count_total",
                    models.IntegerField(
                        default=0, help_text="Cache of total number of items"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"ordering": ("title", "added")},
        ),
        migrations.AddField(
            model_name="entry",
            name="feed",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="entries",
                to="yarr.Feed",
            ),
        ),
    ]
