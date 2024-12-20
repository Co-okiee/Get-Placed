<template>
  <div class="searching-container">
    <h1 class="main-title">Searching Algorithms</h1>
    <p class="intro">
      Searching algorithms are used to retrieve information stored within some data structure. The goal of a search is to determine if a specific element exists within a data structure, and if it does, to locate it.
    </p>

    <h2 class="sub-title">Key Concepts in Searching Algorithms</h2>
    <ul class="characteristics-list">
      <li><strong>Linear Search:</strong> A basic search algorithm that checks every element in a list sequentially until the desired element is found.</li>
      <li><strong>Binary Search:</strong> A faster search algorithm that works on sorted arrays by repeatedly dividing the search interval in half.</li>
      <li><strong>Time Complexity:</strong> A measure of the efficiency of an algorithm, particularly how the runtime increases as the size of the input increases.</li>
      <li><strong>Space Complexity:</strong> Refers to the amount of memory the algorithm uses relative to the input size.</li>
    </ul>

    <h2 class="sub-title">Diagram for Searching Algorithm Complexity</h2>
    <img src="@/assets/searching.png" alt="Searching Algorithm Complexity Diagram" class="searching-diagram imageedit" />

    <h2 class="sub-title">Example Searching Algorithms</h2>
    <p>Select a search algorithm to see the code example:</p>
    <div class="button-container">
      <button @click="showAlgorithm('linear')" class="example-button">Linear Search</button>
      <button @click="showAlgorithm('binary')" class="example-button">Binary Search</button>
    </div>

    <pre v-if="algorithmExample">
      <code>{{ algorithmExample }}</code>
    </pre>

    <h2 class="sub-title">Generative Study Companion</h2>
    <div class="ai-notes-section">
      <button 
        @click="generateAINotes" 
        class="example-button ai-notes-button" 
        :disabled="isGenerating"
      >
        {{ isGenerating ? "Generating Study Guide..." : "Generate Study Guide" }}
      </button>

      <div v-if="aiNotesData" class="ai-notes-display">
        <h3 class="section-title">📘 Comprehensive Study Notes</h3>
        <div v-html="aiNotesData"></div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SearchingAlgorithms",
  data() {
    return {
      algorithmExample: "",
      aiNotesData: null,
      isGenerating: false,
      groqApiKey: "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"
    };
  },
  methods: {
    showAlgorithm(type) {
      if (type === 'linear') {
        this.algorithmExample = `// Example of Linear Search Algorithm
int linearSearch(int arr[], int n, int x) {
  for (int i = 0; i < n; i++) {
    if (arr[i] == x) {
      return i;
    }
  }
  return -1;
}`;
      } else if (type === 'binary') {
        this.algorithmExample = `// Example of Binary Search Algorithm
int binarySearch(int arr[], int l, int r, int x) {
  while (l <= r) {
    int m = l + (r - l) / 2;
    if (arr[m] == x)
      return m;
    if (arr[m] < x)
      l = m + 1;
    else
      r = m - 1;
  }
  return -1;
}`;
      }
    },

    async generateAINotes() {
      this.isGenerating = true;
      this.aiNotesData = null;

      const prompt = `
        Generate a detailed study guide on searching algorithms, including:
        Explanation of key concepts (Linear Search, Binary Search, Time Complexity, Space Complexity).
        Comparison of linear and binary search with examples.
        Practical applications and importance of searching algorithms in real-world scenarios.
        Key interview questions with solutions and coding challenges.
        A list of curated learning resources with clickable links.
      `;

      try {
        const response = await axios.post(
          "https://api.groq.com/openai/v1/chat/completions",
          {
            model: "mixtral-8x7b-32768",
            messages: [{ role: "user", content: prompt }],
            temperature: 0.8,
            max_tokens: 3000,
          },
          {
            headers: {
              Authorization: `Bearer ${this.groqApiKey}`,
              "Content-Type": "application/json"
            }
          }
        );

        if (response.data && response.data.choices && response.data.choices.length > 0) {
          const formattedResponse = response.data.choices[0].message.content
            .replace(/\n/g, "<br>")
            .replace(/(\d\.\s)/g, "<b>$1</b>")
            .replace(
              /(https?:\/\/[^\s]+)/g,
              `<a href="$1" target="_blank" style="color:#00ffcc;">$1</a>`
            );
          this.aiNotesData = `<div>${formattedResponse}</div>`;
        } else {
          throw new Error("Invalid response from API");
        }
      } catch (error) {
        console.error("Error generating AI notes:", error.message);
        alert("Failed to generate AI notes. Please try again.");
      } finally {
        this.isGenerating = false;
      }
    }
  }
};
</script>

<style scoped>
.searching-container {
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
  border-radius: 10px;
  background-color: #121212;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.6);
  font-family: "Roboto", sans-serif;
  color: #e0e0e0;
  line-height: 1.6;
}

.sub-title {
font-size: 1.5em;
color: #0d9bbb;
margin-top: 20px;
}

.main-title {
font-size: 4em;
color: #ccc;
text-align: center;
}

.imageedit {
  margin: 10px; /* Adds space around each image */
  padding: 5px; /* Optional: Adds inner space within the image border */
  border: 1px solid #ccc; /* Optional: Adds a border for better visibility */
}
.type-title {
  font-size: 1.5em;
  color: #e0ce46;
  margin-top: 25px;
}

.characteristics-list {
  margin: 10px 0;
  padding-left: 20px;
  font-size: 1.2em;
}

.searching-diagram {
  width: 100%;
  height: auto;
  margin: 30px 0;
  border: 1px solid #444;
  border-radius: 5px;
}

pre {
  background-color: #1f1f1f;
  padding: 10px;
  border-radius: 5px;
  overflow-x: auto;
  color: #00ff00;
  font-size: 1.2em;
}

.button-container {
  display: flex;
  justify-content: space-around;
  margin: 30px 0;
}

.example-button {
  background-color: #ffcc00;
  color: #121212;
  border: none;
  border-radius: 5px;
  padding: 15px 30px;
  font-size: 1.2em;
  cursor: pointer;
  transition: background-color 0.3s;
}

.example-button:hover {
  background-color: #ffe066;
}

.ai-notes-section {
  margin-top: 30px;
  text-align: center;
}

.ai-notes-display {
  background-color: #1f1f1f;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
  margin-top: 20px;
}

.ai-notes-display a {
  color: #00ffcc;
  text-decoration: underline;
}
</style>