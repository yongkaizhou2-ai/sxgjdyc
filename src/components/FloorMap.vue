<template>
  <div class="floor-map">
    <canvas ref="heatmapCanvas" width="800" height="600"></canvas>
  </div>
</template>

<script>
export default {
  name: 'FloorMap',
  mounted() {
    this.initializeHeatmap();
  },
  methods: {
    initializeHeatmap() {
      const canvas = this.$refs.heatmapCanvas;
      const ctx = canvas.getContext('2d');
      // Heatmap initialization logic goes here
    }
  }
};
</script>

<style scoped>
.floor-map {
  position: relative;
  width: 800px;
  height: 600px;
}
</style>
