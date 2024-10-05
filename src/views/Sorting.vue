<!-- src/views/Sorting.vue -->
<template>
    <div class="sorting-container">
      <h1 class="main-title">Sorting Algorithms</h1>
      <p class="intro">
        A sorting algorithm is a method to arrange elements in a list in a specific order, typically in ascending or descending order. Efficient sorting is important for optimizing the performance of other algorithms (like search algorithms) that require sorted data.
      </p>
      
      <h2 class="sub-title">Types of Sorting Algorithms</h2>
  
      <h3 class="type-title">1. Bubble Sort</h3>
      <p>Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order. It is simple but inefficient for large datasets.</p>
      <img src="@/assets/bubble-sort.png" alt="Bubble Sort Diagram" class="sorting-diagram"/>
  
      <h3 class="type-title">2. Selection Sort</h3>
      <p>Selection Sort repeatedly selects the smallest (or largest) element from the unsorted portion of the list and moves it to the sorted portion.</p>
      <img src="@/assets/selection-sort.png" alt="Selection Sort Diagram" class="sorting-diagram"/>
  
      <h3 class="type-title">3. Insertion Sort</h3>
      <p>Insertion Sort builds the sorted list one element at a time by inserting each new element into its correct position within the already sorted part of the list.</p>
      <img src="@/assets/insertion-sort.png" alt="Insertion Sort Diagram" class="sorting-diagram"/>
  
      <h3 class="type-title">4. Merge Sort</h3>
      <p>Merge Sort is a divide-and-conquer algorithm that splits the list into smaller sub-lists, sorts them, and then merges them back into a single sorted list.</p>
      <img src="@/assets/merge-sort.png" alt="Merge Sort Diagram" class="sorting-diagram"/>
  
      <h3 class="type-title">5. Quick Sort</h3>
      <p>Quick Sort selects a pivot element and partitions the list into two sub-lists: elements less than the pivot and elements greater than the pivot. The sub-lists are then sorted recursively.</p>
      <img src="@/assets/quick-sort.png" alt="Quick Sort Diagram" class="sorting-diagram"/>
  
      <h3 class="type-title">6. Heap Sort</h3>
      <p>Heap Sort first builds a max heap from the list, then repeatedly swaps the root (largest) element with the last element and reduces the heap size.</p>
      <img src="@/assets/heap-sort.png" alt="Heap Sort Diagram" class="sorting-diagram"/>
  
      <h3 class="type-title">7. Radix Sort</h3>
      <p>Radix Sort processes the list digit by digit, sorting the elements according to individual digits, starting from the least significant digit to the most significant.</p>
      <img src="@/assets/radix-sort.png" alt="Radix Sort Diagram" class="sorting-diagram"/>
  
      <h3 class="type-title">8. Bucket Sort</h3>
      <p>Bucket Sort divides the list into several buckets, each containing a range of values. Each bucket is then sorted individually, and the results are concatenated to form the sorted list.</p>
      <img src="@/assets/bucket-sort.png" alt="Bucket Sort Diagram" class="sorting-diagram"/>
  
      <h3 class="type-title">9. Shell Sort</h3>
      <p>Shell Sort is a generalized version of insertion sort that starts by sorting elements far apart and progressively reduces the gap between elements to sort.</p>
      <img src="@/assets/shell-sort.png" alt="Shell Sort Diagram" class="sorting-diagram"/>
  
      <h3 class="type-title">10. Counting Sort</h3>
      <p>Counting Sort works by counting the occurrences of each unique element, then uses that information to place each element in its correct position in the sorted list.</p>
      <img src="@/assets/counting-sort.png" alt="Counting Sort Diagram" class="sorting-diagram"/>
  
      <h2 class="sub-title">Declaration Syntax</h2>
      <p>Select a programming language to see the implementation of sorting algorithms:</p>
      
      <div class="button-container">
        <button @click="showDeclaration('java')" class="example-button">Java</button>
        <button @click="showDeclaration('c')" class="example-button">C</button>
        <button @click="showDeclaration('python')" class="example-button">Python</button>
      </div>
  
      <pre v-if="declarationCode">
        <code>{{ declarationCode }}</code>
      </pre>
  
      <h2 class="sub-title">Advantages of Sorting Algorithms</h2>
      <ul>
        <li>Efficiently arranges data, enabling faster searching and processing.</li>
        <li>Many sorting algorithms can be applied to a variety of data types.</li>
      </ul>
  
      <h2 class="sub-title">Disadvantages of Sorting Algorithms</h2>
      <ul>
        <li>Some sorting algorithms have high time complexity, making them unsuitable for large datasets.</li>
        <li>In-place sorting algorithms may be inefficient in terms of memory usage.</li>
      </ul>
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=nmhjrI-aW5o" target="_blank">Sorting Algorithms in Python (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=kPRA0W1kECg" target="_blank">Quick Sort Algorithm in Hindi</a></li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "SortingAlgorithms",
    data() {
      return {
        declarationCode: "",
      };
    },
    methods: {
      showDeclaration(language) {
        if (language === 'java') {
          this.declarationCode = `// Bubble Sort in Java
  void bubbleSort(int arr[]) {
    int n = arr.length;
    for (int i = 0; i < n-1; i++)
      for (int j = 0; j < n-i-1; j++)
        if (arr[j] > arr[j+1]) {
          // Swap arr[j] and arr[j+1]
          int temp = arr[j];
          arr[j] = arr[j+1];
          arr[j+1] = temp;
        }
  }`; 
        } else if (language === 'c') {
          this.declarationCode = `// Bubble Sort in C
  void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n-1; i++)
      for (int j = 0; j < n-i-1; j++)
        if (arr[j] > arr[j+1]) {
          int temp = arr[j];
          arr[j] = arr[j+1];
          arr[j+1] = temp;
        }
  }`; 
        } else if (language === 'python') {
          this.declarationCode = `# Bubble Sort in Python
  def bubble_sort(arr):
      n = len(arr)
      for i in range(n-1):
          for j in range(0, n-i-1):
              if arr[j] > arr[j+1]:
                  arr[j], arr[j+1] = arr[j+1], arr[j]`;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .sorting-container {
    max-width: 800px;
    margin: 20px auto;
    padding: 20px;
    border-radius: 10px;
    background-color: #121212; /* Dark background color */
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.6);
    font-family: 'Roboto', sans-serif; /* Updated font */
    color: #e0e0e0; /* Light text color for better readability */
    line-height: 1.6; /* Increased line height for better readability */
  }
  
  .main-title {
    font-size: 2.8em; /* Larger font size for main title */
    color: #f8f8f8; /* Bright color for the main title */
    text-align: center;
    margin-bottom: 30px; /* Increased margin for better spacing */
  }
  
  .sub-title, .type-title {
    font-size: 2em; /* Larger font size for sub-titles */
    color: #e0ce46; /* Bright color for sub-titles */
    margin-top: 40px; /* Increased margin for better spacing */
    padding-bottom: 10px; /* Space below the sub-title */
  }
  
  .intro {
    font-size: 1.3em; /* Increased font size for intro text */
    margin-bottom: 25px; /* Increased margin for better spacing */
  }
  
  .sorting-diagram {
    width: 100%;
    height: auto;
    margin: 30px 0; /* Increased margin for better spacing */
    border: 1px solid #e0ce46; /* Bright border for images */
    padding: 15px;
  }
  
  .example-button {
    background-color: #282828;
    color: #e0ce46; /* Matching button color */
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    margin-right: 10px;
  }
  
  button:hover {
    background-color: #1f1f1f;
  }
  
  pre {
    background-color: #333;
    color: #00ff00; /* Green text color for code */
    padding: 15px;
    border-radius: 8px;
    overflow-x: auto;
    margin-top: 20px;
  }
  
  a {
    color: #e0ce46;
    text-decoration: underline;
  }
  
  a:hover {
    color: #f0f0f0;
  }
  
  </style>
  