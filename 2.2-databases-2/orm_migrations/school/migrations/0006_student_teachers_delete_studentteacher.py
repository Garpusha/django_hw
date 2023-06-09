# Generated by Django 4.2.1 on 2023-06-11 18:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0005_remove_student_teachers"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="teachers",
            field=models.ManyToManyField(related_name="students", to="school.teacher"),
        ),
        migrations.DeleteModel(
            name="StudentTeacher",
        ),
    ]
