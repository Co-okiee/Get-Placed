<template>
  <div class="coding-ide-container">
    <div class="nav-header">
      <button @click="goBack" class="back-button">
        <span class="back-icon">←</span>
        Back to Barclays
      </button>
    </div>

    <h1 class="title">Coding IDE</h1>
    <p class="description">This is where you can write and test your code!</p>

    <!-- Problem Description Row -->
    <div class="problem-description">
      <p>{{ currentQuestion?.description }}</p>
    </div>

    <!-- Language Dropdown and Run Code Button Row -->
    <div class="controls">
      <select v-model="selectedLanguage" class="language-select">
        <option value="cpp">C++</option>
        <option value="python3">Python</option>
        <option value="java">Java</option>
        <option value="c">C</option>
        <option value="javascript">Javascript</option>
      </select>
      <button @click="runCode" class="run-button">Run Code</button>
      <button @click="resetCode" class="reset-button">Reset</button>
    </div>

    <!-- Coding Area with Input/Output -->
    <div class="code-container">
      <div
        contenteditable="true"
        @input="updateCode"
        @keydown="handleEnter"
        @focus="clearPlaceholder"
        class="code-input"
        ref="codeInput"
      ></div>
      <div class="io-container">
        <!-- Input Area -->
        <h3>Input</h3>
        <div>
          <textarea
            v-model="inputText"
            rows="5"
            placeholder="Enter input for the program..."
            class="input-text"
          ></textarea>
        </div>

        <!-- Output Area -->
        <h3>Output</h3>
        <div class="output-text">{{ outputText }}</div>
      </div>
    </div>

    <!-- Test case section -->
    <h3>Test Cases</h3>
    <div class="test-case-container">
      <div v-for="(test, index) in testCases" :key="index" class="test-case">
        <p><strong>Test Case {{ index + 1 }}:</strong> {{ test.input }}</p>
        <p><strong>Expected Output:</strong> {{ test.output }}</p>
        <p><strong>Explanation:</strong> {{ test.explanation }}</p>
      </div>
    </div>

    <!-- Hidden Test Cases Section -->
    <h3>Hidden Test Cases Results</h3>
    <div v-if="hiddenTestResults.length > 0" class="hidden-test-results">
      <p>You passed {{ passedHiddenTests }} out of {{ hiddenTestCases.length }} hidden test cases.</p>
    </div>

    <!-- Navigation buttons -->
    <div class="navigation-buttons">
      <button @click="prevQuestion" :disabled="currentQuestionIndex === 0">Back</button>
      <button @click="nextQuestion" :disabled="currentQuestionIndex === questions.length - 1">Next</button>
    </div>
  </div>
</template>

<script>
import hljs from 'highlight.js';
import 'highlight.js/styles/atom-one-dark.css';

