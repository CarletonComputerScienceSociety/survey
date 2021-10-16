<template>
  <div class="survey"></div>
</template>

<script>
export default {
  name: "Survey",
  props: {
    questions: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style scoped lang="scss"></style>
