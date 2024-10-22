<template>
  <div>
    <h1>Track Progress</h1>

    <!-- User name and motivational message -->
    <h2>Welcome, Devansh!</h2>
    <p class="motivational-message">
      You're doing great! Keep pushing your limits and improving your scores. Every step counts, so keep going, and don't give up!
    </p>

    <div v-if="message">{{ message }}</div>

    <div class="progress-section">
      <!-- Table for displaying the scores -->
      <div class="table-container">
        <h2>Your Progress</h2>
        <table v-if="scores.length" class="score-table">
          <thead>
            <tr>
              <th>Date</th>
              <th>Score</th>
              <th>Topic</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(score, index) in scores" :key="index">
              <td>{{ formatDate(score.date) }}</td>
              <td>{{ score.score }}</td>
              <td>{{ score.topic }}</td>
            </tr>
          </tbody>
        </table>
        <!-- Display message if no scores -->
        <p v-if="!scores.length">No scores recorded yet.</p>
      </div>

      <!-- Graphs for each topic -->
      <div v-if="scores.length" class="charts-container">
        <h2>Your Progress by Topic</h2>
        <div v-for="topic in uniqueTopics" :key="topic" class="chart-container">
          <h3>{{ topic }}</h3>
          <canvas :id="`scoreChart-${topic}`"></canvas>
          <p class="feedback">{{ generateFeedback(topic) }}</p> <!-- Feedback for each topic -->
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
      userId: '123', // Example hardcoded user ID
      message: '',
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
      ], // Hardcoded scores data
    };
  },
  computed: {
    uniqueTopics() {
      return [...new Set(this.scores.map(score => score.topic))]; // Get unique topics
    }
  },
  mounted() {
    this.sortScores(); // Sort scores when the component is mounted
    this.renderCharts(); // Render charts after sorting
  },
  methods: {
    formatDate(dateString) {
      if (!dateString) return 'N/A'; // Handle null dates
      const options = { year: 'numeric', month: 'long', day: 'numeric' };
      return new Date(dateString).toLocaleDateString(undefined, options);
    },
    sortScores() {
      this.scores.sort((a, b) => new Date(a.date) - new Date(b.date)); // Sort scores in ascending order by date
    },
    renderCharts() {
      const topicsData = this.uniqueTopics.map(topic => {
        const filteredScores = this.scores.filter(score => score.topic === topic);
        const labels = [...new Set(filteredScores.map(score => this.formatDate(score.date)))]; // Unique dates for the topic

        // Create data for bar graph where each date corresponds to a score
        const data = labels.map(label => {
          const scoresForDate = filteredScores.filter(score => this.formatDate(score.date) === label);
          const totalScore = scoresForDate.reduce((total, score) => total + score.score, 0); // Sum scores for that date

          // Limit the score to a maximum of 18
          return Math.min(totalScore, 18);
        });

        return { topic, labels, data };
      });

      topicsData.forEach(({ topic, labels, data }) => {
        const ctx = document.getElementById(`scoreChart-${topic}`).getContext('2d');

        new Chart(ctx, {
          type: 'bar', // Change to bar chart
          data: {
            labels: labels,
            datasets: [
              {
                label: topic,
                data: data,
                backgroundColor: this.getSubtleColor(), // Use subtle colors for the bars
                borderWidth: 1,
              },
            ],
          },
          options: {
            scales: {
              y: {
                beginAtZero: true,
                max: 18, // Set the maximum value of the y-axis to 18
                title: {
                  display: true,
                  text: 'Score',
                  color: 'white', // Set title color to white
                },
                ticks: {
                  color: 'white', // Set y-axis ticks color to white
                },
              },
              x: {
                title: {
                  display: true,
                  text: 'Date',
                  color: 'white', // Set title color to white
                },
                ticks: {
                  color: 'white', // Set x-axis ticks color to white
                },
              },
            },
            plugins: {
              legend: {
                labels: {
                  color: 'white', // Set legend text color to white
                },
              },
            },
          },
        });
      });
    },
    getSubtleColor() {
      // Return a subtle color for bar graph
      const colors = ['#90EE90', '#ADD8E6', '#FFB6C1', '#FFFFE0', '#E6E6FA']; // Light colors
      return colors[Math.floor(Math.random() * colors.length)];
    },
    generateFeedback(topic) {
      const filteredScores = this.scores.filter(score => score.topic === topic);
      const averageScore = filteredScores.reduce((total, score) => total + score.score, 0) / (filteredScores.length || 1);
      
      let feedback = `Your average score in ${topic} is ${averageScore.toFixed(2)}. `;

      if (averageScore >= 10) {
        feedback += "Excellent work! You're mastering this topic. Keep it up! Consider revisiting advanced materials to further challenge yourself.";
      } else if (averageScore >= 7) {
        feedback += "Good job! You're on the right track. You might want to review some key concepts to solidify your understanding.";
      } else {
        feedback += "It looks like you may need to focus more on this topic. Reviewing the study materials and practicing with quizzes can help improve your scores.";
      }

      feedback += " Don't forget to refer to your study materials to boost your knowledge!";

      return feedback;
    },
  },
};
</script>

<style scoped>
/* Styles for the motivational message */
.motivational-message {
  font-size: 1.2em;
  color: #f0f0f0;
  margin-bottom: 20px;
}

/* Layout: table on left, charts on right */
.progress-section {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

/* Table styling */
.table-container {
  width: 45%;
}

.score-table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
  font-size: 18px;
  text-align: left;
  color: white;
}

.score-table th,
.score-table td {
  padding: 12px;
  border: 1px solid #ffffff;
}

.score-table th {
  background-color: #413d3d;
}

.score-table tr:nth-child(even) {
  background-color: #444343;
}

/* Charts styling */
.charts-container {
  width: 50%;
}

.chart-container {
  margin-bottom: 40px;
}

.feedback {
  margin-top: 10px;
  color: white;
}
</style>
