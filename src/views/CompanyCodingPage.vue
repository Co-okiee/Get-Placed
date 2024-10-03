<template>
  <div class="verbal-reasoning">
    <h1 v-if="!quizStarted">Verbal Reasoning Questions</h1>
    <p v-if="!quizStarted">Welcome to the verbal reasoning section! Click the button below to start the quiz.</p>

    <!-- Start Quiz Button -->
    <button v-if="!quizStarted" @click="startQuiz">Start Quiz</button>

    <!-- Quiz Section -->
    <div v-else>
      <div v-if="questions.length > 0 && currentQuestionIndex < questions.length">
        
        <!-- Display Passage if not null -->
        <div v-if="questions[currentQuestionIndex].passage">
          <h2>Passage</h2>
          <p>{{ questions[currentQuestionIndex].passage }}</p>
        </div>

        <!-- Display question number and question -->
        <h2>Question {{ currentQuestionIndex + 1 }}: {{ questions[currentQuestionIndex].question }}</h2>

        <!-- Display options -->
        <ul class="options-list">
          <li v-for="(option, index) in getOptions(currentQuestionIndex)" :key="index">
            <label>
              <input type="radio" :value="index + 1" v-model="selectedOption" />
              {{ option }}
            </label>
          </li>
        </ul>

        <button @click="nextQuestion">Next</button>
      </div>

      <!-- Quiz Completed Section -->
      <div v-else-if="questions.length > 0 && currentQuestionIndex >= questions.length">
        <h2>Quiz Completed!</h2>
        <p>Your score: {{ score }} out of {{ questions.length }}</p>

        <!-- Show explanations for wrong answers -->
        <div v-if="explanations.length > 0">
          <h3>Explanations for Wrong Answers:</h3>
          <ul class="explanations-list">
            <li v-for="(explanation, index) in explanations" :key="index">
              {{ index + 1 }}. {{ explanation }}
            </li>
          </ul>
        </div>
      </div>

      <!-- Loading Message -->
      <div v-else>
        <p>Loading questions...</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "verbal-reasoning",
  data() {
    return {
      quizStarted: false, // Tracks if the quiz has started
      questions: [], // Stores quiz questions
      currentQuestionIndex: 0, // Tracks the current question index
      selectedOption: null, // Stores the selected option for the current question
      score: 0, // Tracks the user's score
      explanations: [], // To store explanations for wrong answers
    };
  },
  methods: {
    // Function to shuffle questions randomly
    shuffleArray(array) {
      for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
      }
    },
    // Function to fetch quiz questions from the server
    async fetchQuestions() {
      try {
        const response = await axios.get("http://localhost:5000/questions");
        console.log("Questions fetched:", response.data); // Log the fetched questions
        this.questions = response.data;

        // Shuffle the questions for randomness
        this.shuffleArray(this.questions);

        // Ensure quiz starts from the first question
        this.currentQuestionIndex = 0;
        this.score = 0; // Reset score when starting the quiz
        this.explanations = []; // Reset explanations when starting the quiz
      } catch (error) {
        console.error("Error fetching questions:", error.response ? error.response.data : error.message);
        alert("Failed to fetch questions from the server. Please try again.");
      }
    },
    // Function to start the quiz
    startQuiz() {
      this.quizStarted = true;
      this.fetchQuestions(); // Fetch questions when quiz starts
    },
    // Function to get options for the current question
    getOptions(index) {
      const question = this.questions[index];
      return [question.option1, question.option2, question.option3, question.option4];
    },
    // Function to move to the next question
    nextQuestion() {
      // Check if an option is selected before proceeding
      if (this.selectedOption === null) {
        alert("Please select an option!"); // Alert the user to select an option
        return; // Don't proceed until an option is selected
      }

      // Check if the selected option is correct
      if (this.selectedOption === this.questions[this.currentQuestionIndex].answer) {
        this.score++; // Increment score if the selected option is correct
      } else {
        // Store the explanation for the wrong answer
        this.explanations.push(this.questions[this.currentQuestionIndex].explanation);
      }

      // Move to the next question
      this.currentQuestionIndex++;
      this.selectedOption = null; // Reset selected option for the next question
    },
  },
};
</script>

<style scoped>
.verbal-reasoning {
  padding: 20px;
  background-color: #000000;
  color: #ffffff;
  border-radius: 8px;
  max-width: 600px;
  margin: 100px auto; /* Center the container vertically and horizontally */
  text-align: center; /* Center the headings */
}

.options-list, .explanations-list {
  text-align: left; /* Align questions and answers to the left */
  margin: 0 auto;
  max-width: 600px;
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
</style>
