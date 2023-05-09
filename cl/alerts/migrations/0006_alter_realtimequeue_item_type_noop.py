# Generated by Django 3.2.18 on 2023-05-02 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0005_update_triggers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtimequeue',
            name='item_type',
            field=models.CharField(choices=[('o', 'Opinions'), ('r', 'RECAP'), ('d', 'RECAP Dockets'), ('oa', 'Oral Arguments'), ('p', 'People'), ('pa', 'Parenthetical')], db_index=True, help_text='the type of item this is, one of: o (Opinions), r (RECAP), d (RECAP Dockets), oa (Oral Arguments), p (People), pa (Parenthetical)', max_length=3),
        ),
    ]