export default {
  data() {
    return {
      code: '',
      outputText: '',
      inputText: '',
      selectedLanguage: 'cpp',
      currentQuestionIndex: 0,
      questions: [],
      testCases: [
        { input: '3 5', output: '8', explanation: 'Sum of 3 and 5 is 8' },
        { input: '2 4', output: '6', explanation: 'Sum of 2 and 4 is 6' },
      ],
      hiddenTestCases: [],
      hiddenTestResults: [],
      passedHiddenTests: 0,
    };
  },
  mounted() {
    this.fetchQuestions();
  },
  computed: {
    currentQuestion() {
      return this.questions[this.currentQuestionIndex];
    },
  },
  methods: {
    handleEnter(event) {
      if (event.key === "Enter") {
        event.preventDefault();
        const newLine = document.createElement('div');
        newLine.innerHTML = '<br>';
        const selection = window.getSelection();
        const range = selection.getRangeAt(0);
        range.insertNode(newLine);
        range.setStartAfter(newLine);
        range.setEndAfter(newLine);
        selection.removeAllRanges();
        selection.addRange(range);
      }
    },
    updateCode() {
      this.code = this.$refs.codeInput.innerText;
      this.highlightCode();
    },
    highlightCode() {
      this.$nextTick(() => {
        const highlightedCode = hljs.highlight(this.code, { language: this.selectedLanguage }).value;
        this.$refs.codeInput.innerHTML = highlightedCode;
        this.$refs.codeInput.contentEditable = true;
        this.moveCursorToEnd();
      });
    },
    moveCursorToEnd() {
      const range = document.createRange();
      const selection = window.getSelection();
      range.selectNodeContents(this.$refs.codeInput);
      range.collapse(false);
      selection.removeAllRanges();
      selection.addRange(range);
    },
    runCode() {
      const proxyUrl = 'https://thingproxy.freeboard.io/fetch/';
      const apiUrl = 'https://api.jdoodle.com/v1/execute';

      const hiddenTestResults = [];
      const hiddenTestPromises = this.hiddenTestCases.map((testCase) => {
        return fetch(proxyUrl + apiUrl, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            script: this.code,
            stdin: testCase.input,
            language: this.selectedLanguage,
            versionIndex: '0',
            clientId: 'd54b258a994b2fc5c9255013d02df2ad',
            clientSecret: 'db7d1b949affeee03302f5b5ca34c6c4c21eecc4ca325e7b7d16824b9942edc8',
          }),
        })
        .then((response) => response.json())
        .then((data) => {
          const actualOutput = (data.output || data.error).trim().toUpperCase();
          const expectedOutput = testCase.output.trim().toUpperCase();

          hiddenTestResults.push({
            input: testCase.input,
            expected: testCase.output,
            actual: actualOutput,
            passed: actualOutput === expectedOutput,
          });
        })
        .catch((error) => {
          console.error('Error:', error);
        });
      });

      Promise.all(hiddenTestPromises).then(() => {
        this.hiddenTestResults = hiddenTestResults;
        this.passedHiddenTests = hiddenTestResults.filter(result => result.passed).length;
      });
    },

    resetCode() {
      this.code = '';
      this.inputText = '';
      this.outputText = '';
      this.$refs.codeInput.innerHTML = '';
      this.hiddenTestResults = [];
      this.passedHiddenTests = 0;
    },
    fetchQuestions() {
      const sheetId = '16X5oZJX8A96_hIh9O4s5y5CaIH2fe7bZx-q4MUyXbes';
      const apiKey = 'AIzaSyCYXovziLbm9LXRdj3Q6rQt8Yuq5GSeyfk';
      const range = 'Sheet1!A2:Z10';

      fetch(`https://sheets.googleapis.com/v4/spreadsheets/${sheetId}/values/${range}?key=${apiKey}`)
        .then(response => response.json())
        .then(data => {
          this.questions = data.values.map((row, index) => ({
            id: index + 1,
            title: row[1],
            description: row[2],
            testCases: [
              { input: row[3], output: row[4], explanation: row[5] },
              { input: row[6], output: row[7], explanation: row[8] },
            ],
            hiddenTestCases: [
              { input: row[9], output: row[10] },
              { input: row[11], output: row[12] },
              { input: row[13], output: row[14] },
              { input: row[15], output: row[16] },
              { input: row[17], output: row[18] },
            ],
          }));
          this.updateTestCases();
        })
        .catch(error => console.error('Error fetching Google Sheets:', error));
    },
    updateTestCases() {
      if (this.currentQuestion) {
        this.testCases = this.currentQuestion.testCases;
        this.hiddenTestCases = this.currentQuestion.hiddenTestCases;
      }
    },
    nextQuestion() {
      if (this.currentQuestionIndex < this.questions.length - 1) {
        this.currentQuestionIndex++;
        this.updateTestCases();
      }
    },
    prevQuestion() {
      if (this.currentQuestionIndex > 0) {
        this.currentQuestionIndex--;
        this.updateTestCases();
      }
    },
    clearPlaceholder() {
      if (this.$refs.codeInput.innerHTML === '') {
        this.$refs.codeInput.innerHTML = '// Write your code here...';
      }
    },
    goBack() {
      this.$router.push({ name: "barclays-landing" }); // Ensure the name matches the landing page
    },
  },
};
</script>

<style scoped>
.coding-ide-container {
  min-height: 100vh;
  background: linear-gradient(135deg, #000000 0%, #393939 100%);
  color: #d6d7d7;
  padding: 2rem;
  text-align: left;
}

.title, .description{
  text-align: center;
}

.nav-header {
  margin-bottom: 1rem;
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

.title {
  font-size: 3rem;
  font-weight: bold;
  margin: 1rem 0;
}

.description {
  font-size: 1.25rem;
  margin-bottom: 2rem;
}

.problem-description{
  padding:10px;
}

.code-container {
  display: flex;
  flex-direction: row;
  align-items: space-between;
  padding: 20px;
}

.code-input {
  width: 65%;
  height: 300px;
  background-color: #282c34;
  border: 1px solid #ddd;
  padding: 10px;
  overflow-y: auto;
  white-space: pre-wrap;
  color: white;
  font-family: 'Courier New', Courier, monospace;
}

.io-container {
  padding: 15px;
  height: 300px;
  width: 30%;
}

.input-text {
  background-color: #282c34;
  width: 100%;
  margin-bottom: 10px;
  padding: 10px;
  overflow-y: auto;
  color: #ddd;
}

.output-text {
  background-color: #282c34;
  padding: 10px;
  height: 100px;
  margin-bottom: 10px;
  color: #ddd;
  overflow-y: auto;
}

.controls {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;
  margin-bottom: 2rem;
}

.language-select {
  padding: 0.5rem;
  font-size: 1rem;
  border-radius: 4px;
  border: 1px solid #e2e8f0;
}

.run-button,
.reset-button {
  padding: 0.5rem 1rem;
  background: #1e293b;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.run-button:hover,
.reset-button:hover {
  background: #3b475b;
}

.test-case-container {
  background: #1e293b;
  color: white;
  border-radius: 8px;
  padding: 1rem;
  margin-bottom: 1rem;
}

.test-case {
  padding: 1rem;
  background: #2b3749;
  border-radius: 8px;
  margin-bottom: 0.5rem;
}

.hidden-test-results {
  background: #2b3749;
  padding: 1rem;
  border-radius: 8px;
}

.navigation-buttons {
  display: flex;
  justify-content: space-between;
  width: 100%;
  margin-top: 1rem;
}

.navigation-buttons button {
  background: #1e293b;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
}

.navigation-buttons button:disabled {
  background: #3b475b;
  cursor: not-allowed;
}
</style>
