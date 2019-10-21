# Generated by Django 2.2.4 on 2019-10-16 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alloc', '0004_auto_20191009_0724'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('Review', 'Review'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='', max_length=100),
            preserve_default=False,
        ),
    ]
