<template>
  <div class="dashboard">
    <!-- Header Section (unchanged) -->
    <header class="header">
      <div class="header-left">
        <h1 class="header-title">Get Placed</h1>
      </div>
      <nav class="header-nav">
        <template v-if="name">
          <div class="user-section">
            <div class="user-avatar">{{ name[0].toUpperCase() }}</div>
            <span class="username">{{ name }}</span>
            <button @click="logout" class="logout-btn">
              Sign out
            </button>
          </div>
        </template>
        <template v-else>
          <router-link to="/login" class="nav-link">Sign in</router-link>
          <router-link to="/signup" class="nav-link primary">Get started</router-link>
        </template>
      </nav>
    </header>

    <!-- Main Content -->
    <main class="main-content">
      <!-- Hero Section -->
      <section class="hero">
        <div class="hero-content">
          <h2 class="hero-title">Everything you need to succeed</h2>
          <p class="hero-text">
            Take control of your career preparation with our comprehensive tools for studying, 
            testing, progress tracking, and interview practice.
          </p>
          <div class="hero-buttons">
            <button @click="goToStudy" class="btn-primary">Get Started</button>
            <button @click="goToQuiz" class="btn-secondary">Try Quiz</button>
          </div>
        </div>
        <div class="image-gallery">
          <div v-if="isLoading" class="loading-overlay">
            <div class="loading-spinner"></div>
          </div>
          <div class="gallery-grid">
            <div 
              v-for="(image, index) in images" 
              :key="index"
              class="gallery-item"
              :class="{ 'gallery-item-large': index === 0 }"
            >
              <img 
                :src="image.url" 
                :alt="image.alt"
                @load="handleImageLoad"
                class="gallery-image"
              />
              <div class="image-credit">
                Photo by <a :href="image.photographerUrl" target="_blank">{{ image.photographer }}</a>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Features Grid (unchanged) -->
      <section class="features">
        <div class="feature-card" @click="goToStudy">
          <div class="feature-icon">📚</div>
          <h3>Study Materials</h3>
          <p>Access comprehensive study resources</p>
        </div>
        <div class="feature-card" @click="goToQuiz">
          <div class="feature-icon">✍️</div>
          <h3>Practice Quiz</h3>
          <p>Test your knowledge</p>
        </div>
        <div class="feature-card" @click="goToTrackProgress">
          <div class="feature-icon">📊</div>
          <h3>Progress Tracking</h3>
          <p>Monitor your improvement</p>
        </div>
        <div class="feature-card" @click="goToMockInterview">
          <div class="feature-icon">🎯</div>
          <h3>Mock Interview</h3>
          <p>Prepare for real interviews</p>
        </div>
      </section>
    </main>
  </div>
</template>

<script>
const UNSPLASH_ACCESS_KEY = '2AJMrapqFME1cYRh2b4a4E6K4GZrr9Cq67VkT7sGh3A'; // Replace with your Unsplash API key

export default {
  name: "Dashboard",
  data() {
    return {
      username: null,
      name: null,
      images: [],
      isLoading: true,
      loadedImages: 0
    };
  },
  mounted() {
    this.username = localStorage.getItem('username');
    this.name = localStorage.getItem('name');
    this.fetchImages();
  },
  methods: {
    async fetchImages() {
      try {
        const response = await fetch(
          `https://api.unsplash.com/search/photos?query=study+education+learning&per_page=5&orientation=landscape`,
          {
            headers: {
              Authorization: `Client-ID ${UNSPLASH_ACCESS_KEY}`
            }
          }
        );
        const data = await response.json();
        
        this.images = data.results.map(image => ({
          url: image.urls.regular,
          alt: image.alt_description || 'Educational image',
          photographer: image.user.name,
          photographerUrl: image.user.links.html
        }));
      } catch (error) {
        console.error('Error fetching images:', error);
        // Fallback images in case of API error
        this.images = Array(5).fill({
          url: '@/assets/study1.jpg',
          alt: 'Study Banner',
          photographer: 'Local Asset',
          photographerUrl: '#'
        });
      }
    },
    handleImageLoad() {
      this.loadedImages++;
      if (this.loadedImages === this.images.length) {
        this.isLoading = false;
      }
    },
    goToQuiz() {
      this.$router.push({ name: "quiz-options" });
    },
    goToStudy() {
      this.$router.push({ name: "study" });
    },
    goToTrackProgress() {
      this.$router.push({ name: "trackprogress" });
    },
    goToMockInterview() {
      this.$router.push({ name: "mockInterview" });
    },
    logout() {
      localStorage.removeItem('username');
      localStorage.removeItem('name');
      this.username = null;
      this.name = null;
      this.$router.push('/login');
    }
  }
};
</script>

