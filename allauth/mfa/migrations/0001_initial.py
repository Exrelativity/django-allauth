# Generated by Django 5.1.2 on 2024-10-21 06:02

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
            name='Authenticator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('recovery_codes', 'Recovery codes'), ('totp', 'TOTP Authenticator'), ('webauthn', 'WebAuthn')], max_length=20)),
                ('data', models.JSONField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_used_at', models.DateTimeField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'constraints': [models.UniqueConstraint(condition=models.Q(('type__in', ('totp', 'recovery_codes'))), fields=('user', 'type'), name='unique_authenticator_type')],
            },
        ),
    ]