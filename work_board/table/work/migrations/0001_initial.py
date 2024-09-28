# Generated by Django 5.1.1 on 2024-09-26 18:29

import django.db.models.deletion
import taggit.managers
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(blank=True, null=True)),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('category', models.CharField(choices=[('automobile business', 'automobile business'), ('administrative staff', 'administrative staff'), ('senior and middle management', 'senior and middle management'), ('raw material extraction', 'raw material extraction'), ('advertising and marketing', 'advertising and marketing'), ('medicine and pharmaceuticals', 'medicine and pharmaceuticals'), ('sales and customer service', 'sales and customer service'), ('sport club and fitness', 'sport club and fitness'), ('science and education', 'science and education'), ('personnel management', 'personnel management')])),
                ('description', models.TextField(max_length=500)),
                ('experience', models.CharField(choices=[('no experience', 'no experience'), ('1 to 3 years', '1 to 3 years'), ('3 to 6 years', '3 to 6 years'), ('6 to 12 years', '6 to 12 years'), ('from 15 years', 'from 15 years')])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('automobile business', 'automobile business'), ('administrative staff', 'administrative staff'), ('senior and middle management', 'senior and middle management'), ('raw material extraction', 'raw material extraction'), ('advertising and marketing', 'advertising and marketing'), ('medicine and pharmaceuticals', 'medicine and pharmaceuticals'), ('sales and customer service', 'sales and customer service'), ('sport club and fitness', 'sport club and fitness'), ('science and education', 'science and education'), ('personnel management', 'personnel management')])),
                ('title', models.CharField(max_length=40)),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('price', models.IntegerField(default=None, null=True)),
                ('publish', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(max_length=500)),
                ('company', models.CharField(max_length=30)),
                ('experience', models.CharField(choices=[('no experience', 'no experience'), ('1 to 3 years', '1 to 3 years'), ('3 to 6 years', '3 to 6 years'), ('6 to 12 years', '6 to 12 years'), ('from 15 years', 'from 15 years')])),
                ('address', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcement_work', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-id'],
                'indexes': [models.Index(fields=['-id'], name='work_announ_id_6abc21_idx')],
            },
        ),
    ]
