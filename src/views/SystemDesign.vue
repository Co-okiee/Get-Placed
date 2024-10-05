<template>
    <div class="topic">
      <h1>System Design</h1>
      <p>An introduction to system design concepts and their various components...</p>
  
      <div class="button-container">
        <button @click="navigateTo('BasicsSystem')">Basics of System Design</button>
        <button @click="navigateTo('scalability')">Scalability in System Design</button>
        <button @click="navigateTo('database')">Databases in Designing Systems</button>
        <button @click="navigateTo('HLD')">High Level Design (HLD)</button>
        <button @click="navigateTo('LLD')">Low Level Design (LLD)</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "SystemDesign",
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
  