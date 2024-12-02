<template>
  <div class="algorithm-container">
    <h1 class="main-title">Dynamic Programming</h1>
    <p class="intro">
      Dynamic programming is a method for solving complex problems by breaking them down into simpler subproblems. It is particularly useful for optimization problems where decisions can be made in overlapping subproblems, ensuring that each subproblem is solved only once and stored for future reference.
    </p>

    <h2 class="sub-title">Key Concepts in Dynamic Programming</h2>
    <ul class="characteristics-list">
      <li><strong>Optimal Substructure:</strong> A problem exhibits optimal substructure if an optimal solution can be constructed efficiently from optimal solutions to its subproblems.</li>
      <li><strong>Overlapping Subproblems:</strong> Dynamic programming is used when the same subproblems are solved multiple times, which can be optimized by storing the solutions to these subproblems.</li>
      <li><strong>Memoization:</strong> Storing results of expensive function calls and reusing them when the same inputs occur again to avoid redundant calculations.</li>
      <li><strong>Tabulation:</strong> A bottom-up approach where results of subproblems are filled in a table and used to solve the larger problem.</li>
    </ul>

    <h2 class="sub-title">Diagram for Dynamic Programming</h2>
    <img src="@/assets/dynamic.jpg" alt="Dynamic Programming Diagram" class="algorithm-diagram imageedit" />

    <h2 class="sub-title">Example Algorithms</h2>
    <p>Select a category of dynamic programming algorithms to see examples:</p>
    <div class="button-container">
      <button @click="showAlgorithm('fibonacci')" class="example-button">Fibonacci Series</button>
      <button @click="showAlgorithm('knapsack')" class="example-button">0/1 Knapsack</button>
      <button @click="showAlgorithm('longestCommonSubsequence')" class="example-button">Longest Common Subsequence</button>
    </div>

    <pre v-if="algorithmExample">
      <code>{{ algorithmExample }}</code>
    </pre>

    <h2 class="sub-title">Generative Study Companion</h2>
    <div class="ai-notes-section">
      <button 
        @click="generateAINotes" 
        class="example-button ai-notes-button" 
        :disabled="isGenerating"
      >
        {{ isGenerating ? "Generating Study Guide..." : "Generate Study Guide" }}
      </button>
      <div v-if="aiNotesData" class="ai-notes-display">
        <h3 class="section-title">Comprehensive Study Notes</h3>
        <div v-html="aiNotesData"></div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "DynamicProgramming",
  data() {
    return {
      algorithmExample: "",
      aiNotesData: null,
      isGenerating: false,
      groqApiKey: "gsk_aDnm8wp2NRGnT22fo9dgWGdyb3FYxNbCK0jgBvX03KyyHv1UMlrsgr"
    };
  },
  methods: {
    showAlgorithm(type) {
      if (type === "fibonacci") {
        this.algorithmExample = `// Fibonacci Series using Dynamic Programming
int fib(int n) {
  int dp[n+1];
  dp[0] = 0;
  dp[1] = 1;
  for (int i = 2; i <= n; i++) {
    dp[i] = dp[i-1] + dp[i-2];
  }
  return dp[n];
}`;
      } else if (type === "knapsack") {
        this.algorithmExample = `// 0/1 Knapsack Problem using Dynamic Programming
int knapsack(int W, int wt[], int val[], int n) {
  int dp[n+1][W+1];
  for (int i = 0; i <= n; i++) {
    for (int w = 0; w <= W; w++) {
      if (i == 0 || w == 0)
        dp[i][w] = 0;
      else if (wt[i-1] <= w)
        dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w]);
      else
        dp[i][w] = dp[i-1][w];
    }
  }
  return dp[n][W];
}`;
      } else if (type === "longestCommonSubsequence") {
        this.algorithmExample = `// Longest Common Subsequence using Dynamic Programming
int lcs(string X, string Y, int m, int n) {
  int dp[m+1][n+1];
  for (int i = 0; i <= m; i++) {
    for (int j = 0; j <= n; j++) {
      if (i == 0 || j == 0)
        dp[i][j] = 0;
      else if (X[i-1] == Y[j-1])
        dp[i][j] = dp[i-1][j-1] + 1;
      else
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
    }
  }
  return dp[m][n];
}`;
      }
    },

    async generateAINotes() {
      this.isGenerating = true;
      this.aiNotesData = null;
      const prompt = `
        Generate a detailed study guide on dynamic programming, including:
        Explanation of key concepts (Memoization, Tabulation, Optimal Substructure).
        Comparison with greedy algorithms and divide-and-conquer techniques.
        Examples of algorithms (Fibonacci, Knapsack, Longest Common Subsequence).
        Common pitfalls and how to avoid them.
        Interview questions with solutions and coding challenges.
        A list of curated resources with clickable links.
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
          this.aiNotesData = `<div>${formattedResponse}</div>`;
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

.characteristics-list {
  margin: 10px 0;
  padding-left: 20px;
  font-size: 1.2em;
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

.ai-notes-section {
  margin-top: 30px;
  text-align: center;
}

.ai-notes-display {
  background-color: #1f1f1f;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
  margin-top: 20px;
}

.ai-notes-display a {
  color: #00ffcc;
  text-decoration: underline;
}
</style>