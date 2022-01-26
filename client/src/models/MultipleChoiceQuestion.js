import { Question } from "./Question";
import { MultipleChoiceAnswer } from "./MultipleChoiceAnswer";

class MultipleChoiceQuestion extends Question {
  constructor(body, answers) {
    super(body);
    this.selectedAnswerIndex = -1;
    this.answerInputs = this.initAnswerInputs(answers); //list
  }

  initAnswerInputs(answers) {
    return answers.map(
      (answer, index) => new MultipleChoiceAnswer(index, answer.text)
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
}

export { MultipleChoiceQuestion };
