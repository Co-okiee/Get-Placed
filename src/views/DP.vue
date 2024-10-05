<!-- src/views/DynamicProgramming.vue -->
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
      <img src="@/assets/dynamic-programming-diagram.png" alt="Dynamic Programming Diagram" class="algorithm-diagram"/>
  
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
  
      <h2 class="sub-title">Types of Dynamic Programming Problems</h2>
      <h3 class="type-title">Optimization Problems</h3>
      <p>In optimization problems, dynamic programming is used to find the best solution by evaluating various subproblems and combining their solutions.</p>
  
      <h3 class="type-title">Combinatorial Problems</h3>
      <p>Dynamic programming is effective for counting or generating all combinations that satisfy certain constraints.</p>
  
      <h2 class="sub-title">Advantages of Dynamic Programming</h2>
      <ul>
        <li>Reduces redundant calculations by storing solutions to subproblems, leading to significant performance improvement.</li>
        <li>Provides a framework to handle optimization problems with overlapping subproblems efficiently.</li>
        <li>Ensures optimal solutions when the problem exhibits optimal substructure and overlapping subproblems.</li>
      </ul>
  
      <h2 class="sub-title">Disadvantages of Dynamic Programming</h2>
      <ul>
        <li>Requires additional memory to store subproblem solutions, which may be inefficient for large problems.</li>
        <li>Can be complex to implement and understand compared to greedy algorithms.</li>
        <li>It may not work efficiently for problems without overlapping subproblems.</li>
      </ul>
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=oBt53YbR9Kk" target="_blank">Dynamic Programming (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=NGt9YIMb9H8" target="_blank">Dynamic Programming in Hindi</a></li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "DynamicProgramming",
    data() {
      return {
        algorithmExample: "",
      };
    },
    methods: {
      showAlgorithm(type) {
        if (type === 'fibonacci') {
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
        } else if (type === 'knapsack') {
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
        } else if (type === 'longestCommonSubsequence') {
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