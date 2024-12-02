<template>
  <div class="topic-container">
    <div class="navigation-header">
      <button @click="goBack" class="back-button">
        <span class="back-icon">←</span>
        Back to Topics
      </button>
    </div>

    <h1 class="page-title">
      Algorithms
      <span class="title-accent">Introduction</span>
    </h1>
    <p class="subtitle">Explore various algorithm types in depth</p>

    <div class="topics-grid">
      <!-- Analysis of Algorithms -->
      <div class="topic-card" @click="navigateTo('analysisofalgo')">
        <div class="card-icon">📊</div>
        <h3>Analysis of Algorithms</h3>
        <p>Big-O, time and space complexity</p>
      </div>

      <!-- Searching Algorithms -->
      <div class="topic-card" @click="navigateTo('searching')">
        <div class="card-icon">🔍</div>
        <h3>Searching Algorithms</h3>
        <p>Linear, Binary Search, etc.</p>
      </div>

      <!-- Sorting Algorithms -->
      <div class="topic-card" @click="navigateTo('sorting')">
        <div class="card-icon">🗂️</div>
        <h3>Sorting Algorithms</h3>
        <p>Quick Sort, Merge Sort, etc.</p>
      </div>

      <!-- Greedy Algorithms -->
      <div class="topic-card" @click="navigateTo('greedy')">
        <div class="card-icon">💰</div>
        <h3>Greedy Algorithms</h3>
        <p>Optimal solutions for subproblems</p>
      </div>

      <!-- Dynamic Programming -->
      <div class="topic-card" @click="navigateTo('dynamic')">
        <div class="card-icon">🔄</div>
        <h3>Dynamic Programming</h3>
        <p>Overlapping subproblems, memoization</p>
      </div>

      <!-- Graph Algorithms -->
      <div class="topic-card" @click="navigateTo('graphalgo')">
        <div class="card-icon">📈</div>
        <h3>Graph Algorithms</h3>
        <p>BFS, DFS, Dijkstra’s Algorithm</p>
      </div>

      <!-- Pattern Searching -->
      <div class="topic-card" @click="navigateTo('pattern')">
        <div class="card-icon">🔎</div>
        <h3>Pattern Searching</h3>
        <p>KMP, Rabin-Karp, and others</p>
      </div>

      <!-- Recursion -->
      <div class="topic-card" @click="navigateTo('recursion')">
        <div class="card-icon">♾️</div>
        <h3>Recursion</h3>
        <p>Recursion techniques and examples</p>
      </div>

      <!-- Backtracking -->
      <div class="topic-card" @click="navigateTo('backtracking')">
        <div class="card-icon">↩️</div>
        <h3>Backtracking</h3>
        <p>Solving constraint satisfaction problems</p>
      </div>

      <!-- Divide and Conquer -->
      <div class="topic-card" @click="navigateTo('divide-and-conquer')">
        <div class="card-icon">✂️</div>
        <h3>Divide and Conquer</h3>
        <p>Divide problem into subproblems</p>
      </div>

      <!-- Mathematical Algorithms -->
      <div class="topic-card" @click="navigateTo('mathematical-algo')">
        <div class="card-icon">➕</div>
        <h3>Mathematical Algorithms</h3>
        <p>Number theory, combinatorics</p>
      </div>

      <!-- Geometric Algorithms -->
      <div class="topic-card" @click="navigateTo('geometric')">
        <div class="card-icon">📐</div>
        <h3>Geometric Algorithms</h3>
        <p>Convex hull, line intersection</p>
      </div>

      <!-- Bitwise Algorithms -->
      <div class="topic-card" @click="navigateTo('bitwise')">
        <div class="card-icon">🔢</div>
        <h3>Bitwise Algorithms</h3>
        <p>Manipulating bits for efficiency</p>
      </div>

      <!-- Randomized Algorithms -->
      <div class="topic-card" @click="navigateTo('randomised')">
        <div class="card-icon">🎲</div>
        <h3>Randomised Algorithms</h3>
        <p>Monte Carlo, Las Vegas algorithms</p>
      </div>

      <!-- Branch and Bound -->
      <div class="topic-card" @click="navigateTo('branchbound')">
        <div class="card-icon">🔗</div>
        <h3>Branch and Bound</h3>
        <p>Optimization algorithms</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Algorithms",
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
