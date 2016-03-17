# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('condition', models.CharField(max_length=10, choices=[(b'new', b'new'), (b'great', b'great'), (b'okay', b'okay'), (b'fair', b'fair'), (b'working', b'working')])),
                ('image', models.ImageField(null=True, upload_to=b'albums', blank=True)),
                ('market', models.CharField(max_length=10, choices=[(b'sale', b'sale'), (b'trade', b'trade'), (b'sale/trade', b'sale/trade')])),
                ('artist', models.ForeignKey(related_name='albums', to='artists.Artist')),
                ('owner', models.ForeignKey(related_name='albums', to='profiles.Profile')),
            ],
        ),
    ]
