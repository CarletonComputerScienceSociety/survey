import { Question } from "./Question";
import { MultipleChoiceQuestion } from "./MultipleChoiceQuestion";

class Survey {
  constructor(survey) {
    this.title = survey.title;
    this.currentQuestionIndex = 0;
    this.questionInputs = this.initQuestionsInputs(survey.questions);
    this.complete = false;
  }

  initQuestionsInputs(questions) {
    return questions.map((question) => this.initQuestionInput(question));
  }

  initQuestionInput(question) {
    if (question.resourcetype === "MultipleChoiceQuestion") {
      return new MultipleChoiceQuestion(question.body, question.answers);
    }

    return new Question(question.order, question.question.body);
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
    if (this.getCurrentQuestion().type === "MultipleChoiceQuestion") {
      this.getCurrentQuestion().setSelectedIndex(answerIndex);
    }

    this.increaseCurrentQuestionIndex();
  }

  isComplete() {
    return this.complete;
  }
}

export { Survey };
