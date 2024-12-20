<template>
    <div class="quiz">
      <h1>Quiz</h1>
      <p v-if="currentQuestionIndex < questions.length">
        <strong>Question {{ currentQuestionIndex + 1 }}:</strong>
        {{ questions[currentQuestionIndex].question }}
      </p>
      <ul v-if="currentQuestionIndex < questions.length">
        <li
          v-for="(option, index) in questions[currentQuestionIndex].options"
          :key="index"
        >
          <button @click="handleAnswer(option)">{{ option }}</button>
        </li>
      </ul>
      <div v-else>
        <h2>Your Score: {{ score }}/{{ questions.length }}</h2>
        <button @click="finishQuiz">Finish Quiz</button>
      </div>
    </div>
  </template>
  
  <script>
  import { useUserStore } from "@/store";
  
  export default {
    name: "Quiz",
    data() {
      return {
        currentQuestionIndex: 0,
        score: 0,
        questions: [
          {
            question: "What is 2 + 2?",
            options: ["3", "4", "5", "6"],
            answer: "4",
          },
          {
            question: "What is the capital of France?",
            options: ["Berlin", "Madrid", "Paris", "Rome"],
            answer: "Paris",
          },
        ],
      };
    },
    methods: {
      handleAnswer(selectedOption) {
        if (
          selectedOption ===
          this.questions[this.currentQuestionIndex].answer
        ) {
          this.score++;
        }
        this.currentQuestionIndex++;
      },
      finishQuiz() {
        const store = useUserStore();
        store.addScore(this.score);
        this.$router.push({ name: "track-progress" });
      },
    },
  };
  </script>
  