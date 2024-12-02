<template>
  <div class="tree-container">
    <h1 class="main-title">Trees</h1>
    <p class="intro">
      A tree is a hierarchical data structure consisting of nodes, where each node has a value and references to its child nodes. Trees are foundational in computer science and are used in various applications like file systems, databases, and network routing.
    </p>

    <h2 class="sub-title">Key Characteristics of Trees</h2>
    <ul class="characteristics-list">
      <li><strong>Hierarchical Structure:</strong> Trees are organized in levels where a parent node can have child nodes.</li>
      <li><strong>Root Node:</strong> The topmost node in the tree is called the root node, from which all other nodes descend.</li>
      <li><strong>Leaf Nodes:</strong> Nodes that do not have any children are called leaf nodes.</li>
    </ul>

    <h2 class="sub-title">Diagram of a Tree</h2>
    <img src="@/assets/tree.png" alt="Tree Diagram" class="tree-diagram imageedit" />

    <h2 class="sub-title">Types of Trees</h2>
    <h3 class="type-title">Binary Tree</h3>
    <p>A tree where each node has at most two children, referred to as the left child and the right child.</p>

    <h3 class="type-title">Binary Search Tree (BST)</h3>
    <p>
      A binary tree where each node follows the property that all nodes in the left subtree are smaller, and all nodes in the right subtree are larger.
    </p>

    <h3 class="type-title">AVL Tree</h3>
    <p>
      A self-balancing binary search tree where the difference in heights between left and right subtrees is at most one.
    </p>

    <h2 class="sub-title">Tree Operations</h2>
    <p>
      Common operations performed on trees include insertion, deletion, traversal (in-order, pre-order, post-order), and searching for a specific value.
    </p>

    <h2 class="sub-title">Examples</h2>
    <p>Click on the buttons below to see examples of trees in different programming languages:</p>
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
        <div v-html="formattedNotes"></div>
      </div>
    </div>

    <h2 class="sub-title">Useful Links</h2>
    <h3 class="link-title">YouTube Tutorials</h3>
    <ul class="link-list">
      <li>
        <a href="https://www.youtube.com/watch?v=tree1" target="_blank">
          Trees in Java (English)
        </a>
      </li>
      <li>
        <a href="https://www.youtube.com/watch?v=tree2" target="_blank">
          Trees in Hindi
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Tree",
  data() {
    return {
      exampleCode: "",
      aiNotesData: null,
      isGenerating: false,
      groqApiKey: "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",
    };
  },
  computed: {
    formattedNotes() {
      if (!this.aiNotesData) return "";
      return this.aiNotesData
        .replace(/\n\s*\n/g, "<br><br>") // Add line breaks for paragraphs
        .replace(/•/g, "&nbsp;&nbsp;&nbsp;•") // Indent bullet points
        .replace(/(\d\.\s)/g, "<b>$1</b>") // Bold numbered points
        .replace(/(https?:\/\/[^\s]+)/g, '<a href="$1" target="_blank">$1</a>'); // Make links clickable
    },
  },
  methods: {
    showExample(language) {
      if (language === "java") {
        this.exampleCode = `class Node {
    int value;
    Node left, right;
    public Node(int item) {
        value = item;
        left = right = null;
    }
}
Node root = new Node(10);`;
      } else if (language === "c") {
        this.exampleCode = `#include<stdio.h>
#include<stdlib.h>
struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->left = newNode->right = NULL;
    return newNode;
}`;
      } else if (language === "python") {
        this.exampleCode = `class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
root = Node(10)`;
      }
    },

    async generateAINotes() {
      this.isGenerating = true;
      this.aiNotesData = null;

      const prompt = `
        Generate detailed and well-structured programming notes about Trees, including:
        1. A detailed introduction to Trees and their importance in programming.
        2. Types of Trees with examples (Binary, Binary Search Tree, AVL).
        3. Common Tree operations with syntax in Python, Java, and C.
        4. Real-world applications of Trees in databases, file systems, and search engines.
        5. Key interview questions and practical coding challenges with sample solutions.
        6. A curated list of resources for further learning (tutorials, articles, and books).
        Ensure each section is clear, well-formatted, and easy to read.
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
          this.aiNotesData = response.data.choices[0].message.content;
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
.tree-container {
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

.tree-diagram {
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
  text-align: left;
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