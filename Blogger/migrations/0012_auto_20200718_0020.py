# Generated by Django 3.0.8 on 2020-07-18 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogger', '0011_posts_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post_description',
            field=models.CharField(blank=True, max_length=125, null=True),
        ),
    ]
