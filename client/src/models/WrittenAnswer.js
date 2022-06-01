class WrittenAnswer {
  constructor(body, id) {
    this.body = body;
    this.id = id;
  }

  getComponentFormat() {
    return {
      body: this.body,
      id: this.id,
    };
  }
}

export { WrittenAnswer };
