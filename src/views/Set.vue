<template>
    <div class="set-container">
      <h1 class="main-title">Sets</h1>
      <p class="intro">
        A set is a collection of distinct elements, meaning it does not allow duplicate values. Sets are often used to represent collections of unique items, such as tags or categories.
      </p>
  
      <h2 class="sub-title">Key Characteristics of Sets</h2>
      <ul class="characteristics-list">
        <li><strong>Uniqueness:</strong> Each element in a set must be unique; no duplicates are allowed.</li>
        <li><strong>Unordered:</strong> The elements in a set do not have a specific order.</li>
        <li><strong>Dynamic Size:</strong> Sets can grow or shrink dynamically as elements are added or removed.</li>
      </ul>
  
      <h2 class="sub-title">Types of Sets</h2>
      <h3 class="type-title">Finite Set</h3>
      <p>A set with a limited number of elements.</p>
  
      <h3 class="type-title">Infinite Set</h3>
      <p>A set with an unlimited number of elements.</p>
  
      <h3 class="type-title">Subset</h3>
      <p>A set that contains some or all elements of another set.</p>
  
      <h2 class="sub-title">Set Operations</h2>
      <ul>
        <li><strong>Union:</strong> Combines elements from two sets.</li>
        <li><strong>Intersection:</strong> Returns elements that are common to both sets.</li>
        <li><strong>Difference:</strong> Returns elements in one set but not in the other.</li>
        <li><strong>Symmetric Difference:</strong> Returns elements in either of the sets but not in both.</li>
      </ul>
  
      <h2 class="sub-title">Examples</h2>
      <p>Click on the buttons below to see examples of sets in different programming languages:</p>
  
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
        <li><a href="https://www.youtube.com/watch?v=set1" target="_blank">Sets in Java (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=set2" target="_blank">Sets in Hindi</a></li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "Set",
    data() {
      return {
        exampleCode: "",
      };
    },
    methods: {
      showExample(language) {
        if (language === 'java') {
          this.exampleCode = `import java.util.HashSet;
  
  class SetExample {
      public static void main(String[] args) {
          HashSet<Integer> set = new HashSet<>();
          set.add(1);
          set.add(2);
          set.add(3);
          set.add(1); // Duplicate, will not be added
  
          System.out.println(set); // Output: [1, 2, 3]
      }
  }`;
        } else if (language === 'c') {
          this.exampleCode = `#include <stdio.h>
  #include <stdlib.h>
  
  #define MAX_ELEMENTS 100
  
  struct Set {
      int elements[MAX_ELEMENTS];
      int size;
  };
  
  void add(struct Set* set, int element) {
      for (int i = 0; i < set->size; i++) {
          if (set->elements[i] == element) {
              return; // Element already exists
          }
      }
      set->elements[set->size++] = element;
  }
  `;
        } else if (language === 'python') {
          this.exampleCode = `# Creating a set in Python
  my_set = {1, 2, 3}
  my_set.add(4)
  my_set.add(1)  # Duplicate, will not be added
  
  print(my_set)  # Output: {1, 2, 3, 4}
  `;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .set-container {
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
  