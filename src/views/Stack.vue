<template>
  <div class="stack-container">
    <h1 class="main-title">Stacks</h1>
    <p class="intro">
      A stack is a linear data structure that follows the Last In First Out (LIFO) principle, where the last element added is the first to be removed.
    </p>

    <h2 class="sub-title">Key Characteristics of Stacks</h2>
    <ul class="characteristics-list">
      <li><strong>LIFO Structure:</strong> Stacks operate on the Last In First Out (LIFO) principle.</li>
      <li><strong>Push and Pop Operations:</strong> Elements are added using the push operation and removed using the pop operation.</li>
      <li><strong>No Random Access:</strong> Only the top element can be accessed directly.</li>
    </ul>

    <h2 class="sub-title">Diagram of a Stack</h2>
    <img src="@/assets/stack.png" alt="Stack Diagram" class="stack-diagram imageedit" />

    <h2 class="sub-title">Types of Stacks</h2>
    <h3 class="type-title">Simple Stack</h3>
    <p>A basic stack where elements are added to the top and removed from the top.</p>

    <h3 class="type-title">Double-Ended Stack</h3>
    <p>A stack that allows pushing and popping from both ends.</p>

    <h3 class="type-title">Circular Stack</h3>
    <p>A stack that treats the end of the stack as connected to the beginning, forming a circular structure.</p>

    <h2 class="sub-title">Stack Operations</h2>
    <p>Common operations performed on stacks include push, pop, peek (view the top element), and checking if the stack is empty.</p>

    <h2 class="sub-title">Examples</h2>
    <p>Click the buttons below to see examples of stacks in different programming languages:</p>
    <div class="button-container">
      <button @click="showExample('java')" class="example-button">Example in Java</button>
      <button @click="showExample('c')" class="example-button">Example in C</button>
      <button @click="showExample('python')" class="example-button">Example in Python</button>
    </div>
    <pre v-if="exampleCode">
      <code>{{ exampleCode }}</code>
    </pre>

    <h2 class="sub-title">AI-Powered Study Companion</h2>
    <div class="ai-notes-section">
      <button 
        @click="generateAINotes" 
        class="example-button ai-notes-button" 
        :disabled="isGenerating"
      >
        {{ isGenerating ? 'Generating AI Study Guide...' : 'Generate AI Study Guide' }}
      </button>

      <div v-if="aiNotesData" class="ai-notes-display">
        <h3 class="section-title">📘 Comprehensive Study Notes</h3>
        <div class="notes-content">
          <p><strong>1. Introduction and Characteristics:</strong></p>
          <p>{{ aiNotesData.introduction }}</p>

          <p><strong>2. Types of Stacks:</strong></p>
          <ul>
            <li>{{ aiNotesData.types.simple }}</li>
            <li>{{ aiNotesData.types.doubleEnded }}</li>
            <li>{{ aiNotesData.types.circular }}</li>
          </ul>

          <p><strong>3. Common Operations with Details:</strong></p>
          <ul>
            <li v-for="(operation, index) in aiNotesData.operations" :key="index">
              {{ operation }}
            </li>
          </ul>

          <p><strong>4. Practical Applications:</strong></p>
          <p>{{ aiNotesData.applications }}</p>
        </div>

        <h3 class="section-title">🎯 Key Concepts</h3>
        <ul>
          <li v-for="(concept, index) in aiNotesData.keyConcepts" :key="index">
            {{ concept }}
          </li>
        </ul>

        <h3 class="section-title">💡 Interview Questions</h3>
        <ul>
          <li v-for="(question, index) in aiNotesData.interviewQuestions" :key="index">
            Q{{ index + 1 }}: {{ question }}
          </li>
        </ul>

        <h3 class="section-title">🎥 Recommended Tutorials</h3>
        <ul>
          <li v-for="(tutorial, index) in aiNotesData.tutorialLinks" :key="index">
            <a :href="tutorial.url" target="_blank">{{ tutorial.description }}</a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Stack",
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
        this.exampleCode = `import java.util.Stack;
Stack<Integer> stack = new Stack<>();
stack.push(1);
System.out.println(stack.peek()); // Output: 1`;
      } else if (language === "c") {
        this.exampleCode = `#include<stdio.h>
#define MAX 10
int stack[MAX], top = -1;
void push(int val) {
    if (top == MAX - 1) printf("Stack Overflow");
    else stack[++top] = val;
}`;
      } else if (language === "python") {
        this.exampleCode = `class Stack:
    def __init__(self):
        self.stack = []
    def push(self, data):
        self.stack.append(data)
stack = Stack()
stack.push(5)`;
      }
    },

    async generateAINotes() {
      this.isGenerating = true;
      this.aiNotesData = null;

      const prompt = `
        Generate detailed programming notes about Stacks, including:
        1. A comprehensive introduction and characteristics of Stacks.
        2. An in-depth explanation of different types of Stacks.
        3. Detailed descriptions of common operations on Stacks with time complexity.
        4. Extensive practical applications of Stacks in computer science.
        5. Key interview questions and coding challenges for mastering the concept.
        6. A curated list of tutorials and resources for deeper understanding.
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
          const aiResponse = response.data.choices[0].message.content;
          this.aiNotesData = this.parseNotes(aiResponse);
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

    parseNotes(response) {
      return {
        introduction: "Stacks are fundamental data structures used in programming to manage data in a LIFO manner...",
        types: {
          simple: "A Simple Stack supports basic LIFO operations such as push, pop, and peek.",
          doubleEnded: "A Double-Ended Stack allows insertion and deletion from both ends.",
          circular: "A Circular Stack connects the end of the stack back to the beginning, forming a loop.",
        },
        operations: [
          "Push an element: O(1) complexity for adding an element at the top.",
          "Pop an element: O(1) complexity for removing the top element.",
          "Peek at the top element: O(1) complexity for viewing the top element.",
        ],
        applications: "Stacks are used in expression evaluation, backtracking algorithms, and managing function calls in recursion.",
        keyConcepts: [
          "LIFO Principle",
          "Push and Pop Operations",
          "No Random Access",
          "Dynamic Memory Usage",
        ],
        interviewQuestions: [
          "Implement a stack using arrays.",
          "Describe a use case for a stack in real-world applications.",
          "Write a program to evaluate a postfix expression using a stack.",
        ],
        tutorialLinks: [
          {
            description: "Comprehensive Stack Guide on GeeksforGeeks",
            url: "https://www.geeksforgeeks.org/stack-data-structure/",
          },
          {
            description: "YouTube Tutorial: Mastering Stacks",
            url: "https://www.youtube.com/results?search_query=stacks",
          },
        ],
      };
    },
  },
};
</script>

<style scoped>
.stack-container {
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

.type-title {
  font-size: 1.5em;
  color: #e0ce46;
  margin-top: 25px;
}

.intro {
  font-size: 1.3em;
  margin-bottom: 25px;
}

.characteristics-list {
  margin: 10px 0;
  padding-left: 20px;
  font-size: 1.2em;
}

.stack-diagram {
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

.ai-notes-display {
  background: #1e1e1e;
  padding: 20px;
  border-radius: 10px;
  margin-top: 20px;
  color: #ffffff;
}

.imageedit {
  margin: 10px; /* Adds space around each image */
  padding: 5px; /* Optional: Adds inner space within the image border */
  border: 1px solid #ccc; /* Optional: Adds a border for better visibility */
}

.section-title {
  font-size: 1.8em;
  color: #ffcc00;
  margin-bottom: 10px;
}

.notes-content {
  margin-top: 15px;
  line-height: 1.6;
}

ul {
  margin-left: 20px;
}

a {
  color: #e0ce46;
  text-decoration: none;
  font-size: 1.1em;
}

a:hover {
  text-decoration: underline;
}
</style>