<!-- src/views/AnalysisOfAlgorithm.vue -->
<template>
    <div class="algorithm-container">
      <h1 class="main-title">Analysis of Algorithms</h1>
      <p class="intro">
        The analysis of algorithms is a fundamental part of computer science, aimed at determining the computational efficiency of an algorithm in terms of time and space. It helps in understanding how an algorithm will scale with input size.
      </p>
  
      <h2 class="sub-title">Key Concepts in Algorithm Analysis</h2>
      <ul class="characteristics-list">
        <li><strong>Time Complexity:</strong> The amount of time taken by an algorithm to run as a function of the length of the input.</li>
        <li><strong>Space Complexity:</strong> The amount of memory space required by an algorithm as a function of the input size.</li>
        <li><strong>Asymptotic Notation:</strong> Big-O, Omega, and Theta notations are used to describe the efficiency of an algorithm in terms of time and space as the input size grows.</li>
      </ul>
  
      <h2 class="sub-title">Diagram for Algorithm Complexity</h2>
      <img src="@/assets/complexity-diagram.png" alt="Algorithm Complexity Diagram" class="algorithm-diagram"/>
  
      <h2 class="sub-title">Example Algorithms</h2>
      <p>Select a category of algorithms to see examples:</p>
  
      <div class="button-container">
        <button @click="showAlgorithm('sorting')" class="example-button">Sorting Algorithms</button>
        <button @click="showAlgorithm('searching')" class="example-button">Searching Algorithms</button>
        <button @click="showAlgorithm('greedy')" class="example-button">Greedy Algorithms</button>
      </div>
  
      <pre v-if="algorithmExample">
        <code>{{ algorithmExample }}</code>
      </pre>
  
      <h2 class="sub-title">Types of Algorithm Analysis</h2>
      <h3 class="type-title">Worst Case Analysis</h3>
      <p>Worst-case analysis examines the maximum time an algorithm will take under any possible input of a given size.</p>
  
      <h3 class="type-title">Best Case Analysis</h3>
      <p>Best-case analysis looks at the minimum time an algorithm takes for the most favorable input.</p>
  
      <h3 class="type-title">Average Case Analysis</h3>
      <p>This analyzes the expected time an algorithm will take for random input of a given size.</p>
  
      <h2 class="sub-title">Advantages of Algorithm Analysis</h2>
      <ul>
        <li>Helps in comparing different algorithms based on their time and space efficiency.</li>
        <li>Provides insights into potential performance bottlenecks for large input sizes.</li>
        <li>Allows developers to make informed decisions when choosing algorithms for real-world applications.</li>
      </ul>
  
      <h2 class="sub-title">Disadvantages of Algorithm Analysis</h2>
      <ul>
        <li>Asymptotic analysis does not provide precise running time, only the growth rate.</li>
        <li>It may not account for all factors that affect performance, such as hardware and system architecture.</li>
        <li>Average case complexity can be difficult to determine for some algorithms.</li>
      </ul>
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=FEnwCHvdW7A" target="_blank">Algorithm Analysis (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=6FOeTgI7Kec" target="_blank">Algorithm Analysis in Hindi</a></li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "AnalysisOfAlgorithm",
    data() {
      return {
        algorithmExample: "",
      };
    },
    methods: {
      showAlgorithm(type) {
        if (type === 'sorting') {
          this.algorithmExample = `// Example of Bubble Sort Algorithm
  for (int i = 0; i < n-1; i++)
    for (int j = 0; j < n-i-1; j++)
      if (arr[j] > arr[j+1])
        swap(arr[j], arr[j+1]);`;
        } else if (type === 'searching') {
          this.algorithmExample = `// Example of Binary Search Algorithm
  int binarySearch(int arr[], int l, int r, int x) {
    while (l <= r) {
      int m = l + (r - l) / 2;
      if (arr[m] == x)
        return m;
      if (arr[m] < x)
        l = m + 1;
      else
        r = m - 1;
    }
    return -1;
  }`;
        } else if (type === 'greedy') {
          this.algorithmExample = `// Example of Greedy Algorithm (Fractional Knapsack)
  sort(items, by_value_to_weight_ratio);
  for each item in sorted_items:
    if item fits in knapsack:
      take item entirely;
    else:
      take the fraction that fits;`;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .algorithm-container {
    max-width: 800px;
    margin: 20px auto;
    padding: 20px;
    border-radius: 10px;
    background-color: #121212;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.6);
    font-family: 'Roboto', sans-serif;
    color: #e0e0e0;
    line-height: 1.6;
  }
  
  .main-title {
    font-size: 2.8em;
    color: #f8f8f8;
    text-align: center;
    margin-bottom: 30px;
  }
  
  .sub-title {
    font-size: 2em;
    color: #e0ce46;
    margin-top: 40px;
    padding-bottom: 10px;
  }
  
  .type-title {
    font-size: 1.5em;
    color: #e0ce46;
    margin-top: 25px;
  }
  
  .intro {
    font-size: 1.3em;
    margin-bottom: 25px;
  }
  
  .characteristics-list {
    margin: 10px 0;
    padding-left: 20px;
    font-size: 1.2em;
  }
  
  li {
    margin-bottom: 15px;
    line-height: 1.6;
  }
  
  .algorithm-diagram {
    width: 100%;
    height: auto;
    margin: 30px 0;
    border: 1px solid #444;
    border-radius: 5px;
  }
  
  pre {
    background-color: #1f1f1f;
    padding: 10px;
    border-radius: 5px;
    overflow-x: auto;
    color: #00ff00;
    font-size: 1.2em;
  }
  
  .button-container {
    display: flex;
    justify-content: space-around;
    margin: 30px 0;
  }
  
  .example-button {
      background-color: #ffcc00;
      color: #121212;
      border: none;
      border-radius: 5px;
      padding: 15px 30px;
      font-size: 1.2em;
      cursor: pointer;
      transition: background-color 0.3s;
  }
    
  .example-button:hover {
    background-color: #ffe066;
  }
  
  a {
    color: #ddc452;
    text-decoration: none;
    font-size: 1.1em;
  }
  
  a:hover {
    text-decoration: underline;
  }
  
  .link-title {
    color: #ffffff;
    margin-top: 30px;
  }
  </style>
  