<template>
    <div class="tree-container">
      <h1 class="main-title">Trees</h1>
      <p class="intro">
        A tree is a hierarchical data structure consisting of nodes, where each node has a value and references to its child nodes.
      </p>
  
      <h2 class="sub-title">Key Characteristics of Trees</h2>
      <ul class="characteristics-list">
        <li><strong>Hierarchical Structure:</strong> Trees are organized in levels where a parent node can have child nodes.</li>
        <li><strong>Root Node:</strong> The topmost node in the tree is called the root node, from which all other nodes descend.</li>
        <li><strong>Leaf Nodes:</strong> Nodes that do not have any children are called leaf nodes.</li>
      </ul>
  
      <h2 class="sub-title">Diagram of a Tree</h2>
      <img src="@/assets/tree.png" alt="Tree Diagram" class="tree-diagram"/>
  
      <h2 class="sub-title">Types of Trees</h2>
      <h3 class="type-title">Binary Tree</h3>
      <p>A tree where each node has at most two children, referred to as the left child and the right child.</p>
  
      <h3 class="type-title">Binary Search Tree (BST)</h3>
      <p>A binary tree where each node follows the property that all nodes in the left subtree are smaller, and all nodes in the right subtree are larger.</p>
  
      <h3 class="type-title">AVL Tree</h3>
      <p>A self-balancing binary search tree where the difference in heights between left and right subtrees is at most one.</p>
  
      <h2 class="sub-title">Tree Operations</h2>
      <p>Common operations performed on trees include insertion, deletion, traversal (in-order, pre-order, post-order), and searching for a specific value.</p>
  
      <h2 class="sub-title">Tree Functions</h2>
      <p>Key functions include inserting nodes, deleting nodes, and traversing the tree in different orders.</p>
  
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
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=tree1" target="_blank">Trees in Java (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=tree2" target="_blank">Trees in Hindi</a></li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "Tree",
    data() {
      return {
        exampleCode: "",
      };
    },
    methods: {
      showExample(language) {
        if (language === 'java') {
          this.exampleCode = `class Node {
      int value;
      Node left, right;
      public Node(int item) {
          value = item;
          left = right = null;
      }
  }
  Node root = new Node(10);`;
        } else if (language === 'c') {
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
        } else if (language === 'python') {
          this.exampleCode = `class Node:
      def __init__(self, data):
          self.data = data
          self.left = None
          self.right = None
  root = Node(10)`;
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
    font-family: 'Roboto', sans-serif;
    color: #e0e0e0;
    line-height: 1.6;
  }
  
  .main-title {
    font-size: 2.8em;
    color: #f8f8f8;
    text-align: center;
    margin-bottom: 30px;
  }
  
  .sub-title {
    font-size: 2em;
    color: #e0ce46;
    margin-top: 40px;
    padding-bottom: 10px;
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
  
  li {
    margin-bottom: 15px;
    line-height: 1.6;
  }
  
  .tree-diagram {
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
  
  a {
    color: #ddc452;
    text-decoration: none;
    font-size: 1.1em;
  }
  
  a:hover {
    text-decoration: underline;
  }
  
  .link-title {
    color: #ffffff;
    margin-top: 30px;
  }
  </style>
  