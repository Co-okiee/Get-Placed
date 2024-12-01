<template>
  <div class="topic-container">
    <div class="navigation-header">
      <button @click="goBack" class="back-button">
        <span class="back-icon">←</span>
        Back to Topics
      </button>
    </div>

    <h1 class="page-title">
      Data Structures
      <span class="title-accent">Preparation</span>
    </h1>
    <p class="subtitle">Select a data structure topic to explore in detail</p>

    <div class="topics-grid">
      <!-- Arrays -->
      <div class="topic-card" @click="navigateTo('arrays')">
        <div class="card-icon">🔢</div>
        <h3>Arrays</h3>
        <p>Fundamentals of Arrays</p>
      </div>

      <!-- Matrix -->
      <div class="topic-card" @click="navigateTo('matrix')">
        <div class="card-icon">🧮</div>
        <h3>Matrix</h3>
        <p>Matrix Operations and Types</p>
      </div>

      <!-- Strings -->
      <div class="topic-card" @click="navigateTo('strings')">
        <div class="card-icon">🔤</div>
        <h3>Strings</h3>
        <p>Working with Strings</p>
      </div>

      <!-- Linked Lists -->
      <div class="topic-card" @click="navigateTo('linkedlists')">
        <div class="card-icon">🔗</div>
        <h3>Linked Lists</h3>
        <p>Singly, Doubly, and Circular Linked Lists</p>
      </div>

      <!-- Stack -->
      <div class="topic-card" @click="navigateTo('stack')">
        <div class="card-icon">📚</div>
        <h3>Stack</h3>
        <p>Stack Operations and Applications</p>
      </div>

      <!-- Queue -->
      <div class="topic-card" @click="navigateTo('queue')">
        <div class="card-icon">🚶‍♂️</div>
        <h3>Queue</h3>
        <p>Queue Implementation</p>
      </div>

      <!-- Trees -->
      <div class="topic-card" @click="navigateTo('tree')">
        <div class="card-icon">🌳</div>
        <h3>Trees</h3>
        <p>Binary Trees, AVL Trees, and More</p>
      </div>

      <!-- Heap -->
      <div class="topic-card" @click="navigateTo('heap')">
        <div class="card-icon">🏔️</div>
        <h3>Heap</h3>
        <p>Max and Min Heap</p>
      </div>

      <!-- Hashing -->
      <div class="topic-card" @click="navigateTo('hashing')">
        <div class="card-icon">🔑</div>
        <h3>Hashing</h3>
        <p>Hash Functions and Collisions</p>
      </div>

      <!-- Graph -->
      <div class="topic-card" @click="navigateTo('graph')">
        <div class="card-icon">📊</div>
        <h3>Graph</h3>
        <p>Graph Representation and Algorithms</p>
      </div>

      <!-- Set -->
      <div class="topic-card" @click="navigateTo('set')">
        <div class="card-icon">🔢</div>
        <h3>Set Data Structure</h3>
        <p>Set Operations and Implementation</p>
      </div>

      <!-- Map -->
      <div class="topic-card" @click="navigateTo('map')">
        <div class="card-icon">🗺️</div>
        <h3>Map Data Structure</h3>
        <p>HashMap and TreeMap</p>
      </div>

      <!-- Advanced Data Structures -->
      <div class="topic-card" @click="navigateTo('ADS')">
        <div class="card-icon">🚀</div>
        <h3>Advanced Data Structures</h3>
        <p>Segment Tree, Trie, and More</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "DataStructures",
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
