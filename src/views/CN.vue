<template>
    <div class="topic">
      <h1>Computer Networks</h1>
      <p>An introduction to computer networks and their various components...</p>
  
      <div class="button-container">
        <button @click="navigateTo('CNbasics')">CN Basics</button>
        <button @click="navigateTo('datalink')">Data Link Layer</button>
        <button @click="navigateTo('network')">Network Layer</button>
        <button @click="navigateTo('transport')">Transport Layer</button>
        <button @click="navigateTo('application')">Application Layer</button>
        <button @click="navigateTo('networksecurity')">Network Security and Cryptography</button>
        <button @click="navigateTo('compressiontech')">Compression Techniques</button>
        <button @click="navigateTo('networkexp')">Network Experiments</button>
        <button @click="navigateTo('devices')">Devices</button>
        <button @click="navigateTo('misc')">Misc</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "ComputerNetworks",
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
  