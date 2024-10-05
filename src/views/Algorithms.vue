<template>
    <div class="topic">
      <h1>Algorithms</h1>
      <p>An introduction to algorithms and their various types...</p>
  
      <div class="button-container">
        <button @click="navigateTo('analysisofalgo')">Analysis of Algorithms</button>
        <button @click="navigateTo('searching')">Searching Algorithms</button>
        <button @click="navigateTo('sorting')">Sorting Algorithms</button>
        <button @click="navigateTo('greedy')">Greedy Algorithms</button>
        <button @click="navigateTo('dynamic')">Dynamic Programming</button>
        <button @click="navigateTo('graphalgo')">Graph Algorithms</button>
        <button @click="navigateTo('pattern')">Pattern Searching</button>
        <button @click="navigateTo('recursion')">Recursion</button>
        <button @click="navigateTo('backtracking')">Backtracking</button>
        <button @click="navigateTo('divide-and-conquer')">Divide and Conquer</button>
        <button @click="navigateTo('mathematical-algo')">Mathematical Algorithms</button>
        <button @click="navigateTo('geometric')">Geometric Algorithms</button>
        <button @click="navigateTo('bitwise')">Bitwise Algorithms</button>
        <button @click="navigateTo('randomised')">Randomised Algorithms</button>
        <button @click="navigateTo('branchbound')">Branch and Bound</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "Algorithms",
    methods: {
      navigateTo(topic) {
        // Navigate to the specified topic using the router
        this.$router.push({ name: topic });
      }
    }
  };
  </script>
  
  <style scoped>
  .topic {
    text-align: center;
    padding: 20px;
  }
  .button-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 10px;
    margin-top: 20px;
  }
  button {
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    border: none;
    background-color: #555b61; /* Primary button color */
    color: white; /* Text color */
    border-radius: 5px; /* Rounded corners */
    transition: background-color 0.3s; /* Smooth transition for hover effect */
  }
  button:hover {
    background-color: #0056b3; /* Darker color on hover */
  }
  </style>
  