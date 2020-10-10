# Generated by Django 3.1.1 on 2020-09-21 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='銀行名')),
                ('bank_code', models.CharField(max_length=8, verbose_name='銀行コード')),
            ],
            options={
                'verbose_name': '銀行名',
                'verbose_name_plural': '銀行名',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False, verbose_name='user_id')),
                ('user_name', models.CharField(max_length=255, verbose_name='user_name')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
