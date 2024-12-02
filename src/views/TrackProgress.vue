<template>
  <div class="ai-topic-wise-container">
    <!-- Navigation Header -->
   

    <div class="content-wrapper">
      <div class="header-section">
        <h1 class="main-title">Choose Your Topic</h1>
        <p class="subtitle">Select a subject to begin your practice</p>
      </div>

      <div class="fixed-grid">
        <!-- Data Structures -->
        <button @click="goToAiDS" class="topic-card">
          <div class="card-icon">🔷</div>
          <h3>Tracker</h3>
          <p>go</p>
        </button>
        </div>
    </div>

  </div>
</template>

<script>
export default {
  name: "tracker",
  methods: {
    goToAiDS() {
window.location.href = '/track.html';
}
  }
};
</script>

<style scoped>
.ai-topic-wise-container {
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