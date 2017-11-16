# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-08-18 04:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0035_auto_20170602_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestinvite',
            name='invite_sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='requestinvite',
            name='issue_invite',
            field=models.CharField(choices=[('', 'Not Set'), ('YES', 'Yes - Send Invite'), ('NO', 'NO - Do not send invite'), ('DONE', 'Invite has been sent')], default='', max_length=4),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='aal',
            field=models.CharField(blank=True, choices=[('', 'Undefined'), ('0', 'AAL0'), ('1', 'AAL1'), ('2', 'AAL2'), ('3', 'AAL3')], default='1', help_text='See NIST SP 800 63 3 B for definitions.', max_length=1, verbose_name='Authenticator Assurance Level'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='ial',
            field=models.CharField(blank=True, choices=[('', 'Undefined'), ('0', 'IAL0'), ('1', 'IAL1'), ('2', 'IAL2'), ('3', 'IAL3')], default='2', help_text='See NIST SP 800 63 3A for definitions.', max_length=1, verbose_name='Identity Assurance Level'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='loa',
            field=models.CharField(blank=True, choices=[('', 'Undefined'), ('1', 'LOA-1'), ('2', 'LOA-2'), ('3', 'LOA-3'), ('4', 'LOA-4')], default='2', help_text='Legacy and Deprecated. Using IAL AAL is recommended.', max_length=1, verbose_name='Level of Assurance'),
        ),
    ]