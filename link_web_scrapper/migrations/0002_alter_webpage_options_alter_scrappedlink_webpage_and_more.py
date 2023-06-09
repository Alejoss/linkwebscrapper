# Generated by Django 4.2 on 2023-04-03 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('link_web_scrapper', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='webpage',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterField(
            model_name='scrappedlink',
            name='webpage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scrapped_links', to='link_web_scrapper.webpage'),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='state',
            field=models.CharField(choices=[('in_progress', 'In Progress'), ('canceled', 'Canceled'), ('scrapped', 'Scrapped')], default='in_progress', max_length=20),
        ),
    ]
