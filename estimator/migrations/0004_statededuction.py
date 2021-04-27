# Generated by Django 3.1.7 on 2021-04-27 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estimator', '0003_auto_20210427_0004'),
    ]

    operations = [
        migrations.CreateModel(
            name='StateDeduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(blank=True, max_length=30)),
                ('singleAmount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('coupleAmount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
