<template>
  <div class="survey">
    <MultipleChoiceQuestion
      :body="currentQuestion.body"
      :answers="currentQuestion.answers"
      :selectAnswer="selectAnswer"
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
    currentQuestion: {
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
.survey {
  max-width: 800px;
  min-height: fit-content;
  max-height: 100vh;
  display: flex;
  justify-content: center;
  width: 100%;
}
</style>
