<template>
  <div id="app">
    <pie-chart :data="chartData" :options="chartOptions"></pie-chart>
  </div>
</template>

<script>
import PieChart from "./PieChart.js";
//import { Survey, SurveyProgress } from "@/components";
import { getSurvey } from "@/services";
import { Survey as Model } from "@/models";
export default {
  name: "App",
  components: {
    PieChart
  },
  data() {
    return {
      chartOptions: {
        hoverBorderWidth: 20
      },
      chartData: {
        hoverBackgroundColor: "red",
        hoverBorderWidth: 10,
        labels: ["Green", "Red", "Blue"],
        datasets: [
          {
            label: "Data One",
            backgroundColor: ["#41B883", "#E46651", "#00D8FF"],
            data: [1, 10, 5]
          }
        ]
      },

  async created() {
    try {
      let response = await this.getData(this.$route.params.id);
      this.initData(response.data);
    } catch (error) {
      console.log(error);
      this.errorMessage = error;
    }
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
    error() {
      console.log(this.response);
      return false;
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
    makePie (data){
      var labels = Object.keys(Object.values(data)[0]);
      var title = Object.keys(data)[0];
      var results = Object.values(Object.values(data)[0]);
      var backgroundColor = ["#E74C3C", "#8E44AD", "#3498DB", "#16A085", "#F1C40F", "#873600", "#0B5345", "#641E16"].slice(0,labels.length);
      return {
        chartOptions: {
          hoverBorderWidth: 20
        },
        chartData: {
          hoverBackgroundColor: "red",
          hoverBorderWidth: 10,
          labels: labels,
          datasets: [
            {
              label: title,
              backgroundColor: backgroundColor,
              data: results
            }
          ]
        }
      }
    }
  },
    };
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>