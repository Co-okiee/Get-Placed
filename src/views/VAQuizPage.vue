<template>
  <div class="arrays-quiz">
    <!-- Quiz Start Screen -->
    <div v-if="!quizStarted" class="quiz-intro">
      <div class="intro-content">
        <h1 class="intro-title">Verbal Ability Quiz</h1>
        <p class="intro-message">
          Welcome to the Verbal Ability Quiz!<br />
          Test your language skills and verbal reasoning ability.
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
          <h2 class="question-text">{{ questions[currentQuestionIndex].question }}</h2>

          <!-- Passage if available -->
          <div v-if="questions[currentQuestionIndex].passage" class="passage">
            <p>{{ questions[currentQuestionIndex].passage }}</p>
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

      <!-- Results Screen -->
      <div v-else-if="currentQuestionIndex >= questions.length" class="result-container">
        <div class="result-header">
          <h2 class="completion-title">Quiz Completed! 🎉</h2>
          <div class="score-display">
            <div class="score-circle">
              <span class="score-number">{{ score }}</span>
              <span class="score-total">/ {{ questions.length }}</span>
            </div>
            <p class="score-message">
              {{ score === questions.length ? "Perfect Score! Outstanding Performance! 🌟" :
                 score >= questions.length * 0.8 ? "Excellent Work! Keep it up! 🎯" :
                 score >= questions.length * 0.6 ? "Good effort! Room to grow! 💪" :
                 "Keep practicing! You'll improve! 📚" }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "VAQuizPage",
  data() {
    return {
      quizStarted: false,
      loading: false,
      questions: [],
      currentQuestionIndex: 0,
      selectedOption: null,
      score: 0
    };
  },
  methods: {
    startQuiz() {
      this.quizStarted = true;
      this.fetchQuestions();
    },
    async fetchQuestions() {
      this.loading = true;
      try {
        const response = await axios.get(`http://localhost:5000/verbal-ability-quiz-questions?quiz=${this.$route.params.quizNumber}`);
        this.questions = response.data;
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
      this.currentQuestionIndex = this.questions.length;
    },
    getOptions(index) {
      const question = this.questions[index];
      return [question.option1, question.option2, question.option3, question.option4];
    },
    async nextQuestion() {
      const currentQuestion = this.questions[this.currentQuestionIndex];
      if (this.selectedOption === currentQuestion.answer) {
        this.score++;
      }

      if (this.currentQuestionIndex === this.questions.length - 1) {
        await this.saveScore();
      }

      this.currentQuestionIndex++;
      this.selectedOption = null;
    },
    async saveScore() {
      try {
        const userId = localStorage.getItem('user_id');
        await axios.post('http://localhost:5000/save_verbal_score', {
          user_id: userId,
          score: this.score,
          topic: `Verbal Ability Quiz ${this.$route.params.quizNumber}`
        });
      } catch (error) {
        console.error("Error saving score:", error);
      }
    }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap');

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

/* Passage Styles */
.passage {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 12px;
  padding: 1.5rem;
  margin: 1.5rem 0;
  color: #e2e8f0;
  line-height: 1.6;
  font-size: 1rem;
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

/* Result Container Styles */
.result-container {
  max-width: 800px;
  margin: 2rem auto;
  padding: 2rem;
  color: #ffffff;
}

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
