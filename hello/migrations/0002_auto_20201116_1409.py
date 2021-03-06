# Generated by Django 3.0.8 on 2020-11-16 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realname', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254)),
                ('sign', models.BooleanField()),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='paperclip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('abstract', models.CharField(max_length=200)),
                ('publish_time', models.DateTimeField()),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('pid', models.CharField(max_length=16)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='guest',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='guest',
            name='event',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Guest',
        ),
        migrations.AddField(
            model_name='author',
            name='paperclip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.paperclip'),
        ),
        migrations.AlterUniqueTogether(
            name='author',
            unique_together={('phone', 'paperclip')},
        ),
    ]
