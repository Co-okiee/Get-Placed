<template>
  <div class="advanced-data-structures-container">
    <h1 class="main-title">Advanced Data Structures</h1>
    <p class="intro">
      Advanced data structures are specialized structures designed to solve complex problems efficiently. These data structures are often used in advanced algorithms and applications requiring optimized performance.
    </p>

    <h2 class="sub-title">Key Advanced Data Structures</h2>
    <ul class="data-structures-list">
      <li><strong>Trie:</strong> A tree-like data structure used to store a dynamic set of strings, enabling fast retrieval, particularly in applications like autocomplete.</li>
      <li><strong>Segment Tree:</strong> A binary tree used for storing intervals or segments, allowing efficient range queries and updates.</li>
      <li><strong>Fenwick Tree (Binary Indexed Tree):</strong> A data structure that provides efficient methods for cumulative frequency tables, enabling updates and prefix sum queries.</li>
      <li><strong>Disjoint Set Union (Union-Find):</strong> A data structure that keeps track of a set of elements partitioned into disjoint subsets, commonly used in network connectivity problems.</li>
      <li><strong>AVL Tree:</strong> A self-balancing binary search tree that maintains balance through rotations, ensuring O(log n) time complexity for insertions and deletions.</li>
    </ul>

    <h2 class="sub-title">Common Operations</h2>
    <ul>
      <li><strong>Insertion:</strong> Adding an element to the data structure.</li>
      <li><strong>Deletion:</strong> Removing an element from the data structure.</li>
      <li><strong>Search:</strong> Finding an element in the data structure.</li>
      <li><strong>Traversal:</strong> Visiting all elements in the data structure in a specific order.</li>
    </ul>

    <h2 class="sub-title">Examples</h2>
    <p>Click on the buttons below to see examples of advanced data structures in different programming languages:</p>

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

    <h2 class="sub-title">Useful Links</h2>
    <h3 class="link-title">YouTube Tutorials</h3>
    <ul class="link-list">
      <li>
        <a href="https://www.youtube.com/watch?v=advanced_data_structures1" target="_blank">
          Advanced Data Structures in Java (English)
        </a>
      </li>
      <li>
        <a href="https://www.youtube.com/watch?v=advanced_data_structures2" target="_blank">
          Advanced Data Structures in Hindi
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "AdvancedDataStructures",
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
        this.exampleCode = `class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isEndOfWord = false;
}

class Trie {
    TrieNode root = new TrieNode();

    void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            if (node.children[c - 'a'] == null) {
                node.children[c - 'a'] = new TrieNode();
            }
            node = node.children[c - 'a'];
        }
        node.isEndOfWord = true;
    }

    boolean search(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            node = node.children[c - 'a'];
            if (node == null) return false;
        }
        return node.isEndOfWord;
    }
}`;
      } else if (language === "c") {
        this.exampleCode = `#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ALPHABET_SIZE 26

struct TrieNode {
    struct TrieNode* children[ALPHABET_SIZE];
    int isEndOfWord;
};

struct TrieNode* createNode() {
    struct TrieNode* node = (struct TrieNode*)malloc(sizeof(struct TrieNode));
    node->isEndOfWord = 0;
    for (int i = 0; i < ALPHABET_SIZE; i++) {
        node->children[i] = NULL;
    }
    return node;
}

void insert(struct TrieNode* root, char* word) {
    struct TrieNode* node = root;
    for (int i = 0; i < strlen(word); i++) {
        int index = word[i] - 'a';
        if (node->children[index] == NULL) {
            node->children[index] = createNode();
        }
        node = node->children[index];
    }
    node->isEndOfWord = 1;
}`;
      } else if (language === "python") {
        this.exampleCode = `class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word`;
      }
    },

    async generateAINotes() {
      this.isGenerating = true;
      this.aiNotesData = null;

      const prompt = `
        Generate detailed programming notes about Advanced Data Structures, including:
        1. An introduction and their importance in modern computing.
        2. Types of Advanced Data Structures with examples (Trie, Segment Tree, Fenwick Tree, Disjoint Set, AVL Tree).
        3. Key operations and use-cases.
        4. Real-world applications.
        5. Key interview questions and coding challenges with examples.
        6. A curated list of YouTube tutorials with clickable links.
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
            .replace(/(https?:\/\/[^\s<]+)(?=[\s<]|$)/g, '<a href="$1" target="_blank">$1</a>');
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
.advanced-data-structures-container {
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

.section-title {
  font-size: 1.8em;
  color: #007bff;
  margin-bottom: 20px;
}

.data-structures-list {
  margin: 10px 0;
  padding-left: 20px;
  font-size: 1.2em;
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

.ai-notes-display {
  margin-top: 20px;
  background: #1f1f1f;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.link-list a {
  color: #ddc452;
  text-decoration: none;
}

.link-list a:hover {
  text-decoration: underline;
}
</style>