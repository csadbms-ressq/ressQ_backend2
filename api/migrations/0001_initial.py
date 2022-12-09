# Generated by Django 4.1.3 on 2022-12-09 07:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodBankDonor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_available', models.FloatField()),
                ('b_manager', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=10)),
                ('address', models.TextField(max_length=300)),
                ('b_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BloodCompatibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_blood', models.CharField(max_length=3)),
                ('comp_type1', models.CharField(blank=True, max_length=3, null=True)),
                ('comp_type2', models.CharField(blank=True, max_length=3, null=True)),
                ('comp_type3', models.CharField(blank=True, max_length=3, null=True)),
                ('comp_type4', models.CharField(blank=True, max_length=3, null=True)),
                ('comp_type5', models.CharField(blank=True, max_length=3, null=True)),
                ('comp_type6', models.CharField(blank=True, max_length=3, null=True)),
                ('comp_type7', models.CharField(blank=True, max_length=3, null=True)),
                ('comp_type8', models.CharField(blank=True, max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('Others', 'others')], max_length=6)),
                ('dob', models.DateField()),
                ('phoneno', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('weight', models.IntegerField()),
                ('class_name', models.CharField(choices=[('csa', 'CSA'), ('csb', 'CSB'), ('eca', 'ECA'), ('ecb', 'ECB'), ('eee', 'EEE'), ('mech', 'MECH'), ('eb', 'EB')], max_length=4)),
                ('batch', models.CharField(choices=[('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026')], max_length=4)),
                ('city', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=6)),
                ('last_donated_date', models.DateField(blank=True, null=True)),
                ('diseases', models.CharField(choices=[('no', 'No'), ('yes', 'Yes')], max_length=3)),
                ('allergies', models.CharField(choices=[('no', 'No'), ('yes', 'Yes')], max_length=3)),
                ('cardiac', models.CharField(blank=True, choices=[('no', 'No'), ('yes', 'Yes')], max_length=4, null=True)),
                ('bleeding_disorders', models.CharField(blank=True, choices=[('no', 'No'), ('yes', 'Yes')], max_length=4, null=True)),
                ('hiv', models.CharField(blank=True, choices=[('no', 'No'), ('yes', 'Yes')], max_length=4, null=True)),
                ('hepatitis', models.CharField(blank=True, choices=[('no', 'No'), ('yes', 'Yes')], max_length=4, null=True)),
                ('blood_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.bloodcompatibility')),
            ],
        ),
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('user_name', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=150)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('about', models.TextField(blank=True, max_length=500, verbose_name='about')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]