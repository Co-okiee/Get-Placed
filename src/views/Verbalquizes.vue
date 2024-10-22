<template>
  <div class="verbal-quizzes">
    <!-- Navigation Header -->
    <div class="nav-header">
      <button @click="goBack" class="back-button">
        <span class="back-icon">←</span>
        Back to Quiz Selection
      </button>
    </div>

    <div class="content-wrapper">
      <div class="header-section">
        <h1 class="main-title">Verbal Ability Quizzes</h1>
        <p class="subtitle">Select a quiz to begin practicing</p>
      </div>

      <div class="fixed-grid">
        <router-link :to="{ name: 'VerbalAbilityQuizPage', params: { quizNumber: 1 } }">
          <button class="quiz-card">Verbal Ability Quiz 1</button>
        </router-link>
        <router-link :to="{ name: 'VerbalAbilityQuizPage', params: { quizNumber: 2 } }">
          <button class="quiz-card">Verbal Ability Quiz 2</button>
        </router-link>
        <router-link :to="{ name: 'VerbalAbilityQuizPage', params: { quizNumber: 3 } }">
          <button class="quiz-card">Verbal Ability Quiz 3</button>
        </router-link>
        <router-link :to="{ name: 'VerbalAbilityQuizPage', params: { quizNumber: 4 } }">
          <button class="quiz-card">Verbal Ability Quiz 4</button>
        </router-link>
        <router-link :to="{ name: 'VerbalAbilityQuizPage', params: { quizNumber: 5 } }">
          <button class="quiz-card">Verbal Ability Quiz 5</button>
        </router-link>
        <router-link :to="{ name: 'VerbalAbilityQuizPage', params: { quizNumber: 6 } }">
          <button class="quiz-card">Verbal Ability Quiz 6</button>
        </router-link>
        <router-link :to="{ name: 'VerbalAbilityQuizPage', params: { quizNumber: 7 } }">
          <button class="quiz-card">Verbal Ability Quiz 7</button>
        </router-link>
        <router-link :to="{ name: 'VerbalAbilityQuizPage', params: { quizNumber: 8 } }">
          <button class="quiz-card">Verbal Ability Quiz 8</button>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "VerbalAbilityQuizzes",
  methods: {
    goBack() {
      this.$router.push({ name: 'quiz-options' });
    }
  }
};
</script>

<style scoped>
.verbal-quizzes {
  min-height: 100vh;
  background: linear-gradient(135deg, #000000 0%, #393939 100%);
  padding: 2rem;
  display: flex;
  flex-direction: column;
}

.nav-header {
  max-width: 1400px;
  margin: 0 auto 2rem;
  width: 100%;
}

.back-button {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: white;
  border: 1px solid #e2e8f0;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  color: #1e293b;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}

.back-button:hover {
  background: #f1f5f9;
  transform: translateX(-4px);
}

.back-icon {
  font-size: 1.2rem;
}

.content-wrapper {
  max-width: 1400px;
  margin: 0 auto;
  width: 100%;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.header-section {
  text-align: center;
  margin-bottom: 3rem;
}

.main-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 0.5rem;
}

.subtitle {
  color: #cacaca;
  font-size: 1.1rem;
}

.fixed-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
  padding: 1rem 0;
  margin: 0 auto;
  width: 100%;
}

.quiz-card {
  background: rgba(255, 255, 255, 0.95);
  border: none;
  border-radius: 16px;
  padding: 2rem;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100px;
}

.quiz-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.2);
  background: white;
}

/* Responsive grid adjustments */
@media (min-width: 1201px) {
  .fixed-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}

@media (min-width: 901px) and (max-width: 1200px) {
  .fixed-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (min-width: 601px) and (max-width: 900px) {
  .fixed-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 600px) {
  .verbal-quizzes {
    padding: 1rem;
  }

  .main-title {
    font-size: 2rem;
  }

  .fixed-grid {
    grid-template-columns: 1fr;
  }

  .quiz-card {
    height: auto;
    min-height: 80px;
  }
}
</style>
