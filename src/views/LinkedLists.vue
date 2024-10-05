<template>
    <div class="linkedlist-container">
      <h1 class="main-title">Linked Lists</h1>
      <p class="intro">
        A linked list is a linear data structure where each element is a separate object. Each element (node) contains data and a reference (link) to the next node in the sequence.
      </p>
  
      <h2 class="sub-title">Key Characteristics of Linked Lists</h2>
      <ul class="characteristics-list">
        <li><strong>Dynamic Size:</strong> Linked lists can grow and shrink dynamically during execution.</li>
        <li><strong>Efficient Insertions/Deletions:</strong> Insertions and deletions can be performed efficiently without reorganizing the entire data structure.</li>
        <li><strong>No Direct Access:</strong> Elements cannot be accessed directly by their index; traversal is required to find specific elements.</li>
      </ul>
  
      <h2 class="sub-title">Diagram of a Linked List</h2>
      <img src="@/assets/ll.png" alt="Linked List Diagram" class="linkedlist-diagram"/>
  
      <h2 class="sub-title">Types of Linked Lists</h2>
      <h3 class="type-title">Singly Linked List</h3>
      <p>A linked list where each node points to the next node, and the last node points to null.</p>
  
      <h3 class="type-title">Doubly Linked List</h3>
      <p>A linked list where each node contains two references: one to the next node and another to the previous node.</p>
  
      <h3 class="type-title">Circular Linked List</h3>
      <p>A linked list where the last node points back to the first node, forming a circular structure.</p>
  
      <h2 class="sub-title">Linked List Operations</h2>
      <p>Common operations performed on linked lists include insertion, deletion, traversal, and searching.</p>
  
      <h2 class="sub-title">Linked List Functions</h2>
      <p>Key functions include adding nodes, removing nodes, and reversing the linked list.</p>
  
      <h2 class="sub-title">Examples</h2>
      <p>Click on the buttons below to see examples of linked lists in different programming languages:</p>
  
      <div class="button-container">
        <button @click="showExample('java')" class="example-button">Example in Java</button>
        <button @click="showExample('c')" class="example-button">Example in C</button>
        <button @click="showExample('python')" class="example-button">Example in Python</button>
      </div>
  
      <pre v-if="exampleCode">
        <code>{{ exampleCode }}</code>
      </pre>
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=abc123" target="_blank">Linked Lists in Java (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=xyz456" target="_blank">Linked Lists in Hindi</a></li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "LinkedList",
    data() {
      return {
        exampleCode: "",
      };
    },
    methods: {
      showExample(language) {
        if (language === 'java') {
          this.exampleCode = `// Declaration of a linked list in Java
  import java.util.LinkedList;
  LinkedList<String> list = new LinkedList<>();
  list.add("Node1");
  System.out.println(list.get(0)); // Output: Node1`;
        } else if (language === 'c') {
          this.exampleCode = `// Declaration of a linked list in C
  struct Node {
      int data;
      struct Node* next;
  };
  struct Node* head = NULL;`;
        } else if (language === 'python') {
          this.exampleCode = `# Declaration of a linked list in Python
  class Node:
      def __init__(self, data):
          self.data = data
          self.next = None`;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .linkedlist-container {
    max-width: 800px;
    margin: 20px auto;
    padding: 20px;
    border-radius: 10px;
    background-color: #121212; /* Dark background color */
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.6);
    font-family: 'Roboto', sans-serif; /* Updated font */
    color: #e0e0e0; /* Light text color for better readability */
    line-height: 1.6; /* Increased line height for better readability */
  }
  
  .main-title {
    font-size: 2.8em; /* Larger font size for main title */
    color: #f8f8f8; /* Bright color for the main title */
    text-align: center;
    margin-bottom: 30px; /* Increased margin for better spacing */
  }
  
  .sub-title {
    font-size: 2em; /* Larger font size for sub-titles */
    color: #e0ce46; /* Bright color for sub-titles */
    margin-top: 40px; /* Increased margin for better spacing */
    padding-bottom: 10px; /* Space below the sub-title */
  }
  
  .type-title {
    font-size: 1.5em; /* Larger font size for type titles */
    color: #e0ce46; /* Bright color for type titles */
    margin-top: 25px; /* Margin for type titles */
  }
  
  .intro {
    font-size: 1.3em; /* Increased font size for intro text */
    margin-bottom: 25px; /* Increased margin for better spacing */
  }
  
  .characteristics-list {
    margin: 10px 0;
    padding-left: 20px;
    font-size: 1.2em; /* Increased font size for list items */
  }
  
  li {
    margin-bottom: 15px; /* Increased margin for list items */
    line-height: 1.6; /* Increased line height for better readability */
  }
  
  .linkedlists-diagram {
    width: 100%;
    height: auto;
    margin: 30px 0; /* Increased margin for better spacing */
    border: 1px solid #444; /* Darker border for image */
    border-radius: 5px;
  }
  
  pre {
    background-color: #1f1f1f; /* Darker background for code */
    padding: 10px;
    border-radius: 5px;
    overflow-x: auto; /* Allow horizontal scrolling for long code */
    color: #00ff00; /* Green text color for code */
    font-size: 1.2em; /* Increased font size for code */
  }
  
  .button-container {
    display: flex;
    justify-content: space-around; /* Space buttons evenly */
    margin: 30px 0; /* Increased margin for better spacing */
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
  
  a {
    color: #ddc452; /* Link color */
    text-decoration: none; /* Remove underline */
    font-size: 1.1em; /* Increased font size for links */
  }
  
  a:hover {
    text-decoration: underline; /* Underline on hover */
  }
  
  .link-title {
    color: #ffffff; /* Bright color for link titles */
    margin-top: 30px; /* Increased margin for better spacing */
  }
  </style>
  
  