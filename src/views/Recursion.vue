<template>
  <div class="algorithm-container">
    <h1 class="main-title">Recursion</h1>
    <p class="intro">
      Recursion is a programming method where a function solves a problem by calling itself. It divides the problem into smaller sub-problems until reaching a base case.
    </p>

    <h2 class="sub-title">Key Concepts in Recursion</h2>
    <ul class="characteristics-list">
      <li><strong>Base Case:</strong> The stopping condition for recursion to avoid infinite loops.</li>
      <li><strong>Recursive Case:</strong> The function's logic to solve smaller problems.</li>
      <li><strong>Stack Overflow:</strong> An error due to excessive recursive calls exceeding the stack limit.</li>
    </ul>

  

    <h2 class="sub-title">Example Algorithms</h2>
    <p>Choose an algorithm to view its code:</p>
    <div class="button-container">
      <button @click="showAlgorithm('factorial')" class="example-button">Factorial Function</button>
      <button @click="showAlgorithm('fibonacci')" class="example-button">Fibonacci Series</button>
      <button @click="showAlgorithm('towerOfHanoi')" class="example-button">Tower of Hanoi</button>
    </div>

    <pre v-if="algorithmExample">
      <code>{{ algorithmExample }}</code>
    </pre>

    <h2 class="sub-title">Generative Study Notes</h2>
    <div class="ai-notes-section">
      <button 
        @click="generateAINotes" 
        class="example-button ai-notes-button" 
        :disabled="isGenerating"
      >
        {{ isGenerating ? "Generating Study Notes..." : "Generate Study Notes" }}
      </button>
      <div v-if="aiNotesData" class="ai-notes-display">
        <h3 class="section-title">AI Study Notes</h3>
        <div v-html="aiNotesData"></div>
      </div>
    </div>

    <h2 class="sub-title">Useful Links</h2>
    <ul>
      <li><a href="https://www.geeksforgeeks.org/recursion/" target="_blank">GeeksforGeeks - Recursion Explained</a></li>
      <li><a href="https://www.youtube.com/watch?v=Y2a0fdr1h_Q" target="_blank">YouTube - Understanding Recursion (English)</a></li>
      <li><a href="https://www.youtube.com/watch?v=JrY_sKzJ_sA" target="_blank">YouTube - Recursion in Hindi</a></li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Recursion",
  data() {
    return {
      algorithmExample: "",
      aiNotesData: null,
      isGenerating: false,
      groqApiKey: "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"
    };
  },
  methods: {
    showAlgorithm(type) {
      if (type === "factorial") {
        this.algorithmExample = `// Factorial Function using Recursion
function factorial(n) {
  if (n <= 1) return 1; // Base Case
  return n * factorial(n - 1); // Recursive Case
}`;
      } else if (type === "fibonacci") {
        this.algorithmExample = `// Fibonacci Series using Recursion
function fibonacci(n) {
  if (n <= 1) return n; // Base Case
  return fibonacci(n - 1) + fibonacci(n - 2); // Recursive Case
}`;
      } else if (type === "towerOfHanoi") {
        this.algorithmExample = `// Tower of Hanoi using Recursion
function towerOfHanoi(n, source, target, auxiliary) {
  if (n === 1) {
    console.log(\`Move disk 1 from \${source} to \${target}\`);
    return;
  }
  towerOfHanoi(n - 1, source, auxiliary, target);
  console.log(\`Move disk \${n} from \${source} to \${target}\`);
  towerOfHanoi(n - 1, auxiliary, target, source);
}`;
      }
    },

    async generateAINotes() {
      this.isGenerating = true;
      this.aiNotesData = null;

      const prompt = `
        Generate a detailed study guide on recursion, including:
        - Explanation of key concepts (base case, recursive case).
        - Examples with code: Factorial, Fibonacci, Tower of Hanoi.
        - Advantages and disadvantages of recursion.
        - Real-world applications and limitations.
        - Common interview questions and solutions.
      `;

      try {
        const response = await axios.post(
          "https://api.groq.com/openai/v1/chat/completions",
          {
            model: "mixtral-8x7b-32768",
            messages: [{ role: "user", content: prompt }],
            temperature: 0.8,
            max_tokens: 3000,
          },
          {
            headers: {
              Authorization: `Bearer ${this.groqApiKey}`,
              "Content-Type": "application/json"
            }
          }
        );
        if (response.data && response.data.choices && response.data.choices.length > 0) {
          const formattedResponse = response.data.choices[0].message.content
            .replace(/\n/g, "<br>")
            .replace(/(\d\.\s)/g, "<b>$1</b>")
            .replace(
              /(https?:\/\/[^\s]+)/g,
              `<a href="$1" target="_blank" style="color:#00ffcc;">$1</a>`
            );
          this.aiNotesData = `<div style="text-align: left;">${formattedResponse}</div>`;
        } else {
          throw new Error("Invalid response from API");
        }
      } catch (error) {
        console.error("Error generating AI notes:", error.message);
        alert("Failed to generate AI notes. Please try again.");
      } finally {
        this.isGenerating = false;
      }
    }
  }
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

.sub-title {
font-size: 1.5em;
color: #0d9bbb;
margin-top: 20px;
}

.main-title {
font-size: 4em;
color: #ccc;
text-align: center;
}

.imageedit {
  margin: 10px; /* Adds space around each image */
  padding: 5px; /* Optional: Adds inner space within the image border */
  border: 1px solid #ccc; /* Optional: Adds a border for better visibility */
}

.intro {
  font-size: 1.3em;
  margin-bottom: 25px;
}

.algorithm-diagram {
  width: 100%;
  height: auto;
  margin: 30px 0;
}

pre {
  background-color: #1f1f1f;
  padding: 10px;
  border-radius: 5px;
  color: #00ff00;
  font-size: 1.2em;
}

.example-button {
  background-color: #ffcc00;
  color: #121212;
  border-radius: 5px;
  padding: 15px 30px;
}

.example-button:hover {
  background-color: #ffe066;
}

a {
  color: #e0ce46;
  text-decoration: none;
}

a:hover {
  color: #fff;
}
</style>