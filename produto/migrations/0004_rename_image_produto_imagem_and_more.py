# Generated by Django 4.2.6 on 2023-10-23 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_alter_produto_slug_alter_produto_tipo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='image',
            new_name='imagem',
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco_marqueting',
            field=models.FloatField(verbose_name='Preço'),
        ),
    ]
