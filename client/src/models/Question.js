class Question {
  constructor(body, id) {
    this.body = body;
    this.id = id;
  }

  getComponentFormat() {
    return {
      body: this.body,
    };
  }
}

export { Question };
