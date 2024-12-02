<template>
  <div class="algorithm-container">
    <h1 class="main-title">Graph Algorithms</h1>
    <p class="intro">
      Graph algorithms solve problems related to graphs, collections of nodes (vertices) connected by edges. They are used in applications like shortest path calculation, cycle detection, and graph traversal.
    </p>

    <h2 class="sub-title">Key Concepts in Graph Algorithms</h2>
    <ul class="characteristics-list">
      <li><strong>Graph Representation:</strong> Represented as adjacency matrices or adjacency lists depending on storage and performance requirements.</li>
      <li><strong>Directed and Undirected Graphs:</strong> Directed graphs have edges with a specific direction, while undirected graphs do not.</li>
      <li><strong>Weighted and Unweighted Graphs:</strong> Weighted graphs have weights assigned to edges, influencing algorithms like Dijkstra's.</li>
    </ul>

  

    <h2 class="sub-title">Example Graph Algorithms</h2>
    <p>Select an algorithm to view its code:</p>
    <div class="button-container">
      <button @click="showAlgorithm('bfs')" class="example-button">Breadth-First Search (BFS)</button>
      <button @click="showAlgorithm('dfs')" class="example-button">Depth-First Search (DFS)</button>
      <button @click="showAlgorithm('dijkstra')" class="example-button">Dijkstra's Algorithm</button>
    </div>

    <pre v-if="algorithmExample">
      <code>{{ algorithmExample }}</code>
    </pre>

    <h2 class="sub-title">Generative Study Notes</h2>
    <div class="ai-notes-section">
      <button 
        @click="generateAINotes" 
        class="example-button ai-notes-button" 
        :disabled="isGenerating"
      >
        {{ isGenerating ? "Generating Study Notes..." : "Generate Study Notes" }}
      </button>
      <div v-if="aiNotesData" class="ai-notes-display">
        <h3 class="section-title">AI Study Notes</h3>
        <div v-html="aiNotesData"></div>
      </div>
    </div>

    <h2 class="sub-title">Useful Resources</h2>
    <ul class="resource-links">
      <li><a href="https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/" target="_blank">GeeksforGeeks - Graph Algorithms</a></li>
      <li><a href="https://www.youtube.com/watch?v=pcKY4hjDrxk" target="_blank">YouTube - Graph Algorithms Explained</a></li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "GraphAlgorithms",
  data() {
    return {
      algorithmExample: "",
      aiNotesData: null,
      isGenerating: false,
      groqApiKey: "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"
    };
  },
  methods: {
    showAlgorithm(type) {
      if (type === "bfs") {
        this.algorithmExample = `// BFS Algorithm
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
      } else if (type === "dfs") {
        this.algorithmExample = `// DFS Algorithm
void DFS(int node, boolean[] visited) {
  visited[node] = true;
  System.out.print(node + " ");
  for (int adjacent : adj[node]) {
    if (!visited[adjacent]) {
      DFS(adjacent, visited);
    }
  }
}`;
      } else if (type === "dijkstra") {
        this.algorithmExample = `// Dijkstra's Algorithm
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

    async generateAINotes() {
      this.isGenerating = true;
      this.aiNotesData = null;
      const prompt = `
        Provide a study guide on graph algorithms with the following:
        - Key concepts: Graph representation, directed vs. undirected, weighted vs. unweighted graphs.
        - Practical applications and use cases.
        - Examples: BFS, DFS, Dijkstra's algorithm.
        - Common challenges and solutions.
        - Recommended resources with clickable links.
      `;
      try {
        const response = await axios.post(
          "https://api.groq.com/openai/v1/chat/completions",
          {
            model: "mixtral-8x7b-32768",
            messages: [{ role: "user", content: prompt }],
            temperature: 0.8,
            max_tokens: 3000,
          },
          {
            headers: {
              Authorization: `Bearer ${this.groqApiKey}`,
              "Content-Type": "application/json"
            }
          }
        );
        if (response.data && response.data.choices && response.data.choices.length > 0) {
          const formattedResponse = response.data.choices[0].message.content
            .replace(/\n/g, "<br>")
            .replace(/(\d\.\s)/g, "<b>$1</b>")
            .replace(
              /(https?:\/\/[^\s]+)/g,
              `<a href="$1" target="_blank" style="color:#00ffcc;">$1</a>`
            );
          this.aiNotesData = `<div style="text-align: left;">${formattedResponse}</div>`;
        } else {
          throw new Error("Invalid response from API");
        }
      } catch (error) {
        console.error("Error generating AI notes:", error.message);
        alert("Failed to generate AI notes. Please try again.");
      } finally {
        this.isGenerating = false;
      }
    }
  }
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


.intro {
  font-size: 1.3em;
  margin-bottom: 25px;
}

.characteristics-list {
  margin: 10px 0;
  padding-left: 20px;
  font-size: 1.2em;
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

.ai-notes-section {
  margin-top: 30px;
  text-align: center;
}

.ai-notes-display {
  background-color: #1f1f1f;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
  margin-top: 20px;
}

.ai-notes-display a {
  color: #00ffcc;
  text-decoration: underline;
}

.resource-links a {
  color: #e0ce46;
  text-decoration: none;
}

.resource-links a:hover {
  color: #fff;
}
</style>