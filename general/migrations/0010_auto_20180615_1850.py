# Generated by Django 2.0.4 on 2018-06-15 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0009_auto_20180615_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(choices=[('N/A', 'N/A'), ('Marketing', 'Marketing'), ('Tech', 'Tech'), ('Production', 'Production'), ('Customer Service', 'Customer Service'), ('Accounting', 'Accounting')], default='N/A', max_length=50),
        ),
    ]
