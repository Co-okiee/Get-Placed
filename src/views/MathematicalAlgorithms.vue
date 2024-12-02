<!-- src/views/MathematicalAlgorithms.vue -->
<template>
    <div class="math-algo-container">
      <h1 class="main-title">Mathematical Algorithms</h1>
      <p class="intro">
        Mathematical algorithms focus on solving mathematical problems such as finding the greatest common divisor (GCD), primality tests, factorials, and Fibonacci series. These algorithms are foundational and used across multiple fields like cryptography, number theory, and scientific computing.
      </p>
  
      <h2 class="sub-title">Types of Mathematical Algorithms</h2>
  
      <h3 class="type-title">1. Euclidean Algorithm (GCD)</h3>
      <p>The Euclidean algorithm is used to find the greatest common divisor (GCD) of two numbers by repeatedly dividing them and using the remainder until the remainder is zero.</p>
      <img src="@/assets/euclidean-diagram.png" alt="Euclidean Algorithm Diagram" class="algorithm-diagram"/>
  
      <h3 class="type-title">2. Sieve of Eratosthenes</h3>
      <p>The Sieve of Eratosthenes is an efficient algorithm to find all prime numbers up to a given limit by iteratively marking the multiples of each prime starting from 2.</p>
      <img src="@/assets/sieve-diagram.png" alt="Sieve of Eratosthenes Diagram" class="algorithm-diagram"/>
  
      <h3 class="type-title">3. Fibonacci Series</h3>
      <p>The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. The series can be generated using a simple recursive or iterative approach.</p>
      <img src="@/assets/fibonacci-diagram.png" alt="Fibonacci Series Diagram" class="algorithm-diagram"/>
  
      <h3 class="type-title">4. Fast Exponentiation</h3>
      <p>Fast exponentiation (also known as exponentiation by squaring) is an efficient way to compute large powers of a number by dividing the problem into smaller parts recursively.</p>
      <img src="@/assets/fast-exponentiation-diagram.png" alt="Fast Exponentiation Diagram" class="algorithm-diagram"/>
  
      <h3 class="type-title">5. Factorial Calculation</h3>
      <p>The factorial of a non-negative integer n is the product of all positive integers less than or equal to n, denoted as n!. Factorials can be computed using recursive or iterative approaches.</p>
      <img src="@/assets/factorial-diagram.png" alt="Factorial Diagram" class="algorithm-diagram"/>
  
      <h3 class="type-title">6. Modular Arithmetic</h3>
      <p>Modular arithmetic involves operations on integers where numbers wrap around upon reaching a certain value (the modulus). It is widely used in cryptography and number theory.</p>
      <img src="@/assets/modular-arithmetic-diagram.png" alt="Modular Arithmetic Diagram" class="algorithm-diagram"/>
  
      <h2 class="sub-title">Declaration Syntax</h2>
      <p>Select a programming language to see the implementation of a mathematical algorithm:</p>
  
      <div class="button-container">
        <button @click="showDeclaration('java')" class="example-button">Java</button>
        <button @click="showDeclaration('c')" class="example-button">C</button>
        <button @click="showDeclaration('python')" class="example-button">Python</button>
      </div>
  
      <pre v-if="declarationCode">
        <code>{{ declarationCode }}</code>
      </pre>
  
      <h2 class="sub-title">Advantages of Mathematical Algorithms</h2>
      <ul>
        <li>Efficiently solve mathematical problems that arise in various fields like cryptography and computer science.</li>
        <li>Highly optimized to deal with large numbers and complex computations.</li>
      </ul>
  
      <h2 class="sub-title">Disadvantages of Mathematical Algorithms</h2>
      <ul>
        <li>Some algorithms may require deep mathematical understanding to implement correctly.</li>
        <li>Can become complex when dealing with high precision or large numbers.</li>
      </ul>
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=pBK-wE54kUY" target="_blank">Sieve of Eratosthenes Algorithm (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=4NzPa7AoQn0" target="_blank">Euclidean Algorithm for GCD (Hindi)</a></li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "MathematicalAlgorithms",
    data() {
      return {
        declarationCode: "",
      };
    },
    methods: {
      showDeclaration(language) {
        if (language === 'java') {
          this.declarationCode = `// GCD using Euclidean Algorithm in Java
  int gcd(int a, int b) {
    if (b == 0)
      return a;
    return gcd(b, a % b);
  }`;
        } else if (language === 'c') {
          this.declarationCode = `// GCD using Euclidean Algorithm in C
  int gcd(int a, int b) {
    if (b == 0)
      return a;
    return gcd(b, a % b);
  }`;
        } else if (language === 'python') {
          this.declarationCode = `# GCD using Euclidean Algorithm in Python
  def gcd(a, b):
      while b:
          a, b = b, a % b
      return a`;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  
  .math-algo-container {
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
  
  .intro,
  p {
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
  
  .example-button:hover {
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
  