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
    <img src="@/assets/stack.png" alt="Stack Diagram" class="stack-diagram"/>

    <h2 class="sub-title">Types of Stacks</h2>
    <h3 class="type-title">Simple Stack</h3>
    <p>A basic stack where elements are added to the top and removed from the top.</p>

    <h3 class="type-title">Double-Ended Stack</h3>
    <p>A stack that allows pushing and popping from both ends.</p>

    <h3 class="type-title">Circular Stack</h3>
    <p>A stack that treats the end of the stack as connected to the beginning, forming a circular structure.</p>

    <h2 class="sub-title">Stack Operations</h2>
    <p>Common operations performed on stacks include push, pop, peek (view the top element), and checking if the stack is empty.</p>

    <h2 class="sub-title">Stack Functions</h2>
    <p>Key functions include pushing elements, popping elements, and checking if the stack is full or empty.</p>

    <h2 class="sub-title">Examples</h2>
    <p>Click on the buttons below to see examples of stacks in different programming languages:</p>

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
      <li><a href="https://www.youtube.com/watch?v=stack1" target="_blank">Stacks in Java (English)</a></li>
      <li><a href="https://www.youtube.com/watch?v=stack2" target="_blank">Stacks in Hindi</a></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "Stack",
  data() {
    return {
      exampleCode: "",
    };
  },
  methods: {
    showExample(language) {
      if (language === 'java') {
        this.exampleCode = `import java.util.Stack;
Stack<Integer> stack = new Stack<>();
stack.push(1);
System.out.println(stack.peek()); // Output: 1`;
      } else if (language === 'c') {
        this.exampleCode = `#include<stdio.h>
#define MAX 10
int stack[MAX], top = -1;
void push(int val) {
    if (top == MAX - 1) printf("Stack Overflow");
    else stack[++top] = val;
}`;
      } else if (language === 'python') {
        this.exampleCode = `class Stack:
    def __init__(self):
        self.stack = []
    def push(self, data):
        self.stack.append(data)
stack = Stack()
stack.push(5)`;
      }
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