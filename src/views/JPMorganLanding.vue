<template>
  <div class="landing-container">
    <div class="nav-header">
      <button @click="goBack" class="back-button">
        <svg xmlns="http://www.w3.org/2000/svg" class="back-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
        </svg>
        Back to Quiz Options
      </button>
    </div>

    <div class="content-wrapper">
      <h1 class="company-title">JP Morgan Chase</h1>
      
      <div class="company-description">
        <p>JP Morgan Chase is a leading global financial services firm and one of the largest banking institutions in the United States. Known for its innovative financial solutions, cutting-edge technology, and comprehensive investment banking services.</p>
      </div>

      <div class="placement-details">
        <h2>Placement Information</h2>
        <div class="placement-grid">
          <div class="placement-item">
            <div class="placement-icon">🎓</div>
            <div class="placement-text">
              <strong>Students Hired</strong>
              <span>20-30 annually</span>
            </div>
          </div>
          <div class="placement-item">
            <div class="placement-icon">💼</div>
            <div class="placement-text">
              <strong>Average Package</strong>
              <span>₹12 - 18 LPA</span>
            </div>
          </div>
          <div class="placement-item">
            <div class="placement-icon">🏆</div>
            <div class="placement-text">
              <strong>Highest Package</strong>
              <span>₹22 - 25 LPA</span>
            </div>
          </div>
        </div>
      </div>

      <div class="resources-container">
        <div 
          v-for="resource in resources" 
          :key="resource.id" 
          class="resource-card"
          @click="navigateTo(resource.route)"
        >
          <div class="resource-icon">{{ resource.icon }}</div>
          <div class="resource-content">
            <h3>{{ resource.title }}</h3>
            <p>{{ resource.description }}</p>
          </div>
          <div class="resource-arrow">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" />
            </svg>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "JPMorganLanding",
  data() {
    return {
      resources: [
        {
          id: 1,
          icon: '💹',
          title: 'Algorithms',
          description: 'Focus on solving optimization problems',
          route: '/aialgo.html'
        },
        {
          id: 2,
          icon: '🔧',
          title: 'System Design',
          description: 'Designing scalable financial platforms',
          route: '/aisystem.html'
        },
        {
          id: 3,
          icon: '📊',
          title: 'Data Structures',
          description: 'Solve advanced problems',
          route: '/aids.html'
        },
        {
          id: 4,
          icon: '🤖',
          title: 'OOPS',
          description: 'AI applications in financial services',
          route: '/aioops.html'
        },
        {
          id: 5,
          icon: '👩‍💻',
          title: 'Coding Practice',
          description: 'Live coding environment',
          route: 'coding-ide'
        },
        {
          id: 6,
          icon: '📚',
          title: 'Mock Exam',
          description: 'Full-length practice assessment',
          route: 'mock-exam-page'
        }
      ]
    }
  },
  methods: {
    goBack() {
      this.$router.push({ name: "company-specific" });
    },
    navigateTo(routeName) {
      window.location.href = routeName;
  }
}
}
</script>

<style scoped>
.landing-container {
  min-height: 100vh;
  background: linear-gradient(135deg, #000000 0%, #121212 100%);
  padding: 2rem;
  color: #d6d7d7;
  font-family: 'Inter', sans-serif;
}

.content-wrapper {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1rem;
}

.company-title {
  font-size: 3rem;
  font-weight: bold;
  text-align: center;
  margin-bottom: 1.5rem;
  color: #ffffff;
}

.company-description {
  text-align: center;
  max-width: 800px;
  margin: 0 auto 2rem;
  font-size: 1.1rem;
  line-height: 1.6;
}

.placement-details {
  background: rgba(30, 30, 30, 0.5);
  border-radius: 12px;
  padding: 2rem;
  margin-bottom: 2rem;
}

.placement-details h2 {
  text-align: center;
  margin-bottom: 1.5rem;
  color: #ffffff;
}

.placement-grid {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
}

.placement-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex: 1;
  background: rgba(40, 40, 40, 0.5);
  padding: 1rem;
  border-radius: 8px;
}

.placement-icon {
  font-size: 2.5rem;
}

.placement-text {
  display: flex;
  flex-direction: column;
}

.placement-text strong {
  color: #ffffff;
  margin-bottom: 0.5rem;
}

.resources-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

.resource-card {
  display: flex;
  align-items: center;
  background: rgba(30, 30, 30, 0.5);
  border-radius: 12px;
  padding: 1.5rem;
  cursor: pointer;
  transition: all 0.3s ease;
  gap: 1rem;
}

.resource-card:hover {
  background: rgba(40, 40, 40, 0.7);
  transform: translateY(-5px);
}

.resource-icon {
  font-size: 2.5rem;
  background: rgba(255, 255, 255, 0.1);
  padding: 0.75rem;
  border-radius: 8px;
}

.resource-content {
  flex-grow: 1;
}

.resource-content h3 {
  color: #ffffff;
  margin-bottom: 0.5rem;
}

.resource-content p {
  color: #a0a0a0;
}

.resource-arrow {
  width: 40px;
  height: 40px;
  background: rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  color: #ffffff;
}

.back-button {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  color: #d6d7d7;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  margin-bottom: 2rem;
}

.back-button:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: translateX(-4px);
}

.back-icon {
  width: 1.2rem;
  height: 1.2rem;
}
</style>