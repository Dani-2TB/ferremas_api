# Generated by Django 4.2.6 on 2024-06-12 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_service', '0002_detalleusuario_remove_detalleuser_user_delete_genero_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='detalleusuario',
            name='genero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth_service.genero'),
        ),
    ]
