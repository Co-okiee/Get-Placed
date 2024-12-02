<template>
  <div class="progress-tracker">
    <!-- Header Section with Animated Welcome -->
    <div class="header-section">
      <h1 class="text-4xl font-bold mb-6 animate-slide-down">
        Track Progress
      </h1>
      <div class="welcome-card animate-fade-in">
        <h2 class="text-2xl font-semibold mb-2">Welcome, Mili!</h2>
        <p class="text-lg text-gray-200">
          You're doing great! Keep pushing your limits and improving your scores.
        </p>
      </div>
    </div>

    <!-- Main Content Grid -->
    <div class="content-grid">
      <!-- Scores Table Section -->
      <div class="table-section animate-slide-up">
        <h2 class="text-2xl font-semibold mb-4">Your Progress</h2>
        <div class="table-container">
          <table v-if="scores.length" class="modern-table">
            <thead>
              <tr>
                <th>Date</th>
                <th>Score</th>
                <th>Topic</th>
                <th>Trend</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(score, index) in sortedScores" 
                  :key="index"
                  class="score-row"
                  :class="{'improved': isImproved(score, index)}">
                <td>{{ formatDate(score.date) }}</td>
                <td class="score-cell">
                  <span class="score-value">{{ score.score }}</span>
                  <div class="score-bar" :style="{ width: `${(score.score/18)*100}%` }"></div>
                </td>
                <td>{{ score.topic }}</td>
                <td>
                  <span :class="getTrendIcon(score, index)"></span>
                </td>
              </tr>
            </tbody>
          </table>
          <p v-else class="no-scores">No scores recorded yet.</p>
        </div>
      </div>

      <!-- Charts Section -->
      <div class="charts-section animate-slide-up-delayed">
        <div v-for="topic in uniqueTopics" 
             :key="topic" 
             class="topic-chart">
          <h3 class="text-xl font-semibold mb-3">{{ topic }}</h3>
          <div class="chart-container">
            <canvas :id="`scoreChart-${topic}`"></canvas>
          </div>
          <div class="feedback-card" :class="getFeedbackClass(topic)">
            {{ generateFeedback(topic) }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Chart } from 'chart.js/auto';

export default {
  data() {
    return {
      scores: [
        {"date": "2024-10-01", "score": 5, "topic": "Arrays"},
        {"date": "2024-10-02", "score": 5, "topic": "Arrays"},
        {"date": "2024-10-03", "score": 7, "topic": "Arrays"},
        {"date": "2024-10-04", "score": 9, "topic": "Arrays"},
        {"date": "2024-10-03", "score": 3, "topic": "Matrices"},
        {"date": "2024-10-05", "score": 6, "topic": "Arrays"},
        {"date": "2024-10-04", "score": 1, "topic": "Matrices"},
        {"date": "2024-10-05", "score": 5, "topic": "Verbal Ability Quiz 1"},
        {"date": "2024-10-05", "score": 4, "topic": "Matrices"},
        {"date": "2024-10-06", "score": 6, "topic": "Matrices"},
        {"date": "2024-10-07", "score": 8, "topic": "Matrices"},
        {"date": "2024-10-06", "score": 7, "topic": "Arrays"},
        {"date": "2024-10-07", "score": 11, "topic": "Arrays"},
        {"date": "2024-10-07", "score": 4, "topic": "Verbal Ability Quiz 1"},
        {"date": "2024-10-08", "score": 6, "topic": "Verbal Ability Quiz 1"},
        {"date": "2024-10-08", "score": 1, "topic": "Matrices"},
        {"date": "2024-10-08", "score": 15, "topic": "Arrays"}
      ],
      charts: {},
    };
  },
  computed: {
    uniqueTopics() {
      return [...new Set(this.scores.map(score => score.topic))];
    },
    sortedScores() {
      return [...this.scores].sort((a, b) => new Date(b.date) - new Date(a.date));
    }
  },
  mounted() {
    this.initializeCharts();
  },
  methods: {
    formatDate(dateString) {
      const options = { year: 'numeric', month: 'long', day: 'numeric' };
      return new Date(dateString).toLocaleDateString(undefined, options);
    },
    isImproved(score, index) {
      if (index === this.scores.length - 1) return false;
      const prevScore = this.scores.find(s => 
        s.topic === score.topic && 
        new Date(s.date) < new Date(score.date)
      );
      return prevScore && score.score > prevScore.score;
    },
    getTrendIcon(score, index) {
      const improved = this.isImproved(score, index);
      return {
        'trend-icon': true,
        'trend-up': improved,
        'trend-down': !improved
      };
    },
    getFeedbackClass(topic) {
      const avgScore = this.getAverageScore(topic);
      return {
        'feedback-excellent': avgScore >= 10,
        'feedback-good': avgScore >= 7 && avgScore < 10,
        'feedback-needs-work': avgScore < 7
      };
    },
    getAverageScore(topic) {
      const topicScores = this.scores.filter(s => s.topic === topic);
      return topicScores.reduce((sum, s) => sum + s.score, 0) / topicScores.length;
    },
    generateFeedback(topic) {
      const avgScore = this.getAverageScore(topic);
      if (avgScore >= 10) {
        return `Outstanding progress in ${topic}! You're mastering this topic.`;
      } else if (avgScore >= 7) {
        return `Good work in ${topic}! Keep practicing to reach excellence.`;
      }
      return `Keep working on ${topic}. Regular practice will help improve your scores.`;
    },
    initializeCharts() {
      this.uniqueTopics.forEach(topic => {
        const ctx = document.getElementById(`scoreChart-${topic}`).getContext('2d');
        const topicData = this.scores
          .filter(score => score.topic === topic)
          .sort((a, b) => new Date(a.date) - new Date(b.date));

        this.charts[topic] = new Chart(ctx, {
          type: 'line',
          data: {
            labels: topicData.map(score => this.formatDate(score.date)),
            datasets: [{
              label: 'Score',
              data: topicData.map(score => score.score),
              borderColor: '#60A5FA',
              backgroundColor: 'rgba(96, 165, 250, 0.1)',
              tension: 0.4,
              fill: true
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            animation: {
              duration: 1500,
              easing: 'easeInOutQuart'
            },
            scales: {
              y: {
                beginAtZero: true,
                max: 18,
                grid: {
                  color: 'rgba(255, 255, 255, 0.1)'
                },
                ticks: {
                  color: '#FFFFFF'
                }
              },
              x: {
                grid: {
                  color: 'rgba(255, 255, 255, 0.1)'
                },
                ticks: {
                  color: '#FFFFFF'
                }
              }
            },
            plugins: {
              legend: {
                display: false
              }
            }
          }
        });
      });
    }
  }
};
</script>

<style scoped>
.progress-tracker {
  padding: 2rem;
  color: white;
  min-height: 100vh;
  background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
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