<style scoped>
.dashboard {
  font-family: 'Atlas Grotesk', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  color: #fffefe;
  background-color: #000000;
  min-height: 100vh;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 24px;
  border-bottom: 1px solid #424242;
  background-color: #000000;
}

.header-title {
  font-size: 24px;
  font-weight: 500;
  color: #fcfcfc;
}

.header-nav {
  display: flex;
  align-items: center;
  gap: 16px;
}

.nav-link {
  text-decoration: none;
  color: #e9e3e3;
  padding: 8px 16px;
  border-radius: 4px;
  font-weight: 500;
}

.nav-link.primary {
  background-color: #0061fe;
  color: rgb(255, 255, 255);
}

.user-section {
  display: flex;
  align-items: center;
  gap: 12px;
}

.user-avatar {
  width: 32px;
  height: 32px;
  background-color: #fe6600;
  color: rgb(255, 255, 255);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 500;
}

.logout-btn {
  background: none;
  border: none;
  color: #ffe30f;
  cursor: pointer;
  padding: 8px 16px;
  font-weight: 500;
}

.main-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 24px;
}

.hero {
  display: flex;
  align-items: center;
  gap: 48px;
  margin-bottom: 64px;
}

.hero-content {
  flex: 1;
}

.hero-title {
  font-size: 48px;
  font-weight: 700;
  margin-bottom: 24px;
  line-height: 1.2;
  color: #bcbcbc;
}

.hero-text {
  font-size: 20px;
  line-height: 1.6;
  color: #80a4c5;
  margin-bottom: 32px;
}

.hero-image {
  flex: 1;
}

.hero-image img {
  width: 100%;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.hero-buttons {
  display: flex;
  gap: 16px;
}

.btn-primary, .btn-secondary {
  padding: 12px 24px;
  border-radius: 4px;
  font-weight: 500;
  font-size: 16px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-primary {
  background-color: #969696;
  color: white;
  border: none;
}

.btn-secondary {
  background-color: white;
  color: #000000;
  border: 1px solid #f1fe00;
}

.features {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 24px;
  margin-top: 48px;
}

.feature-card {
  background-color: #e4e2e2;
  padding: 24px;
  border-radius: 8px;
  border: 1px solid #e6e8eb;
  cursor: pointer;
  transition: all 0.2s ease;
}

.feature-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.feature-icon {
  font-size: 32px;
  margin-bottom: 16px;
}

.feature-card h3 {
  font-size: 20px;
  font-weight: 500;
  margin-bottom: 8px;
  color: #1e1919;
}

.feature-card p {
  color: #637381;
  line-height: 1.5;
}
.image-gallery {
  flex: 1;
  position: relative;
  min-height: 400px;
}

.loading-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(255, 255, 255, 0.9);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10;
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #f3f3f3;
  border-top: 4px solid #0061fe;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.gallery-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: repeat(3, 1fr);
  gap: 16px;
  height: 100%;
  min-height: 400px;
}

.gallery-item {
  position: relative;
  overflow: hidden;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.gallery-item-large {
  grid-column: span 2;
  grid-row: span 2;
}

.gallery-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.gallery-item:hover .gallery-image {
  transform: scale(1.05);
}

.image-credit {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: rgba(0, 0, 0, 0.7);
  color: white;
  padding: 8px;
  font-size: 12px;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.gallery-item:hover .image-credit {
  opacity: 1;
}

.image-credit a {
  color: white;
  text-decoration: none;
  font-weight: 500;
}

.image-credit a:hover {
  text-decoration: underline;
}
  

@media (max-width: 768px) {
  .hero {
    flex-direction: column;
  }

  .hero-title {
    font-size: 36px;
  }

  .hero-text {
    font-size: 18px;
  }

  .features {
    grid-template-columns: 1fr;
  }
  .gallery-grid {
    grid-template-columns: 1fr;
    grid-template-rows: repeat(5, 200px);
  }

  .gallery-item-large {
    grid-column: 1;
    grid-row: span 1;
  }
}
</style>