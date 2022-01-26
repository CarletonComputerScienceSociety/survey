import { Question } from "./Question";
import { MultipleChoiceQuestion } from "./MultipleChoiceQuestion";

class Survey {
  constructor(survey) {
    this.title = survey.title;
    this.currentQuestionIndex = 0;
    this.questionInputs = this.initQuestionsInputs(survey.questions); //list
    this.complete = false;
  }

  initQuestionsInputs(questions) {
    return questions.map((question) => this.initQuestionInput(question));
  }

  initQuestionInput(question) {
    if (question.type === "MultipleChoiceQuestion") {
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
    if (this.getCurrentQuestion() instanceof MultipleChoiceQuestion) {
      //check with instance
      this.getCurrentQuestion().setSelectedIndex(answerIndex); //index
      console.log(answerIndex);
    }
    console.log(this.getCurrentQuestion().type);
    this.increaseCurrentQuestionIndex();
  }

  isComplete() {
    return this.complete;
  }
  getData() {
    const data1 = {
      data: [
        { submission: 1, question: 2, answer: "vue3" },
        { submission: 1, question: 1, answer: "1" },
      ],
    };
    return data1;
  }
}

export { Survey };
