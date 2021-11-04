# Generated by Django 3.2 on 2021-11-04 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0006_remove_poll_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="multiplechoicequestion",
            name="multiple_choice_answer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="answers",
                to="polls.multiplechoiceanswer",
            ),
        ),
    ]