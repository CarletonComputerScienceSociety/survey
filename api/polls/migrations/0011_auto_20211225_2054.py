# Generated by Django 3.2 on 2021-12-26 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0010_auto_20211202_1913"),
    ]

    operations = [
        migrations.AlterField(
            model_name="multiplechoiceanswer",
            name="multiple_choice_question",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="answers",
                to="polls.multiplechoicequestion",
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="poll",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="questions",
                to="polls.poll",
            ),
        ),
    ]