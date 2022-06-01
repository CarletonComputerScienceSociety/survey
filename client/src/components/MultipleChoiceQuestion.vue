<template>
  <div class="multiple-choice-question">
    <div class="multiple-choice-question-body">{{ body }}</div>
    <MultipleChoiceAnswer
      v-for="answer in answers"
      :key="answer.id"
      :index="answer.index"
      :body="answer.text"
      :selectAnswer="selectAnswer"
    />
  </div>
</template>

<script>
import MultipleChoiceAnswer from "@/components/MultipleChoiceAnswer.vue";

export default {
  name: "MultipleChoiceQuestion",
  components: {
    MultipleChoiceAnswer,
  },
  props: {
    body: {
      type: String,
      required: true,
    },
    answers: {
      type: Array,
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
.multiple-choice-question {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 95%;
}

.multiple-choice-question-body {
  font-size: 32px;
  font-weight: 700;
  margin-bottom: 2rem;
  min-height: 5rem;
}
</style>
