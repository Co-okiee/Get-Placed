<template>
    <div class="queue-container">
      <h1 class="main-title">Queues</h1>
      <p class="intro">
        A queue is a linear data structure that follows the First In First Out (FIFO) principle, where the first element added is the first to be removed.
      </p>
  
      <h2 class="sub-title">Key Characteristics of Queues</h2>
      <ul class="characteristics-list">
        <li><strong>FIFO Structure:</strong> Queues operate on the First In First Out (FIFO) principle.</li>
        <li><strong>Enqueue and Dequeue Operations:</strong> Elements are added using the enqueue operation and removed using the dequeue operation.</li>
        <li><strong>No Random Access:</strong> Only the front and rear elements can be accessed directly.</li>
      </ul>
  
      <h2 class="sub-title">Diagram of a Queue</h2>
      <img src="@/assets/queue.png" alt="Queue Diagram" class="queue-diagram"/>
  
      <h2 class="sub-title">Types of Queues</h2>
      <h3 class="type-title">Simple Queue</h3>
      <p>A basic queue where elements are added to the rear and removed from the front.</p>
  
      <h3 class="type-title">Circular Queue</h3>
      <p>A queue where the rear of the queue wraps around to the front, forming a circular structure.</p>
  
      <h3 class="type-title">Priority Queue</h3>
      <p>A queue where elements are removed based on priority rather than the order they were added.</p>
  
      <h2 class="sub-title">Queue Operations</h2>
      <p>Common operations performed on queues include enqueue, dequeue, peek (view the front element), and checking if the queue is empty.</p>
  
      <h2 class="sub-title">Queue Functions</h2>
      <p>Key functions include enqueuing elements, dequeuing elements, and checking if the queue is full or empty.</p>
  
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
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=queue1" target="_blank">Queues in Java (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=queue2" target="_blank">Queues in Hindi</a></li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "Queue",
    data() {
      return {
        exampleCode: "",
      };
    },
    methods: {
      showExample(language) {
        if (language === 'java') {
          this.exampleCode = `import java.util.LinkedList;
  Queue<Integer> queue = new LinkedList<>();
  queue.add(1);
  System.out.println(queue.peek()); // Output: 1`;
        } else if (language === 'c') {
          this.exampleCode = `#include<stdio.h>
  #define MAX 10
  int queue[MAX], front = -1, rear = -1;
  void enqueue(int val) {
      if (rear == MAX - 1) printf("Queue Overflow");
      else queue[++rear] = val;
  }`;
        } else if (language === 'python') {
          this.exampleCode = `class Queue:
      def __init__(self):
          self.queue = []
      def enqueue(self, data):
          self.queue.append(data)
  queue = Queue()
  queue.enqueue(5)`;
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
  
  .queue-diagram {
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
  