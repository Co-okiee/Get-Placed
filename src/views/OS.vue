<!-- src/views/OperatingSystems.vue -->
<template>
  <div class="topic-container">
    <div class="navigation-header">
      <button @click="goBack" class="back-button">
        <span class="back-icon">←</span>
        Back to Topics
      </button>
    </div>

    <h1 class="page-title">
      Operating Systems
      <span class="title-accent">Overview</span>
    </h1>
    <p class="subtitle">Explore the fundamentals of Operating Systems</p>

    <div class="topics-grid">
      <div class="topic-card" @click="navigateTo('basics')">
        <div class="card-icon">📘</div>
        <h3>Basics</h3>
        <p>Introduction to OS fundamentals</p>
      </div>

      <div class="topic-card" @click="navigateTo('system')">
        <div class="card-icon">🔧</div>
        <h3>System Structure</h3>
        <p>Internal architecture and organization</p>
      </div>

      <div class="topic-card" @click="navigateTo('CPU')">
        <div class="card-icon">⚙️</div>
        <h3>CPU Scheduling</h3>
        <p>Scheduling algorithms and efficiency</p>
      </div>

      <div class="topic-card" @click="navigateTo('processsyn')">
        <div class="card-icon">🔗</div>
        <h3>Process Synchronization</h3>
        <p>Deadlocks, semaphores, and more</p>
      </div>

      <div class="topic-card" @click="navigateTo('deadlock')">
        <div class="card-icon">🚫</div>
        <h3>Deadlock</h3>
        <p>Handling and avoiding deadlock</p>
      </div>

      <div class="topic-card" @click="navigateTo('pt')">
        <div class="card-icon">👥</div>
        <h3>Processes & Threads</h3>
        <p>Concurrency and multitasking</p>
      </div>

      <div class="topic-card" @click="navigateTo('memory')">
        <div class="card-icon">💾</div>
        <h3>Memory Management</h3>
        <p>Paging, segmentation, and more</p>
      </div>

      <div class="topic-card" @click="navigateTo('disk')">
        <div class="card-icon">💽</div>
        <h3>Disk Management</h3>
        <p>Disk scheduling and storage allocation</p>
      </div>

      <div class="topic-card" @click="navigateTo('misc')">
        <div class="card-icon">🔍</div>
        <h3>Miscellaneous Topics</h3>
        <p>Other important OS concepts</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "OperatingSystems",
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

.topics-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr); /* 4 columns */
  gap: 1.5rem;
  padding: 1rem 0;
  max-width: 100%; /* Ensure it fits the viewport */
}

.topic-card {
  background: rgb(250, 249, 249);
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
</style>
