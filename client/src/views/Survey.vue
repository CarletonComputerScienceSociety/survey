<template>
  <div class="survey-page" v-if="!this.loading()">
    <SurveyProgress
      :currentPage="this.determinePageCount()"
      :pageCount="this.object.getQuestionCount()"
    />
    <Survey
      v-if="!this.object.isComplete()"
      :questions="this.response.questions"
      :currentQuestion="this.object.getCurrentQuestion().getComponentFormat()"
      :selectAnswer="selectAnswer"
    />
    <p class="survey-complete-message" v-if="this.object.isComplete()">
      Thank you for your feedback!
    </p>
  </div>
</template>

<script>
import { Survey, SurveyProgress } from "@/components";
import { getSurvey } from "@/services";
import { Survey as Model } from "@/models";

export default {
  name: "SurveyPage",
  components: {
    Survey,
    SurveyProgress,
  },
  data() {
    return {
      object: null,
      response: null,
    };
  },
  async created() {
    let response = await this.getData(1);
    console.log(response);
    this.initData(response.data);
  },
  methods: {
    getData: async (id) => {
      return await getSurvey(id);
    },
    initData(response) {
      this.response = response;
      this.object = new Model(response);
    },
    loading() {
      return this.response === null;
    },
    determinePageCount() {
      if (this.object.isComplete()) {
        return this.object.getQuestionCount();
      }

      return this.object.getCurrentQuestionDisplayIndex();
    },
    selectAnswer(answerIndex) {
      this.object.selectAnswer(answerIndex);

      if (this.object.isComplete()) {
        // create reponse request
      }
    },
  },
};
</script>
