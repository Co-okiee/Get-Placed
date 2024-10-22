<template>
  <div>
    <h1>Aptitude Quiz</h1>
    <!-- Aptitude Button -->
    <button @click="fetchAptitudeQuestions">Aptitude</button>

    <!-- Display Questions -->
    <div v-if="questions.length > 0">
      <h2>Questions</h2>
      <ul>
        <li v-for="(question, index) in questions" :key="index">
          {{ question.question }}
        </li>
      </ul>
    </div>

    <div v-else>
      <p>No questions available. Click on "Aptitude" to fetch.</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      questions: [], // Store fetched questions
    };
  },
  methods: {
  async fetchAptitudeQuestions() {
    try {
      // Call Flask backend to get questions
      const response = await fetch('http://localhost:5000/api/aptitude-questions');  // Change the URL if needed

      if (!response.ok) {
        throw new Error('Error fetching questions');
      }

      const data = await response.json();
      this.questions = data.questions;  // Adjust based on response structure
    } catch (error) {
      console.error('Failed to fetch questions:', error);
    }
  },

  },
};
</script>

<style scoped>
button {
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}

ul {
  list-style-type: none;
}

li {
  background: #f9f9f9;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
</style>
