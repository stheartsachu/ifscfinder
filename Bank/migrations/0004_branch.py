# Generated by Django 2.1.7 on 2020-07-02 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0003_auto_20200702_1103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifsc', models.CharField(default='', max_length=20, null=True, unique=True)),
                ('branch', models.CharField(default='', max_length=100, null=True)),
                ('address', models.CharField(default='', max_length=200, null=True)),
                ('city', models.CharField(default='', max_length=100, null=True)),
                ('district', models.CharField(default='', max_length=50, null=True)),
                ('state', models.CharField(default='', max_length=50, null=True)),
                ('bank', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Bank.banks')),
            ],
        ),
    ]
