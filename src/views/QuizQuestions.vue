<template>
    <div class="quiz-options">
      <h2>Select a Quiz Type</h2>
      <div class="button-container">
        <router-link to="/company-coding" class="option-button">Company Specific Coding Questions</router-link>
        <router-link to="/verbal-ability" class="option-button">Verbal Ability Questions</router-link>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "QuizOptions"
  };
  </script>
  
  <style scoped>
  .quiz-options {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    font-family: 'Roboto', sans-serif;
    color: #fff;
    background-color: #181C14;
  }
  
  .button-container {
    display: flex;
    flex-direction: column;
    gap: 20px; /* Space between buttons */
  }
  
  .option-button {
    background-color: #3C3D37;
    color: white;
    padding: 15px 30px;
    border-radius: 5px;
    text-align: center;
    font-size: 20px;
    font-weight: bold;
    text-decoration: none;
    transition: background-color 0.3s ease;
  }
  
  .option-button:hover {
    background-color: #181C14;
  }
  </style>
  