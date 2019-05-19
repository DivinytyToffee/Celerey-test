# Generated by Django 2.2.1 on 2019-05-16 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('token', models.UUIDField()),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.UUIDField(auto_created=True, primary_key=True, serialize=False)),
                ('tag', models.CharField(max_length=128)),
                ('tag_id', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youtube_tag.User')),
            ],
        ),
    ]
