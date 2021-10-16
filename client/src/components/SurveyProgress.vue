<template>
  <div class="survey-progress">
    <div class="survey-progress-pages">
      {{ currentPage }} of {{ pageCount }}
    </div>
    <div class="survey-progress-bar">
      <progress id="file" :value="currentPage" :max="pageCount"></progress>
    </div>
  </div>
</template>

<script>
export default {
  name: "SurveyProgress",
  props: {
    currentPage: {
      type: Number,
      required: true,
    },
    pageCount: {
      type: Number,
      required: true,
    },
  },
};
</script>

<style scoped lang="scss">
.survey-progress {
  font-weight: 700;
  margin-top: 3rem;
  margin-bottom: 3rem;
}

progress {
  border-radius: 7px;
  height: 0.65rem;
}
progress::-webkit-progress-bar {
  background-color: #e4e5e6;
  border-radius: 7px;
}
progress::-webkit-progress-value {
  background-color: #c40729;
  border-radius: 7px;
}
progress::-moz-progress-bar {
  /* style rules */
}
</style>
