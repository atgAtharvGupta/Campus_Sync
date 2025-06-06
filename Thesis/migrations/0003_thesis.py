# Generated by Django 3.2.8 on 2022-02-11 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Thesis', '0002_delete_thesis'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thesis',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Department', models.CharField(max_length=200)),
                ('Thesis_Name', models.CharField(max_length=150)),
                ('Description', models.CharField(max_length=500)),
                ('Student_Name', models.CharField(max_length=200)),
                ('Enrollment', models.CharField(max_length=100)),
                ('DOS', models.DateField()),
                ('Pdf', models.FileField(upload_to='doc/')),
            ],
        ),
    ]
