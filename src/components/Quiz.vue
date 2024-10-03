<template>
    <div class="quiz">
      <h2>Quiz</h2>
      <div v-if="questions.length > 0">
        <div v-if="!quizFinished">
          <h3>{{ currentQuestionIndex + 1 }}. {{ currentQuestion.question }}</h3>
          <div v-for="(choice, index) in currentQuestion.choices" :key="index">
            <button @click="selectAnswer(choice)">{{ choice }}</button>
          </div>
        </div>
  
        <div v-else>
          <h3>Quiz Finished!</h3>
          <p>Your score: {{ score }}/{{ questions.length }}</p>
          <button @click="restartQuiz">Restart Quiz</button>
        </div>
      </div>
      <p v-else>Loading questions...</p>
    </div>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue';
  import { useCounterStore } from '../stores/counter';
  
  const store = useCounterStore();
  const questions = store.quizData; // Assuming your store has a property for quiz questions
  const currentQuestionIndex = ref(0);
  const score = ref(0);
  const quizFinished = ref(false);
  
  // Prepare the choices array with correct and incorrect answers
  const currentQuestion = computed(() => {
    const question = questions[currentQuestionIndex.value];
    if (question) {
      const choices = [question.correct_answer, ...question.incorrect_answers];
      return {
        question: question.question,
        choices: shuffleArray(choices) // Shuffle the choices for randomness
      };
    }
    return {};
  });
  
  function selectAnswer(choice) {
    if (choice === currentQuestion.value.correct_answer) {
      score.value++;
    }
    if (currentQuestionIndex.value < questions.length - 1) {
      currentQuestionIndex.value++;
    } else {
      quizFinished.value = true;
    }
  }
  
  function restartQuiz() {
    score.value = 0;
    currentQuestionIndex.value = 0;
    quizFinished.value = false;
  }
  
  // Helper function to shuffle the array of choices
  function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]]; // Swap elements
    }
    return array;
  }
  
  </script>
  
  <style scoped>
  .quiz {
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 8px;
  }
  </style>
  