<template>

  
  <div>
    <textarea type="text" id="inputAnswer" name="inputAnswer"></textarea>
    <div class="written-answer" v-on:click="selectAnswer(index)">{{ "submit" }}</div>

  </div>
</template>

<script>
export default {
  name: "WrittenAnswer",
  props: {
selectAnswer: {
      type: Function,
      required: true,
    },
  },
};

</script>

<style scoped lang="scss">
.written-answer {
  width: 90%;
  font-weight: 700;
  border: 0.13rem solid #ddd;
  border-radius: 0.5rem;
  padding: 1rem;
  margin: 0.5rem auto;
  transition: box-shadow 0.25s cubic-bezier(0.08, 0.59, 0.29, 0.99) 0s,
    color 0.25s cubic-bezier(0.08, 0.59, 0.29, 0.99) 0s,
    border-color 0.25s cubic-bezier(0.08, 0.59, 0.29, 0.99) 0s,
    transform 0.25s cubic-bezier(0.08, 0.59, 0.29, 0.99) 0s,
    background-color 0.25s cubic-bezier(0.08, 0.59, 0.29, 0.99) 0s;
}

@media only screen and (min-width: 800px) {
  .written-answer:hover {
    border-color: #c40729;
    background-color: #c40729;
    color: white;
  }
}

@media only screen and (max-width: 800px) {
  .written-answer:active {
    border-color: #c40729;
    background-color: #f9969626;
  }
}

.written-answer {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 21%;
   margin-left: 71%; 
}

#inputAnswer   {
  font-size: 32px;
  font-weight: 700;
  margin-bottom: 2rem;
  min-height: 14rem;
  min-width: 53rem;
  align-items : right;
  border-radius: 0.5rem;
 
}
</style>
