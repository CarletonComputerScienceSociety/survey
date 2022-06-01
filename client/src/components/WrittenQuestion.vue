<template>
  <div class="written-question">
    <div class="written-question-body">{{ question.body }}</div>
    
      <WrittenAnswer
      :selectAnswer="selectAnswer"
      :updateAnswer="updateAnswer"
      :value="question.answer"
      />
  
  </div>
</template>

<script>
import WrittenAnswer from  "@/components/WrittenAnswer"

export default {
  name: "WrittenQuestion",
  components: {
    WrittenAnswer,
  },
  props: {
    question: {
      required: true,
    },
    selectAnswer: {
      type: Function,
      required: true,
    },
    updateAnswer: {
      type: Function,
      required: true,
    },
  },
};
</script>
<style scoped lang="scss">
.written-question {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 95%;
}

.written-question-body {
  font-size: 32px;
  font-weight: 700;
  margin-bottom: 2rem;
  min-height: 5rem;
}
</style>
