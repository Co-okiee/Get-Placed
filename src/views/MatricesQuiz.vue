<template>
    <div class="matrices-quiz">
      <h1 v-if="!quizStarted">Matrices Quiz</h1>
      <p v-if="!quizStarted" class="welcome-message">
        Welcome to the matrices quiz!
        <br />
        Test your knowledge on matrices and see how much you really know.
        <br />
        Click the button below to start and challenge yourself!
      </p>
  
      <button v-if="!quizStarted" @click="startQuiz" class="start-button">Start Quiz</button>
  
      <div v-else>
        <div v-if="loading">
          <p>Loading questions...</p>
        </div>
  
        <div v-else-if="questions.length > 0 && currentQuestionIndex < questions.length">
          <h2>Question {{ currentQuestionIndex + 1 }}</h2>
          <p>{{ questions[currentQuestionIndex].question }}</p>
  
          <div v-if="questions[currentQuestionIndex].snippet" class="code-snippet">
            <pre><code>{{ questions[currentQuestionIndex].snippet }}</code></pre>
          </div>
  
          <table class="options-table">
            <tbody>
              <tr v-for="(option, index) in getOptions(currentQuestionIndex)" :key="index">
                <td>
                  <label>
                    <input type="radio" :value="index + 1" v-model="selectedOption" />
                    {{ option }}
                  </label>
                </td>
              </tr>
            </tbody>
          </table>
  
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
  
          <div v-if="explanations.length > 0">
            <h3>Explanations for Wrong Answers:</h3>
            <ul class="explanations-list">
              <li v-for="(explanation, index) in explanations" :key="index">
                <button @click="showWrongAnswerDetails(index)">Question {{ explanation.questionIndex + 1 }}</button>
              </li>
            </ul>
          </div>
  
          <div v-if="selectedWrongQuestionIndex !== null" class="details">
            <h3>Details for Question {{ explanations[selectedWrongQuestionIndex].questionIndex + 1 }}</h3>
            <p>{{ explanations[selectedWrongQuestionIndex].question }}</p>
  
            <div v-if="questions[explanations[selectedWrongQuestionIndex].questionIndex].snippet" class="code-snippet">
              <pre><code>{{ questions[explanations[selectedWrongQuestionIndex].questionIndex].snippet }}</code></pre>
            </div>
  
            <table class="options-table">
              <tbody>
                <tr class="wrong-option">
                  <td>
                    <label style="color: red;">
                      Your answer:
                      {{ getOptions(explanations[selectedWrongQuestionIndex].questionIndex)[explanations[selectedWrongQuestionIndex].selectedAnswer - 1] || 'No answer selected' }}
                    </label>
                  </td>
                </tr>
                <tr class="correct-option">
                  <td>
                    <label style="color: green;">
                      Correct answer:
                      {{ getOptions(explanations[selectedWrongQuestionIndex].questionIndex)[explanations[selectedWrongQuestionIndex].correctAnswer - 1] }}
                    </label>
                  </td>
                </tr>
              </tbody>
            </table>
  
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
    name: "MatricesQuiz",
    data() {
      return {
        quizStarted: false,
        loading: false,
        questions: [],
        currentQuestionIndex: 0,
        selectedOption: null,
        score: 0,
        explanations: [],
        selectedWrongQuestionIndex: null,
        user_id: null,
      };
    },
    mounted() {
      this.user_id = localStorage.getItem("user_id");
      this.score = localStorage.getItem("score");
    },
    methods: {
      async fetchQuestions() {
        this.loading = true;
        try {
          const response = await axios.get("http://localhost:5000/matrices-quiz-questions"); // Change the endpoint to your matrices questions API
          this.questions = response.data;
          this.shuffleArray(this.questions);
          this.currentQuestionIndex = 0;
          this.score = 0;
          this.explanations = [];
        } catch (error) {
          console.error("Error fetching questions:", error);
          alert("Failed to fetch questions from the server. Please try again.");
        } finally {
          this.loading = false;
        }
      },
      startQuiz() {
        this.quizStarted = true;
        this.fetchQuestions();
      },
      quitQuiz() {
        this.currentQuestionIndex = this.questions.length; // Set to end to show completion screen
      },
      getOptions(index) {
        const question = this.questions[index];
        return [question.option1, question.option2, question.option3, question.option4];
      },
      nextQuestion() {
        const currentQuestion = this.questions[this.currentQuestionIndex];
        const correctAnswer = currentQuestion.answer;
  
        if (this.selectedOption === correctAnswer) {
          this.score++;
        } else {
          this.explanations.push({
            questionIndex: this.currentQuestionIndex,
            question: currentQuestion.question,
            selectedAnswer: this.selectedOption,
            correctAnswer: correctAnswer,
            explanation: currentQuestion.explanation,
          });
        }
  
        this.currentQuestionIndex++;
  
        // Check if the quiz is completed
        if (this.currentQuestionIndex >= this.questions.length) {
          this.submitScore(); // Submit score when quiz is finished
        }
  
        this.selectedOption = null;
      },
      async submitScore() {
        console.log("Score:", this.score);
        console.log("User ID:", this.user_id);
        
        // Check if user_id is present
        if (!this.user_id) {
            console.error("Error getting user_id: User ID is not defined.");
            return; // Exit if user_id is not available
        }
  
        // Get the current date in UTC
        const now = new Date();
        
        // Convert to IST by adding 5 hours and 30 minutes (330 minutes)
        const istOffset = 330; // IST is UTC+5:30
        const istDate = new Date(now.getTime() + istOffset * 60 * 1000);
  
        // Log the request data
        console.log("Request data:", {
            score: this.score,
            user_id: this.user_id,
            date: istDate.toISOString(), // Send the adjusted time to the backend
        });
  
        try {
            const response = await axios.post("http://localhost:5000/save-score", {
                score: this.score,
                user_id: this.user_id,
                date: istDate.toISOString(), // Use the IST adjusted date
            });
  
            console.log(response.data.message);
            alert("Score saved successfully!");
        } catch (error) {
            if (error.response) {
                console.error("Error saving score:", error.response.data);
                alert(`Failed to save score: ${error.response.data.error || error.message}`);
            } else {
                console.error("Error saving score:", error.message);
                alert("Failed to save score. Please try again.");
            }
        }
      },
      showWrongAnswerDetails(index) {
        this.selectedWrongQuestionIndex = index; 
      },
      shuffleArray(array) {
        for (let i = array.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          [array[i], array[j]] = [array[j], array[i]];
        }
      },
    },
  };
  </script>
  
  <style scoped>
  body {
    display: flex;
    justify-content: center; /* Center horizontally */
    align-items: center; /* Center vertically */
    height: 100vh; /* Full height of the viewport */
    margin: 0; /* Remove default margin */
    background-color: #f0f0f0; /* Optional: set a background color */
  }
  
  .matrices-quiz {
    max-width: 600px;
    width: 100%; /* Allow it to shrink in smaller screens */
    padding: 80px;
    border: 0px solid #ccc;
    border-radius: 8px;
    background-color: #000000;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  
  .welcome-message {
    font-size: 1.2em;
    margin: 20px 0;
  }
  
  .start-button, .quit-button {
    background-color: #13c81c;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .start-button:hover, .quit-button:hover {
    background-color: #e74c3c;
  }
  
  .options-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
  }
  
  .options-table td {
    padding: 10px;
    border: 1px solid #ccc;
  }
  
  .details {
    border: 1px solid #ccc;
    padding: 10px;
    margin-top: 20px;
  }
  
  .correct-option {
    color: green;
  }
  
  .wrong-option {
    color: red;
  }
  
  .button-container {
    margin-top: 20px;
  }
  
  .code-snippet {
    background-color: #1e1e1e;
    color: white;
    padding: 10px;
    border-radius: 4px;
    margin: 10px 0;
  }
  </style>
  