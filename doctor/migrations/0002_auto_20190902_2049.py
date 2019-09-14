# Generated by Django 2.2.4 on 2019-09-02 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthcentrestaff',
            name='user_id',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='patientrecord',
            name='patient_id',
            field=models.ForeignKey(db_column='person_id', default='16-1-5-009', on_delete=django.db.models.deletion.CASCADE, to='doctor.StudentRecord'),
        ),
        migrations.AlterField(
            model_name='patientrecord',
            name='prescription_serial_no',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.Prescription'),
        ),
    ]
