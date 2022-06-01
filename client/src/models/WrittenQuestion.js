import { Question } from "./Question";

class WrittenQuestion extends Question {
    constructor(id, body) {
      super(body,id);
      this.answer = "";
    }
  

    getComponentFormat() {
      return {
        body: this.body,
        id: this.id
      };
    }

    updateAnswer(answerBody){
      this.answer = answerBody;
    }
}

  
  export { WrittenQuestion };
  