<template>
  <div class="algorithm-container">
    <h1 class="main-title">Backtracking</h1>
    <p class="intro">
      Backtracking is an algorithmic method that incrementally builds solutions to problems, abandoning paths that fail to meet constraints. It is widely used in combinatorial search problems like the N-Queens problem, maze solving, and subset sums.
    </p>

    <h2 class="sub-title">Key Concepts in Backtracking</h2>
    <ul class="characteristics-list">
      <li><strong>State Space Tree:</strong> A conceptual tree structure representing all potential solutions.</li>
      <li><strong>Pruning:</strong> Eliminating branches that cannot yield a valid solution.</li>
      <li><strong>Recursive Approach:</strong> Most backtracking algorithms use recursion to explore solution paths.</li>
    </ul>

    <h2 class="sub-title">Diagram for Backtracking</h2>
    <img src="@/assets/backtracking.png" alt="Backtracking Diagram" class="algorithm-diagram imageedit" />

    <h2 class="sub-title">Example Algorithms</h2>
    <p>Select an algorithm to view its implementation:</p>
    <div class="button-container">
      <button @click="showAlgorithm('nqueens')" class="example-button">N-Queens Problem</button>
      <button @click="showAlgorithm('subset')" class="example-button">Subset Sum Problem</button>
      <button @click="showAlgorithm('maze')" class="example-button">Maze Solver</button>
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
      <li><a href="https://www.geeksforgeeks.org/backtracking-algorithms/" target="_blank">GeeksforGeeks - Backtracking Algorithms</a></li>
      <li><a href="https://www.youtube.com/watch?v=7q2Rl8coZ-0" target="_blank">YouTube - Backtracking Algorithms (English)</a></li>
      <li><a href="https://www.youtube.com/watch?v=4_0I4dZ7F8s" target="_blank">YouTube - Backtracking in Hindi</a></li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Backtracking",
  data() {
    return {
      algorithmExample: "",
      aiNotesData: null,
      isGenerating: false,
      groqApiKey: "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",
    };
  },
  methods: {
    showAlgorithm(type) {
      if (type === "nqueens") {
        this.algorithmExample = `// N-Queens Problem using Backtracking
void solveNQueens(int n) {
  vector<int> board(n, -1);
  placeQueens(board, 0);
}

void placeQueens(vector<int>& board, int row) {
  if (row == board.size()) {
    // Print the solution
    return;
  }
  for (int col = 0; col < board.size(); col++) {
    if (isSafe(board, row, col)) {
      board[row] = col;
      placeQueens(board, row + 1);
      board[row] = -1; // Backtrack
    }
  }
}`;
      } else if (type === "subset") {
        this.algorithmExample = `// Subset Sum Problem using Backtracking
bool subsetSum(int arr[], int n, int sum) {
  if (sum == 0) return true;
  if (n == 0) return false;
  if (arr[n - 1] > sum) return subsetSum(arr, n - 1, sum);
  return subsetSum(arr, n - 1, sum) || subsetSum(arr, n - 1, sum - arr[n - 1]);
}`;
      } else if (type === "maze") {
        this.algorithmExample = `// Maze Solver using Backtracking
bool solveMaze(int maze[N][N], int x, int y, int sol[N][N]) {
  if (x == N - 1 && y == N - 1) {
    sol[x][y] = 1;
    return true;
  }
  if (isSafe(maze, x, y)) {
    sol[x][y] = 1;
    if (solveMaze(maze, x + 1, y, sol)) return true;
    if (solveMaze(maze, x, y + 1, sol)) return true;
    sol[x][y] = 0; // Backtrack
  }
  return false;
}`;
      }
    },

    async generateAINotes() {
      this.isGenerating = true;
      this.aiNotesData = null;

      const prompt = `
        Provide a detailed guide on backtracking including:
        - Key concepts (state space tree, pruning, recursion).
        - Examples: N-Queens Problem, Subset Sum Problem, Maze Solver.
        - Advantages and disadvantages.
        - Real-world applications and constraints.
        - Interview questions and solutions.
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
              "Content-Type": "application/json",
            },
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
        alert("Failed to generate AI study notes. Please try again.");
      } finally {
        this.isGenerating = false;
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
  font-family: "Roboto", sans-serif;
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
  font-size: 1.2em;
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