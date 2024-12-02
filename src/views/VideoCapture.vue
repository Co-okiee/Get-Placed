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
      <h2>Interview Questions & Correct Answers</h2>
      <p v-if="loadingQuestions" class="loading">Loading questions...</p>
      <ul v-if="!loadingQuestions">
        <li v-for="(item, index) in questions" :key="index" class="question">
          <strong>Q{{ index + 1 }}: {{ item.question }}</strong>
          <p v-if="item.showAnswer"><strong>Correct Answer:</strong> {{ item.answer }}</p>
          <p v-else class="hidden-answer">The correct answer will appear after recording stops.</p>
        </li>
      </ul>
      <p v-if="!loadingQuestions && questions.length === 0" class="no-questions">
        No questions available.
      </p>
    </div>

    <div id="transcription" class="transcription-section">
      <h2>Live Transcription</h2>
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
      transcription: "",
      recognition: null,
      loadingQuestions: false,
    };
  },
  mounted() {
    this.generateQuestions();
  },
  methods: {
    generateQuestions() {
      // Add questions with correct answers
      this.questions = [
        {
          question: "What is event bubbling in JavaScript?",
          answer: "Event bubbling is a mechanism where an event propagates from the innermost element to the outer elements in the DOM.",
          showAnswer: false,
        },
        {
          question: "What is the purpose of closures in JavaScript?",
          answer: "Closures allow functions to access variables from their outer scope, even after the outer function has returned.",
          showAnswer: false,
        },
        {
          question: "What are React hooks?",
          answer: "React hooks are functions that let you use state and other React features without writing a class.",
          showAnswer: false,
        },
        {
          question: "What is Python's GIL (Global Interpreter Lock)?",
          answer: "GIL is a mutex in CPython that prevents multiple threads from executing Python bytecode at once.",
          showAnswer: false,
        },
        {
          question: "What is the difference between inline and block elements in HTML?",
          answer: "Inline elements do not start on a new line and take up only as much width as necessary, whereas block elements start on a new line and take up the full width.",
          showAnswer: false,
        },
      ];
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

          // Display correct answers
          this.showCorrectAnswers();
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
          transcript += event.results[i][0].transcript + " ";
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
    showCorrectAnswers() {
      // Set showAnswer to true for all questions
      this.questions.forEach((item) => {
        item.showAnswer = true;
      });
    },
  },
};
</script>

<style scoped>
/* Styling remains the same */
</style>