<!-- src/views/Study.vue -->
<template>
    <div class="study-material">
      <h1>Placement Preparation Topics</h1>
      <div class="topics">
        <button @click="goToTopic('data-structures')">Data Structures</button>
        <button @click="goToTopic('algorithms')">Algorithms</button>
        <button @click="goToTopic('os')">Operating Systems</button>
        <button @click="goToTopic('dbms')">DBMS</button>
        <button @click="goToTopic('oops')">Object-Oriented Programming</button>
        <button @click="goToTopic('Apt')">Aptitude & Reasoning</button>
        <button @click="goToTopic('CN')">Computer Networks</button>
        <button @click="goToTopic('SystemDesign')">System Design</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "Study",
    methods: {
      goToTopic(topic) {
        // Logic to navigate to the respective topic page
        this.$router.push({ name: topic });
      },
    },
  };
  </script>
  
  <style scoped>
  .study-material {
    text-align: center;
    padding: 20px;
  }
  .topics {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
  }
  button {
    padding: 10px 20px;
    background-color: #2c3e50;
    color: white;
    border: none;
    cursor: pointer;
    font-size: 16px;
    border-radius: 5px;
  }
  button:hover {
    background-color: #34495e;
  }
  </style>
  