# Generated by Django 5.1 on 2024-09-26 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_user_bio_user_name_alter_user_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="avatar",
            field=models.ImageField(default="avatar.svg", null=True, upload_to=""),
        ),
    ]
