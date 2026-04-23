interface FloorData {
  id: string;
  name: string;
  heatmapData: number[][];
}

export const floorData: FloorData[] = [
  {
    id: 'B1',
    name: 'Basement 1',
    heatmapData: [
      // Example heatmap data
      [0, 1, 2, 1],
      [1, 2, 0, 1],
      [0, 0, 0, 1],
    ],
  },
  {
    id: 'L1',
    name: 'Level 1',
    heatmapData: [
      // Example heatmap data
      [2, 2, 1, 0],
      [1, 0, 0, 0],
      [0, 1, 1, 1],
    ],
  },
  {
    id: 'L2',
    name: 'Level 2',
    heatmapData: [
      // Example heatmap data
      [1, 0, 0, 1],
      [2, 2, 2, 1],
      [1, 0, 1, 2],
    ],
  },
  {
    id: 'L3',
    name: 'Level 3',
    heatmapData: [
      // Example heatmap data
      [2, 1, 1, 1],
      [1, 0, 0, 0],
      [2, 2, 1, 1],
    ],
  },
];
