<template>
    <div class="randomized-container">
      <h1 class="main-title">Randomized Algorithms</h1>
      <p class="intro">
        Randomized algorithms make random choices during execution to achieve good performance on average, often simplifying problem-solving and improving efficiency.
      </p>
  
      <h2 class="sub-title">Key Characteristics of Randomized Algorithms</h2>
      <ul class="characteristics-list">
        <li><strong>Randomness:</strong> Utilizes random numbers to make decisions.</li>
        <li><strong>Averaged Performance:</strong> Often provides good average-case performance.</li>
        <li><strong>Simple Implementation:</strong> Can simplify complex algorithms by reducing the number of cases to consider.</li>
      </ul>
  
      <h2 class="sub-title">Diagram of Randomized Algorithms</h2>
      <img src="@/assets/randomized.png" alt="Randomized Algorithms Diagram" class="randomized-diagram"/>
  
      <h2 class="sub-title">Common Randomized Algorithms</h2>
      <h3 class="algorithm-title">Randomized QuickSort</h3>
      <p>Utilizes random pivot selection to improve the average case of the sorting algorithm.</p>
  
      <h3 class="algorithm-title">Randomized Selection</h3>
      <p>Finds the k-th smallest (or largest) element in an unordered list using random partitioning.</p>
  
      <h3 class="algorithm-title">Monte Carlo Methods</h3>
      <p>Employ random sampling to obtain numerical results for problems that might be deterministic in principle.</p>
  
      <h2 class="sub-title">Randomized Algorithms Examples</h2>
      <p>Click on the buttons below to see examples of randomized algorithms in different programming languages:</p>
  
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
        <li><a href="https://www.youtube.com/watch?v=randomized1" target="_blank">Randomized Algorithms in Java (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=randomized2" target="_blank">Randomized Algorithms in Hindi</a></li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "RandomizedAlgorithms",
    data() {
      return {
        exampleCode: "",
      };
    },
    methods: {
      showExample(language) {
        if (language === 'java') {
          this.exampleCode = `import java.util.Random;
  
  public class RandomizedQuickSort {
      public static void quickSort(int[] arr, int low, int high) {
          if (low < high) {
              int pivotIndex = randomizedPartition(arr, low, high);
              quickSort(arr, low, pivotIndex - 1);
              quickSort(arr, pivotIndex + 1, high);
          }
      }
  
      public static int randomizedPartition(int[] arr, int low, int high) {
          Random rand = new Random();
          int pivotIndex = low + rand.nextInt(high - low + 1);
          int pivotValue = arr[pivotIndex];
          swap(arr, pivotIndex, high);
          int storeIndex = low;
          for (int i = low; i < high; i++) {
              if (arr[i] < pivotValue) {
                  swap(arr, storeIndex, i);
                  storeIndex++;
              }
          }
          swap(arr, storeIndex, high);
          return storeIndex;
      }
  
      private static void swap(int[] arr, int i, int j) {
          int temp = arr[i];
          arr[i] = arr[j];
          arr[j] = temp;
      }
  }`;
        } else if (language === 'c') {
          this.exampleCode = `#include <stdio.h>
  #include <stdlib.h>
  #include <time.h>
  
  int randomizedPartition(int arr[], int low, int high) {
      int pivotIndex = low + rand() % (high - low + 1);
      int pivotValue = arr[pivotIndex];
      int temp = arr[pivotIndex];
      arr[pivotIndex] = arr[high];
      arr[high] = temp;
      int storeIndex = low;
      for (int i = low; i < high; i++) {
          if (arr[i] < pivotValue) {
              temp = arr[storeIndex];
              arr[storeIndex] = arr[i];
              arr[i] = temp;
              storeIndex++;
          }
      }
      temp = arr[storeIndex];
      arr[storeIndex] = arr[high];
      arr[high] = temp;
      return storeIndex;
  }
  
  void randomizedQuickSort(int arr[], int low, int high) {
      if (low < high) {
          int pivotIndex = randomizedPartition(arr, low, high);
          randomizedQuickSort(arr, low, pivotIndex - 1);
          randomizedQuickSort(arr, pivotIndex + 1, high);
      }
  }
  
  int main() {
      srand(time(NULL));
      int arr[] = {10, 7, 8, 9, 1, 5};
      int n = sizeof(arr) / sizeof(arr[0]);
      randomizedQuickSort(arr, 0, n - 1);
      for (int i = 0; i < n; i++) {
          printf("%d ", arr[i]);
      }
      return 0;
  }`;
        } else if (language === 'python') {
          this.exampleCode = `import random
  
  def randomized_partition(arr, low, high):
      pivot_index = low + random.randint(0, high - low)
      pivot_value = arr[pivot_index]
      arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
      store_index = low
      for i in range(low, high):
          if arr[i] < pivot_value:
              arr[store_index], arr[i] = arr[i], arr[store_index]
              store_index += 1
      arr[store_index], arr[high] = arr[high], arr[store_index]
      return store_index
  
  def randomized_quick_sort(arr, low, high):
      if low < high:
          pivot_index = randomized_partition(arr, low, high)
          randomized_quick_sort(arr, low, pivot_index - 1)
          randomized_quick_sort(arr, pivot_index + 1, high)
  
  arr = [10, 7, 8, 9, 1, 5]
  randomized_quick_sort(arr, 0, len(arr) - 1)
  print(arr)`;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .randomized-container {
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
  
  .algorithm-title {
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
  
  .randomized-diagram {
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
  </style>
  