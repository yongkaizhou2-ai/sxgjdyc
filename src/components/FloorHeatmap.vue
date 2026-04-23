<template>
  <div class="floor-heatmap">
    <canvas ref="heatmapCanvas" width="800" height="600"></canvas>
    <div class="floor-buttons">
      <button v-for="floor in floors" :key="floor" @click="selectFloor(floor)">{{ floor }}</button>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  data() {
    return {
      selectedFloor: null,
      floors: ['1', '2', '3'], // Example floors
    };
  },
  computed: {
    ...mapState(['heatmapData']), // Assuming heatmap data is stored in Vuex
  },
  methods: {
    selectFloor(floor) {
      this.selectedFloor = floor;
      this.renderHeatmap();
    },
    renderHeatmap() {
      const canvas = this.$refs.heatmapCanvas;
      const ctx = canvas.getContext('2d');
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      // Here goes the heatmap rendering based on this.heatmapData
      if (this.heatmapData && this.selectedFloor) {
        const dataForFloor = this.heatmapData[this.selectedFloor];
        // Custom rendering logic for heatmap goes here, using dataForFloor
      }
    },
  },
  watch: {
    heatmapData: 'renderHeatmap', // Re-render on data change
  },
};
</script>

<style scoped>
.floor-heatmap {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.floor-buttons {
  margin-top: 10px;
}
button {
  margin: 0 5px;
}
</style>
