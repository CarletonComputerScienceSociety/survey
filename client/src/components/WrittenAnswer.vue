<template>
  <div class="multiple-choice-answer" v-on:click="selectAnswer(index)">
    <div>{{ body }}</div>
    <p>this is answer</p>
  </div>
</template>

<script>

</script>

<style scoped lang="scss">
.multiple-choice-answer {
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
  .multiple-choice-answer:hover {
    border-color: #c40729;
    background-color: #c40729;
    color: white;
  }
}

@media only screen and (max-width: 800px) {
  .multiple-choice-answer:active {
    border-color: #c40729;
    background-color: #f9969626;
  }
}
</style>
