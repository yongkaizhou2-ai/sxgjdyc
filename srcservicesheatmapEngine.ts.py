export class HeatmapEngine {
  // 计算店铺销售强度（0-100）
  calculateIntensity(sales: number, maxSales: number): number {
    return (sales / maxSales) * 100;
  }

  // 根据强度返回颜色
  getHeatColor(intensity: number): string {
    if (intensity >= 80) return '#FF4444'; // 红色 - 优秀
    if (intensity >= 60) return '#FF9900'; // 橙色 - 良好
    if (intensity >= 40) return '#FFCC00'; // 黄色 - 一般
    return '#66CC66'; // 绿色 - 需改进
  }
}
