<template>
    <div class="bitwise-container">
      <h1 class="main-title">Bitwise Algorithms</h1>
      <p class="intro">
        Bitwise algorithms manipulate individual bits of data, performing operations directly on binary representations of numbers.
      </p>
  
      <h2 class="sub-title">Key Characteristics of Bitwise Algorithms</h2>
      <ul class="characteristics-list">
        <li><strong>Direct Bit Manipulation:</strong> Operate directly on the bits of binary numbers.</li>
        <li><strong>Performance:</strong> Often faster than arithmetic operations due to lower-level processing.</li>
        <li><strong>Common Operations:</strong> Include AND, OR, NOT, XOR, left shift, and right shift.</li>
      </ul>
  
      <h2 class="sub-title">Diagram of Bitwise Operations</h2>
      <img src="@/assets/bitwise.png" alt="Bitwise Operations Diagram" class="bitwise-diagram"/>
  
      <h2 class="sub-title">Types of Bitwise Operations</h2>
      <h3 class="type-title">Bitwise AND</h3>
      <p>Performs a logical AND operation on each corresponding pair of bits.</p>
  
      <h3 class="type-title">Bitwise OR</h3>
      <p>Performs a logical OR operation on each corresponding pair of bits.</p>
  
      <h3 class="type-title">Bitwise XOR</h3>
      <p>Performs a logical exclusive OR operation on each corresponding pair of bits.</p>
  
      <h3 class="type-title">Bitwise NOT</h3>
      <p>Inverts the bits of a binary number.</p>
  
      <h2 class="sub-title">Bitwise Operations Examples</h2>
      <p>Click on the buttons below to see examples of bitwise operations in different programming languages:</p>
  
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
        <li><a href="https://www.youtube.com/watch?v=bitwise1" target="_blank">Bitwise Operations in Java (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=bitwise2" target="_blank">Bitwise Operations in Hindi</a></li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "BitwiseAlgorithms",
    data() {
      return {
        exampleCode: "",
      };
    },
    methods: {
      showExample(language) {
        if (language === 'java') {
          this.exampleCode = `public class BitwiseExample {
    public static void main(String[] args) {
      int a = 5; // 0101
      int b = 3; // 0011
      System.out.println(a & b); // Bitwise AND
      System.out.println(a | b); // Bitwise OR
      System.out.println(a ^ b); // Bitwise XOR
      System.out.println(~a); // Bitwise NOT
    }
  }`;
        } else if (language === 'c') {
          this.exampleCode = `#include <stdio.h>
  int main() {
      int a = 5; // 0101
      int b = 3; // 0011
      printf("%d\\n", a & b); // Bitwise AND
      printf("%d\\n", a | b); // Bitwise OR
      printf("%d\\n", a ^ b); // Bitwise XOR
      printf("%d\\n", ~a); // Bitwise NOT
      return 0;
  }`;
        } else if (language === 'python') {
          this.exampleCode = `a = 5  # 0101
  b = 3  # 0011
  print(a & b)  # Bitwise AND
  print(a | b)  # Bitwise OR
  print(a ^ b)  # Bitwise XOR
  print(~a)     # Bitwise NOT`;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .bitwise-container {
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
  
  .bitwise-diagram {
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
  