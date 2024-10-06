<template>
  <div class="quiz-options">
    <h1>Choose Quiz Type</h1>
    <button @click="goToVerbalquizes">Verbal Ability</button>
    <button @click="goToVerbalAbility">Company Specific Coding Questions</button>
    <button @click="goToTopicWiseQuiz">Topic Wise Quiz</button> <!-- New button -->
  </div>
</template>

<script>
export default {
  name: "QuizOptions",
  methods: {
    goToVerbalquizes() {
      this.$router.push({ name: "verbalquizes" }); // Ensure this matches the router
    },
    goToVerbalAbility() {
      console.log("Verbal Ability button clicked!"); // Debugging log
      this.$router.push({ name: "verbal-reasoning" }); // Ensure this matches the router
    },
    goToTopicWiseQuiz() {
      this.$router.push({ name: "topic-wise-quiz" }); // Ensure this matches the router
    }
  }
};
</script>

<style scoped>
.quiz-options {
  text-align: center;
  margin-top: 50px;
  color: #f2f2f2; /* Added text color for better contrast */
}

.quiz-options h1 {
  margin-bottom: 20px;
  font-size: 2.5em; /* Increased font size for the title */
  color: #ffffff; /* Changed the color to white */
}

.quiz-options button {
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

.quiz-options button:hover {
  background-color: #181C14;
  transform: scale(1.05); /* Slightly scale up the button on hover for effect */
}
</style>
