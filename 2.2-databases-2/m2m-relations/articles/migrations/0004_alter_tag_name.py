# Generated by Django 4.2.2 on 2023-06-12 16:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0003_remove_tag_articles_article_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(max_length=30),
        ),
    ]
