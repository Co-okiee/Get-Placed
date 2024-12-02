<template>
  <div class="arrays-quiz">
    
    <!-- Quiz Start Screen -->
    <div v-if="!quizStarted" class="quiz-intro">
      <div class="intro-content">
        <h1 class="intro-title">Data Structure Quiz</h1>
        <p class="intro-message">
          Welcome to the Data Structure quiz!<br />
          Test your knowledge on data structures and see how much you really know.
        </p>
        <button @click="startQuiz" class="intro-button">
          <span>Start Quiz</span>
          <svg xmlns="http://www.w3.org/2000/svg" class="icon" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none">
            <path d="M9 6l6 6l-6 6"/>
          </svg>
        </button>
      </div>
    </div>

    <div v-else>
      <!-- Loading State -->
      <div v-if="loading" class="loading-state">
          <div class="loading-spinner"></div>
          <p>Loading questions...</p>
        </div>

       <!-- Quiz Questions -->
      <div v-else-if="questions.length > 0 && currentQuestionIndex < questions.length" class="quiz-container">
          <!-- Progress Bar -->
          <div class="progress-bar">
            <div class="progress-text">
              <span>Question {{ currentQuestionIndex + 1 }} of {{ questions.length }}</span>
              <span>{{ Math.round(((currentQuestionIndex + 1) / questions.length) * 100) }}% Complete</span>
            </div>
            <div class="progress-track">
              <div 
                class="progress-fill"
                :style="{ width: `${((currentQuestionIndex + 1) / questions.length) * 100}%` }"
              ></div>
            </div>
          </div>

      <!-- Question Content -->
      <div class="question-content">
            <h2 class="question-text">
              {{ questions[currentQuestionIndex].question }}
            </h2>
  
            <!-- Code Snippet -->
            <div v-if="questions[currentQuestionIndex].snippet" class="code-snippet">
              <pre><code>{{ questions[currentQuestionIndex].snippet }}</code></pre>
            </div>
  
            <!-- Options -->
            <div class="options-grid">
              <button
                v-for="(option, index) in getOptions(currentQuestionIndex)"
                :key="index"
                @click="selectedOption = index + 1"
                :class="[
                  'option-button',
                  { 'selected': selectedOption === index + 1 }
                ]"
              >
                <div class="option-content">
                  <span class="option-marker">{{ String.fromCharCode(65 + index) }}</span>
                  <span class="option-text">{{ option }}</span>
                </div>
              </button>
            </div>

      <!-- Navigation Buttons -->
      <div class="navigation-buttons">
              <button @click="quitQuiz" class="quit-button">
                <svg xmlns="http://www.w3.org/2000/svg" class="button-icon" width="20" height="20" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none">
                  <path d="M9 6l6 6l-6 6"/>
                </svg>
                <span>Quit Quiz</span>
              </button>
              
              <button 
                @click="nextQuestion" 
                :disabled="selectedOption === null"
                class="next-button"
              >
                <span>{{ currentQuestionIndex === questions.length - 1 ? 'Submit' : 'Next' }}</span>
                <svg xmlns="http://www.w3.org/2000/svg" class="button-icon" width="20" height="20" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none">
                  <path d="M9 6l6 6l-6 6"/>
                </svg>
              </button>
            </div>
            </div>
      </div>

      <div v-else-if="currentQuestionIndex >= questions.length" class="result-container">
        <div class="result-header">
          <h2 class="completion-title">Quiz Completed! 🎉</h2>
          <div class="score-display">
            <div class="score-circle">
              <span class="score-number">{{ score }}</span>
              <span class="score-total">/ {{ questions.length }}</span>
            </div>
            <p class="score-message">
              {{ score === questions.length ? "Perfect Score! You're Amazing! 🌟" :
                 score >= questions.length * 0.8 ? "Excellent Work! Keep it up! 🎯" :
                 score >= questions.length * 0.6 ? "Good effort! Room to grow! 💪" :
                 "Keep practicing! You've got this! 📚" }}
            </p>
          </div>
        </div>

        <div v-if="explanations.length > 0" class="explanations-section">
          <h3 class="review-title">Review Your Answers</h3>
          <div class="wrong-answers-container">
            <button
              v-for="(explanation, index) in explanations"
              :key="index"
              class="review-button"
              @click="showWrongAnswerDetails(index)"
            >
              Question {{ explanation.questionIndex + 1 }}
            </button>
          </div>
        </div>

        <div v-if="selectedWrongQuestionIndex !== null" class="explanation-card">
          <div class="explanation-header">
            <h3>Question {{ explanations[selectedWrongQuestionIndex].questionIndex + 1 }}</h3>
            <button @click="selectedWrongQuestionIndex = null" class="close-button">
              <span>×</span>
            </button>
          </div>
          
          <div class="explanation-content">
            <p class="question-text">{{ explanations[selectedWrongQuestionIndex].question }}</p>

            <div v-if="questions[explanations[selectedWrongQuestionIndex].questionIndex].snippet" class="code-snippet">
              <pre><code>{{ questions[explanations[selectedWrongQuestionIndex].questionIndex].snippet }}</code></pre>
            </div>

            <div class="answer-comparison">
              <div class="wrong-answer">
                <span class="answer-label">Your Answer</span>
                <p>{{ getOptions(explanations[selectedWrongQuestionIndex].questionIndex)[explanations[selectedWrongQuestionIndex].selectedAnswer - 1] || 'No answer selected' }}</p>
              </div>
              
              <div class="correct-answer">
                <span class="answer-label">Correct Answer</span>
                <p>{{ getOptions(explanations[selectedWrongQuestionIndex].questionIndex)[explanations[selectedWrongQuestionIndex].correctAnswer - 1] }}</p>
              </div>
            </div>

            <div class="explanation-text">
              <h4>Explanation</h4>
              <p>{{ explanations[selectedWrongQuestionIndex].explanation }}</p>
            </div>
          </div>
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

      if (this.currentQuestionIndex >= this.questions.length) {
        this.submitScore(); // Submit score when quiz is finished
      }

      this.selectedOption = null; 
    },
    async submitScore() {
      console.log("Score:", this.score);
      console.log("User ID:", this.user_id);

      if (!this.user_id) {
        console.error("Error getting user_id: User ID is not defined.");
        return; // Exit if user_id is not available
      }

      const now = new Date();
      const istOffset = 330; // IST is UTC+5:30
      const istDate = new Date(now.getTime() + istOffset * 60 * 1000);

      console.log("Request data:", {
        score: this.score,
        user_id: this.user_id,
        date: istDate.toISOString(),
      });

      try {
        const response = await axios.post("http://localhost:5000/save-score", {
          score: this.score,
          user_id: this.user_id,
          date: istDate.toISOString(),
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
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap');

html, body {
  height: 100%; /* Ensures the body takes full height */
  margin: 0; /* Removes default margins */
  background-color: #000000; /* Background color for contrast */
  color: white; /* Default text color */
  font-family: 'Arial', sans-serif; /* Global font style */
}

.arrays-quiz {
    min-height: 100vh;
    background: linear-gradient(135deg, #020202 0%, #22262d 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 2rem;
    font-family: 'Poppins', sans-serif;
  }

/* Quiz Intro Styles */
.quiz-intro {
    text-align: center;
    max-width: 600px;
    padding: 3rem;
    background: rgba(0, 0, 0, 0.05);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.1);
  }

  .intro-title {
    font-size: 2.5rem;
    color: #ffffff;
    margin-bottom: 1.5rem;
    font-weight: 700;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .intro-message {
    color: #a0aec0;
    font-size: 1.1rem;
    line-height: 1.6;
    margin-bottom: 2rem;
  }
  
  .intro-button {
    background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
    color: white;
    border: none;
    padding: 1rem 2rem;
    border-radius: 12px;
    font-size: 1.1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
  }
  
  .intro-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
  }
  
/* Quiz Container Styles */
.quiz-container {
    width: 100%;
    max-width: 800px;
    background: rgba(0, 0, 0, 0.05);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 2rem;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.1);
  }
  
  /* Progress Bar Styles */
  .progress-bar {
    margin-bottom: 2rem;
  }
  
  .progress-text {
    display: flex;
    justify-content: space-between;
    color: #a0aec0;
    font-size: 0.9rem;
    margin-bottom: 0.5rem;
  }
  
  .progress-track {
    width: 100%;
    height: 6px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 3px;
    overflow: hidden;
  }
  
  .progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #3b82f6 0%, #2563eb 100%);
    transition: width 0.3s ease;
  }
  
  /* Question Content Styles */
  .question-content {
    padding: 1rem;
  }
  
  .question-text {
    font-size: 1.3rem;
    color: #ffffff;
    margin-bottom: 2rem;
    line-height: 1.5;
  }
  
  /* Code Snippet Styles */
  .code-snippet {
    background: #353636;
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 2rem;
    overflow-x: auto;
  }
  
  .code-snippet code {
    color: #e2e8f0;
    font-family: 'Fira Code', monospace;
    font-size: 0.9rem;
    line-height: 1.5;
  }
  
  /* Options Grid Styles */
  .options-grid {
    display: grid;
    gap: 1rem;
    margin-bottom: 2rem;
  }
  
  .option-button {
    background: rgba(5, 5, 5, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 1rem;
    border-radius: 12px;
    cursor: pointer;
    transition: all 0.2s ease;
    text-align: left;
  }
  
  .option-button:hover {
    background: rgba(255, 255, 255, 0.1);
    transform: translateY(-2px);
  }
  
  .option-button.selected {
    background: #000000;
    border-color: #fbff0f;
    box-shadow: 0 4px 12px rgba(235, 162, 37, 0.3);
  }
  
  .option-content {
    display: flex;
    align-items: center;
    gap: 1rem;
    color: white;
  }
  
  .option-marker {
    background: rgba(208, 203, 203, 0.1);
    width: 30px;
    height: 30px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 600;
  }
  
  .option-text {
    font-size: 1rem;
    line-height: 1.5;
  }
  
  /* Navigation Buttons Styles */
  .navigation-buttons {
    display: flex;
    justify-content: space-between;
    margin-top: 2rem;
  }
  
  .quit-button, .next-button {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.8rem 1.5rem;
    border-radius: 12px;
    font-weight: 600;
    transition: all 0.2s ease;
  }
  
  .quit-button {
    background: #ef4444;
    color: white;
    border: none;
  }
  
  .quit-button:hover {
    background: #dc2626;
    transform: translateY(-2px);
  }
  
  .next-button {
    background: #10b981;
    color: white;
    border: none;
  }
  
  .next-button:hover:not(:disabled) {
    background: #059669;
    transform: translateY(-2px);
  }
  
  .next-button:disabled {
    background: #6b7280;
    cursor: not-allowed;
    opacity: 0.7;
  }
  
  .button-icon {
    width: 20px;
    height: 20px;
  }
  
  /* Loading State Styles */
  .loading-state {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
    color: white;
  }
  
  .loading-spinner {
    width: 40px;
    height: 40px;
    border: 4px solid rgba(255, 255, 255, 0.1);
    border-left-color: #3b82f6;
    border-radius: 50%;
    animation: spin 1s linear infinite;
  }
  
  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }



/* Media Queries to improve responsiveness */
@media (max-width: 600px) {
  .arrays-quiz {
    max-width: 90%; /* Adjust for smaller screens */
  }

  .quiz-header {
    font-size: 20px; /* Smaller header font size for small screens */
  }

  .question-text {
    font-size: 18px; /* Smaller question font size for small screens */
  }
}



.result-container {
  max-width: 800px;
  margin: 2rem auto;
  padding: 2rem;
  font-family: 'Poppins', sans-serif;
  color: #ffffff;
}

/* Result Header Styles */
.result-header {
  text-align: center;
  margin-bottom: 3rem;
}

.completion-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 2rem;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* Score Display Styles */
.score-display {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.5rem;
}

.score-circle {
  width: 150px;
  height: 150px;
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  border-radius: 50%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  box-shadow: 0 8px 16px rgba(99, 102, 241, 0.2);
}

.score-number {
  font-size: 3.5rem;
  font-weight: 700;
  line-height: 1;
  color: #ffffff;
}

.score-total {
  font-size: 1.5rem;
  color: rgba(255, 255, 255, 0.9);
}

.score-message {
  font-size: 1.25rem;
  font-weight: 500;
  color: #ffffff;
  text-align: center;
  margin-top: 1rem;
}

/* Review Section Styles */
.explanations-section {
  margin-top: 3rem;
}

.review-title {
  font-size: 1.75rem;
  font-weight: 600;
  color: #ffffff;
  margin-bottom: 1.5rem;
  text-align: center;
}

.wrong-answers-container {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  justify-content: center;
  margin-top: 1.5rem;
}

.review-button {
  background: linear-gradient(135deg, #3b82f6, #1d4ed8);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 12px;
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  font-size: 1rem;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
  box-shadow: 0 4px 6px rgba(59, 130, 246, 0.2);
}

.review-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 8px rgba(59, 130, 246, 0.3);
  background: linear-gradient(135deg, #2563eb, #1e40af);
}

/* Explanation Card Styles */
.explanation-card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-radius: 16px;
  padding: 2rem;
  margin-top: 2rem;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.explanation-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

.explanation-header h3 {
  font-size: 1.5rem;
  font-weight: 600;
  color: #ffffff;
  margin: 0;
}

.close-button {
  background: transparent;
  border: none;
  color: #ffffff;
  font-size: 1.5rem;
  cursor: pointer;
  padding: 0.5rem;
  border-radius: 50%;
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background-color 0.2s;
}

.close-button:hover {
  background-color: rgba(255, 255, 255, 0.1);
}

/* Answer Comparison Styles */
.answer-comparison {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
  margin: 1.5rem 0;
}

.wrong-answer, .correct-answer {
  padding: 1rem;
  border-radius: 12px;
}

.wrong-answer {
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.2);
}

.correct-answer {
  background: rgba(34, 197, 94, 0.1);
  border: 1px solid rgba(34, 197, 94, 0.2);
}

.answer-label {
  display: block;
  font-size: 0.875rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.wrong-answer .answer-label {
  color: #ef4444;
}

.correct-answer .answer-label {
  color: #22c55e;
}

.explanation-text {
  margin-top: 1.5rem;
  padding: 1.5rem;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 12px;
}

.explanation-text h4 {
  font-size: 1.25rem;
  font-weight: 600;
  color: #ffffff;
  margin-bottom: 1rem;
}

.explanation-text p {
  font-size: 1rem;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.9);
}

/* Code Snippet Styles */
.code-snippet {
  background: #1a1a1a;
  border-radius: 8px;
  padding: 1rem;
  margin: 1rem 0;
  overflow-x: auto;
}

.code-snippet code {
  font-family: 'Fira Code', monospace;
  color: #e5e5e5;
  font-size: 0.9rem;
  line-height: 1.5;
}



@media (max-width: 768px) {
    .arrays-quiz {
      padding: 1rem;
    }
  
    .quiz-container {
      padding: 1.5rem;
    }
  
    .question-text {
      font-size: 1.1rem;
    }
  
    .option-button {
      padding: 0.8rem;
    }
  
    .navigation-buttons {
      flex-direction: column;
      gap: 1rem;
    }
  
    .quit-button, .next-button {
      width: 100%;
      justify-content: center;
    }

    .result-container {
    padding: 1rem;
  }
  
  .completion-title {
    font-size: 2rem;
  }
  
  .score-circle {
    width: 120px;
    height: 120px;
  }
  
  .score-number {
    font-size: 2.5rem;
  }
  
  .answer-comparison {
    grid-template-columns: 1fr;
  }
  }
</style>
