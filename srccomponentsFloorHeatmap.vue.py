<template>
  <div class="heatmap-container">
    <!-- 楼层选择 -->
    <div class="floor-selector">
      <button 
        v-for="floor in ['B1', 'L1', 'L2', 'L3']"
        :key="floor"
        :class="['floor-btn', {active: currentFloor === floor}]"
        @click="currentFloor = floor"
      >
        {{ floor }}
      </button>
    </div>

    <!-- 热力图画布 -->
    <canvas 
      ref="heatmapCanvas"
      width="1000"
      height="800"
      @click="handleCanvasClick"
    ></canvas>

    <!-- 店铺详情 -->
    <div v-if="selectedStore" class="store-info">
      <h3>{{ selectedStore.name }}</h3>
      <p>销售额: ¥{{ selectedStore.sales }}</p>
      <p>坪效: ¥{{ selectedStore.sqm }}/㎡</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentFloor: 'B1',
      selectedStore: null
    };
  },
  mounted() {
    this.renderHeatmap();
  },
  methods: {
    renderHeatmap() {
      // 绘制热力图
    },
    handleCanvasClick(e) {
      // 处理点击店铺
    }
  }
};
</script>

<style scoped>
.heatmap-container { padding: 20px; }
.floor-selector { margin-bottom: 20px; }
.floor-btn { padding: 8px 16px; margin-right: 10px; }
.floor-btn.active { background: #2563eb; color: white; }
canvas { border: 1px solid #ddd; cursor: pointer; }
.store-info { margin-top: 20px; padding: 16px; background: #f5f5f5; }
</style>
