<template>
    <div class="topic">
      <h1>OOPS in C++</h1>
      <p>An introduction to Object-Oriented Programming (OOP) concepts in C++...</p>
  
      <div class="button-container">
        <button @click="navigateTo('OOPSbasic')">OOPs Basics</button>
        <button @click="navigateTo('encapsulation')">Encapsulation</button>
        <button @click="navigateTo('abstraction')">Abstraction</button>
        <button @click="navigateTo('polymorphism')">Polymorphism</button>
        <button @click="navigateTo('inheritance')">Inheritance</button>
        <button @click="navigateTo('dynamicbinding')">Dynamic Binding and Message Passing</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "OOPSCpp",
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
  