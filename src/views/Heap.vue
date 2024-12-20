<template>
    <div class="heap-container">
      <h1 class="main-title">Heaps</h1>
      <p class="intro">
        A heap is a special tree-based data structure that satisfies the heap property: for a max heap, every parent node is greater than or equal to its child nodes, and for a min heap, every parent node is less than or equal to its child nodes.
      </p>
  
      <h2 class="sub-title">Key Characteristics of Heaps</h2>
      <ul class="characteristics-list">
        <li><strong>Complete Binary Tree:</strong> Heaps are always complete binary trees, meaning all levels are fully filled except possibly for the last level.</li>
        <li><strong>Heap Property:</strong> In a max heap, the value of the parent node is greater than or equal to the values of its children. In a min heap, the value of the parent node is less than or equal to its children.</li>
        <li><strong>Efficient Operations:</strong> Heaps provide efficient insertion and deletion operations, with time complexities of O(log n).</li>
      </ul>
  
      <h2 class="sub-title">Diagram of a Heap</h2>
      <img src="@/assets/heap.png" alt="Heap Diagram" class="heap-diagram"/>
  
      <h2 class="sub-title">Types of Heaps</h2>
      <h3 class="type-title">Max Heap</h3>
      <p>A heap where the value of each node is greater than or equal to the values of its children, with the maximum value at the root.</p>
  
      <h3 class="type-title">Min Heap</h3>
      <p>A heap where the value of each node is less than or equal to the values of its children, with the minimum value at the root.</p>
  
      <h2 class="sub-title">Heap Operations</h2>
      <p>Common operations performed on heaps include insertion, deletion (removing the root), and heapify (maintaining the heap property).</p>
  
      <h2 class="sub-title">Heap Functions</h2>
      <p>Key functions include inserting a new value, deleting the maximum/minimum value, and building a heap from an array.</p>
  
      <h2 class="sub-title">Examples</h2>
      <p>Click on the buttons below to see examples of heaps in different programming languages:</p>
  
      <div class="button-container">
        <button @click="showExample('java')" class="example-button">Example in Java</button>
        <button @click="showExample('c')" class="example-button">Example in C</button>
        <button @click="showExample('python')" class="example-button">Example in Python</button>
      </div>
  
      <pre v-if="exampleCode">
        <code>{{ exampleCode }}</code>
      </pre>
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=heap1" target="_blank">Heaps in Java (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=heap2" target="_blank">Heaps in Hindi</a></li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "Heap",
    data() {
      return {
        exampleCode: "",
      };
    },
    methods: {
      showExample(language) {
        if (language === 'java') {
          this.exampleCode = `import java.util.PriorityQueue;
  PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
  maxHeap.add(5);
  maxHeap.add(10);
  System.out.println(maxHeap.peek()); // Output: 10`;
        } else if (language === 'c') {
          this.exampleCode = `#include<stdio.h>
  #include<stdlib.h>
  #define MAX 100
  int heap[MAX], size = 0;
  void insert(int value) {
      heap[size++] = value;
      // Code to maintain the heap property goes here
  }`;
        } else if (language === 'python') {
          this.exampleCode = `import heapq
  max_heap = []
  heapq.heappush(max_heap, -1 * 10)  # Store negative values for max heap
  print(-1 * max_heap[0])  # Output: 10`;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .heap-container {
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
  
  .heap-diagram {
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
  