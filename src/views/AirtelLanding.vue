<template>
  <div class="landing-container">
    <div class="nav-header">
      <button @click="goBack" class="back-button">
        <span class="back-icon">←</span>
        Back to Quiz Options
      </button>
    </div>

    <h1 class="company-title">Barclays</h1>
    <p class="company-description">
      Barclays is a British multinational investment bank and financial services company headquartered in London. It provides various financial services, including personal banking, corporate banking, and investment management.
    </p>
    
    <div class="resources-container">
      <button class="resource-button" @click="goToCodingTopics('topic1')">
        <div class="card-icon">🔷</div>
        <span class="resource-title">Data Structures</span>
      </button>
      <button class="resource-button" @click="goToCodingTopics('topic2')">
        <div class="card-icon">🗃️</div>
        <span class="resource-title">DBMS</span>
      </button>
      <button class="resource-button" @click="goToCodingTopics('topic3')">
        <div class="card-icon">💻</div>
        <span class="resource-title">Operating Systems</span>
      </button>
      <button class="resource-button" @click="goToCodingTopics('topic4')">
        <div class="card-icon">👩‍💻</div>
        <span class="resource-title">Coding</span>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "BarclaysLanding",
  methods: {
    goBack() {
      this.$router.push({ name: "company-specific" });
    },
    goToCodingTopics(topic) {
      console.log(`Navigating to ${topic}`);
      this.$router.push({ name: `${topic}-page` });
    },
    goToProblems() {
      console.log('Navigating to Coding Problems');
      this.$router.push({ name: 'coding-problems' });
    }
  }
};
</script>

<style scoped>
.landing-container {
  min-height: 100vh;
  background: linear-gradient(135deg, #000000 0%, #393939 100%);
  padding: 2rem;
  color: #d6d7d7;
  text-align: center;
}

.company-title {
  font-size: 3rem;
  font-weight: bold;
  margin-bottom: 1rem;
}

.company-description {
  font-size: 1.25rem;
  margin-bottom: 2rem;
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

.resources-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 2rem;
  margin-top: 2rem;
}

.resource-button {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: rgb(251, 251, 251);
  border-radius: 16px;
  padding: 1rem;
  width: 200px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.resource-title {
  color: black; /* Set text color to black */
  font-weight: 500;
  text-align: center; /* Center the text */
  flex-grow: 1; /* Allow the text to take remaining space */
}

.resource-button:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.resource-logo {
  width: 40px;
  height: 40px;
  margin-right: 1rem;
}

.resource-title {
  color: black; /* Set text color to black */
  font-weight: 500;
}

.card-icon {
  color: #1e293b;
  font-weight: 500;
  font-size: 2rem; /* Adjust size as needed */
}
</style>
