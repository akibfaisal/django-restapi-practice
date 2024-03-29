# Generated by Django 2.0.13 on 2019-12-08 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(blank=True, max_length=50)),
                ('category', models.CharField(blank=True, max_length=50)),
                ('studentid', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='studentinfo', to='student.Student')),
            ],
        ),
    ]
