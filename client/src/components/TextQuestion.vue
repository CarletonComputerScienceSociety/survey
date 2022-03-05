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
    <p>input here?</p>
    <input type="text">
  </div>
</template>

<script>

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
