<template>
  <div class="multiple-choice-answer" v-on:click="selectAnswer(index)">
    <div>{{ body }}</div>
  </div>
</template>

<script>
export default {
  name: "MultipleChoiceAnswer",
  props: {
    index: {
      type: Number,
      required: true,
    },
    body: {
      type: String,
      required: true,
    },
    selectAnswer: {
      type: Function,
      required: true,
    },
  },
};
</script>

<style scoped lang="scss">
.multiple-choice-answer {
  width: 90%;
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
  .multiple-choice-answer:hover {
    border-color: #c40729;
    background-color: #f9969626;
  }
}

@media only screen and (max-width: 800px) {
  .multiple-choice-answer:active {
    border-color: #c40729;
    background-color: #f9969626;
  }
}
</style>
