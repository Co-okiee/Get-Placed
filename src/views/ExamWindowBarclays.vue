<template>
  <div class="exam-window-container">
    <iframe :src="htmlFilePath" frameborder="0" class="exam-iframe"></iframe>
  </div>
</template>

<script>
export default {
  data() {
    return {
      htmlFilePath: '/src/views/ExamWindowBarclays.html' // Path to your HTML file (relative path from the public directory)
    };
  }
};
</script>

<style scoped>
.exam-window-container {
  width: 88vw;  /* Full viewport width */
  height: 100vh; /* Full viewport height */
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0;    /* Ensure no extra padding is limiting the space */
}


.exam-iframe {
  width: 90%;
  height: 90%;  /* Adjust iframe height to fit within the container */
  border: none;
}


body, html {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
}

</style>
