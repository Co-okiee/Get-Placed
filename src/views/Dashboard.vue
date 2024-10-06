<template>
  <div class="dashboard">
    <!-- Header Section -->
    <header class="header">
      <h1 class="header-title">Get Placed</h1>
      <nav class="header-nav">
        <template v-if="name">
          <span>Welcome, {{ name }}</span>
          <button @click="logout" class="logout-btn">Logout</button>
        </template>
        <template v-else>
          <router-link to="/login">Login</router-link>
          <router-link to="/signup">Sign Up</router-link>
        </template>
      </nav>
    </header>

    <!-- Main Banner Section -->
    <section class="banner">
      <img src="@/assets/study1.jpg" alt="Study Banner" class="banner-image" />
      <div class="banner-content">
        <h2>Prepare for Success</h2>
        <p>
          Welcome to our web app designed to help you prepare for your future career! 
          Whether you want to study, take quizzes, track your progress, or simulate mock interviews, we've got you covered.
        </p>
      </div>
    </section>

    <!-- Action Buttons Section -->
    <section class="actions">
      <button @click="goToStudy">Study</button>
      <button @click="goToQuiz">Quiz Me</button>
      <button @click="goToTrackProgress">Track Progress</button>
      <button @click="goToMockInterview">Mock Interview</button>
    </section>
  </div>
</template>

<script>
export default {
  name: "Dashboard",
  data() {
    return {
      username: null, // Store username if logged in
      name:null
    };
  },
  mounted() {
    // When the component is mounted, check if the user is logged in
    this.username = localStorage.getItem('username'); // Retrieve the username from localStorage
    this.name=localStorage.getItem('name');
  },
  methods: {
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
      localStorage.removeItem('username'); // Remove the username from localStorage
      this.username = null; // Reset the username in the component
      this.$router.push('/login'); // Redirect to the login page
    }
  }
};
</script>

<style scoped>
/* General Styles */
.dashboard {
  font-family: 'Roboto', sans-serif;
  color: #ffffff;
  background-color: #181C14;
  padding: 20px;
  min-height: 100vh;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  background-color: #3C3D37;
}

.header-title {
  font-size: 24px;
  font-weight: bold;
  color: #fff;
}

.header-nav a {
  margin-left: 15px;
  font-size: 18px;
  color: #fff;
  text-decoration: none;
}

.header-nav a:hover {
  text-decoration: underline;
}

.header-nav span {
  margin-right: 15px;
  font-size: 18px;
  color: #fff;
}

.logout-btn {
  background-color: transparent;
  color: #fff;
  border: none;
  cursor: pointer;
}

.logout-btn:hover {
  text-decoration: underline;
}

/* Banner Section */
.banner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: #3C3D37;
  padding: 40px;
  border-radius: 10px;
  margin: 20px 0;
}

.banner-image {
  width: 50%;
  border-radius: 10px;
}

.banner-content {
  max-width: 45%;
}

.banner-content h2 {
  font-size: 36px;
  margin-bottom: 10px;
}

.banner-content p {
  font-size: 18px;
  line-height: 1.6;
}

/* Action Buttons */
.actions {
  display: flex;
  justify-content: space-around;
  margin-top: 30px;
}

.actions button {
  background-color: #3C3D37;
  color: white;
  padding: 20px 30px;
  border: none;
  border-radius: 10px;
  font-size: 20px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.actions button:hover {
  background-color: #181C14;
}
</style>
