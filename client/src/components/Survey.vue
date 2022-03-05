<template>
  <div class="survey">
    <!--Need some logic here 
    right now its printing both -->
    <MultipleChoiceQuestion
      v-if="this.isMultipleModel()"
      :body="currentQuestion.body"
      :answers="currentQuestion.answers"
      :selectAnswer="selectAnswer"
      />
    <WrittenQuestion
      v-if="this.isWrittenModel()"
    />
  </div>
</template>

<script>
import MultipleChoiceQuestion from "@/components/MultipleChoiceQuestion.vue";
import WrittenQuestion from "@/components/TextQuestion.vue";
//import {MultipleChoiceQuestion as MultipleModel} from "@/models/MultipleChoiceQuestion";
//import {WrittenQuestion as WrittenModel} from "@/models/WrittenQuestion";
export default {
  name: "Survey",
  components: {
    MultipleChoiceQuestion,WrittenQuestion
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
  methods: {
  isMultipleModel (item) {
    console.log(item);
    console.log("hi");
      //return item instanceof MultipleModel;
  },
  isWrittenModel (item) {
    console.log(item);
      //return item instanceof WrittenModel;
}
}};
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
