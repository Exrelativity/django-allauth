# Generated by Django 5.1.2 on 2024-10-21 06:02

import allauth.account.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(db_index=True, max_length=254, verbose_name='email address')),
                ('verified', models.BooleanField(default=False, verbose_name='verified')),
                ('primary', models.BooleanField(default=False, verbose_name='primary')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'email address',
                'verbose_name_plural': 'email addresses',
            },
        ),
        migrations.CreateModel(
            name='EmailConfirmation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created')),
                ('sent', models.DateTimeField(null=True, verbose_name='sent')),
                ('key', models.CharField(max_length=64, unique=True, verbose_name='key')),
                ('email_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.emailaddress', verbose_name='email address')),
            ],
            options={
                'verbose_name': 'email confirmation',
                'verbose_name_plural': 'email confirmations',
            },
            bases=(allauth.account.models.EmailConfirmationMixin, models.Model),
        ),
        migrations.AddConstraint(
            model_name='emailaddress',
            constraint=models.UniqueConstraint(condition=models.Q(('primary', True)), fields=('user', 'primary'), name='unique_primary_email'),
        ),
        migrations.AddConstraint(
            model_name='emailaddress',
            constraint=models.UniqueConstraint(condition=models.Q(('verified', True)), fields=('email',), name='unique_verified_email'),
        ),
        migrations.AlterUniqueTogether(
            name='emailaddress',
            unique_together={('user', 'email')},
        ),
    ]