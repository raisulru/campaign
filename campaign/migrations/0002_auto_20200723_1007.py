# Generated by Django 3.0.8 on 2020-07-23 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recipients',
            new_name='Recipient',
        ),
        migrations.AlterModelOptions(
            name='campaign',
            options={'verbose_name': 'Campaign', 'verbose_name_plural': 'Campaigns'},
        ),
        migrations.AlterModelOptions(
            name='recipient',
            options={'verbose_name': 'Recipient', 'verbose_name_plural': 'Recipients'},
        ),
        migrations.AlterModelOptions(
            name='sentbox',
            options={'verbose_name': 'Sent Box', 'verbose_name_plural': 'Sent Boxes'},
        ),
        migrations.AlterModelTable(
            name='campaign',
            table='campaigns',
        ),
        migrations.AlterModelTable(
            name='recipient',
            table='recipients',
        ),
        migrations.AlterModelTable(
            name='sentbox',
            table='sent_box',
        ),
    ]
