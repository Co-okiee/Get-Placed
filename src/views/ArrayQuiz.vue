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
  
            <ul class="options-list">
              <li class="wrong-option">
                <label style="color: red;">
                  Your answer:
                  {{ getOptions(explanations[selectedWrongQuestionIndex].questionIndex)[explanations[selectedWrongQuestionIndex].selectedAnswer - 1] || 'No answer selected' }}
                </label>
              </li>
  
              <li class="correct-option">
                <label style="color: green;">
                  Correct answer:
                  {{ getOptions(explanations[selectedWrongQuestionIndex].questionIndex)[explanations[selectedWrongQuestionIndex].correctAnswer - 1] }}
                </label>
              </li>
            </ul>
  
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
        loading: false,
        questions: [],
        currentQuestionIndex: 0,
        selectedOption: null,
        score: 0,
        explanations: [],
        selectedWrongQuestionIndex: null,
      };
    },
    methods: {
      async fetchQuestions() {
        this.loading = true;
        try {
          const response = await axios.get("http://localhost:5000/arrays-quiz-questions");
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
  try {
    const response = await axios.post("http://localhost:5000/save-score", {
      score: this.score,
      date: new Date().toISOString(), // Get the current date in ISO format
    });
    console.log(response.data.message);
  } catch (error) {
    console.error("Error saving score:", error);
    alert("Failed to save score. Please try again.");
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

.arrays-quiz {
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

.start-button:hover {
  background-color: #000000;
}

.options-list {
  list-style-type: none;
  padding: 0;
}

.options-list li {
  margin: 10px 0;
}

.code-snippet {
  background-color: #262424;
  border: 0px solid #ccc;
  padding: 10px;
  border-radius: 4px;
  overflow-x: auto;
}

.details {
  margin-top: 20px;
}

.explanations-list {
  list-style-type: none;
  padding: 0;
}

.wrong-option {
  color: red;
}

.correct-option {
  color: green;
}
</style>
