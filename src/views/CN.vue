<template>
  <div class="topic-container">
    <h1 class="main-title">Computer Networks</h1>
    <p class="intro">An introduction to computer networks and their various components...</p>
    
    <div class="topics-grid">
      <div class="topic-card" @click="navigateTo('CNbasics')">
        <div class="card-icon">🌐</div>
        <h3>CN Basics</h3>
      </div>

      <div class="topic-card" @click="navigateTo('datalink')">
        <div class="card-icon">🔗</div>
        <h3>Data Link Layer</h3>
      </div>

      <div class="topic-card" @click="navigateTo('network')">
        <div class="card-icon">🔐</div>
        <h3>Network Security</h3>
      </div>

      <div class="topic-card" @click="navigateTo('transport')">
        <div class="card-icon">🚚</div>
        <h3>Transport Layer</h3>
      </div>

      <div class="topic-card" @click="navigateTo('application')">
        <div class="card-icon">🛠️</div>
        <h3>Application Layer</h3>
      </div>

      <div class="topic-card" @click="navigateTo('networksecurity')">
        <div class="card-icon">📡</div>
        <h3>Network Layer</h3>
      </div>

      <div class="topic-card" @click="navigateTo('compressiontech')">
        <div class="card-icon">📉</div>
        <h3>Compression Techniques</h3>
      </div>

      <div class="topic-card" @click="navigateTo('networkexp')">
        <div class="card-icon">🧪</div>
        <h3>Network Experiments</h3>
      </div>

      <div class="topic-card" @click="navigateTo('devices')">
        <div class="card-icon">📟</div>
        <h3>Devices</h3>
      </div>

      <div class="topic-card" @click="navigateTo('CNmisc')">
        <div class="card-icon">🔍</div>
        <h3>Miscellaneous</h3>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ComputerNetworks",
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
