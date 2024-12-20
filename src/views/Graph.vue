<template>
    <div class="graph-container">
      <h1 class="main-title">Graphs</h1>
      <p class="intro">
        A graph is a non-linear data structure consisting of nodes (vertices) and edges connecting pairs of nodes. Graphs can represent various structures, such as social networks, road maps, and more.
      </p>
  
      <h2 class="sub-title">Key Characteristics of Graphs</h2>
      <ul class="characteristics-list">
        <li><strong>Vertices and Edges:</strong> A graph is made up of vertices (nodes) and edges (connections between nodes).</li>
        <li><strong>Directed and Undirected:</strong> Edges can be directed (one-way) or undirected (two-way).</li>
        <li><strong>Weighted and Unweighted:</strong> Edges can have weights (costs) or be unweighted.</li>
      </ul>
  
      <h2 class="sub-title">Types of Graphs</h2>
      <h3 class="type-title">Undirected Graph</h3>
      <p>A graph where the edges have no direction. The relationship between vertices is bidirectional.</p>
  
      <h3 class="type-title">Directed Graph (Digraph)</h3>
      <p>A graph where the edges have a direction. The relationship is one-way.</p>
  
      <h3 class="type-title">Weighted Graph</h3>
      <p>A graph where edges have weights associated with them, indicating costs or distances.</p>
  
      <h2 class="sub-title">Graph Representation</h2>
      <p>Graphs can be represented in multiple ways, including adjacency lists and adjacency matrices.</p>
      
      <h2 class="sub-title">Graph Traversal Algorithms</h2>
      <p>Common graph traversal algorithms include Depth-First Search (DFS) and Breadth-First Search (BFS).</p>
  
      <h2 class="sub-title">Examples</h2>
      <p>Click on the buttons below to see examples of graphs in different programming languages:</p>
  
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
        <li><a href="https://www.youtube.com/watch?v=graph1" target="_blank">Graphs in Java (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=graph2" target="_blank">Graphs in Hindi</a></li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "Graph",
    data() {
      return {
        exampleCode: "",
      };
    },
    methods: {
      showExample(language) {
        if (language === 'java') {
          this.exampleCode = `import java.util.ArrayList;
  import java.util.List;
  
  class Graph {
      private List<List<Integer>> adjacencyList;
  
      public Graph(int vertices) {
          adjacencyList = new ArrayList<>(vertices);
          for (int i = 0; i < vertices; i++) {
              adjacencyList.add(new ArrayList<>());
          }
      }
  
      public void addEdge(int source, int destination) {
          adjacencyList.get(source).add(destination);
          adjacencyList.get(destination).add(source); // For undirected graph
      }
  }`;
        } else if (language === 'c') {
          this.exampleCode = `#include <stdio.h>
  #include <stdlib.h>
  
  #define MAX_VERTICES 100
  
  struct Graph {
      int vertices;
      int adjacencyMatrix[MAX_VERTICES][MAX_VERTICES];
  };
  
  void addEdge(struct Graph* graph, int src, int dest) {
      graph->adjacencyMatrix[src][dest] = 1;
      graph->adjacencyMatrix[dest][src] = 1; // For undirected graph
  }`;
        } else if (language === 'python') {
          this.exampleCode = `class Graph:
      def __init__(self):
          self.graph = {}
  
      def add_edge(self, u, v):
          if u not in self.graph:
              self.graph[u] = []
          if v not in self.graph:
              self.graph[v] = []
          self.graph[u].append(v)
          self.graph[v].append(u)  # For undirected graph
  
  g = Graph()
  g.add_edge(1, 2)`;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .graph-container {
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
  