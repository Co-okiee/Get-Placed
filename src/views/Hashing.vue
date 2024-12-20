<template>
    <div class="hashing-container">
      <h1 class="main-title">Hashing</h1>
      <p class="intro">
        Hashing is a technique used to uniquely identify a specific object from a group of similar objects. It transforms input data of arbitrary size into a fixed-size value, often called a hash code, using a hash function.
      </p>
  
      <h2 class="sub-title">Key Characteristics of Hashing</h2>
      <ul class="characteristics-list">
        <li><strong>Efficient Data Retrieval:</strong> Hashing allows for quick data access through direct indexing.</li>
        <li><strong>Fixed Size:</strong> The output of the hash function has a fixed size, regardless of the input size.</li>
        <li><strong>Collision Handling:</strong> Hashing must handle collisions where different inputs produce the same hash value.</li>
      </ul>
  
      <h2 class="sub-title">Hash Table Structure</h2>
      <img src="@/assets/hash_table.png" alt="Hash Table Diagram" class="hash-table-diagram"/>
  
      <h2 class="sub-title">Types of Hashing</h2>
      <h3 class="type-title">Closed Addressing (Chaining)</h3>
      <p>Each slot of the hash table contains a linked list of entries that hash to the same index.</p>
  
      <h3 class="type-title">Open Addressing</h3>
      <p>All entries are stored directly in the hash table, with probing used to find the next available slot when collisions occur.</p>
  
      <h2 class="sub-title">Hashing Operations</h2>
      <p>Common operations include inserting a key-value pair, searching for a value by key, and deleting a key-value pair.</p>
  
      <h2 class="sub-title">Hash Functions</h2>
      <p>Hash functions map input data to a fixed size. A good hash function minimizes collisions and uniformly distributes values across the hash table.</p>
  
      <h2 class="sub-title">Examples</h2>
      <p>Click on the buttons below to see examples of hashing in different programming languages:</p>
  
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
        <li><a href="https://www.youtube.com/watch?v=hashing1" target="_blank">Hashing in Java (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=hashing2" target="_blank">Hashing in Hindi</a></li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "Hashing",
    data() {
      return {
        exampleCode: "",
      };
    },
    methods: {
      showExample(language) {
        if (language === 'java') {
          this.exampleCode = `import java.util.HashMap;
  HashMap<String, Integer> map = new HashMap<>();
  map.put("Key1", 1);
  System.out.println(map.get("Key1")); // Output: 1`;
        } else if (language === 'c') {
          this.exampleCode = `#include <stdio.h>
  #include <stdlib.h>
  #define TABLE_SIZE 10
  struct HashNode {
      int key;
      int value;
      struct HashNode* next;
  };
  struct HashNode* table[TABLE_SIZE];`;
        } else if (language === 'python') {
          this.exampleCode = `hash_map = {}
  hash_map["key1"] = 1
  print(hash_map["key1"])  # Output: 1`;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .hashing-container {
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
  
  .hash-table-diagram {
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
  