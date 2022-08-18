# Generated by Django 4.1 on 2022-08-18 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchdb', '0002_student2'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'midel 1', 'verbose_name_plural': 'midel 1'},
        ),
        migrations.AlterModelOptions(
            name='student2',
            options={'verbose_name': 'midel 2', 'verbose_name_plural': 'midel 2'},
        ),
        migrations.AddField(
            model_name='student',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='student2',
            name='total',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4),
            preserve_default=False,
        ),
    ]
