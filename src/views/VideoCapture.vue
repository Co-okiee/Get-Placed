<template>
  <div class="container">
    <div class="camera-section">
      <h1>Record Your Interview Response</h1>
      <div class="video-wrapper">
        <video id="video" autoplay></video>
      </div>
      <div class="controls">
        <button @click="startCamera" :disabled="cameraStarted">Start Camera</button>
        <button @click="startRecording" :disabled="!cameraStarted || recording">Start Recording</button>
        <button @click="stopRecording" :disabled="!recording">Stop Recording</button>
      </div>
    </div>

    <div class="playback-section">
      <h2>Playback Your Response</h2>
      <video id="playbackVideo" controls></video>
    </div>

    <div class="questions-section">
      <h2>Interview Questions</h2>
      <p v-if="loadingQuestions" class="loading">Loading questions...</p>
      <ul v-if="!loadingQuestions">
        <li v-for="question in questions" :key="question" class="question">
          {{ question }}
        </li>
      </ul>
      <p v-if="!loadingQuestions && questions.length === 0" class="no-questions">
        No questions available.
      </p>
    </div>

    <div id="transcription" class="transcription-section">
      <h2>Transcription</h2>
      <div class="transcription-box">
        <p id="transcriptionText">{{ transcription }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      cameraStarted: false,
      recording: false,
      stream: null,
      mediaRecorder: null,
      recordedChunks: [],
      questions: [],
      transcription: "Your transcription will appear here...",
      recognition: null,
      loadingQuestions: false,
    };
  },
  mounted() {
    this.generateQuestions();
  },
  methods: {
    generateQuestions() {
      const quizData = {
        javascript: [
          "What is event bubbling in JavaScript?",
          "What is the purpose of closures in JavaScript?",
        ],
        react: [
          "What are React hooks?",
          "Explain the difference between functional and class components in React.",
        ],
        html: [
          "What is the difference between inline and block elements in HTML?",
          "What are semantic HTML elements?",
        ],
        python: [
          "What is Python's GIL (Global Interpreter Lock)?",
          "How is memory managed in Python?",
        ],
      };

      const keywords = ["javascript", "react", "html", "python"]; // Example keywords
      const matchedQuestions = [];
      keywords.forEach((keyword) => {
        if (quizData[keyword]) {
          matchedQuestions.push(...quizData[keyword]);
        }
      });

      this.questions = matchedQuestions;
    },
    async startCamera() {
      try {
        this.stream = await navigator.mediaDevices.getUserMedia({
          video: true,
          audio: true,
        });
        const video = document.getElementById("video");
        video.srcObject = this.stream;
        this.cameraStarted = true;
      } catch (error) {
        alert("Error accessing the camera or microphone: " + error.message);
      }
    },
    startRecording() {
      this.recordedChunks = [];
      try {
        this.mediaRecorder = new MediaRecorder(this.stream, {
          mimeType: "video/webm",
        });
        this.mediaRecorder.ondataavailable = (event) => {
          if (event.data.size > 0) {
            this.recordedChunks.push(event.data);
          }
        };
        this.mediaRecorder.start();
        this.recording = true;

        // Start transcription when recording starts
        this.startTranscription();
      } catch (error) {
        console.error("Error starting recording:", error);
      }
    },
    stopRecording() {
      try {
        this.mediaRecorder.stop();
        this.mediaRecorder.onstop = () => {
          const recordedBlob = new Blob(this.recordedChunks, {
            type: "video/webm",
          });
          const playbackVideo = document.getElementById("playbackVideo");
          playbackVideo.src = URL.createObjectURL(recordedBlob);
          this.recording = false;

          // Stop transcription when recording stops
          this.stopTranscription();
        };
      } catch (error) {
        console.error("Error stopping recording:", error);
      }
    },
    startTranscription() {
      if (!("SpeechRecognition" in window || "webkitSpeechRecognition" in window)) {
        alert("Speech Recognition is not supported in this browser.");
        return;
      }

      this.recognition = new (window.SpeechRecognition ||
        window.webkitSpeechRecognition)();
      this.recognition.interimResults = true;
      this.recognition.continuous = true;

      this.recognition.onresult = (event) => {
        let transcript = "";
        for (let i = event.resultIndex; i < event.results.length; i++) {
          transcript += event.results[i][0].transcript;
        }
        this.transcription = transcript;
      };

      this.recognition.onerror = (event) => {
        console.error("Speech recognition error:", event.error);
        this.transcription = `Error: ${event.error}`;
      };

      this.recognition.onend = () => {
        console.log("Speech recognition ended.");
      };

      try {
        this.recognition.start();
      } catch (error) {
        console.error("Error starting transcription:", error);
      }
    },
    stopTranscription() {
      if (this.recognition) {
        this.recognition.stop();
        this.recognition = null;
      }
    },
  },
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: "Roboto", sans-serif;
  padding: 20px;
  background-color: #f9f9f9;
  min-height: 100vh;
  color: #333;
}

.camera-section,
.playback-section,
.questions-section {
  margin-bottom: 30px;
}

.video-wrapper {
  width: 90%;
  max-width: 800px;
  margin: 20px auto;
}

video {
  width: 100%;
  max-height: 400px;
  border-radius: 10px;
  border: 3px solid #007bff;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

button {
  background-color: #007bff;
  color: #fff;
  font-size: 16px;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

button:hover:enabled {
  background-color: #0056b3;
}

.transcription-section {
  width: 90%;
  max-width: 800px;
  margin: 20px auto;
  text-align: center;
}

.transcription-box {
  background: #f1f1f1;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 8px;
  text-align: left;
  min-height: 100px;
  max-height: 300px;
  overflow-y: auto;
  font-family: "Roboto", sans-serif;
  font-size: 16px;
}
</style>