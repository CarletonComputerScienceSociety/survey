//import { Question } from "./Question";
import { MultipleChoiceQuestion } from "./MultipleChoiceQuestion";
import { WrittenQuestion } from "./WrittenQuestion";

class Survey {
  constructor(survey) {
    this.title = survey.title;
    this.surveyId = survey.id;
    this.currentQuestionIndex = 0;
    this.questionInputs = this.initQuestionsInputs(survey.questions); //list
    this.complete = false;
  }

  initQuestionsInputs(questions) {
    return questions.map((question) => this.initQuestionInput(question));
  }

  initQuestionInput(question) {
    if (question.resourcetype === "MultipleChoiceQuestion") {
      return new MultipleChoiceQuestion(
        question.body,
        question.id,
        question.answers
      );
    }
    //console.log(question.body);//breaking here
    return new WrittenQuestion(question.order, question.body);
  }

  getCurrentQuestionDisplayIndex() {
    return this.currentQuestionIndex;
  }

  getCurrentQuestion() {
    return this.questionInputs[this.currentQuestionIndex];
  }

  getQuestionCount() {
    return this.questionInputs.length;
  }

  increaseCurrentQuestionIndex() {
    if (this.currentQuestionIndex + 1 < this.questionInputs.length) {
      this.currentQuestionIndex += 1;
    } else {
      this.complete = true;
    }
  }

  selectAnswer(answerIndex) {
    if (this.getCurrentQuestion() instanceof MultipleChoiceQuestion) {
      //check with instance
      this.getCurrentQuestion().setSelectedIndex(answerIndex);
    }
    this.increaseCurrentQuestionIndex();
  }

  isComplete() {
    return this.complete;
  }
  getData() {
    let data = [];
    for (let i = 0; i < this.questionInputs.length; i++) {
      let questionDatabaseIndex = this.questionInputs[i].id;
      let answerDatabaseIndex =
        this.questionInputs[i].getSelectedAnswerDatabaseIndex();
      data.push({
        poll: this.surveyId,
        question: questionDatabaseIndex,
        answer: answerDatabaseIndex,
      });
    }

    return { data: data };
  }
}

export { Survey };
