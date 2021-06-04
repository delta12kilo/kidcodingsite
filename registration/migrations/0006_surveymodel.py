# Generated by Django 3.1.4 on 2021-06-04 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20210529_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyModel',
            fields=[
                ('survey_id', models.AutoField(primary_key=True, serialize=False)),
                ('srvy_rating', models.IntegerField()),
                ('srvy_desp', models.CharField(max_length=500)),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.addinstitute')),
            ],
        ),
    ]