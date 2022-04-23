<template>
  <div class="about">
    <h1>This is an about page</h1>
    <PlanetChart/>
    <PlanetChart/>
  </div>
</template>

<script>
import PlanetChart from '../components/PlanetChart.vue'

export default {
  name: 'About',
   components: {
    PlanetChart
  }
}
</script>