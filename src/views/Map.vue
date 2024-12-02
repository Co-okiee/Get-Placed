<template>
    <div class="map-container">
      <h1 class="main-title">Maps</h1>
      <p class="intro">
        A map is a collection of key-value pairs where each key is unique. Maps are used to associate values with keys, allowing for efficient retrieval of values based on their keys.
      </p>
  
      <h2 class="sub-title">Key Characteristics of Maps</h2>
      <ul class="characteristics-list">
        <li><strong>Key-Value Pairs:</strong> Each element in a map consists of a key and a corresponding value.</li>
        <li><strong>Unique Keys:</strong> Each key in a map must be unique; duplicate keys are not allowed.</li>
        <li><strong>Dynamic Size:</strong> Maps can grow or shrink as elements are added or removed.</li>
      </ul>
  
      <h2 class="sub-title">Types of Maps</h2>
      <h3 class="type-title">HashMap</h3>
      <p>A map implementation that uses a hash table to store key-value pairs, providing average constant time complexity for basic operations.</p>
  
      <h3 class="type-title">TreeMap</h3>
      <p>A map implementation that stores keys in a sorted order based on their natural ordering or a specified comparator.</p>
  
      <h3 class="type-title">LinkedHashMap</h3>
      <p>A map that maintains the insertion order of keys, combining the properties of hash tables and linked lists.</p>
  
      <h2 class="sub-title">Map Operations</h2>
      <ul>
        <li><strong>Put:</strong> Adds a key-value pair to the map.</li>
        <li><strong>Get:</strong> Retrieves the value associated with a given key.</li>
        <li><strong>Remove:</strong> Removes a key-value pair from the map based on the key.</li>
        <li><strong>Contains Key:</strong> Checks if a specific key exists in the map.</li>
      </ul>
  
      <h2 class="sub-title">Examples</h2>
      <p>Click on the buttons below to see examples of maps in different programming languages:</p>
  
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
        <li><a href="https://www.youtube.com/watch?v=map1" target="_blank">Maps in Java (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=map2" target="_blank">Maps in Hindi</a></li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "Map",
    data() {
      return {
        exampleCode: "",
      };
    },
    methods: {
      showExample(language) {
        if (language === 'java') {
          this.exampleCode = `import java.util.HashMap;
  
  class MapExample {
      public static void main(String[] args) {
          HashMap<String, Integer> map = new HashMap<>();
          map.put("one", 1);
          map.put("two", 2);
          map.put("three", 3);
  
          System.out.println(map.get("two")); // Output: 2
      }
  }`;
        } else if (language === 'c') {
          this.exampleCode = `#include <stdio.h>
  #include <stdlib.h>
  
  #define TABLE_SIZE 100
  
  struct MapEntry {
      char* key;
      int value;
      struct MapEntry* next;
  };
  
  struct Map {
      struct MapEntry* table[TABLE_SIZE];
  };
  
  unsigned int hash(char* key) {
      // Simple hash function
      return (unsigned int)key[0] % TABLE_SIZE;
  }
  
  void put(struct Map* map, char* key, int value) {
      unsigned int index = hash(key);
      struct MapEntry* new_entry = malloc(sizeof(struct MapEntry));
      new_entry->key = key;
      new_entry->value = value;
      new_entry->next = map->table[index];
      map->table[index] = new_entry;
  }
  `;
        } else if (language === 'python') {
          this.exampleCode = `# Creating a map in Python
  my_map = {'one': 1, 'two': 2, 'three': 3}
  print(my_map['two'])  # Output: 2
  `;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .map-container {
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
  