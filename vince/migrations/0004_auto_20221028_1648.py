# Generated by Django 2.2.28 on 2022-10-28 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vince', '0003_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='case',
        ),
        migrations.AddField(
            model_name='product',
            name='cve',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vince.CVEAllocation'),
        ),
        migrations.AddField(
            model_name='product',
            name='version_affected',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Version Affected'),
        ),
    ]