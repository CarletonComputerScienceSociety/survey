from django.db import models
from django.db.models.base import Model
from polymorphic.models import PolymorphicModel
import uuid

class Poll(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.CharField(max_length=200, null=True, blank = True)
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return str(self.url)

    def save(self, *args, **kwargs):
        if self.url == None:
            self.url = self.id
        super().save(*args, **kwargs)

    def questions_list(self):
        return self.questions.all()


    def statistics(self):

        statisitics = {}

        questions = self.questions_list()
        submissions = self.submissions_list()
        
        for question in questions:
            
            answers = {}
            for answer in question.answers_list():
                answers.update({answer.answer_body:0})

            statisitics.update({question.body:answers})


        for submission in submissions:
            for response in submission.response_list():         

                statisitics[response.question_multiplechoice.body][response.answer.answer_body] +=1

                
        return statisitics
        

    def submissions_list(self):
        return list(self.submission_set.all())

    def stats(self):
        print(self.questions.all)


class Question(PolymorphicModel):
    body = models.CharField(max_length=200)

    poll = models.ForeignKey(
        Poll,
        related_name="questions",
        on_delete=models.CASCADE,
        null=True,
    )


class MultipleChoiceQuestion(Question):
    def __str__(self):
        return str(self.id)

    def answers_list(self):
        return self.answers.all()


class MultipleChoiceAnswer(models.Model):
    answer_body = models.CharField(max_length=200)

    multiple_choice_question = models.ForeignKey(
        MultipleChoiceQuestion,
        related_name="answers",
        on_delete=models.CASCADE,
        null=True,
    )


class WrittenQuestion(Question):
    def __str__(self):
        return str(self.id)  # TypeError: __str__ returned non-string


class Submission(models.Model):
    # poll exhibits a one to many relationship
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, null=True, blank=True)
    
    def response_list(self):
        return self.responses.all()

class Response(PolymorphicModel):
    # submission will have many responses
    #submission = models.ForeignKey(
    #    Submission, on_delete=models.CASCADE, null=True, blank=True
    #)

    submission = models.ForeignKey(
        Submission,
        related_name="responses",
        on_delete=models.CASCADE,
        null=True,
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
