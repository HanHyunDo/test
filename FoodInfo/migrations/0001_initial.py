# Generated by Django 3.0.8 on 2020-08-14 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
                ('last_name', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='음식 이름')),
                ('serving_wt', models.FloatField(verbose_name='제공량')),
                ('kcal', models.FloatField(verbose_name='칼로리')),
                ('carbo', models.FloatField(verbose_name='탄수화물')),
                ('protein', models.FloatField(verbose_name='단백질')),
                ('fat', models.FloatField(verbose_name='지방')),
                ('company', models.TextField(max_length=30, verbose_name='회사명')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FoodInfo.AuthUser')),
            ],
        ),
    ]
