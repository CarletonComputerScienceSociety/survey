class MultipleChoiceAnswer {
  constructor(index, text) {
    this.index = index;
    this.text = text;
  }

  getComponentFormat() {
    return {
      index: this.index,
      text: this.text,
    };
  }
}

export { MultipleChoiceAnswer };
