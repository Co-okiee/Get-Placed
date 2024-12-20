<!-- src/views/Backtracking.vue -->
<template>
    <div class="algorithm-container">
      <h1 class="main-title">Backtracking</h1>
      <p class="intro">
        Backtracking is an algorithmic technique used for solving problems incrementally by trying partial solutions and then abandoning them if they are not viable. It is commonly used in problems related to combinatorial search, constraint satisfaction, and optimization.
      </p>
  
      <h2 class="sub-title">Key Concepts in Backtracking</h2>
      <ul class="characteristics-list">
        <li><strong>State Space Tree:</strong> A tree structure that represents all possible states of a problem, where each node represents a decision.</li>
        <li><strong>Pruning:</strong> The process of eliminating branches in the state space tree that cannot yield a valid solution.</li>
        <li><strong>Recursive Approach:</strong> Backtracking often employs recursion to explore possible solutions.</li>
      </ul>
  
      <h2 class="sub-title">Diagram for Backtracking</h2>
      <img src="@/assets/backtracking-diagram.png" alt="Backtracking Diagram" class="algorithm-diagram"/>
  
      <h2 class="sub-title">Example Algorithms</h2>
      <p>Select a category of algorithms to see examples:</p>
  
      <div class="button-container">
        <button @click="showAlgorithm('nqueens')" class="example-button">N-Queens Problem</button>
        <button @click="showAlgorithm('subset')" class="example-button">Subset Sum Problem</button>
        <button @click="showAlgorithm('maze')" class="example-button">Maze Solver</button>
      </div>
  
      <pre v-if="algorithmExample">
        <code>{{ algorithmExample }}</code>
      </pre>
  
      <h2 class="sub-title">Types of Backtracking Problems</h2>
      <h3 class="type-title">Constraint Satisfaction Problems</h3>
      <p>These problems require finding a solution that satisfies all given constraints, such as Sudoku.</p>
  
      <h3 class="type-title">Combinatorial Problems</h3>
      <p>Problems that involve generating combinations or permutations, like generating subsets of a set.</p>
  
      <h3 class="type-title">Optimization Problems</h3>
      <p>These involve finding the best solution from a set of feasible solutions, such as the Traveling Salesman Problem.</p>
  
      <h2 class="sub-title">Advantages of Backtracking</h2>
      <ul>
        <li>Provides a systematic way to explore all potential solutions to a problem.</li>
        <li>Efficiently prunes the search space, reducing time complexity in many cases.</li>
        <li>Can be implemented using recursion, leading to simpler code in many scenarios.</li>
      </ul>
  
      <h2 class="sub-title">Disadvantages of Backtracking</h2>
      <ul>
        <li>Can have exponential time complexity in the worst case, making it unsuitable for large problem instances.</li>
        <li>Requires additional memory for maintaining the recursion stack.</li>
        <li>Not always optimal; may require additional heuristics to improve performance.</li>
      </ul>
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=7q2Rl8coZ-0" target="_blank">Backtracking Algorithms (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=4_0I4dZ7F8s" target="_blank">Backtracking in Hindi</a></li>
      </ul>
    </div>
</template>

<script>
export default {
    name: "Backtracking",
    data() {
      return {
        algorithmExample: "",
      };
    },
    methods: {
      showAlgorithm(type) {
        if (type === 'nqueens') {
          this.algorithmExample = `// Example of N-Queens Problem
  void solveNQueens(int n) {
      vector<int> board(n, -1);
      placeQueens(board, 0);
  }

  void placeQueens(vector<int>& board, int row) {
      if (row == board.size()) {
          // Print the board
          return;
      }
      for (int col = 0; col < board.size(); col++) {
          if (isSafe(board, row, col)) {
              board[row] = col;
              placeQueens(board, row + 1);
              board[row] = -1; // backtrack
          }
      }
  }`;
        } else if (type === 'subset') {
          this.algorithmExample = `// Example of Subset Sum Problem
  bool subsetSum(int arr[], int n, int sum) {
      if (sum == 0) return true;
      if (n == 0) return false;
      if (arr[n-1] > sum)
          return subsetSum(arr, n-1, sum);
      return subsetSum(arr, n-1, sum) || subsetSum(arr, n-1, sum - arr[n-1]);
  }`;
        } else if (type === 'maze') {
          this.algorithmExample = `// Example of Maze Solver
  bool solveMaze(int maze[N][N], int x, int y, int sol[N][N]) {
      if (x == N-1 && y == N-1) {
          sol[x][y] = 1;
          return true;
      }
      if (isSafe(maze, x, y)) {
          sol[x][y] = 1;
          if (solveMaze(maze, x + 1, y, sol)) return true;
          if (solveMaze(maze, x, y + 1, sol)) return true;
          sol[x][y] = 0; // backtrack
      }
      return false;
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