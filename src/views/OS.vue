<!-- src/views/OperatingSystems.vue -->
<template>
    <div class="topic">
      <h1>Operating Systems</h1>
      <p>An introduction to operating systems and their various components...</p>
  
      <div class="button-container">
        <button @click="navigateTo('basics')">Basics</button>
        <button @click="navigateTo('system')">System Structure</button>
        <button @click="navigateTo('CPU')">CPU Scheduling</button>
        <button @click="navigateTo('processsyn')">Process Synchronization</button>
        <button @click="navigateTo('deadlock')">Deadlock</button>
        <button @click="navigateTo('pt')">Processes & Threads</button>
        <button @click="navigateTo('memory')">Memory Management</button>
        <button @click="navigateTo('disk')">Disk Management</button>
        <button @click="navigateTo('misc')">Misc</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "OperatingSystems",
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
  