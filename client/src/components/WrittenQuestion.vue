<template>
  <div class="written-question">
    <div class="written-question-body">{{ body }}</div>
    <!--for now just holder later add wrriten answer-->
    <!--crashed browser if i remove for loop-->
    <!--<WrittenAnswer
    v-for="answer in answers"
      :key="answer.id"
      :index="answer.index"
      :body="answer.text"
      :selectAnswer="selectAnswer"
      />-->
      <WrittenAnswer
      :selectAnswer="selectAnswer"
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
