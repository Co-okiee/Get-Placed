<template>
  <div class="linkedlist-container">
    <h1 class="main-title">Linked Lists</h1>
    <p class="intro">
      A linked list is a linear data structure where each element (node) contains data and a reference to the next node in the sequence.
    </p>

    <h2 class="sub-title">Key Characteristics of Linked Lists</h2>
    <ul class="characteristics-list">
      <li><strong>Dynamic Size:</strong> Linked lists can grow and shrink dynamically during execution.</li>
      <li><strong>Efficient Insertions/Deletions:</strong> Insertions and deletions do not require reorganization of the entire structure.</li>
      <li><strong>No Direct Access:</strong> Elements cannot be accessed directly by index; traversal is required.</li>
    </ul>

    <h2 class="sub-title">Diagram of a Linked List</h2>
    <img src="@/assets/ll.png" alt="Linked List Diagram" class="linkedlist-diagram imageedit" />

    <h2 class="sub-title">Types of Linked Lists</h2>
    <h3 class="type-title">Singly Linked List</h3>
    <p>A linked list where each node points to the next node, and the last node points to null.</p>

    <h3 class="type-title">Doubly Linked List</h3>
    <p>A linked list where each node contains two references: one to the next node and one to the previous node.</p>

    <h3 class="type-title">Circular Linked List</h3>
    <p>A linked list where the last node points back to the first node, forming a circular structure.</p>

    <h2 class="sub-title">Linked List Operations</h2>
    <p>Common operations include insertion, deletion, traversal, and searching.</p>

    <h2 class="sub-title">Adjacency and Reverse</h2>
    <p>Adjacency refers to the relationship between nodes, while reversing involves changing the direction of node pointers.</p>

    <h2 class="sub-title">Examples</h2>
    <p>Click the buttons below to see examples of linked lists in different programming languages:</p>
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
        <div class="ai-notes-content">
          <div class="notes-section">
            <h3 class="section-title">📘 Comprehensive Study Notes</h3>
            <p class="notes-text">{{ aiNotesData.studyNotes }}</p>
          </div>

          <div class="notes-section">
            <h3 class="section-title">🎯 Key Concepts</h3>
            <ul class="key-concepts-list">
              <li v-for="(concept, index) in aiNotesData.keyConcepts" :key="index">
                {{ concept }}
              </li>
            </ul>
          </div>

          <div class="notes-section">
            <h3 class="section-title">💡 Interview Questions</h3>
            <div class="interview-questions">
              <div 
                v-for="(question, index) in aiNotesData.interviewQuestions" 
                :key="index" 
                class="interview-question"
              >
                <strong>Q{{ index + 1 }}:</strong> {{ question }}
              </div>
            </div>
          </div>

          <div class="notes-section">
            <h3 class="section-title">🎥 Recommended Tutorials</h3>
            <div class="tutorial-links">
              <a 
                v-for="(tutorial, index) in aiNotesData.tutorialLinks" 
                :key="index"
                :href="tutorial.url"
                target="_blank"
                class="tutorial-link"
              >
                <span class="tutorial-platform">{{ tutorial.platform }}</span>
                <span class="tutorial-description">{{ tutorial.description }}</span>
              </a>
            </div>
          </div>

          <div class="notes-actions">
            <button @click="copyNotes" class="example-button copy-button">
              📋 Copy Study Guide
            </button>
            <button @click="downloadNotesPDF" class="example-button download-button">
              📥 Download PDF
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import jspdf from "jspdf";

export default {
  name: "LinkedList",
  data() {
    return {
      exampleCode: "",
      aiNotesData: null,
      isGenerating: false,
      selectedTopic: "",
      error: null,
      groqApiKey: "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",
    };
  },
  methods: {
    showExample(language) {
      if (language === "java") {
        this.exampleCode = `// Linked List in Java
import java.util.LinkedList;
LinkedList<String> list = new LinkedList<>();
list.add("Node1");
System.out.println(list.get(0)); // Output: Node1`;
      } else if (language === "c") {
        this.exampleCode = `// Linked List in C
struct Node {
    int data;
    struct Node* next;
};
struct Node* head = NULL;`;
      } else if (language === "python") {
        this.exampleCode = `# Linked List in Python
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None`;
      }
    },

    generateAINotes() {
      this.isGenerating = true;
      // Simulated API call to generate notes
      setTimeout(() => {
        this.aiNotesData = {
          studyNotes: "Detailed notes about Linked Lists...",
          keyConcepts: ["Dynamic Size", "Efficient Insertions", "No Direct Access"],
          interviewQuestions: [
            "What are the advantages of a linked list?",
            "Explain the difference between singly and doubly linked lists.",
          ],
          tutorialLinks: [
            {
              platform: "YouTube",
              description: "Linked List Basics",
              url: "https://www.youtube.com/results?search_query=linked+list",
            },
          ],
        };
        this.isGenerating = false;
      }, 2000);
    },
  },
};
</script>

<style scoped>

.linkedlist-container {
  padding: 20px;
  background: #282c34;
  color: #ffffff;
  font-family: Arial, sans-serif;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
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

.example-button {
  background-color: #61dafb;
  color: #282c34;
  margin: 5px;
  padding: 10px 20px;
  border-radius: 5px;
  border: none;
  cursor: pointer;
}

.example-button:hover {
  background-color: #21a1f1;
}
</style>