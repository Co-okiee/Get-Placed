<!-- src/views/DataStructures.vue -->
<template>
  <div class="topic">
    <h1>Data Structures</h1>
    <p>Content and resources for preparing Data Structures...</p>
    <div class="button-container">
      <button @click="navigateTo('arrays')">Arrays</button>
      <button @click="navigateTo('matrix')">Matrix</button>
      <button @click="navigateTo('strings')">Strings</button>
      <button @click="navigateTo('linkedlists')">Linked Lists</button>
      <button @click="navigateTo('stack')">Stack</button>
      <button @click="navigateTo('queue')">Queue</button>
      <button @click="navigateTo('tree')">Trees</button>
      <button @click="navigateTo('heap')">Heap</button>
      <button @click="navigateTo('hashing')">Hashing</button>
      <button @click="navigateTo('graph')">Graph</button>
      <button @click="navigateTo('set')">Set Data Structure</button>
      <button @click="navigateTo('map')">Map Data Structure</button>
      <button @click="navigateTo('ADS')">Advanced Data Structures</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "DataStructures",
  methods: {
    navigateTo(topic) {
      // Navigate to the specified topic using the router
      this.$router.push({ name: topic });
    }
  }
};
</script>

<style scoped>
.topic {
  text-align: center;
  padding: 20px;
}
.button-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px;
  margin-top: 20px;
}
button {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  border: none;
  background-color: #555b61; /* Primary button color */
  color: white; /* Text color */
  border-radius: 5px; /* Rounded corners */
  transition: background-color 0.3s; /* Smooth transition for hover effect */
}
button:hover {
  background-color: #0056b3; /* Darker color on hover */
}
</style>
