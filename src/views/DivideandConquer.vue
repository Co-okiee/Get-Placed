<!-- src/views/DivideAndConquer.vue -->
<template>
    <div class="divide-conquer-container">
      <h1 class="main-title">Divide and Conquer Algorithms</h1>
      <p class="intro">
        Divide and Conquer is an algorithm design paradigm that breaks a problem down into smaller sub-problems, solves each sub-problem recursively, and then combines their solutions to solve the original problem.
      </p>
  
      <h2 class="sub-title">Types of Divide and Conquer Algorithms</h2>
  
      <h3 class="type-title">1. Merge Sort</h3>
      <p>Merge Sort splits the array into two halves, recursively sorts them, and then merges the sorted halves to form a completely sorted array.</p>
      <img src="@/assets/merge-sort-diagram.png" alt="Merge Sort Diagram" class="algorithm-diagram"/>
  
      <h3 class="type-title">2. Quick Sort</h3>
      <p>Quick Sort selects a pivot element and partitions the array into sub-arrays where elements less than the pivot go to one side, and elements greater go to the other. The process is repeated recursively for both sub-arrays.</p>
      <img src="@/assets/quick-sort-diagram.png" alt="Quick Sort Diagram" class="algorithm-diagram"/>
  
      <h3 class="type-title">3. Binary Search</h3>
      <p>Binary Search repeatedly divides the sorted array in half, eliminating the half in which the target element cannot be, until the target element is found or the search space is empty.</p>
      <img src="@/assets/binary-search-diagram.png" alt="Binary Search Diagram" class="algorithm-diagram"/>
  
      <h3 class="type-title">4. Strassen’s Matrix Multiplication</h3>
      <p>Strassen's algorithm multiplies two matrices using a divide and conquer approach, reducing the number of multiplication operations compared to standard matrix multiplication.</p>
      <img src="@/assets/strassen-diagram.png" alt="Strassen Matrix Multiplication Diagram" class="algorithm-diagram"/>
  
      <h3 class="type-title">5. Closest Pair of Points</h3>
      <p>The Closest Pair of Points algorithm recursively divides the set of points into halves, finds the closest pairs in each half, and then checks across the dividing line for any closer pairs.</p>
      <img src="@/assets/closest-pair-diagram.png" alt="Closest Pair of Points Diagram" class="algorithm-diagram"/>
  
      <h3 class="type-title">6. Karatsuba Multiplication</h3>
      <p>Karatsuba’s algorithm is an efficient way to multiply two large numbers by splitting them into smaller parts, multiplying those parts, and combining the results.</p>
      <img src="@/assets/karatsuba-diagram.png" alt="Karatsuba Multiplication Diagram" class="algorithm-diagram"/>
  
      <h3 class="type-title">7. Matrix Chain Multiplication</h3>
      <p>This algorithm determines the optimal order to multiply matrices to minimize the number of scalar multiplications.</p>
      <img src="@/assets/matrix-chain-diagram.png" alt="Matrix Chain Multiplication Diagram" class="algorithm-diagram"/>
  
      <h2 class="sub-title">Declaration Syntax</h2>
      <p>Select a programming language to see the implementation of a Divide and Conquer algorithm:</p>
  
      <div class="button-container">
        <button @click="showDeclaration('java')" class="example-button">Java</button>
        <button @click="showDeclaration('c')" class="example-button">C</button>
        <button @click="showDeclaration('python')" class="example-button">Python</button>
      </div>
  
      <pre v-if="declarationCode">
        <code>{{ declarationCode }}</code>
      </pre>
  
      <h2 class="sub-title">Advantages of Divide and Conquer Algorithms</h2>
      <ul>
        <li>Divide and Conquer breaks complex problems into smaller, easier-to-manage sub-problems.</li>
        <li>It enables efficient recursive solutions that often outperform iterative approaches.</li>
      </ul>
  
      <h2 class="sub-title">Disadvantages of Divide and Conquer Algorithms</h2>
      <ul>
        <li>It can sometimes lead to higher space complexity due to recursion.</li>
        <li>Some divide and conquer algorithms are harder to implement and understand than their iterative counterparts.</li>
      </ul>
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=kPRA0W1kECg" target="_blank">Quick Sort Algorithm (Hindi)</a></li>
        <li><a href="https://www.youtube.com/watch?v=JSceec-wEyw" target="_blank">Merge Sort Algorithm (English)</a></li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "DivideAndConquer",
    data() {
      return {
        declarationCode: "",
      };
    },
    methods: {
      showDeclaration(language) {
        if (language === 'java') {
          this.declarationCode = `// Merge Sort in Java
  void mergeSort(int arr[], int l, int r) {
    if (l < r) {
      int m = l + (r - l) / 2;
      mergeSort(arr, l, m);
      mergeSort(arr, m + 1, r);
      merge(arr, l, m, r);
    }
  }
  
  void merge(int arr[], int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;
    int L[] = new int[n1];
    int R[] = new int[n2];
    for (int i = 0; i < n1; ++i)
      L[i] = arr[l + i];
    for (int j = 0; j < n2; ++j)
      R[j] = arr[m + 1 + j];
    int i = 0, j = 0;
    int k = l;
    while (i < n1 && j < n2) {
      if (L[i] <= R[j]) {
        arr[k] = L[i];
        i++;
      } else {
        arr[k] = R[j];
        j++;
      }
      k++;
    }
    while (i < n1) {
      arr[k] = L[i];
      i++;
      k++;
    }
    while (j < n2) {
      arr[k] = R[j];
      j++;
      k++;
    }
  }`;
        } else if (language === 'c') {
          this.declarationCode = `// Merge Sort in C
  void mergeSort(int arr[], int l, int r) {
    if (l < r) {
      int m = l + (r - l) / 2;
      mergeSort(arr, l, m);
      mergeSort(arr, m + 1, r);
      merge(arr, l, m, r);
    }
  }
  
  void merge(int arr[], int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;
    int L[n1], R[n2];
    for (int i = 0; i < n1; i++)
      L[i] = arr[l + i];
    for (int j = 0; j < n2; j++)
      R[j] = arr[m + 1 + j];
    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2) {
      if (L[i] <= R[j]) {
        arr[k] = L[i];
        i++;
      } else {
        arr[k] = R[j];
        j++;
      }
      k++;
    }
    while (i < n1) {
      arr[k] = L[i];
      i++;
      k++;
    }
    while (j < n2) {
      arr[k] = R[j];
      j++;
      k++;
    }
  }`;
        } else if (language === 'python') {
          this.declarationCode = `# Merge Sort in Python
  def mergeSort(arr):
      if len(arr) > 1:
          mid = len(arr) // 2
          L = arr[:mid]
          R = arr[mid:]
  
          mergeSort(L)
          mergeSort(R)
  
          i = j = k = 0
          while i < len(L) and j < len(R):
              if L[i] < R[j]:
                  arr[k] = L[i]
                  i += 1
              else:
                  arr[k] = R[j]
                  j += 1
              k += 1
          while i < len(L):
              arr[k] = L[i]
              i += 1
              k += 1
          while j < len(R):
              arr[k] = R[j]
              j += 1
              k += 1`;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .divide-conquer-container {
    max-width: 800px;
    margin: 0 auto;
    color: #e0e0e0;
  }
  
  .main-title {
    text-align: center;
    color: #e0ce46;
    margin-bottom: 20px;
  }
  
  .sub-title {
    margin-top: 40px;
    font-size: 1.5em;
    color: #e0ce46;
  }
  
  .intro, p {
    font-size: 1.1em;
    line-height: 1.6;
  }
  
  ul {
    margin-left: 20px;
  }
  
  .algorithm-diagram {
    width: 100%;
    max-height: 300px;
    border: 5px solid #e0ce46;
    padding: 15px;
    margin-bottom: 20px;
  }
  
  .example-button {
    background-color: #282828;
    color: #e0ce46;
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
    color: #00ff00;
    padding: 15px;
    border-radius: 8px;
    overflow-x: auto;
    margin-top: 20px;
  }
  
  a {
    color: #e0ce46;
  }
  
  a:hover {
    color: #f0f0f0;
  }
  </style>
  