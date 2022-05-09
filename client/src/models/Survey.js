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
    console.log(9);
    console.log(questions.map((question) => this.initQuestionInput(question)));
    return questions.map((question) => this.initQuestionInput(question));
  }

  initQuestionInput(question) {
    console.log(77);
    console.log(this);
    if (question.resourcetype === "MultipleChoiceQuestion") {
      return new MultipleChoiceQuestion(
        question.body,
        question.id,
        question.answers
      );
    }
    //console.log(question.body);//breaking here
    else{
      return new WrittenQuestion(question.id, question.body );
    }
    
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
    console.log(66);
    console.log(this.getCurrentQuestion());
    console.log("called select answer")
    if (this.getCurrentQuestion() instanceof MultipleChoiceQuestion) {
      //check with instance
      this.getCurrentQuestion().setSelectedIndex(answerIndex);
    }
    else{
      let currentAnswer = document.getElementById("inputAnswer");
      console.log(88);
      console.log(currentAnswer.value);
      console.log(this.getCurrentQuestion().answer);  
      this.getCurrentQuestion().answer = currentAnswer.value    ;
    }
    this.increaseCurrentQuestionIndex();
    
  }

  isComplete() {
    return this.complete;
  }
  getData() {
    let data = [];
    for (let i = 0; i < this.questionInputs.length; i++) {
      console.log(data)
      let questionDatabaseIndex = this.questionInputs[i].id;
      console.log(3);
      console.log(this.questionInputs);

      try {
        let answerDatabaseIndex =
        this.questionInputs[i].getSelectedAnswerDatabaseIndex();
        data.push({
          poll: this.surveyId,
          question: questionDatabaseIndex,
          answer: answerDatabaseIndex,
      });
        
      } catch (error) {
        let answerDatabaseIndex =this.questionInputs[i].answer;
        data.push({
          poll: this.surveyId,
          question: questionDatabaseIndex,
          answer: answerDatabaseIndex,
        });
      
      }
      }
      console.log(data);
      return { data: data };
      
      
  }
}

export { Survey };
