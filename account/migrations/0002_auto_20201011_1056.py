# Generated by Django 3.1.1 on 2020-10-11 10:56

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='angina_or_heart_attack',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='atrial_fibrillation',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(null=True, verbose_name='Birthdate'),
        ),
        migrations.AlterField(
            model_name='user',
            name='blood_group',
            field=models.CharField(choices=[('A RH+', 'A RH+'), ('A RH-', 'A RH-'), ('AB RH+', 'AB RH+'), ('AB RH-', 'AB RH-'), ('B RH+', 'B RH+'), ('B RH-', 'B RH-'), ('0 RH+', '0 RH+'), ('0 RH-', '0 RH-')], default='A RH+', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=255, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='diabets',
            field=models.CharField(choices=[('None', 'None'), ('Type 1', 'Type 1'), ('Type 2', 'Type 2')], default='None', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True, verbose_name='Email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='ethnicity',
            field=models.CharField(choices=[('White', 'White or not stated'), ('Indian', 'Indian'), ('Pakistani', 'Pakistani'), ('Bangladeshi', 'Bangladeshi'), ('Asian', 'Other Asian'), ('Caribbean', 'Black Caribbean'), ('African', 'White or not stated'), ('African', 'Black African'), ('Chinese', 'Chinese'), ('Others', 'Others')], default='White', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='F', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='height',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='kidney_disease',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(choices=[('EN', 'English'), ('RU', 'Russian'), ('TR', 'Turkish'), ('AZ', 'Azerbaijan')], default='EN', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='menopause',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=30, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='passport',
            field=models.CharField(max_length=255, null=True, unique=True, verbose_name='Passport ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=50, null=True, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='user',
            name='physical_activity',
            field=models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], default='Low', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='pressure_treatment',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='rheumatoid_arthritis',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='smoking',
            field=models.CharField(choices=[('Non-smoker', 'Non-smoker'), ('Ex-smoker', 'Ex-smoker'), ('Light-smoker', 'Light smoker (less than 10)'), ('Moderate-smoker', 'Light smoker (10 to 19)'), ('Heavy-smoker', 'Light smoker (20 or over)')], default='Non-smoker', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='surname',
            field=models.CharField(max_length=30, null=True, verbose_name='Surname'),
        ),
    ]