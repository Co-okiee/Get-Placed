<template>
  <div class="heap-container">
    <h1 class="main-title">Heaps</h1>
    <p class="intro">
      A heap is a special tree-based data structure that satisfies the heap property: for a max heap, every parent node is greater than or equal to its child nodes, and for a min heap, every parent node is less than or equal to its child nodes.
    </p>

    <h2 class="sub-title">Key Characteristics of Heaps</h2>
    <ul class="characteristics-list">
      <li><strong>Complete Binary Tree:</strong> Heaps are always complete binary trees, meaning all levels are fully filled except possibly for the last level.</li>
      <li><strong>Heap Property:</strong> In a max heap, the value of the parent node is greater than or equal to the values of its children. In a min heap, the value of the parent node is less than or equal to its children.</li>
      <li><strong>Efficient Operations:</strong> Heaps provide efficient insertion and deletion operations, with time complexities of O(log n).</li>
    </ul>

    <h2 class="sub-title">Diagram of a Heap</h2>
    <img src="@/assets/heap.png" alt="Heap Diagram" class="heap-diagram imageedit" />

    <h2 class="sub-title">Types of Heaps</h2>
    <h3 class="type-title">Max Heap</h3>
    <p>
      A heap where the value of each node is greater than or equal to the values of its children, with the maximum value at the root.
    </p>

    <h3 class="type-title">Min Heap</h3>
    <p>
      A heap where the value of each node is less than or equal to the values of its children, with the minimum value at the root.
    </p>

    <h2 class="sub-title">Heap Operations</h2>
    <p>
      Common operations performed on heaps include insertion, deletion (removing the root), and heapify (maintaining the heap property).
    </p>

    <h2 class="sub-title">Examples</h2>
    <p>Click on the buttons below to see examples of heaps in different programming languages:</p>
    <div class="button-container">
      <button @click="showExample('java')" class="example-button">Example in Java</button>
      <button @click="showExample('c')" class="example-button">Example in C</button>
      <button @click="showExample('python')" class="example-button">Example in Python</button>
    </div>
    <pre v-if="exampleCode">
      <code>{{ exampleCode }}</code>
    </pre>

    <h2 class="sub-title">Generative Study Companion</h2>
    <div class="ai-notes-section">
      <button
        @click="generateAINotes"
        class="example-button ai-notes-button"
        :disabled="isGenerating"
      >
        {{ isGenerating ? 'Generating Study Guide...' : 'Generate Study Guide' }}
      </button>

      <div v-if="aiNotesData" class="ai-notes-display">
        <h3 class="section-title">📘 Comprehensive Study Notes</h3>
        <div v-html="aiNotesData"></div>
      </div>
    </div>

    <h2 class="sub-title">Useful Links</h2>
    <h3 class="link-title">YouTube Tutorials</h3>
    <ul class="link-list">
      <li>
        <a href="https://www.youtube.com/watch?v=heap1" target="_blank">
          Heaps in Java (English)
        </a>
      </li>
      <li>
        <a href="https://www.youtube.com/watch?v=heap2" target="_blank">
          Heaps in Hindi
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Heap",
  data() {
    return {
      exampleCode: "",
      aiNotesData: null,
      isGenerating: false,
      groqApiKey: "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", // Replace with your actual Groq API key
    };
  },
  methods: {
    showExample(language) {
      if (language === "java") {
        this.exampleCode = `import java.util.PriorityQueue;
PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
maxHeap.add(5);
maxHeap.add(10);
System.out.println(maxHeap.peek()); // Output: 10`;
      } else if (language === "c") {
        this.exampleCode = `#include<stdio.h>
#include<stdlib.h>
#define MAX 100
int heap[MAX], size = 0;
void insert(int value) {
    heap[size++] = value;
    // Code to maintain the heap property goes here
}`;
      } else if (language === "python") {
        this.exampleCode = `import heapq
max_heap = []
heapq.heappush(max_heap, -1 * 10)  # Store negative values for max heap
print(-1 * max_heap[0])  # Output: 10`;
      }
    },

    async generateAINotes() {
      this.isGenerating = true;
      this.aiNotesData = null;

      const prompt = `
        Generate detailed programming notes about Heaps, including:
        1. A detailed introduction to Heaps and their importance in programming.
        2. Types of Heaps with examples (Max Heap, Min Heap).
        3. Common Heap operations with syntax in Python, Java, and C.
        4. Real-world applications of Heaps in priority queues and memory management.
        5. Key interview questions and coding challenges with sample solutions.
        6. A curated list of resources for further learning.
      `;

      try {
        const response = await axios.post(
          "https://api.groq.com/openai/v1/chat/completions",
          {
            model: "mixtral-8x7b-32768",
            messages: [{ role: "user", content: prompt }],
            temperature: 0.7,
            max_tokens: 3000,
          },
          {
            headers: {
              Authorization: `Bearer ${this.groqApiKey}`,
              "Content-Type": "application/json",
            },
          }
        );

        if (response.data && response.data.choices && response.data.choices.length > 0) {
          const formattedResponse = response.data.choices[0].message.content
            .replace(/\n/g, "<br>")
            .replace(/•/g, "&nbsp;&nbsp;&nbsp;•")
            .replace(/(\d\.\s)/g, "<b>$1</b>");
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
    },
  },
};
</script>

<style scoped>
.heap-container {
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

.heap-diagram {
  width: 100%;
  height: auto;
  margin: 30px 0;
  border: 1px solid #444;
  border-radius: 5px;
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

.ai-notes-display {
  margin-top: 20px;
  background: #1f1f1f;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.section-title {
  font-size: 1.5em;
  color: #007bff;
  margin-bottom: 10px;
}

.link-list a {
  color: #ddc452;
  text-decoration: none;
}

.link-list a:hover {
  text-decoration: underline;
}
</style>