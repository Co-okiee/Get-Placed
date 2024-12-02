<template>
  <div class="graph-container">
    <h1 class="main-title">Graphs</h1>
    <p class="intro">
      A graph is a non-linear data structure consisting of nodes (vertices) and edges connecting pairs of nodes. Graphs are versatile and can represent various real-world problems, including social networks, transportation routes, and dependency structures.
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
    <p>Graphs can be represented in multiple ways, including adjacency lists and adjacency matrices, each suitable for different applications.</p>

    <h2 class="sub-title">Graph Traversal Algorithms</h2>
    <p>Common graph traversal algorithms include Depth-First Search (DFS) for exploring paths and Breadth-First Search (BFS) for level-wise exploration.</p>

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

    <h2 class="sub-title">Generative Study Companion</h2>
    <div class="ai-notes-section">
      <button 
        @click="generateAINotes" 
        class="example-button ai-notes-button" 
        :disabled="isGenerating"
      >
        {{ isGenerating ? "Generating Study Guide..." : "Generate Study Guide" }}
      </button>

      <div v-if="aiNotesData" class="ai-notes-display">
        <h3 class="section-title">📘 Comprehensive Study Notes</h3>
        <div v-html="aiNotesData"></div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Graph",
  data() {
    return {
      exampleCode: "",
      aiNotesData: null,
      isGenerating: false,
      groqApiKey: "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", // Replace with your actual API key
    };
  },
  methods: {
    showExample(language) {
      if (language === "java") {
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
      } else if (language === "c") {
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
      } else if (language === "python") {
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

    async generateAINotes() {
      this.isGenerating = true;
      this.aiNotesData = null;

      const prompt = `
        Generate well-structured programming notes about Graphs, including:
        1. A detailed introduction to Graphs and their importance in computer science.
        2. Types of Graphs (Undirected, Directed, Weighted) with examples.
        3. Explanation of Graph representation methods (Adjacency List, Adjacency Matrix) with syntax in Python, Java, and C.
        4. Real-world applications of Graphs in routing, scheduling, and dependency tracking.
        5. Key interview questions and practical coding challenges with sample solutions.
        6. A list of curated resources for further learning (tutorials, articles, and books).
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
              "Content-Type": "application/json",
            },
          }
        );

        if (response.data && response.data.choices && response.data.choices.length > 0) {
          const formattedResponse = response.data.choices[0].message.content
            .replace(/\n/g, "<br>")
            .replace(/•/g, "&nbsp;&nbsp;&nbsp;•")
            .replace(/(\d\.\s)/g, "<b>$1</b>")
            .replace(
              /(https?:\/\/[^\s]+)/g,
              `<a href="$1" target="_blank" style="color:#00ffcc;">$1</a>`
            );
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
.graph-container {
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

.characteristics-list {
  margin: 10px 0;
  padding-left: 20px;
  font-size: 1.2em;
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
</style>