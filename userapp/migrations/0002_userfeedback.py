# Generated by Django 4.1.5 on 2023-01-17 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFeedback',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('feedback_sentiment', models.CharField(max_length=100)),
                ('booking_experience', models.IntegerField()),
                ('slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.bookingslots')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.usermodel')),
            ],
            options={
                'db_table': 'User-Feedback',
            },
        ),
    ]
