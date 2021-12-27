from django.db import models
from django.db.models.base import Model
from polymorphic.models import PolymorphicModel


class Poll(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200)


class Question(PolymorphicModel):
    body = models.CharField(max_length=200)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, null=True)


class MultipleChoiceQuestion(Question):
    def __str__(self):
        return str(self.id)  # TypeError: __str__ returned non-string


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
        return str(self.id)  # TypeError: __str__ returned non-string


class Submission(models.Model):
    # poll exhibits a one to many relationship
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, null=True, blank=True)


class Response(PolymorphicModel):
    # submission will have many responses
    submission = models.ForeignKey(
        Submission, on_delete=models.CASCADE, null=True, blank=True
    )


class MultipleChoiceResponse(Response):
    #
    question_multiplechoice = models.ForeignKey(
        MultipleChoiceQuestion, on_delete=models.CASCADE, null=True, blank=True
    )

    answer = models.ForeignKey(MultipleChoiceAnswer, on_delete=models.CASCADE)
    # multiple choice answer can be gotten from MultipleChoiceAnswer


class WrittenResponse(Response):
    question_written = models.ForeignKey(
        WrittenQuestion,
        related_name="questions",
        on_delete=models.CASCADE,
        null=True,
    )
    answer_body = models.CharField(max_length=200)
