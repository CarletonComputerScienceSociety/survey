<template>
  <!--<div class="survey-page" v-if="!this.loading() && this.errorMessage === null" > {{JSON.stringify(this.response)}}</div>-->
  <div class="small">
    <bar-chart :chart-data=createChart(this.response[0])></bar-chart>
  </div>
</template>
<script>
import { getStatistics } from "@/services";
import { Bar } from 'vue-chartjs'
export default {
  name: "StatisticsPage",
  components: {Bar},
  data() {
    return {
      response: null,
      statistics: null,
      errorMessage: null,
    };
  },
  async created() {
    try {
      let response = await this.getData(this.$route.params.id);
      this.initData(response.statistics);
    } catch (error) {
      console.log(error);
      this.errorMessage = error;
    }
  },
  methods: {
    getData: async (id) => {
      return await getStatistics(id);
    },
    initData(response) {
      this.response = response;
    },
    loading() {
      return this.response === null;
    },
    error() {
      console.log(this.response);
      return false;
    },
    
    createChart(stats){
      const values = {};

      for(var i = 0; i < stats[0].length; i++) {
        values.push(stats[0][stats[0].keys[i]])
      }
      console.log(values)
      const data = {
        labels: stats[0].keys,
        datasets: [
          {
            label: 'Dataset 1',
            data: stats[0],
            //backgroundColor: Object.values(Utils.CHART_COLORS),
          }
        ]
      };
      return {
        type: 'bar',
        data: data,
        options: {
          responsive: true,
         plugins: {
           legend: {
             position: 'top',
           },
           title: {
             display: true,
              text: 'Chart.js Pie Chart'
            }
          }
        },
      };
    }

    
  },
};
</script>
