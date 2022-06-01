import { Question } from "./Question";
import { MultipleChoiceAnswer } from "./MultipleChoiceAnswer";

class MultipleChoiceQuestion extends Question {
  constructor(body, id, answers) {
    super(body, id);
    this.selectedAnswerIndex = -1;
    this.answerInputs = this.initAnswerInputs(answers); //list
  }

  initAnswerInputs(answers) {
    return answers.map(
      (answer, index) =>
        new MultipleChoiceAnswer(index, answer.id, answer.answerBody)
    );
  }

  getComponentFormat() {
    return {
      body: this.body,
      answers: this.answerInputs.map((answer) => answer.getComponentFormat()),
    };
  }

  setSelectedIndex(answerIndex) {
    this.selectedAnswerIndex = answerIndex;
  }
  getSelectedAnswerDatabaseIndex() {
    return this.answerInputs[this.selectedAnswerIndex].id;
  }
}

export { MultipleChoiceQuestion };
