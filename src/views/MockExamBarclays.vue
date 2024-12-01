<template>
  <div class="landing-container">
    <div class="nav-header">
      <button @click="goBack" class="back-button">
        <span class="back-icon">←</span>
        Back to Barclays
      </button>
    </div>

    <h1 class="company-title">Mock Exam for Barclays</h1>
    <p class="mock-exam-description">
      Test your knowledge and skills with our curated mock exam. This includes multiple-choice questions from topics like Data Structures, DBMS, and Operating Systems.
    </p>

    <div class="mock-exam-container">
      <p class="mock-exam-instructions">
        <strong>Instructions:</strong><br>
        - Answer all questions to the best of your ability.<br>
        - Your score and explanations for correct/incorrect answers will be displayed at the end.<br>
        - Click "Start Exam" to begin.
      </p>

      <button @click="startExam">Start Exam</button>

    </div>
  </div>
</template>

<script>
export default {
  name: "MockExamPage",
  methods: {
    goBack() {
      this.$router.push({ name: "barclays-landing" });
    },
    startExam() {
      console.log("Navigating to the Mock Exam Quiz Page...");
      // this.$router.push({ path: '/ExamWindowBarclays1' });
      window.open('/ExamWindowBarclays1.html', '_blank');
    }

  },
};
</script>

<style scoped>
.landing-container {
  min-height: 100vh;
  background: linear-gradient(135deg, #000000 0%, #393939 100%);
  padding: 2rem;
  color: #d6d7d7;
  text-align: center;
}

.company-title {
  font-size: 3rem;
  font-weight: bold;
  margin-bottom: 1rem;
}

.mock-exam-description {
  font-size: 1.25rem;
  margin-bottom: 2rem;
}

.mock-exam-instructions {
  font-size: 1rem;
  margin-bottom: 1.5rem;
}

.start-exam-button {
  background: white;
  border: 1px solid #e2e8f0;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  color: #1e293b;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}

.start-exam-button:hover {
  background: #f1f5f9;
  transform: translateY(-3px);
}

.back-button {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: white;
  border: 1px solid #e2e8f0;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  color: #1e293b;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}

.back-button:hover {
  background: #f1f5f9;
  transform: translateX(-4px);
}

.back-icon {
  font-size: 1.2rem;
}
</style>
