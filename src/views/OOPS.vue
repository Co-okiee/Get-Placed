<template>
  <div class="topic-container">
    <div class="navigation-header">
      <button @click="goBack" class="back-button">
        <span class="back-icon">←</span>
        Back to Topics
      </button>
    </div>

    <h1 class="main-title">
      OOP in C++
      <span class="title-accent">Introduction</span>
    </h1>
    <p class="intro">Learn the core concepts of Object-Oriented Programming (OOP) in C++</p>

    <div class="topics-grid">
      <div class="topic-card" @click="navigateTo('OOPSbasic')">
        <div class="card-icon">🔧</div>
        <h3>OOP Basics</h3>
        <p>Classes, objects, and more</p>
      </div>

      <div class="topic-card" @click="navigateTo('encapsulation')">
        <div class="card-icon">🔐</div>
        <h3>Encapsulation</h3>
        <p>Data hiding and abstraction</p>
      </div>

      <div class="topic-card" @click="navigateTo('abstraction')">
        <div class="card-icon">🚪</div>
        <h3>Abstraction</h3>
        <p>Hiding complexity with simple interfaces</p>
      </div>

      <div class="topic-card" @click="navigateTo('polymorphism')">
        <div class="card-icon">🔀</div>
        <h3>Polymorphism</h3>
        <p>One interface, many implementations</p>
      </div>

      <div class="topic-card" @click="navigateTo('inheritance')">
        <div class="card-icon">📜</div>
        <h3>Inheritance</h3>
        <p>Reusing code through hierarchies</p>
      </div>

      <div class="topic-card" @click="navigateTo('dynamicbinding')">
        <div class="card-icon">🔗</div>
        <h3>Dynamic Binding & Message Passing</h3>
        <p>Late binding and inter-object communication</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "OOPSCpp",
  methods: {
    navigateTo(topic) {
      this.$router.push({ name: topic });
    },
    goBack() {
      this.$router.push({ name: 'study' });
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

.main-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: #c8c9ca;
  margin-bottom: 0.5rem;
  text-align: center;
}

.title-accent {
  color: #3280ff;
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

.topic-card p {
  color: #d2d2d3;
  font-size: 0.9rem;
  margin-bottom: 1rem;
  line-height: 1.4;
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
