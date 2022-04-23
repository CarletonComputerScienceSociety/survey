<template>
  <div>
    <canvas id="planet-chart"></canvas>
    ok
  </div>
</template>

<script>
import Chart from 'chart.js'
import planetChartData from './planet-data'

export default {
  name: 'PlanetChart',
  data() {
    return {
      planetChartData: planetChartData
    }
  },
  mounted() {
    const ctx = document.getElementById('planet-chart');
    new Chart(ctx, this.planetChartData);
  }
}
</script>