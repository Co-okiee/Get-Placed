<template>
  <div class="array-container">
    <h1 class="main-title">Arrays</h1>
    <p class="intro">
      An array is a collection of items stored at contiguous memory locations. It is used to store multiple values of the same data type under a single variable name. Arrays are widely used in programming for efficient data storage and manipulation.
    </p>

    <h2 class="sub-title">Key Characteristics of Arrays</h2>
    <ul class="characteristics-list">
      <li><strong>Fixed Size:</strong> The size of an array is defined at the time of declaration and cannot be altered later.</li>
      <li><strong>Homogeneous Elements:</strong> All elements in an array are of the same data type.</li>
      <li><strong>Random Access:</strong> Array elements can be accessed directly using their index.</li>
    </ul>

    <h2 class="sub-title">Diagram of an Array</h2>
    <img src="@/assets/Array.png" alt="Array Diagram" class="array-diagram imageedit" />

    <h2 class="sub-title">Types of Arrays</h2>
    <h3 class="type-title">One-Dimensional Array</h3>
    <p>A linear array where elements are stored in a single row or column.</p>

    <h3 class="type-title">Multi-Dimensional Array</h3>
    <p>Arrays with more than one dimension, such as 2D arrays (matrices).</p>

    <h3 class="type-title">Dynamic Array</h3>
    <p>An array whose size can be modified during runtime (e.g., ArrayList in Java).</p>

    <h2 class="sub-title">Array Operations</h2>
    <p>
      Common operations on arrays include traversal, insertion, deletion, sorting, and searching.
    </p>

    <h2 class="sub-title">Examples</h2>
    <p>Click on the buttons below to see examples of arrays in different programming languages:</p>

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
        {{ isGenerating ? 'Generating Study Guide...' : 'Generate Study Guide' }}
      </button>

      <div v-if="aiNotesData" class="ai-notes-display">
        <h3 class="section-title">📘 Comprehensive Study Notes</h3>
        <div class="formatted-ai-notes">
          <div v-html="aiNotesData"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Array",
  data() {
    return {
      exampleCode: "",
      aiNotesData: null,
      isGenerating: false,
      groqApiKey: "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",
    };
  },
  methods: {
    showExample(language) {
      if (language === "java") {
        this.exampleCode = `// Declaration of an array in Java
int[] numbers = {10, 20, 30, 40, 50};
System.out.println(numbers[0]); // Output: 10`;
      } else if (language === "c") {
        this.exampleCode = `// Declaration of an array in C
int numbers[] = {10, 20, 30, 40, 50};
printf("%d", numbers[0]); // Output: 10`;
      } else if (language === "python") {
        this.exampleCode = `# Declaration of an array in Python
numbers = [10, 20, 30, 40, 50]
print(numbers[0])  # Output: 10`;
      }
    },

    async generateAINotes() {
      this.isGenerating = true;
      this.aiNotesData = null;

      const prompt = `
        Generate comprehensive programming notes about Arrays, including:
        1. A detailed introduction and characteristics of Arrays.
        2. Common operations on Arrays with examples.
        3. Practical applications of Arrays in programming.
        4. Key interview questions and coding challenges.
        5. A curated list of resources for learning more about Arrays.
        Ensure the content is well-formatted and includes clickable links for resources.
      `;

      try {
        const response = await axios.post(
          "https://api.groq.com/openai/v1/chat/completions",
          {
            model: "mixtral-8x7b-32768",
            messages: [{ role: "user", content: prompt }],
            temperature: 0.7,
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
              `<a href="$1" target="_blank" style="color:#00ffcc; text-decoration:underline;">$1</a>`
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
.array-container {
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
  border-radius: 10px;
  background-color: #121212;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.6);
  font-family: "Roboto", sans-serif;
  color: #f5f5f5;
  line-height: 1.6;
}

.main-title {
  font-size: 4em;
  color: #ccc;
  text-align: center;
  margin-bottom: 30px;
}

.sub-title {
  font-size: 1.5em;
  color: #0d9bbb;
  margin-top: 40px;
  padding-bottom: 10px;
}

.type-title {
  font-size: 1.5em;
  color: #ffcc00;
  margin-top: 25px;
}

.characteristics-list {
  margin: 10px 0;
  padding-left: 20px;
  font-size: 1.2em;
}

.array-diagram {
  width: 100%;
  height: auto;
  margin: 30px 0;
  border: 1px solid #555;
  border-radius: 5px;
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

.imageedit {
  margin: 10px; /* Adds space around each image */
  padding: 5px; /* Optional: Adds inner space within the image border */
  border: 1px solid #ccc; /* Optional: Adds a border for better visibility */
}

.example-button:hover {
  background-color: #ffe066;
}

.ai-notes-display {
  margin-top: 20px;
  background: #1c1c1c;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.formatted-ai-notes div {
  text-align: justify;
  line-height: 1.8;
  color: #e6e6e6;
}

.ai-notes-button {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  background-color: #28a745;
  color: #fff;
  cursor: pointer;
  font-size: 1em;
  transition: background-color 0.3s;
}

.ai-notes-button:hover {
  background-color: #218838;
}

.ai-notes-display a {
  color: #00ffcc;
  text-decoration: underline;
}
</style>