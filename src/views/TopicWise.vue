<template>
  <div class="topic-wise-container">
    <!-- Navigation Header -->
    <div class="nav-header">
      <button @click="goBack" class="back-button">
        <span class="back-icon">←</span>
        Back to Quiz Selection
      </button>
    </div>

    <div class="content-wrapper">
      <div class="header-section">
        <h1 class="main-title">Choose Your Topic</h1>
        <p class="subtitle">Select a subject to begin your practice</p>
      </div>

      <div class="fixed-grid">
        <!-- Data Structures -->
        <button @click="goToArrayQuiz" class="topic-card">
          <div class="card-icon">🔷</div>
          <h3>Data Structures</h3>
          <p>Arrays, Linked Lists, Trees & more</p>
        </button>

        <!-- Algorithms -->
        <button @click="goToMatrices" class="topic-card">
          <div class="card-icon">🔄</div>
          <h3>Algorithms</h3>
          <p>Sorting, Searching & Problem Solving</p>
        </button>

        <!-- Operating Systems -->
        <button @click="goToStrings" class="topic-card">
          <div class="card-icon">💻</div>
          <h3>Operating Systems</h3>
          <p>Processes, Memory & File Systems</p>
        </button>

        <!-- DBMS -->
        <button @click="goToTopic('dbms')" class="topic-card">
          <div class="card-icon">🗃️</div>
          <h3>DBMS</h3>
          <p>SQL, Normalization & Transactions</p>
        </button>

        <!-- OOP -->
        <button @click="goToTopic('oops')" class="topic-card">
          <div class="card-icon">🎯</div>
          <h3>Object-Oriented Programming</h3>
          <p>Classes, Inheritance & Polymorphism</p>
        </button>

        <!-- Aptitude -->
        <button @click="goToTopic('Apt')" class="topic-card">
          <div class="card-icon">🧮</div>
          <h3>Aptitude & Reasoning</h3>
          <p>Logical & Quantitative Problems</p>
        </button>

        <!-- Computer Networks -->
        <button @click="goToTopic('CN')" class="topic-card">
          <div class="card-icon">🌐</div>
          <h3>Computer Networks</h3>
          <p>TCP/IP, OSI Model & Protocols</p>
        </button>

        <!-- System Design -->
        <button @click="goToTopic('SystemDesign')" class="topic-card">
          <div class="card-icon">⚡</div>
          <h3>System Design</h3>
          <p>Architecture, Scalability & Design Patterns</p>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TopicWiseQuiz",
  methods: {
    goToArrayQuiz() {
      this.$router.push({ name: "array-quiz" });
    },
    goToMatrices() {
      this.$router.push({ name: "matrix-quiz" });
    },
    goToStrings() {
      this.$router.push({ name: "strings-quiz" });
    },
    goToTopic(topic) {
      this.$router.push({ name: `${topic}-quiz` });
    },
    goBack() {
      this.$router.push({ name: 'quiz-options' });
    }
  }
};
</script>

<style scoped>
.topic-wise-container {
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

.topic-card {
  background: rgba(255, 255, 255, 0.95);
  border: none;
  border-radius: 16px;
  padding: 2rem;
  text-align: left;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  height: 200px;
}

.topic-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.2);
  background: white;
}

.card-icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.topic-card h3 {
  color: #1e293b;
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.topic-card p {
  color: #64748b;
  font-size: 0.95rem;
  line-height: 1.5;
  margin: 0;
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
  .topic-wise-container {
    padding: 1rem;
  }

  .main-title {
    font-size: 2rem;
  }

  .fixed-grid {
    grid-template-columns: 1fr;
  }

  .topic-card {
    height: auto;
    min-height: 180px;
  }
}
</style>