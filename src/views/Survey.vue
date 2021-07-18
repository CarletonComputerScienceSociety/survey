<template>
  <div class="survey-page">
    <Survey :questions="questions" />
  </div>
</template>

<script>
import Survey from "@/components/Survey.vue";

const data = { questions: [1, 2, 3, 4, 5] };

export default {
  name: "SurveyPage",
  components: {
    Survey,
  },
  data() {
    return data;
  },
};
</script>
