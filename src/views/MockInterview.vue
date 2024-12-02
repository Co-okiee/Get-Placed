<template>
  <div class="mock-interview">
    <h1>Mock Interview</h1>
    <p>Simulate real interviews to prepare for placement opportunities.</p>

    <!-- Upload Form -->
    <form @submit.prevent="uploadResume" class="upload-form">
      <label for="resume">Upload Your Resume (PDF/DOCX):</label>
      <input type="file" id="resume" ref="resume" />
      <button type="submit">Upload</button>
    </form>

    <!-- Display Questions -->
    <div v-if="questions.length > 0" class="questions-section">
      <h2>Generated Questions</h2>
      <ul>
        <li v-for="(question, index) in questions" :key="index">{{ question }}</li>
      </ul>
    </div>

    <!-- Video Capture -->
    <div v-if="questions.length > 0" class="video-section">
      <h2>Record Your Response</h2>
      <video id="video" autoplay></video>
      <button @click="startCamera">Start Camera</button>
      <button @click="startRecording" :disabled="!cameraActive">Start Recording</button>
      <button @click="stopRecording" :disabled="!recording">Stop Recording</button>

      <h2>Playback</h2>
      <video id="playback" controls></video>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      questions: [], // List of generated questions
      cameraActive: false,
      recording: false,
      stream: null,
      mediaRecorder: null,
      recordedChunks: [],
    };
  },
  methods: {
    async uploadResume() {
      const fileInput = this.$refs.resume;
      if (!fileInput.files.length) {
        alert("Please select a file to upload.");
        return;
      }

      const formData = new FormData();
      formData.append("resume", fileInput.files[0]);

      try {
        const response = await fetch("http://127.0.0.1:5001/upload", {
          method: "POST",
          body: formData,
        });

        if (response.redirected) {
          window.location.href = response.url; // Redirect to Flask-generated page
        } else {
          const data = await response.json();
          this.questions = data.questions || [];
        }
      } catch (error) {
        console.error("Error uploading resume:", error);
        alert("Failed to upload resume. Please try again.");
      }
    },
    async startCamera() {
      try {
        this.stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
        const video = document.getElementById("video");
        video.srcObject = this.stream;
        this.cameraActive = true;
      } catch (error) {
        alert("Unable to access camera: " + error.message);
      }
    },
    startRecording() {
      this.recordedChunks = [];
      this.mediaRecorder = new MediaRecorder(this.stream, { mimeType: "video/webm" });

      this.mediaRecorder.ondataavailable = (event) => {
        if (event.data.size > 0) {
          this.recordedChunks.push(event.data);
        }
      };

      this.mediaRecorder.start();
      this.recording = true;
    },
    stopRecording() {
      this.mediaRecorder.stop();
      this.mediaRecorder.onstop = () => {
        const videoBlob = new Blob(this.recordedChunks, { type: "video/webm" });
        const playback = document.getElementById("playback");
        playback.src = URL.createObjectURL(videoBlob);
        playback.controls = true;
        this.recording = false;
      };
    },
  },
};
</script>

<style scoped>
/* Add styles similar to your HTML templates */
</style>