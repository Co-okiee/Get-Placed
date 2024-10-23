<template>
  <div class="topic-container">
    <h1 class="main-title">System Design</h1>
    <p class="intro">An introduction to system design concepts and their various components...</p>
    
    <div class="topics-grid">
      <div class="topic-card" @click="navigateTo('BasicsSystem')">
        <div class="card-icon">🔧</div>
        <h3>Basics of System Design</h3>
      </div>

      <div class="topic-card" @click="navigateTo('scalability')">
        <div class="card-icon">📈</div>
        <h3>Scalability in System Design</h3>
      </div>

      <div class="topic-card" @click="navigateTo('database')">
        <div class="card-icon">💾</div>
        <h3>Databases in Designing Systems</h3>
      </div>

      <div class="topic-card" @click="navigateTo('HLD')">
        <div class="card-icon">📋</div>
        <h3>High Level Design (HLD)</h3>
      </div>

      <div class="topic-card" @click="navigateTo('LLD')">
        <div class="card-icon">📐</div>
        <h3>Low Level Design (LLD)</h3>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SystemDesign",
  methods: {
    navigateTo(topic) {
      // Navigate to the specified topic using the router
      this.$router.push({ name: topic });
    }
  }
};
</script>

<style scoped>
.topic-container {
  min-height: 100vh;
  background-color: #1e1e2f;
  color: #f5f5f7;
  padding: 2rem;
  max-width: 1200px;
  margin: 20px auto;
  border-radius: 10px;
}

.main-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: #c8c9ca;
  margin-bottom: 0.5rem;
  text-align: center;
}

.intro {
  font-size: 1.1rem;
  text-align: center;
  margin-bottom: 3rem;
  line-height: 1.6;
}

.topics-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr); /* 3 columns */
  gap: 1.5rem;
  padding: 1rem 0;
}

.topic-card {
  background: rgb(45, 45, 60);
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  cursor: pointer;
  transition: all 0.3s ease;
  text-align: center;
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
  color: #f5f5f7;
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

@media (max-width: 1200px) {
  .topics-grid {
    grid-template-columns: repeat(2, 1fr); /* 2 columns for medium screens */
  }
}

@media (max-width: 768px) {
  .topics-grid {
    grid-template-columns: 1fr; /* 1 column for smaller screens */
  }
}
</style>
