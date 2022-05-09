class WrittenAnswer{
    constructor(body, id){
        super(body,id)
    }

    getComponentFormat() {
        return {
          body: this.body,
          id: this.id,
        };
      }
}


export { WrittenAnswer };