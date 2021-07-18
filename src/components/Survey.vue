<template>
  <div class="survey">
    <MultipleChoiceQuestion
      v-for="question in questions"
      :key="question"
      :body="question"
      :answers="questions"
    />
  </div>
</template>

<script>
import MultipleChoiceQuestion from "@/components/MultipleChoiceQuestion.vue";

export default {
  name: "Survey",
  components: {
    MultipleChoiceQuestion,
  },
  props: {
    questions: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style scoped lang="scss"></style>
