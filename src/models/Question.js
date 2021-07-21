class Question {
  constructor(body) {
    this.body = body;
  }

  getComponentFormat() {
    return {
      body: this.body,
    };
  }
}

export { Question };
