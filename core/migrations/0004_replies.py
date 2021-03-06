# Generated by Django 3.0.5 on 2020-05-06 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200413_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Replies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=280)),
                ('author', models.CharField(max_length=40)),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Tweet')),
            ],
        ),
    ]
