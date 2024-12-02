<template>
  <div class="queue-container">
    <h1 class="main-title">Queues</h1>
    <p class="intro">
      A queue is a linear data structure that follows the First In First Out (FIFO) principle, where the first element added is the first to be removed. Queues are widely used in real-world applications such as task scheduling, order processing, and buffering data.
    </p>

    <h2 class="sub-title">Key Characteristics of Queues</h2>
    <ul class="characteristics-list">
      <li><strong>FIFO Structure:</strong> Queues operate on the First In First Out (FIFO) principle.</li>
      <li><strong>Enqueue and Dequeue Operations:</strong> Elements are added using the enqueue operation and removed using the dequeue operation.</li>
      <li><strong>No Random Access:</strong> Only the front and rear elements can be accessed directly.</li>
    </ul>

    <h2 class="sub-title">Diagram of a Queue</h2>
    <img src="@/assets/queue.png" alt="Queue Diagram" class="queue-diagram imageedit" />

    <h2 class="sub-title">Types of Queues</h2>
    <h3 class="type-title">Simple Queue</h3>
    <p>A basic queue where elements are added to the rear and removed from the front.</p>

    <h3 class="type-title">Circular Queue</h3>
    <p>A queue where the rear of the queue wraps around to the front, forming a circular structure.</p>

    <h3 class="type-title">Priority Queue</h3>
    <p>A queue where elements are removed based on priority rather than the order they were added.</p>

    <h2 class="sub-title">Queue Operations</h2>
    <p>
      Common operations performed on queues include enqueue (add an element), dequeue (remove an element),
      peek (view the front element), and checking if the queue is empty or full.
    </p>

    <h2 class="sub-title">Examples</h2>
    <p>Click on the buttons below to see examples of queues in different programming languages:</p>
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
  name: "Queue",
  data() {
    return {
      exampleCode: "",
      aiNotesData: null,
      isGenerating: false,
      groqApiKey: "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",
    };
  },
  methods: {
    showExample(language) {
      if (language === "java") {
        this.exampleCode = `import java.util.LinkedList;
Queue<Integer> queue = new LinkedList<>();
queue.add(1);
System.out.println(queue.peek()); // Output: 1`;
      } else if (language === "c") {
        this.exampleCode = `#include<stdio.h>
#define MAX 10
int queue[MAX], front = -1, rear = -1;
void enqueue(int val) {
    if (rear == MAX - 1) printf("Queue Overflow");
    else queue[++rear] = val;
}`;
      } else if (language === "python") {
        this.exampleCode = `class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, data):
        self.queue.append(data)
queue = Queue()
queue.enqueue(5)`;
      }
    },

    async generateAINotes() {
      this.isGenerating = true;
      this.aiNotesData = null;

      const prompt = `
        Generate well-structured programming notes about Queues, including:
        1. A detailed introduction to Queues and their importance in programming.
        2. Types of Queues with examples (Simple, Circular, Priority).
        3. Common Queue operations with syntax in Python, Java, and C.
        4. Real-world applications of Queues in scheduling, networking, and buffering.
        5. Key interview questions and practical coding challenges with sample solutions.
        6. A list of resources for further learning (tutorials, articles, and books).
        Ensure each section is well-formatted and includes examples and explanations.
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
              "Content-Type": "application/json",
            },
          }
        );

        if (response.data && response.data.choices && response.data.choices.length > 0) {
          const formattedResponse = response.data.choices[0].message.content
            .replace(/\n/g, "<br>")
            .replace(/•/g, "&nbsp;&nbsp;&nbsp;•")
            .replace(/(\d\.\s)/g, "<b>$1</b>")
            .replace(
              /(https?:\/\/[^\s]+)/g,
              `<a href="$1" target="_blank" style="color:#00ffcc; text-decoration:underline;">$1</a>`
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
    },
  },
};
</script>

<style scoped>
.queue-container {
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


.type-title {
  font-size: 1.5em;
  color: #e0ce46;
  margin-top: 25px;
}

.queue-diagram {
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

.imageedit {
  margin: 10px; /* Adds space around each image */
  padding: 5px; /* Optional: Adds inner space within the image border */
  border: 1px solid #ccc; /* Optional: Adds a border for better visibility */
}
.section-title {
  font-size: 1.5em;
  color: #007bff;
  margin-bottom: 10px;
}

.ai-notes-display a {
  color: #00ffcc;
  text-decoration: underline;
}
</style>