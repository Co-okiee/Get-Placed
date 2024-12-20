<!-- src/views/GraphAlgorithms.vue -->
<template>
    <div class="algorithm-container">
      <h1 class="main-title">Graph Algorithms</h1>
      <p class="intro">
        Graph algorithms are a set of algorithms designed to solve problems related to graphs, which are a collection of nodes (vertices) connected by edges. These algorithms are used in various applications such as finding the shortest path, detecting cycles, and searching through a graph structure.
      </p>
  
      <h2 class="sub-title">Key Concepts in Graph Algorithms</h2>
      <ul class="characteristics-list">
        <li><strong>Graph Representation:</strong> Graphs can be represented in different ways, such as an adjacency matrix or an adjacency list, depending on the use case and storage requirements.</li>
        <li><strong>Directed and Undirected Graphs:</strong> In directed graphs, edges have a direction, while in undirected graphs, edges do not. The type of graph affects how algorithms traverse and process the graph.</li>
        <li><strong>Weighted and Unweighted Graphs:</strong> Some graphs have weights associated with edges, and algorithms like Dijkstra's are designed to work on such graphs.</li>
      </ul>
  
      <h2 class="sub-title">Diagram for Graph Traversal</h2>
      <img src="@/assets/graph-diagram.png" alt="Graph Traversal Diagram" class="algorithm-diagram"/>
  
      <h2 class="sub-title">Example Graph Algorithms</h2>
      <p>Select a category of graph algorithms to see examples:</p>
  
      <div class="button-container">
        <button @click="showAlgorithm('bfs')" class="example-button">Breadth-First Search (BFS)</button>
        <button @click="showAlgorithm('dfs')" class="example-button">Depth-First Search (DFS)</button>
        <button @click="showAlgorithm('dijkstra')" class="example-button">Dijkstra's Algorithm</button>
      </div>
  
      <pre v-if="algorithmExample">
        <code>{{ algorithmExample }}</code>
      </pre>
  
      <h2 class="sub-title">Types of Graph Algorithms</h2>
      <h3 class="type-title">Traversal Algorithms</h3>
      <p>Traversal algorithms explore the graph, visiting nodes in a specific order. Common algorithms include BFS and DFS.</p>
  
      <h3 class="type-title">Shortest Path Algorithms</h3>
      <p>Shortest path algorithms find the shortest path between two vertices. Dijkstra's and Bellman-Ford algorithms are commonly used for this.</p>
  
      <h3 class="type-title">Minimum Spanning Tree Algorithms</h3>
      <p>Algorithms like Prim's and Kruskal's are used to find a minimum spanning tree, connecting all vertices with the least total edge weight.</p>
  
      <h2 class="sub-title">Advantages of Graph Algorithms</h2>
      <ul>
        <li>Help in efficiently solving real-world problems such as network routing, scheduling, and social network analysis.</li>
        <li>Various algorithms can handle different types of graphs and specific problems, offering flexibility in use.</li>
        <li>They can find optimal solutions, such as the shortest path or the minimum spanning tree.</li>
      </ul>
  
      <h2 class="sub-title">Disadvantages of Graph Algorithms</h2>
      <ul>
        <li>For very large graphs, algorithms can be computationally expensive in terms of both time and space.</li>
        <li>Some graph problems are NP-complete, meaning they cannot be solved efficiently for large inputs.</li>
        <li>Choosing the right graph representation can impact performance and complexity.</li>
      </ul>
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=pcKY4hjDrxk" target="_blank">Graph Algorithms Tutorial (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=AZb2TptYox8" target="_blank">Graph Algorithms in Hindi</a></li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "GraphAlgorithms",
    data() {
      return {
        algorithmExample: "",
      };
    },
    methods: {
      showAlgorithm(type) {
        if (type === 'bfs') {
          this.algorithmExample = `// Example of BFS Algorithm
  void BFS(int start) {
    boolean[] visited = new boolean[V];
    Queue<Integer> queue = new LinkedList<>();
    
    visited[start] = true;
    queue.add(start);
    
    while (!queue.isEmpty()) {
      int node = queue.poll();
      System.out.print(node + " ");
      
      for (int adjacent : adj[node]) {
        if (!visited[adjacent]) {
          visited[adjacent] = true;
          queue.add(adjacent);
        }
      }
    }
  }`;
        } else if (type === 'dfs') {
          this.algorithmExample = `// Example of DFS Algorithm
  void DFS(int node, boolean[] visited) {
    visited[node] = true;
    System.out.print(node + " ");
    
    for (int adjacent : adj[node]) {
      if (!visited[adjacent]) {
        DFS(adjacent, visited);
      }
    }
  }`;
        } else if (type === 'dijkstra') {
          this.algorithmExample = `// Example of Dijkstra's Algorithm
  void Dijkstra(int src) {
    int[] dist = new int[V];
    boolean[] visited = new boolean[V];
    
    Arrays.fill(dist, Integer.MAX_VALUE);
    dist[src] = 0;
    
    for (int i = 0; i < V - 1; i++) {
      int u = selectMinVertex(dist, visited);
      visited[u] = true;
      
      for (int v = 0; v < V; v++) {
        if (!visited[v] && adj[u][v] != 0 && dist[u] != Integer.MAX_VALUE
            && dist[u] + adj[u][v] < dist[v]) {
          dist[v] = dist[u] + adj[u][v];
        }
      }
    }
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