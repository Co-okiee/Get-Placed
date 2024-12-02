<template>
  <div class="sorting-container">
    <h1 class="main-title">Sorting Algorithms</h1>
    <p class="intro">
      A sorting algorithm is a method to arrange elements in a list in a specific order, typically in ascending or descending order. Efficient sorting is important for optimizing the performance of other algorithms (like search algorithms) that require sorted data.
    </p>

    <h2 class="sub-title">Types of Sorting Algorithms</h2>
    <h3 class="type-title">1. Bubble Sort</h3>
    <p>Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order. It is simple but inefficient for large datasets.</p>
    
    <h3 class="type-title">2. Selection Sort</h3>
    <p>Selection Sort repeatedly selects the smallest (or largest) element from the unsorted portion of the list and moves it to the sorted portion.</p>
    

    <h3 class="type-title">3. Insertion Sort</h3>
    <p>Insertion Sort builds the sorted list one element at a time by inserting each new element into its correct position within the already sorted part of the list.</p>
    
    <img src="@/assets/sorting.png" alt=" Sorting Diagram" class="sorting-diagram imageedit" />


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
  name: "SortingAlgorithms",
  data() {
    return {
      declarationCode: "",
      aiNotesData: null,
      isGenerating: false,
      groqApiKey: "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"
    };
  },
  methods: {
    showDeclaration(language) {
      if (language === "java") {
        this.declarationCode = `// Bubble Sort in Java
void bubbleSort(int arr[]) {
  int n = arr.length;
  for (int i = 0; i < n-1; i++)
    for (int j = 0; j < n-i-1; j++)
      if (arr[j] > arr[j+1]) {
        int temp = arr[j];
        arr[j] = arr[j+1];
        arr[j+1] = temp;
      }
}`;
      } else if (language === "c") {
        this.declarationCode = `// Bubble Sort in C
void bubbleSort(int arr[], int n) {
  for (int i = 0; i < n-1; i++)
    for (int j = 0; j < n-i-1; j++)
      if (arr[j] > arr[j+1]) {
        int temp = arr[j];
        arr[j] = arr[j+1];
        arr[j+1] = temp;
      }
}`;
      } else if (language === "python") {
        this.declarationCode = `# Bubble Sort in Python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]`;
      }
    },
    async generateAINotes() {
      this.isGenerating = true;
      this.aiNotesData = null;
      const prompt = `
        Generate a detailed study guide on sorting algorithms, including:
        Explanation of key sorting algorithms (Bubble Sort, Quick Sort, Merge Sort, Heap Sort).
        Comparison of their time and space complexities with practical examples.
        Practical applications and the importance of sorting in programming.
        Key interview questions with solutions and example coding challenges.
        A list of curated learning resources with clickable links.
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
    }
  }
};
</script>

<style scoped>
.sorting-container {
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

.sorting-diagram {
  width: 100%;
  height: auto;
  margin: 30px 0;
  border: 1px solid #e0ce46;
}

.pre {
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
</style>