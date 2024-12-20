<template>
  <div class="hashing-container">
    <h1 class="main-title">Hashing</h1>
    <p class="intro">
      Hashing is a technique used to uniquely identify a specific object from a group of similar objects. It transforms input data of arbitrary size into a fixed-size value, often called a hash code, using a hash function.
    </p>

    <h2 class="sub-title">Key Characteristics of Hashing</h2>
    <ul class="characteristics-list">
      <li><strong>Efficient Data Retrieval:</strong> Hashing allows for quick data access through direct indexing.</li>
      <li><strong>Fixed Size:</strong> The output of the hash function has a fixed size, regardless of the input size.</li>
      <li><strong>Collision Handling:</strong> Hashing must handle collisions where different inputs produce the same hash value.</li>
    </ul>

    <h2 class="sub-title">Hash Table Structure</h2>
    <img src="@/assets/hash_table.png" alt="Hash Table Diagram" class="hash-table-diagram imageedit" />

    <h2 class="sub-title">Types of Hashing</h2>
    <h3 class="type-title">Closed Addressing (Chaining)</h3>
    <p>Each slot of the hash table contains a linked list of entries that hash to the same index.</p>

    <h3 class="type-title">Open Addressing</h3>
    <p>All entries are stored directly in the hash table, with probing used to find the next available slot when collisions occur.</p>

    <h2 class="sub-title">Hashing Operations</h2>
    <p>
      Common operations include inserting a key-value pair, searching for a value by key, and deleting a key-value pair.
    </p>

    <h2 class="sub-title">Examples</h2>
    <p>Click on the buttons below to see examples of hashing in different programming languages:</p>
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
        <a href="https://www.youtube.com/watch?v=hashing1" target="_blank">
          Hashing in Java (English)
        </a>
      </li>
      <li>
        <a href="https://www.youtube.com/watch?v=hashing2" target="_blank">
          Hashing in Hindi
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Hashing",
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
        this.exampleCode = `import java.util.HashMap;
HashMap<String, Integer> map = new HashMap<>();
map.put("Key1", 1);
System.out.println(map.get("Key1")); // Output: 1`;
      } else if (language === "c") {
        this.exampleCode = `#include <stdio.h>
#include <stdlib.h>
#define TABLE_SIZE 10
struct HashNode {
    int key;
    int value;
    struct HashNode* next;
};
struct HashNode* table[TABLE_SIZE];`;
      } else if (language === "python") {
        this.exampleCode = `hash_map = {}
hash_map["key1"] = 1
print(hash_map["key1"])  # Output: 1`;
      }
    },

    async generateAINotes() {
      this.isGenerating = true;
      this.aiNotesData = null;

      const prompt = `
        Generate detailed and well-structured programming notes about Hashing, including:
        1. A detailed introduction to Hashing and its importance.
        2. Types of Hashing with examples (Closed Addressing, Open Addressing).
        3. Common Hashing operations with syntax in Python, Java, and C.
        4. Real-world applications of Hashing in data retrieval, databases, and cryptography.
        5. Key interview questions and coding challenges with sample solutions.
        6. A curated list of resources for further learning.
        Ensure each section is clear, well-formatted, and easy to understand.
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
.hashing-container {
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

.hash-table-diagram {
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