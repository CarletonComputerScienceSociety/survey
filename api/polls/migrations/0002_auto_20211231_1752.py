# Generated by Django 3.2 on 2021-12-31 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="multiplechoicequestion",
            options={"base_manager_name": "objects"},
        ),
        migrations.AlterModelOptions(
            name="question",
            options={"base_manager_name": "objects"},
        ),
        migrations.AlterModelOptions(
            name="writtenquestion",
            options={"base_manager_name": "objects"},
        ),
        migrations.AddField(
            model_name="question",
            name="polymorphic_ctype",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="polymorphic_polls.question_set+",
                to="contenttypes.contenttype",
            ),
        ),
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
