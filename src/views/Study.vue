<template>
  <div class="study-container">
    <!-- Back Button -->
    <div class="navigation-header">
      <button @click="goBack" class="back-button">
        <span class="back-icon">←</span>
        Back to Dashboard
      </button>
    </div>

    <!-- Main Content -->
    <div class="study-content">
      <h1 class="page-title">
        Placement Preparation
        <span class="title-accent">Topics</span>
      </h1>
      
      <p class="subtitle">Select a topic to start your preparation journey</p>

      <div class="topics-grid">
        <!-- Data Structures -->
        <div class="topic-card" @click="goToTopic('data-structures')">
          <div class="card-icon">🔍</div>
          <h3>Data Structures</h3>
          <p>Arrays, Linked Lists, Trees, Graphs, and more</p>
          <div class="progress-bar">
            <div class="progress" :style="{ width: '60%' }"></div>
          </div>
          <span class="progress-text">60% Complete</span>
        </div>

        <!-- Algorithms -->
        <div class="topic-card" @click="goToTopic('algorithms')">
          <div class="card-icon">⚡</div>
          <h3>Algorithms</h3>
          <p>Sorting, Searching, Dynamic Programming</p>
          <div class="progress-bar">
            <div class="progress" :style="{ width: '45%' }"></div>
          </div>
          <span class="progress-text">45% Complete</span>
        </div>

        <!-- Operating Systems -->
        <div class="topic-card" @click="goToTopic('os')">
          <div class="card-icon">💻</div>
          <h3>Operating Systems</h3>
          <p>Processes, Memory Management, File Systems</p>
          <div class="progress-bar">
            <div class="progress" :style="{ width: '30%' }"></div>
          </div>
          <span class="progress-text">30% Complete</span>
        </div>

        <!-- DBMS -->
        <div class="topic-card" @click="goToTopic('dbms')">
          <div class="card-icon">🗄️</div>
          <h3>DBMS</h3>
          <p>SQL, Normalization, Transaction Management</p>
          <div class="progress-bar">
            <div class="progress" :style="{ width: '75%' }"></div>
          </div>
          <span class="progress-text">75% Complete</span>
        </div>

        <!-- OOP -->
        <div class="topic-card" @click="goToTopic('oops')">
          <div class="card-icon">🎯</div>
          <h3>Object-Oriented Programming</h3>
          <p>Classes, Inheritance, Polymorphism</p>
          <div class="progress-bar">
            <div class="progress" :style="{ width: '55%' }"></div>
          </div>
          <span class="progress-text">55% Complete</span>
        </div>

        <!-- Aptitude -->
        <div class="topic-card" @click="goToTopic('Apt')">
          <div class="card-icon">🧮</div>
          <h3>Aptitude & Reasoning</h3>
          <p>Quantitative, Logical, Verbal Ability</p>
          <div class="progress-bar">
            <div class="progress" :style="{ width: '40%' }"></div>
          </div>
          <span class="progress-text">40% Complete</span>
        </div>

        <!-- Computer Networks -->
        <div class="topic-card" @click="goToTopic('CN')">
          <div class="card-icon">🌐</div>
          <h3>Computer Networks</h3>
          <p>OSI Model, TCP/IP, Network Security</p>
          <div class="progress-bar">
            <div class="progress" :style="{ width: '25%' }"></div>
          </div>
          <span class="progress-text">25% Complete</span>
        </div>

        <!-- System Design -->
        <div class="topic-card" @click="goToTopic('SystemDesign')">
          <div class="card-icon">🏗️</div>
          <h3>System Design</h3>
          <p>Scalability, High Availability, Load Balancing</p>
          <div class="progress-bar">
            <div class="progress" :style="{ width: '15%' }"></div>
          </div>
          <span class="progress-text">15% Complete</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Study",
  methods: {
    goToTopic(topic) {
      this.$router.push({ name: topic });
    },
    goBack() {
      this.$router.push({ name: 'Dashboard' });
    }
  }
};
</script>

<style scoped>
.study-container {
  min-height: 100vh;
  background-color: #000000;
  padding: 2rem;
}

.navigation-header {
  max-width: 1200px;
  margin: 0 auto;
  padding-bottom: 1rem;
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

.study-content {
  max-width: 1200px;
  margin: 0 auto;
}

.page-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: #c8c9ca;
  margin-bottom: 0.5rem;
  text-align: center;
}

.title-accent {
  color: #3280ff;
}

.subtitle {
  text-align: center;
  color: #d2d2d3;
  margin-bottom: 3rem;
  font-size: 1.1rem;
}


.topic-card {
  background: rgb(250, 249, 249);
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  cursor: pointer;
  transition: all 0.3s ease;
}

.topic-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}

.card-icon {
  font-size: 2rem;
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
  font-size: 0.9rem;
  margin-bottom: 1rem;
  line-height: 1.4;
}

.progress-bar {
  width: 100%;
  height: 6px;
  background: #e2e8f0;
  border-radius: 3px;
  margin-bottom: 0.5rem;
  overflow: hidden;
}

.progress {
  height: 100%;
  background: #0061fe;
  border-radius: 3px;
  transition: width 0.3s ease;
}

.progress-text {
  font-size: 0.8rem;
  color: #64748b;
}
.topics-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr); /* 4 columns */
  gap: 1.5rem;
  padding: 1rem 0;
  max-width: 100%; /* Ensure it fits the viewport */
}

@media (max-width: 1200px) {
  .topics-grid {
    grid-template-columns: repeat(3, 1fr); /* 3 columns for medium screens */
  }
}

@media (max-width: 768px) {
  .topics-grid {
    grid-template-columns: repeat(2, 1fr); /* 2 columns for smaller screens */
  }
}

@media (max-width: 480px) {
  .topics-grid {
    grid-template-columns: 1fr; /* 1 column for very small screens */
  }
}


@media (max-width: 768px) {
  .study-container {
    padding: 1rem;
  }

  .page-title {
    font-size: 2rem;
  }

  .topics-grid {
    grid-template-columns: 1fr;
  }
}
</style>