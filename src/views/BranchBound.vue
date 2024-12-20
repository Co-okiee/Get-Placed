<!-- src/views/BranchAndBound.vue -->
<template>
    <div class="algorithm-container">
      <h1 class="main-title">Branch and Bound</h1>
      <p class="intro">
        Branch and Bound is an algorithm design paradigm used for solving combinatorial and optimization problems. It systematically explores branches of a decision tree to find optimal solutions while avoiding paths that do not lead to a feasible solution.
      </p>
  
      <h2 class="sub-title">Key Concepts in Branch and Bound</h2>
      <ul class="characteristics-list">
        <li><strong>State Space Tree:</strong> A tree structure that represents all possible solutions, where each node represents a partial solution.</li>
        <li><strong>Bounding Function:</strong> A function that provides an upper or lower bound on the optimal solution that can be obtained from the current node.</li>
        <li><strong>Pruning:</strong> The process of eliminating branches that cannot yield better solutions than already known ones, thus reducing the search space.</li>
      </ul>
  
      <h2 class="sub-title">Diagram for Branch and Bound</h2>
      <img src="@/assets/branch-and-bound-diagram.png" alt="Branch and Bound Diagram" class="algorithm-diagram"/>
  
      <h2 class="sub-title">Example Problems</h2>
      <p>Select a category of problems to see examples:</p>
  
      <div class="button-container">
        <button @click="showProblem('knapsack')" class="example-button">Knapsack Problem</button>
        <button @click="showProblem('tsp')" class="example-button">Traveling Salesman Problem</button>
        <button @click="showProblem('assignment')" class="example-button">Assignment Problem</button>
      </div>
  
      <pre v-if="problemExample">
        <code>{{ problemExample }}</code>
      </pre>
  
      <h2 class="sub-title">Types of Problems Solved by Branch and Bound</h2>
      <h3 class="type-title">Knapsack Problem</h3>
      <p>The goal is to maximize the total value in a knapsack without exceeding its weight capacity.</p>
  
      <h3 class="type-title">Traveling Salesman Problem</h3>
      <p>The objective is to find the shortest possible route that visits each city exactly once and returns to the origin city.</p>
  
      <h3 class="type-title">Assignment Problem</h3>
      <p>This involves assigning tasks to resources while minimizing the total cost.</p>
  
      <h2 class="sub-title">Advantages of Branch and Bound</h2>
      <ul>
        <li>Provides exact solutions to optimization problems.</li>
        <li>Efficiently prunes large portions of the search space, reducing computation time.</li>
        <li>Can be applied to various types of combinatorial optimization problems.</li>
      </ul>
  
      <h2 class="sub-title">Disadvantages of Branch and Bound</h2>
      <ul>
        <li>The performance can degrade with larger problem sizes, leading to longer computation times.</li>
        <li>Finding effective bounding functions can be challenging for some problems.</li>
        <li>It may require significant memory resources to store the state space tree.</li>
      </ul>
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=lD4f1ZV9drI" target="_blank">Branch and Bound Introduction (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=9WmFDAB9XHs" target="_blank">Branch and Bound in Hindi</a></li>
      </ul>
    </div>
</template>

<script>
export default {
    name: "BranchAndBound",
    data() {
      return {
        problemExample: "",
      };
    },
    methods: {
      showProblem(type) {
        if (type === 'knapsack') {
          this.problemExample = `// Example of Branch and Bound for Knapsack Problem
  function knapsackBranchBound(capacity, weights, values, n) {
      // Implement the Branch and Bound algorithm for the Knapsack problem
      // Use bounding function to prune branches
      // Return maximum value obtained
  }`;
        } else if (type === 'tsp') {
          this.problemExample = `// Example of Branch and Bound for Traveling Salesman Problem
  function tspBranchBound(graph) {
      // Implement the Branch and Bound algorithm for TSP
      // Use bounding function to determine minimum cost
      // Return shortest path found
  }`;
        } else if (type === 'assignment') {
          this.problemExample = `// Example of Branch and Bound for Assignment Problem
  function assignmentBranchBound(costMatrix) {
      // Implement the Branch and Bound algorithm for Assignment problem
      // Use bounding function to minimize total cost
      // Return optimal assignment
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