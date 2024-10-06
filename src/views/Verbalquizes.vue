<template>
    <div class="verbal-quizzes">
      <h1>Verbal Ability Quizzes</h1>
      <div class="quiz-buttons">
        <router-link :to="{ name: 'VerbalAbilityQuizPage', params: { quizNumber: 1 } }">
          <button>Verbal Ability Quiz 1</button>
        </router-link>
        <router-link :to="{ name: 'VerbalAbilityQuizPage', params: { quizNumber: 2 } }">
          <button>Verbal Ability Quiz 2</button>
        </router-link>
        <router-link :to="{ name: 'VerbalAbilityQuizPage', params: { quizNumber: 3 } }">
          <button>Verbal Ability Quiz 3</button>
        </router-link>
        <router-link :to="{ name: 'VerbalAbilityQuizPage', params: { quizNumber: 4 } }">
          <button>Verbal Ability Quiz 4</button>
        </router-link>
        <router-link :to="{ name: 'VerbalAbilityQuizPage', params: { quizNumber: 5 } }">
          <button>Verbal Ability Quiz 5</button>
        </router-link>
        <router-link :to="{ name: 'VerbalAbilityQuizPage', params: { quizNumber: 6 } }">
          <button>Verbal Ability Quiz 6</button>
        </router-link>
        <router-link :to="{ name: 'VerbalAbilityQuizPage', params: { quizNumber: 7 } }">
          <button>Verbal Ability Quiz 7</button>
        </router-link>
        <router-link :to="{ name: 'VerbalAbilityQuizPage', params: { quizNumber: 8 } }">
          <button>Verbal Ability Quiz 8</button>
        </router-link>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "VerbalAbilityQuizzes",
  };
  </script>
  
  <style scoped>
  .verbal-quizzes {
    max-width: 600px;
    width: 100%; /* Allow it to shrink in smaller screens */
    padding: 80px;
    border-radius: 8px;
    background-color: #000000;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  
  .quiz-buttons {
    display: flex;
    flex-direction: column;
  }
  
  .quiz-buttons button {
    margin: 10px 0;
    background-color: #29bfdd;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1em;
  }
  
  .quiz-buttons button:hover {
    background-color: #000000;
  }
  </style>
  