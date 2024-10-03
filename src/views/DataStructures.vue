<!-- src/views/DataStructures.vue -->
<template>
  <div class="topic">
    <h1>Data Structures</h1>
    <p>Content and resources for preparing Data Structures...</p>
    <div class="button-container">
      <button @click="navigateTo('Arrays')">Arrays</button>
      <button @click="navigateTo('Matrix')">Matrix</button>
      <button @click="navigateTo('Strings')">Strings</button>
      <button @click="navigateTo('LinkedLists')">Linked Lists</button>
      <button @click="navigateTo('Stack')">Stack</button>
      <button @click="navigateTo('Queue')">Queue</button>
      <button @click="navigateTo('Trees')">Trees</button>
      <button @click="navigateTo('Heap')">Heap</button>
      <button @click="navigateTo('Hashing')">Hashing</button>
      <button @click="navigateTo('Graph')">Graph</button>
      <button @click="navigateTo('Set')">Set Data Structure</button>
      <button @click="navigateTo('Map')">Map Data Structure</button>
      <button @click="navigateTo('Advanced')">Advanced Data Structures</button>
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
