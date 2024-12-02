<!-- src/views/Searching.vue -->
<template>
    <div class="searching-container">
      <h1 class="main-title">Searching Algorithms</h1>
      <p class="intro">
        Searching algorithms are used to retrieve information stored within some data structure. The goal of a search is to determine if a specific element exists within a data structure, and if it does, to locate it.
      </p>
  
      <h2 class="sub-title">Key Concepts in Searching Algorithms</h2>
      <ul class="characteristics-list">
        <li><strong>Linear Search:</strong> A basic search algorithm that checks every element in a list sequentially until the desired element is found.</li>
        <li><strong>Binary Search:</strong> A faster search algorithm that works on sorted arrays by repeatedly dividing the search interval in half.</li>
        <li><strong>Time Complexity:</strong> A measure of the efficiency of an algorithm, particularly how the runtime increases as the size of the input increases.</li>
        <li><strong>Space Complexity:</strong> Refers to the amount of memory the algorithm uses relative to the input size.</li>
      </ul>
  
      <h2 class="sub-title">Diagram for Searching Algorithm Complexity</h2>
      <img src="@/assets/search-complexity-diagram.png" alt="Searching Algorithm Complexity Diagram" class="searching-diagram"/>
  
      <h2 class="sub-title">Example Searching Algorithms</h2>
      <p>Select a search algorithm to see the code example:</p>
  
      <div class="button-container">
        <button @click="showAlgorithm('linear')" class="example-button">Linear Search</button>
        <button @click="showAlgorithm('binary')" class="example-button">Binary Search</button>
      </div>
  
      <pre v-if="algorithmExample">
        <code>{{ algorithmExample }}</code>
      </pre>
  
      <h2 class="sub-title">Types of Analysis for Searching Algorithms</h2>
      <h3 class="type-title">Worst Case Analysis</h3>
      <p>For linear search, the worst case occurs when the element is not in the list or is at the last position. For binary search, the worst case occurs when the element is at the extreme ends of the sorted list.</p>
  
      <h3 class="type-title">Best Case Analysis</h3>
      <p>In the best case, for linear search, the element is at the first position. For binary search, the element is located in the middle of the list in the first step.</p>
  
      <h3 class="type-title">Average Case Analysis</h3>
      <p>On average, linear search will take time proportional to half the size of the list, while binary search will take logarithmic time, making it much faster for large lists.</p>
  
      <h2 class="sub-title">Advantages of Searching Algorithms</h2>
      <ul>
        <li><strong>Linear Search:</strong> Simple to implement, does not require sorted data.</li>
        <li><strong>Binary Search:</strong> Extremely efficient for large datasets but requires the data to be sorted.</li>
      </ul>
  
      <h2 class="sub-title">Disadvantages of Searching Algorithms</h2>
      <ul>
        <li><strong>Linear Search:</strong> Inefficient for large datasets due to O(n) time complexity.</li>
        <li><strong>Binary Search:</strong> Requires sorted data, so there is an overhead of sorting if the data is unsorted.</li>
      </ul>
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=CBYHwZcbD-s" target="_blank">Linear Search Explained</a></li>
        <li><a href="https://www.youtube.com/watch?v=P3YID7liBug" target="_blank">Binary Search Visualization</a></li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "SearchingAlgorithms",
    data() {
      return {
        algorithmExample: "",
      };
    },
    methods: {
      showAlgorithm(type) {
        if (type === 'linear') {
          this.algorithmExample = `// Example of Linear Search Algorithm
  int linearSearch(int arr[], int n, int x) {
    for (int i = 0; i < n; i++) {
      if (arr[i] == x) {
        return i;
      }
    }
    return -1;
  }`;
        } else if (type === 'binary') {
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
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .searching-container {
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
  
  .searching-diagram {
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