# Generated by Django 2.0.4 on 2018-04-30 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0004_auto_20180420_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='display_order',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='brandtestimonial',
            name='testimonial_by',
            field=models.CharField(max_length=254),
        ),
    ]
