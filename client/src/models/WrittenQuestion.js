import { Question } from "./Question";

class WrittenQuestion extends Question {
    constructor(id, body) {
      super(body,id);
      this.answer = "99";
    }
  

    getComponentFormat() {
        //console.log(this);
       // console.log(this.id);
        //id and body got switched for some reason
      return {
        body: this.body,
        id: this.id
      };
    }
    setSelectedIndex(answerBody) {
      this.answer = answerBody;
    }
}

  
  export { WrittenQuestion };
  