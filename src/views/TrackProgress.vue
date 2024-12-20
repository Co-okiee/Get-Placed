

<template>
  <div class="track-progress">
    <h1>Track Progress</h1>
    <p v-if="!scores || scores.length === 0">No scores available. Take a quiz!</p>
    <ul v-else>
      <li v-for="(score, index) in scores" :key="index">
        Quiz {{ index + 1 }}: {{ score }}/{{ totalQuestions }}
      </li>
    </ul>

    <div class="ai-topic-wise-container">
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
            <p>Go</p>
          </button>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import { useUserStore } from "@/store";

export default {
  name: "TrackProgress",
  data() {
    return {
      username: null,
      name: null,
    };
  },
  computed: {
    scores() {
      const store = useUserStore();
      return store.scores[store.user];
    },
    totalQuestions() {
      return 2; // Adjust based on your quiz length
    },
  },
  methods: {
    goToAiDS() {
      window.location.href = "/track.html";
    },
  },

</script>
<style scoped>
.track-progress {
  padding: 2rem;
  background-color: #f9f9f9;
}

.ai-topic-wise-container {
  min-height: 100vh;
  background: linear-gradient(135deg, #000000 0%, #393939 100%);
}

.content-wrapper {
  max-width: 1400px;
  margin: 0 auto;
}

.header-section {
  margin-bottom: 3rem;
}

.welcome-card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  padding: 1.5rem;
  border-radius: 1rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.welcome-card:hover {
  transform: translateY(-5px);
}

.content-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
}

.modern-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 1rem;
  overflow: hidden;
}

.modern-table th,
.modern-table td {
  padding: 1rem;
  text-align: left;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.modern-table th {
  background: rgba(255, 255, 255, 0.1);
  font-weight: 600;
}

.score-cell {
  position: relative;
}

.score-bar {
  position: absolute;
  left: 0;
  bottom: 0;
  height: 4px;
  background: #60A5FA;
  transition: width 0.5s ease;
}

.score-row {
  transition: background-color 0.3s ease;
}

.score-row:hover {
  background: rgba(255, 255, 255, 0.1);
}

.improved {
  animation: pulse 2s infinite;
}

.topic-chart {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 1rem;
  padding: 1.5rem;
  margin-bottom: 2rem;
  transition: transform 0.3s ease;
}

.topic-chart:hover {
  transform: translateY(-5px);
}

.chart-container {
  height: 200px;
  margin: 1rem 0;
}

.feedback-card {
  padding: 1rem;
  border-radius: 0.5rem;
  margin-top: 1rem;
  transition: all 0.3s ease;
}

.feedback-excellent {
  background: rgba(34, 197, 94, 0.2);
  border-left: 4px solid #22c55e;
}

.feedback-good {
  background: rgba(234, 179, 8, 0.2);
  border-left: 4px solid #eab308;
}

.feedback-needs-work {
  background: rgba(239, 68, 68, 0.2);
  border-left: 4px solid #ef4444;
}

.fixed-grid {
  grid-template-columns: repeat(4, 1fr);
}

.main-title {
  font-size: 2rem;
}

/* Animations */
@keyframes pulse {
  0% { background-color: transparent; }
  50% { background-color: rgba(96, 165, 250, 0.1); }
  100% { background-color: transparent; }
}

.animate-slide-down {
  animation: slideDown 0.5s ease-out;
}

.animate-slide-up {
  animation: slideUp 0.5s ease-out;
}

.animate-slide-up-delayed {
  animation: slideUp 0.5s ease-out 0.2s both;
}

.animate-fade-in {
  animation: fadeIn 0.5s ease-out;
}

@keyframes slideDown {
  from { transform: translateY(-20px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}

@keyframes slideUp {
  from { transform: translateY(20px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.trend-icon {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 5px;
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
}

.trend-up {
  border-bottom: 8px solid #22c55e;
}

.trend-down {
  border-top: 8px solid #ef4444;
}
</style>
