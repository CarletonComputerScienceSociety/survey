from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200)


class Question(models.Model):
    body = models.CharField(max_length=200)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, null=True)


class MultipleChoiceQuestion(Question):
    def __str__(self):
        return self.id


class MultipleChoiceAnswer(models.Model):
    answer_body = models.CharField(max_length=200)
    multiple_choice_question = models.ForeignKey(
        MultipleChoiceQuestion,
        related_name="questions",
        on_delete=models.CASCADE,
        null=True,
    )


class WrittenQuestion(Question):
    def __str__(self):
        return self.id
