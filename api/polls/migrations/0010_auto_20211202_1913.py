# Generated by Django 3.2 on 2021-12-03 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("polls", "0009_auto_20211104_1211"),
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
    ]
