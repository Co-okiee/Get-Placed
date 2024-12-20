<!-- src/views/GreedyAlgorithms.vue -->
<template>
    <div class="algorithm-container">
      <h1 class="main-title">Greedy Algorithms</h1>
      <p class="intro">
        Greedy algorithms build up a solution piece by piece, choosing the most immediate benefit at each step without considering the global context. It guarantees that the solution is optimal for some problems, but not all.
      </p>
  
      <h2 class="sub-title">Key Concepts in Greedy Algorithms</h2>
      <ul class="characteristics-list">
        <li><strong>Greedy Choice Property:</strong> A local optimum is chosen at every step with the hope of finding a global optimum.</li>
        <li><strong>Optimal Substructure:</strong> A problem is said to have an optimal substructure if an optimal solution to the problem contains optimal solutions to subproblems.</li>
      </ul>
  
      <h2 class="sub-title">Diagram for Greedy Algorithm</h2>
      <img src="@/assets/greedy-diagram.png" alt="Greedy Algorithm Diagram" class="algorithm-diagram"/>
  
      <h2 class="sub-title">Example Algorithms</h2>
      <p>Select a category of greedy algorithms to see examples:</p>
  
      <div class="button-container">
        <button @click="showAlgorithm('fractionalKnapsack')" class="example-button">Fractional Knapsack</button>
        <button @click="showAlgorithm('activitySelection')" class="example-button">Activity Selection</button>
        <button @click="showAlgorithm('huffmanCoding')" class="example-button">Huffman Coding</button>
      </div>
  
      <pre v-if="algorithmExample">
        <code>{{ algorithmExample }}</code>
      </pre>
  
      <h2 class="sub-title">Types of Greedy Problems</h2>
      <h3 class="type-title">Optimization Problems</h3>
      <p>Greedy algorithms are often used for optimization problems where the goal is to find the best solution among a set of feasible solutions.</p>
  
      <h3 class="type-title">Decision Problems</h3>
      <p>In decision problems, a greedy algorithm is used to decide on a sequence of choices to achieve a certain goal.</p>
  
      <h2 class="sub-title">Advantages of Greedy Algorithms</h2>
      <ul>
        <li>Greedy algorithms are simple and easy to understand and implement.</li>
        <li>They can provide optimal solutions to some types of problems, such as fractional knapsack and activity selection.</li>
        <li>Greedy algorithms are typically more time-efficient than dynamic programming approaches.</li>
      </ul>
  
      <h2 class="sub-title">Disadvantages of Greedy Algorithms</h2>
      <ul>
        <li>They do not always produce optimal solutions for all problems.</li>
        <li>Greedy algorithms focus only on local optima, which might not lead to the best global solution.</li>
        <li>Some problems may require backtracking or dynamic programming for the best solution.</li>
      </ul>
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=bUSaenttI24" target="_blank">Greedy Algorithms (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=2NQ85n7JIvM" target="_blank">Greedy Algorithms in Hindi</a></li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "GreedyAlgorithms",
    data() {
      return {
        algorithmExample: "",
      };
    },
    methods: {
      showAlgorithm(type) {
        if (type === 'fractionalKnapsack') {
          this.algorithmExample = `// Fractional Knapsack Algorithm
  int n = items.size();
  sort(items.begin(), items.end(), by_value_to_weight_ratio);
  double totalValue = 0;
  for (int i = 0; i < n; i++) {
    if (capacity >= items[i].weight) {
      totalValue += items[i].value;
      capacity -= items[i].weight;
    } else {
      totalValue += (items[i].value / items[i].weight) * capacity;
      break;
    }
  }`;
        } else if (type === 'activitySelection') {
          this.algorithmExample = `// Activity Selection Algorithm
  sort(activities, by_finish_time);
  int count = 1;
  int last_finish = activities[0].finish;
  for (int i = 1; i < activities.size(); i++) {
    if (activities[i].start >= last_finish) {
      count++;
      last_finish = activities[i].finish;
    }
  }
  return count;`;
        } else if (type === 'huffmanCoding') {
          this.algorithmExample = `// Huffman Coding Algorithm
  priority_queue<Node*, vector<Node*>, compare> minHeap;
  for (int i = 0; i < freq.size(); i++) {
    Node* newNode = new Node(characters[i], freq[i]);
    minHeap.push(newNode);
  }
  while (minHeap.size() != 1) {
    Node *left = minHeap.top(); minHeap.pop();
    Node *right = minHeap.top(); minHeap.pop();
    Node *newNode = new Node('$', left->freq + right->freq);
    newNode->left = left;
    newNode->right = right;
    minHeap.push(newNode);
  }`;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .algorithm-container {
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
    
    .algorithm-diagram {
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