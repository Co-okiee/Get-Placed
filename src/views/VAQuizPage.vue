<template>
    <div class="verbal-quiz">
      <h1>Verbal Ability Quiz</h1>
      <p v-if="loading">Loading questions...</p>
  
      <div v-else-if="questions.length > 0 && currentQuestionIndex < questions.length">
        <h2>Question {{ currentQuestionIndex + 1 }}: {{ questions[currentQuestionIndex].question }}</h2>
  
        <!-- Display passage if available -->
        <div v-if="questions[currentQuestionIndex].passage" class="passage">
          <p>{{ questions[currentQuestionIndex].passage }}</p>
        </div>
  
        <ul class="options-list">
          <li v-for="(option, index) in getOptions(currentQuestionIndex)" :key="index">
            <label>
              <input type="radio" :value="index + 1" v-model="selectedOption" />
              {{ option }}
            </label>
          </li>
        </ul>
  
        <div class="button-container">
          <button @click="quitQuiz" class="quit-button">Quit</button>
          <button @click="nextQuestion" :disabled="selectedOption === null" style="margin-left: 10px;">
            {{ currentQuestionIndex === questions.length - 1 ? 'Submit' : 'Next' }}
          </button>
        </div>
      </div>
  
      <div v-else-if="currentQuestionIndex >= questions.length">
        <h2>Quiz Completed!</h2>
        <p class="score">Your score: {{ score }} out of {{ questions.length }}</p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    name: "VerbalAbilityQuizPage",
    data() {
      return {
        loading: false,
        questions: [],
        currentQuestionIndex: 0,
        selectedOption: null,
        score: 0,
      };
    },
    created() {
      this.fetchQuestions(this.$route.params.quizNumber);
    },
    methods: {
      async fetchQuestions(quizNumber) {
        this.loading = true;
        try {
          const response = await axios.get(`http://localhost:5000/verbal-ability-quiz-questions?quiz=${quizNumber}`);
          this.questions = response.data; // Assuming the response contains the questions for the specified quiz
          this.currentQuestionIndex = 0;
          this.score = 0;
        } catch (error) {
          console.error("Error fetching questions:", error);
          alert("Failed to fetch questions from the server. Please try again.");
        } finally {
          this.loading = false;
        }
      },
      quitQuiz() {
        this.currentQuestionIndex = this.questions.length; // Set to end to show completion screen
      },
      getOptions(index) {
        const question = this.questions[index];
        return [question.option1, question.option2, question.option3, question.option4];
      },
      async nextQuestion() {
        const currentQuestion = this.questions[this.currentQuestionIndex];
        const correctAnswer = currentQuestion.answer;
  
        // Check if the selected option is correct
        if (this.selectedOption === correctAnswer) {
          this.score++;
        }
  
        // Move to the next question or submit the quiz
        if (this.currentQuestionIndex === this.questions.length - 1) {
          // If this is the last question, show completion screen
          this.currentQuestionIndex++;
          await this.saveScore(); // Save the score when quiz is completed
        } else {
          this.currentQuestionIndex++;
          this.selectedOption = null;
        }
      },
      async saveScore() {
        try {
          const userId = this.$store.state.userId; // Assuming you're using Vuex for state management
          const response = await axios.post('http://localhost:5000/save_verbal_score', {
            user_id: userId,
            score: this.score,
            topic: `Verbal Ability Quiz ${this.$route.params.quizNumber}`,
          });
          console.log(response.data.message); // Confirm score saved
        } catch (error) {
          console.error("Error saving score:", error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .verbal-quiz {
    max-width: 600px;
    width: 100%; /* Allow it to shrink in smaller screens */
    padding: 80px;
    border: 0px solid #ccc;
    border-radius: 8px;
    background-color: #000000;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    margin: 0 auto; /* Center the component */
  }
  
  .passage {
    margin: 20px 0; /* Add some margin for better spacing */
    background-color: #262424; /* Optional: background color for passages */
    padding: 10px; /* Optional: padding for passages */
    border-radius: 4px; /* Optional: rounded corners for passages */
    color: white; /* Optional: white text for readability */
  }
  
  .options-list {
    list-style-type: none;
    padding: 0;
  }
  
  .options-list li {
    margin: 10px 0;
  }
  
  .button-container {
    margin-top: 20px; /* Add space above the button container */
  }
  
  .quit-button,
  .next-button {
    background-color: #2fb7d6;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1em;
  }
  
  .quit-button {
    background-color: red;
  }
  
  .quit-button:hover {
    background-color: darkred;
  }
  
  .score {
    font-size: 1.5em; /* Increase score font size */
  }
  </style>
  