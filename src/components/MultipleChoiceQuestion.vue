<template>
  <div class="multiple-choice-question">
    <div>{{ body }}</div>
    <li v-for="answer in answers" :key="answer">
      {{ answer }}
    </li>
  </div>
</template>

<script>
export default {
  name: "MultipleChoiceQuestion",
  props: {
    body: {
      type: String,
      required: true,
    },
    answers: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style scoped lang="scss"></style>
