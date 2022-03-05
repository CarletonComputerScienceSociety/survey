import { Question } from "./Question";

class WrittenQuestion extends Question {
    constructor(id, body) {
      super(body,id);
      
    }
  

    getComponentFormat() {
        //console.log(this);
       // console.log(this.id);
        //id and body got switched for some reason
      return {
        body: this.body
      };
    }
}

  
  export { WrittenQuestion };
  