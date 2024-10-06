<template>
  <div>
    <h1>Track Progress</h1>
    <button @click="saveScore">Save Score</button>
    <div v-if="message">{{ message }}</div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      score: 0, // Assume you have a way to set this score
      userId: '', // You should set this to the current user's ID
      topic: 'Arrays', // Example topic, this should match your quiz topic
      message: '',
    };
  },
  methods: {
    async saveScore() {
      try {
        const response = await axios.post('http://localhost:5000/save-score', {
          score: this.score,
          user_id: this.userId,
          topic: this.topic,
        });
        this.message = response.data.message;
      } catch (error) {
        console.error('Error saving score:', error.response.data.error);
        this.message = error.response.data.error || 'An error occurred while saving the score.';
      }
    },
  },
};
</script>

<style scoped>
/* Add your styles here */
</style>
