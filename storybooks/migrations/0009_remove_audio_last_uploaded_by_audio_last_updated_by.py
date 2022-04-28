# Generated by Django 4.0.3 on 2022-04-26 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storybooks', '0008_remove_audio_last_updated_by_audio_last_uploaded_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio',
            name='last_uploaded_by',
        ),
        migrations.AddField(
            model_name='audio',
            name='last_updated_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='audio_last_updated_by', to='storybooks.extended_user'),
            preserve_default=False,
        ),
    ]
