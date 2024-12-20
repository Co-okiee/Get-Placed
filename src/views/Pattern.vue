<template>
  <div class="algorithm-container">
    <h1 class="main-title">Pattern Searching</h1>
    <p class="intro">
      Pattern searching is a key area in computer science, solving the challenge of locating occurrences of a "pattern" within a larger "text". This technique is vital for text editors, search engines, and bioinformatics.
    </p>

    <h2 class="sub-title">Key Concepts in Pattern Searching</h2>
    <ul class="characteristics-list">
      <li><strong>Text:</strong> The larger string in which we want to locate occurrences of the pattern.</li>
      <li><strong>Pattern:</strong> The smaller string being searched for within the text.</li>
      <li><strong>Search Algorithms:</strong> Algorithms with varying efficiencies and applications used to locate patterns in text.</li>
    </ul>

    <h2 class="sub-title">Pattern Searching Diagram</h2>
    <img src="@/assets/pattern.png" alt="Pattern Searching Diagram" class="algorithm-diagram imageedit" />

    <h2 class="sub-title">Example Algorithms</h2>
    <p>Choose a pattern searching algorithm to see its example:</p>
    <div class="button-container">
      <button @click="showAlgorithm('naive')" class="example-button">Naive Pattern Searching</button>
      <button @click="showAlgorithm('kmp')" class="example-button">KMP Algorithm</button>
      <button @click="showAlgorithm('bm')" class="example-button">Boyer-Moore Algorithm</button>
    </div>

    <pre v-if="algorithmExample">
      <code>{{ algorithmExample }}</code>
    </pre>

    <h2 class="sub-title">Generative Study Notes</h2>
    <div class="ai-notes-section">
      <button 
        @click="generateAINotes" 
        class="example-button ai-notes-button" 
        :disabled="isGenerating"
      >
        {{ isGenerating ? "Generating Study Notes..." : "Generate Study Notes" }}
      </button>
      <div v-if="aiNotesData" class="ai-notes-display">
        <h3 class="section-title">AI Study Notes</h3>
        <div v-html="aiNotesData"></div>
      </div>
    </div>

    <h2 class="sub-title">Useful Resources</h2>
    <ul class="resource-links">
      <li><a href="https://www.geeksforgeeks.org/searching-for-patterns-set-1-naive-pattern-searching/" target="_blank">GeeksforGeeks - Naive Pattern Searching</a></li>
      <li><a href="https://www.youtube.com/watch?v=3W8hN4WblYc" target="_blank">YouTube - Pattern Searching in English</a></li>
      <li><a href="https://www.youtube.com/watch?v=W9rX1nAxPPE" target="_blank">YouTube - Pattern Searching in Hindi</a></li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "PatternSearching",
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
      if (type === "naive") {
        this.algorithmExample = `// Naive Pattern Searching Algorithm
for (int i = 0; i <= n - m; i++) {
  int j;
  for (j = 0; j < m; j++)
    if (text[i + j] != pattern[j])
      break;
  if (j == m)
    print("Pattern found at index " + i);
}`;
      } else if (type === "kmp") {
        this.algorithmExample = `// KMP Algorithm
void KMPSearch(string text, string pattern) {
  int M = pattern.length();
  int N = text.length();
  int lps[M];
  computeLPSArray(pattern, M, lps);
  int i = 0, j = 0;
  while (N - i >= M) {
    if (pattern[j] == text[i]) {
      j++;
      i++;
    }
    if (j == M) {
      print("Pattern found at index " + (i - j));
      j = lps[j - 1];
    } else if (i < N && pattern[j] != text[i]) {
      j = (j != 0) ? lps[j - 1] : i++;
    }
  }
}`;
      } else if (type === "bm") {
        this.algorithmExample = `// Boyer-Moore Algorithm
void search(string text, string pattern) {
  int m = pattern.length();
  int n = text.length();
  int badChar[256];
  preprocessBadChar(pattern, badChar);
  int s = 0;
  while (s <= n - m) {
    int j = m - 1;
    while (j >= 0 && pattern[j] == text[s + j])
      j--;
    if (j < 0) {
      print("Pattern found at index " + s);
      s += (s + m < n) ? m - badChar[text[s + m]] : 1;
    } else
      s += max(1, j - badChar[text[s + j]]);
  }
}`;
      }
    },

    async generateAINotes() {
      this.isGenerating = true;
      this.aiNotesData = null;
      const prompt = `
        Generate a detailed study guide on pattern searching algorithms. Include:
        - Overview and importance of pattern searching.
        - Key concepts: Text, Pattern, Algorithm categories.
        - Examples with explanations: Naive, KMP, Boyer-Moore.
        - Real-world applications.
        - Interview questions and links to resources.
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
          this.aiNotesData = `<div style="text-align: left;">${formattedResponse}</div>`;
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
.algorithm-container {
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
  border-radius: 10px;
  background-color: #121212;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.6);
  font-family: 'Roboto', sans-serif;
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

.intro {
  font-size: 1.3em;
  margin-bottom: 25px;
}

.algorithm-diagram {
  width: 100%;
  height: auto;
  margin: 30px 0;
}

pre {
  background-color: #1f1f1f;
  padding: 10px;
  border-radius: 5px;
  color: #00ff00;
  font-size: 1.2em;
}

.example-button {
  background-color: #ffcc00;
  color: #121212;
  border-radius: 5px;
  padding: 15px 30px;
}

.example-button:hover {
  background-color: #ffe066;
}

.resource-links a {
  color: #e0ce46;
  text-decoration: none;
}

.resource-links a:hover {
  color: #fff;
}
</style>