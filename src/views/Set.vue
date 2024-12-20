<template>
  <div class="set-container">
    <h1 class="main-title">Sets</h1>
    <p class="intro">
      A set is a collection of distinct elements, meaning it does not allow duplicate values. Sets are widely used to represent unique items like tags or categories.
    </p>

    <h2 class="sub-title">Key Characteristics of Sets</h2>
    <ul class="characteristics-list">
      <li><strong>Uniqueness:</strong> Each element in a set must be unique; duplicates are not allowed.</li>
      <li><strong>Unordered:</strong> The elements in a set do not follow a specific order.</li>
      <li><strong>Dynamic Size:</strong> Sets can dynamically grow or shrink as elements are added or removed.</li>
    </ul>

    <h2 class="sub-title">Diagram of a Set</h2>
<img src="@/assets/set.png" alt="Set Diagram" class="set-diagram imageedit" />

    <h2 class="sub-title">Types of Sets</h2>
    <h3 class="type-title">Finite Set</h3>
    <p>A set with a limited number of elements.</p>

    <h3 class="type-title">Infinite Set</h3>
    <p>A set with an unlimited number of elements.</p>

    <h3 class="type-title">Subset</h3>
    <p>A set that contains some or all elements of another set.</p>

    <h2 class="sub-title">Set Operations</h2>
    <ul>
      <li><strong>Union:</strong> Combines elements from two sets.</li>
      <li><strong>Intersection:</strong> Returns elements that are common to both sets.</li>
      <li><strong>Difference:</strong> Returns elements in one set but not in the other.</li>
      <li><strong>Symmetric Difference:</strong> Returns elements in either of the sets but not in both.</li>
    </ul>

    <h2 class="sub-title">Examples</h2>
    <p>Click on the buttons below to see examples of sets in different programming languages:</p>
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

    <h2 class="sub-title">Useful Links</h2>
    <h3 class="link-title">YouTube Tutorials</h3>
    <ul class="link-list">
      <li>
        <a href="https://www.youtube.com/watch?v=set1" target="_blank">
          Sets in Java (English)
        </a>
      </li>
      <li>
        <a href="https://www.youtube.com/watch?v=set2" target="_blank">
          Sets in Hindi
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Set",
  data() {
    return {
      exampleCode: "",
      aiNotesData: null,
      isGenerating: false,
      groqApiKey: "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", // Replace with your actual Groq API key
    };
  },
  methods: {
    showExample(language) {
      if (language === "java") {
        this.exampleCode = `import java.util.HashSet;

class SetExample {
    public static void main(String[] args) {
        HashSet<Integer> set = new HashSet<>();
        set.add(1);
        set.add(2);
        set.add(3);
        set.add(1); // Duplicate, will not be added

        System.out.println(set); // Output: [1, 2, 3]
    }
}`;
      } else if (language === "c") {
        this.exampleCode = `#include <stdio.h>
#include <stdlib.h>

#define MAX_ELEMENTS 100

struct Set {
    int elements[MAX_ELEMENTS];
    int size;
};

void add(struct Set* set, int element) {
    for (int i = 0; i < set->size; i++) {
        if (set->elements[i] == element) {
            return; // Element already exists
        }
    }
    set->elements[set->size++] = element;
}`;
      } else if (language === "python") {
        this.exampleCode = `# Creating a set in Python
my_set = {1, 2, 3}
my_set.add(4)
my_set.add(1)  # Duplicate, will not be added

print(my_set)  # Output: {1, 2, 3, 4}`;
      }
    },

    async generateAINotes() {
      this.isGenerating = true;
      this.aiNotesData = null;

      const prompt = `
        Generate detailed programming notes about Sets, including:
        1. Introduction to Sets and their importance.
        2. Types of Sets with examples.
        3. Key operations like Union, Intersection, Difference, and Symmetric Difference with examples.
        4. Real-world applications of Sets.
        5. Key interview questions and practical coding challenges.
        6. A curated list of YouTube tutorials with clickable links.
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
            .replace(/(https?:\/\/[^\s<]+)(?=[\s<]|$)/g, '<a href="$1" target="_blank">$1</a>');
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
.set-container {
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

.pre {
  background-color: #1f1f1f;
  padding: 10px;
  border-radius: 5px;
  overflow-x: auto;
  color: #00ff00;
  font-size: 1.2em;
}

.ai-notes-display {
  margin-top: 20px;
  background: #1f1f1f;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.link-list a {
  color: #ddc452;
  text-decoration: none;
}

.link-list a:hover {
  text-decoration: underline;
}
</style>