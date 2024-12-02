<template>
  <div class="algorithm-container">
    <h1 class="main-title">Greedy Algorithms</h1>
    <p class="intro">
      Greedy algorithms build up a solution piece by piece, choosing the most immediate benefit at each step without considering the global context. It guarantees that the solution is optimal for some problems, but not all.
    </p>

    <h2 class="sub-title">Key Concepts in Greedy Algorithms</h2>
    <ul class="characteristics-list">
      <li><strong>Greedy Choice Property:</strong> A local optimum is chosen at every step with the hope of finding a global optimum.</li>
      <li><strong>Optimal Substructure:</strong> A problem is said to have an optimal substructure if an optimal solution to the problem contains optimal solutions to subproblems.</li>
    </ul>

    <h2 class="sub-title">Diagram for Greedy Algorithm</h2>
    <img src="@/assets/greedy.jpg" alt="Greedy Algorithm Diagram" class="algorithm-diagram imageedit" />

    <h2 class="sub-title">Example Algorithms</h2>
    <p>Select a category of greedy algorithms to see examples:</p>
    <div class="button-container">
      <button @click="showAlgorithm('fractionalKnapsack')" class="example-button">Fractional Knapsack</button>
      <button @click="showAlgorithm('activitySelection')" class="example-button">Activity Selection</button>
      <button @click="showAlgorithm('huffmanCoding')" class="example-button">Huffman Coding</button>
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
  name: "GreedyAlgorithms",
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
      if (type === "fractionalKnapsack") {
        this.algorithmExample = `// Fractional Knapsack Algorithm
int n = items.size();
sort(items.begin(), items.end(), by_value_to_weight_ratio);
double totalValue = 0;
for (int i = 0; i < n; i++) {
  if (capacity >= items[i].weight) {
    totalValue += items[i].value;
    capacity -= items[i].weight;
  } else {
    totalValue += (items[i].value / items[i].weight) * capacity;
    break;
  }
}`;
      } else if (type === "activitySelection") {
        this.algorithmExample = `// Activity Selection Algorithm
sort(activities, by_finish_time);
int count = 1;
int last_finish = activities[0].finish;
for (int i = 1; i < activities.size(); i++) {
  if (activities[i].start >= last_finish) {
    count++;
    last_finish = activities[i].finish;
  }
}
return count;`;
      } else if (type === "huffmanCoding") {
        this.algorithmExample = `// Huffman Coding Algorithm
priority_queue<Node*, vector<Node*>, compare> minHeap;
for (int i = 0; i < freq.size(); i++) {
  Node* newNode = new Node(characters[i], freq[i]);
  minHeap.push(newNode);
}
while (minHeap.size() != 1) {
  Node *left = minHeap.top(); minHeap.pop();
  Node *right = minHeap.top(); minHeap.pop();
  Node *newNode = new Node('$', left->freq + right->freq);
  newNode->left = left;
  newNode->right = right;
  minHeap.push(newNode);
}`;
      }
    },
    async generateAINotes() {
      this.isGenerating = true;
      this.aiNotesData = null;
      const prompt = `
        Generate a detailed study guide on greedy algorithms, including:
        Explanation of key concepts (Greedy Choice Property, Optimal Substructure).
        Examples of greedy algorithms (Fractional Knapsack, Activity Selection, Huffman Coding).
        Comparison with dynamic programming and when greedy algorithms fail.
        Key interview questions with coding challenges and solutions.
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
.algorithm-container {
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

.algorithm-diagram {
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