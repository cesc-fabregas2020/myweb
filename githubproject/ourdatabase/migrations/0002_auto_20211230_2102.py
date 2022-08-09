# Generated by Django 3.2.5 on 2021-12-30 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourdatabase', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='osrimolecule',
            name='descriptions',
            field=models.CharField(blank=True, max_length=4000, null=True),
        ),
        migrations.AddField(
            model_name='osrimolecule',
            name='disease',
            field=models.CharField(blank=True, max_length=4000, null=True),
        ),
        migrations.AlterField(
            model_name='osrimolecule',
            name='image',
            field=models.FilePathField(blank=True, null=True, path='/home/jxy/myweb/myweb/static//images/inhouse'),
        ),
    ]