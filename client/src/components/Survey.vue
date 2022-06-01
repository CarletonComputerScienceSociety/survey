<template>
  <div class="survey">

    <MultipleChoiceQuestion
      v-if="className==='MultipleChoiceQuestion'"
      :body="currentQuestion.body"
      :answers="currentQuestion.answers"
      :selectAnswer="selectAnswer"
      />
      <WrittenQuestion
      v-if="className==='WrittenQuestion'"
      :question="currentQuestion"
      :updateAnswer="updateAnswer"
      :selectAnswer="selectAnswer"
      
    
    />
      
  </div>
</template>

<script>
import MultipleChoiceQuestion from "@/components/MultipleChoiceQuestion.vue";
import WrittenQuestion from "@/components/WrittenQuestion.vue";

export default {
  name: "Survey",
  components: {
    MultipleChoiceQuestion,
    WrittenQuestion,
  },
  props: {
    currentQuestion: {
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

    className: {
      type: String,
      required: true,
    }
  
  
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
