class MultipleChoiceAnswer {
  constructor(index, id, text) {
    this.index = index;
    this.id = id;
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
