# Generated by Django 2.2.7 on 2019-11-17 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('left', models.PositiveIntegerField(editable=False)),
                ('right', models.PositiveIntegerField(editable=False)),
                ('depth', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(editable=False)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.Category')),
            ],
            options={
                'ordering': ('left',),
                'abstract': False,
            },
        ),
    ]