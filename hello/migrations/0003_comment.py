# Generated by Django 3.0.8 on 2020-11-17 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20201116_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.CharField(max_length=200)),
                ('publish_time', models.DateTimeField()),
                ('cid', models.CharField(max_length=16)),
                ('phone', models.CharField(max_length=16)),
                ('paperclip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.paperclip')),
            ],
            options={
                'ordering': ['-id'],
                'unique_together': {('phone', 'paperclip')},
            },
        ),
    ]
