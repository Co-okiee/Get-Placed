<template>
  <div class="main-container">
    <!-- Sidebar -->
    <div class="sidebar">
      <router-link to="/automata" class="exam-link">
        <button class="sidebar-button">
          Automata
        </button>
      </router-link>
    </div>

    <!-- Main Content Area -->
    <div class="content-container">
      <iframe :src="htmlFilePath" frameborder="0" class="exam-iframe"></iframe>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      htmlFilePath: '/src/views/ExamWindowBarclays.html',
    };
  },
};
</script>

<style scoped>
/* Main container to hold both sidebar and content */
.main-container {
  display: flex;
  height: 100vh;
  width: 100vw;
}

/* Sidebar styling */
.sidebar {
  width: 15%; /* Adjust width as per design */
  background-color: #1e1e1e; /* Sidebar background */
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1rem;
}

/* Sidebar button styling */
.sidebar-button {
  width: 100%;
  padding: 1rem;
  margin-bottom: 1rem;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  text-align: center;
  font-weight: bold;
}

.sidebar-button:hover {
  background-color: #45a049;
}

/* Content area styling */
.content-container {
  flex-grow: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f9f9f9;
}

/* iFrame styling */
.exam-iframe {
  width: 90%;
  height: 90%;
  border: none;
}
</style>
