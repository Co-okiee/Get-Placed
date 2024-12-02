<!-- src/views/Recursion.vue -->
<template>
    <div class="algorithm-container">
      <h1 class="main-title">Recursion</h1>
      <p class="intro">
        Recursion is a programming technique where a function calls itself directly or indirectly to solve a problem. It is used to break down complex problems into simpler sub-problems.
      </p>
  
      <h2 class="sub-title">Key Concepts in Recursion</h2>
      <ul class="characteristics-list">
        <li><strong>Base Case:</strong> The condition under which the recursion ends. It prevents infinite loops.</li>
        <li><strong>Recursive Case:</strong> The part of the function that includes the recursive call to solve smaller instances of the problem.</li>
        <li><strong>Stack Overflow:</strong> A common issue in recursion where too many function calls are made, exceeding the call stack limit.</li>
      </ul>
  
      <h2 class="sub-title">Diagram for Recursion Flow</h2>
      <img src="@/assets/recursion-diagram.png" alt="Recursion Flow Diagram" class="algorithm-diagram"/>
  
      <h2 class="sub-title">Example Algorithms</h2>
      <p>Select a category of algorithms to see examples:</p>
  
      <div class="button-container">
        <button @click="showAlgorithm('factorial')" class="example-button">Factorial Function</button>
        <button @click="showAlgorithm('fibonacci')" class="example-button">Fibonacci Series</button>
        <button @click="showAlgorithm('towerOfHanoi')" class="example-button">Tower of Hanoi</button>
      </div>
  
      <pre v-if="algorithmExample">
        <code>{{ algorithmExample }}</code>
      </pre>
  
      <h2 class="sub-title">Types of Recursion</h2>
      <h3 class="type-title">Direct Recursion</h3>
      <p>Direct recursion occurs when a function calls itself directly to solve smaller sub-problems.</p>
  
      <h3 class="type-title">Indirect Recursion</h3>
      <p>Indirect recursion occurs when a function calls another function, which then calls the first function.</p>
  
      <h2 class="sub-title">Advantages of Recursion</h2>
      <ul>
        <li>Simplifies code by reducing the need for explicit stack management.</li>
        <li>Provides clear solutions for problems that can be defined in terms of smaller sub-problems.</li>
        <li>Helps in solving problems like tree traversal and graph algorithms efficiently.</li>
      </ul>
  
      <h2 class="sub-title">Disadvantages of Recursion</h2>
      <ul>
        <li>Can lead to high memory consumption due to the call stack.</li>
        <li>Risk of stack overflow for deep recursion without optimization.</li>
        <li>Performance can be slower than iterative solutions due to function call overhead.</li>
      </ul>
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=Y2a0fdr1h_Q" target="_blank">Understanding Recursion (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=JrY_sKzJ_sA" target="_blank">Recursion in Hindi</a></li>
      </ul>
    </div>
</template>

<script>
export default {
  name: "Recursion",
  data() {
    return {
      algorithmExample: "",
    };
  },
  methods: {
    showAlgorithm(type) {
      if (type === 'factorial') {
        this.algorithmExample = `// Example of Factorial Function using Recursion
function factorial(n) {
  if (n <= 1) return 1; // Base Case
  return n * factorial(n - 1); // Recursive Case
}`;
      } else if (type === 'fibonacci') {
        this.algorithmExample = `// Example of Fibonacci Function using Recursion
function fibonacci(n) {
  if (n <= 1) return n; // Base Case
  return fibonacci(n - 1) + fibonacci(n - 2); // Recursive Case
}`;
      } else if (type === 'towerOfHanoi') {
        this.algorithmExample = `// Example of Tower of Hanoi using Recursion
function towerOfHanoi(n, source, target, auxiliary) {
  if (n === 1) {
    console.log(\Move disk 1 from \${source} to \${target}\);
    return;
  }
  towerOfHanoi(n - 1, source, auxiliary, target);
  console.log(\Move disk \${n} from \${source} to \${target}\);
  towerOfHanoi(n - 1, auxiliary, target, source);
}`;
      }
    },
  },
};
</script>

<style scoped>
.algorithm-container {
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

.algorithm-diagram {
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