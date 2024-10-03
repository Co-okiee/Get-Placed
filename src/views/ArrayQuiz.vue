<template>
    <div class="arrays-quiz">
      <h1 v-if="!quizStarted">Arrays Quiz</h1>
      <p v-if="!quizStarted" class="welcome-message">
        Welcome to the arrays quiz! 
        <br />
        Test your knowledge on arrays and see how much you really know. 
        <br />
        Click the button below to start and challenge yourself!
      </p>
  
      <button v-if="!quizStarted" @click="startQuiz" class="start-button">Start Quiz</button>
  
      <div v-else>
        <div v-if="loading">
          <p>Loading questions...</p>
        </div>
        
        <div v-else-if="questions.length > 0 && currentQuestionIndex < questions.length">
          <h2>Question {{ currentQuestionIndex + 1 }}: {{ questions[currentQuestionIndex].question }}</h2>
  
          <!-- Check if the snippet exists and display it -->
          <div v-if="questions[currentQuestionIndex].snippet" class="code-snippet">
            <pre><code>{{ questions[currentQuestionIndex].snippet }}</code></pre>
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
            <button @click="nextQuestion" :disabled="selectedOption === null">
              {{ currentQuestionIndex === questions.length - 1 ? 'Submit' : 'Next' }}
            </button>
          </div>
        </div>
  
        <div v-else-if="currentQuestionIndex >= questions.length">
          <h2>Quiz Completed!</h2>
          <p class="score">Your score: {{ score }} out of {{ questions.length }}</p>
  
          <div v-if="explanations.length > 0">
            <h3>Explanations for Wrong Answers:</h3>
            <ul class="explanations-list">
              <li v-for="(explanation, index) in explanations" :key="index">
                <button @click="showWrongAnswerDetails(index)">Question {{ index + 1 }}</button>
              </li>
            </ul>
          </div>
  
          <div v-if="selectedWrongQuestionIndex !== null" class="details">
            <h3>Details for Question {{ selectedWrongQuestionIndex + 1 }}</h3>
            <p>{{ explanations[selectedWrongQuestionIndex].question }}</p>
            
            <!-- Check if the snippet exists for wrong answers -->
            <div v-if="questions[selectedWrongQuestionIndex].snippet" class="code-snippet">
              <pre><code>{{ questions[selectedWrongQuestionIndex].snippet }}</code></pre>
            </div>
  
            <ul class="options-list">
              <!-- Display the selected answer -->
              <li class="wrong-option">
                <label style="color: red;">
                  Your answer: 
                  <!-- Ensure the correct index is used to fetch the selected option text -->
                  {{ getOptions(selectedWrongQuestionIndex)[explanations[selectedWrongQuestionIndex].selectedAnswer - 1] || 'No answer selected' }}
                </label>
              </li>
  
              <!-- Display the correct answer -->
              <li class="correct-option">
                <label style="color: green;">
                  Correct answer: 
                  <!-- Ensure the correct index is used to fetch the correct option text -->
                  {{ getOptions(selectedWrongQuestionIndex)[explanations[selectedWrongQuestionIndex].correctAnswer - 1] }}
                </label>
              </li>
            </ul>
  
            <!-- Explanation for the answer -->
            <p>{{ explanations[selectedWrongQuestionIndex].explanation }}</p>
            <button @click="selectedWrongQuestionIndex = null">Close</button>
          </div>
        </div>
      </div>
    </div>
  </template>
<script>
import axios from "axios";

export default {
  name: "ArraysQuiz",
  data() {
    return {
      quizStarted: false,
      loading: false, // Added loading state
      questions: [],
      currentQuestionIndex: 0,
      selectedOption: null,
      score: 0,
      explanations: [],
      wrongAnswers: [], // Store the wrong answers
      selectedWrongQuestionIndex: null, // Track which wrong question is selected
    };
  },
  methods: {
    async fetchQuestions() {
      this.loading = true; // Set loading to true before fetching questions
      try {
        const response = await axios.get("http://localhost:5000/arrays-quiz-questions");
        this.questions = response.data;
        this.shuffleArray(this.questions);
        this.currentQuestionIndex = 0;
        this.score = 0;
        this.explanations = [];
        this.wrongAnswers = []; // Reset wrong answers
      } catch (error) {
        console.error("Error fetching questions:", error);
        alert("Failed to fetch questions from the server. Please try again.");
      } finally {
        this.loading = false; // Set loading to false after fetching questions
      }
    },
    startQuiz() {
      this.quizStarted = true;
      this.fetchQuestions();
    },
    getOptions(index) {
      const question = this.questions[index];
      return [question.option1, question.option2, question.option3, question.option4];
    },
    nextQuestion() {
      const currentQuestion = this.questions[this.currentQuestionIndex];
      const correctAnswer = currentQuestion.answer;

      // Check if the selected option is correct
      if (this.selectedOption === correctAnswer) {
        this.score++;
      } else {
        // Store the selected wrong answer and explanation
        this.explanations.push({
          question: currentQuestion.question,
          selectedAnswer: this.selectedOption, // Index of user's selected answer
          correctAnswer: correctAnswer, // Correct answer for the current question
          explanation: currentQuestion.explanation
        });
      }

      // Move to the next question
      this.currentQuestionIndex++;
      this.selectedOption = null; // Reset selected option for the next question
    },
    showWrongAnswerDetails(index) {
      this.selectedWrongQuestionIndex = index; // Set the selected question index
    },
    shuffleArray(array) {
      for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]]; // Swap elements
      }
    },
  },
};
</script>
<style scoped>
.arrays-quiz {
  padding: 40px;
  background-color: #000000;
  color: #ffffff;
  border-radius: 8px;
  max-width: 600px;
  margin: 100px auto;
  text-align: center;
}

.welcome-message {
  margin: 20px 0;
  font-size: 18px;
}

.start-button {
  padding: 15px 30px;
  font-size: 16px;
}

.options-list,
.explanations-list {
  text-align: left;
  margin: 0 auto;
  max-width: 600px;
}

.button-container {
  text-align: center;
}

button {
  background-color: #4caf50;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 10px;
}

.score {
  font-size: 24px;
  color: #4caf50;
}

.wrong-option {
  color: red;
}

.correct-option {
  color: green;
}

/* Styling for the code snippet to look like VS Code */
.code-snippet {
  background-color: #1e1e1e;
  color: #dcdcdc;
  padding: 10px;
  margin-top: 10px;
  border-radius: 6px;
  font-family: "Courier New", Courier, monospace;
  text-align: left;
  overflow-x: auto;
}

.code-snippet pre {
  margin: 0;
  white-space: pre-wrap;
}

.details {
  text-align: left;
}
</style>
  