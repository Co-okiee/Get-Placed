
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
import { useUserStore } from "@/stores/counter"; // Adjust import path as necessary

export default {
  name: "TrackProgress",
  computed: {
    scores() {
      const store = useUserStore();
      return store.scores[store.user] || [];
    },
    totalQuestions() {
      return 10; // Adjust to match your quiz length
    },
  },
  methods: {
    goToAiDS() {
      window.location.href = "/track.html";
    },
  },
};
</script>

<style scoped>
.track-progress {
  padding: 2rem;
  background-color: #f9f9f9;
}

.ai-topic-wise-container {
  min-height: 100vh;
  background: linear-gradient(135deg, #000000 0%, #393939 100%);
  padding: 2rem;
  display: flex;
  flex-direction: column;
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