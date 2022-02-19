# Generated by Django 4.0.2 on 2022-02-18 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storybooks', '0003_auto_20211110_0004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('spaced', models.BooleanField()),
            ],
            options={
                'verbose_name': 'language',
                'verbose_name_plural': 'languages',
            },
        ),
        migrations.RemoveField(
            model_name='story',
            name='page',
        ),
        migrations.AddField(
            model_name='audio',
            name='description',
            field=models.CharField(default='Empty', max_length=2048),
        ),
        migrations.AddField(
            model_name='story',
            name='translation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='storybooks.translation'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='title',
            field=models.CharField(default='Untitled Audio', max_length=255),
        ),
        migrations.AlterField(
            model_name='story',
            name='timestamp',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Page',
        ),
        migrations.AddField(
            model_name='translation',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='translation_language', to='storybooks.language'),
        ),
    ]