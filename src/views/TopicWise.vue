<template>
  <div class="topic-wise-quiz">
    <h1>Choose Topic</h1>
    <button @click="goToArrayQuiz">Arrays</button>
    <button @click="goToMatrices">Matrices</button>
    <button @click="goToStrings">Strings</button>
    <!-- Add more topics as needed -->
  </div>
</template>

<script>
export default {
  name: "TopicWiseQuiz",
  methods: {
    goToArrayQuiz() {
      this.$router.push({ name: "array-quiz" }); // Ensure this matches the router
    },
    goToMatrices() {
      this.$router.push({ name: "matrix-quiz" }); // Ensure this matches the router
    },
    goToStrings() {
      this.$router.push({ name: "strings-quiz" }); // Ensure this matches the router
    }
  }
};
</script>

<style scoped>
.topic-wise-quiz {
  text-align: center;
  margin-top: 50px;
  color: #f2f2f2; /* Added text color for better contrast */
}

.topic-wise-quiz h1 {
  margin-bottom: 20px;
  font-size: 2.5em; /* Increased font size for the title */
  color: #ffffff; /* Changed the color to white */
}

.topic-wise-quiz button {
  margin: 10px;
  padding: 15px 30px; /* Increased padding for larger buttons */
  font-size: 18px;
  background-color: #3C3D37;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease; /* Added transform transition */
}

.topic-wise-quiz button:hover {
  background-color: #181C14;
  transform: scale(1.05); /* Slightly scale up the button on hover for effect */
}
</style>
