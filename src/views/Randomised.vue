<template>
  <div class="randomized-container">
    <h1 class="main-title">Randomized Algorithms</h1>
    <p class="intro">
      Randomized algorithms make random choices during execution to achieve good performance on average, often simplifying problem-solving and improving efficiency.
    </p>

    <h2 class="sub-title">Key Characteristics of Randomized Algorithms</h2>
    <ul class="characteristics-list">
      <li><strong>Randomness:</strong> Utilizes random numbers to make decisions.</li>
      <li><strong>Averaged Performance:</strong> Often provides good average-case performance.</li>
      <li><strong>Simple Implementation:</strong> Can simplify complex algorithms by reducing the number of cases to consider.</li>
    </ul>

    <h2 class="sub-title">Diagram of Randomized Algorithms</h2>
    <img src="@/assets/randomised.png" alt="Randomized Algorithms Diagram" class="randomized-diagram imageedit"/>

    <h2 class="sub-title">Common Randomized Algorithms</h2>
    <h3 class="algorithm-title">Randomized QuickSort</h3>
    <p>Utilizes random pivot selection to improve the average case of the sorting algorithm.</p>

    <h3 class="algorithm-title">Randomized Selection</h3>
    <p>Finds the k-th smallest (or largest) element in an unordered list using random partitioning.</p>

    <h3 class="algorithm-title">Monte Carlo Methods</h3>
    <p>Employ random sampling to obtain numerical results for problems that might be deterministic in principle.</p>

    <h2 class="sub-title">Randomized Algorithms Examples</h2>
    <p>Click on the buttons below to see examples of randomized algorithms in different programming languages:</p>

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
<div class="ai-notes-content">
  <div class="notes-section">
    <h3 class="section-title">📘 Comprehensive Study Notes</h3>
    <p class="notes-text">{{ aiNotesData.studyNotes }}</p>
  </div>


      <div class="notes-section">
        <h3 class="section-title">🎯 Key Concepts</h3>
        <ul class="key-concepts-list">
          <li v-for="(concept, index) in aiNotesData.keyConcepts" :key="index">
            {{ concept }}
          </li>
        </ul>
      </div>

      <div class="notes-section">
        <h3 class="section-title">💡 Interview Questions</h3>
        <div class="interview-questions">
          <div 
            v-for="(question, index) in aiNotesData.interviewQuestions" 
            :key="index" 
            class="interview-question"
          >
            <strong>Q{{ index + 1 }}:</strong> {{ question }}
          </div>
        </div>
      </div>

      <div class="notes-section">
        <h3 class="section-title">🎥 Recommended Tutorials</h3>
        <div class="tutorial-links">
          <a 
            v-for="(tutorial, index) in aiNotesData.tutorialLinks" 
            :key="index"
            :href="tutorial.url"
            target="_blank"
            class="tutorial-link"
          >
            <span class="tutorial-platform">{{ tutorial.platform }}</span>
            <span class="tutorial-description">{{ tutorial.description }}</span>
          </a>
        </div>
      </div>

      <div class="notes-actions">
        <button @click="copyNotes" class="example-button copy-button">
          📋 Copy Study Guide
        </button>
        <button @click="downloadNotesPDF" class="example-button download-button">
          📥 Download PDF
        </button>
      </div>
    </div>
  </div>
</div>
</div>
</template>

<script>

import axios from 'axios';
import jspdf from 'jspdf';

export default {
name: "scalability",
data() {
return {
  exampleCode: "",
  aiNotesData: null,
  isGenerating: false,
  selectedTopic: "",
  selectedSubtopic: "",
  loading: false,
  error: null,
  
  // Hardcoded API key (Note: In production, use secure methods)
  groqApiKey: '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',
  
  // Topics and subtopics
  
  
  // Expanded topics state
  expandedTopics: {}
};

},

methods: {
    showExample(language) {
      if (language === 'java') {
        this.exampleCode = `import java.util.Random;

public class RandomizedQuickSort {
    public static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pivotIndex = randomizedPartition(arr, low, high);
            quickSort(arr, low, pivotIndex - 1);
            quickSort(arr, pivotIndex + 1, high);
        }
    }

    public static int randomizedPartition(int[] arr, int low, int high) {
        Random rand = new Random();
        int pivotIndex = low + rand.nextInt(high - low + 1);
        int pivotValue = arr[pivotIndex];
        swap(arr, pivotIndex, high);
        int storeIndex = low;
        for (int i = low; i < high; i++) {
            if (arr[i] < pivotValue) {
                swap(arr, storeIndex, i);
                storeIndex++;
            }
        }
        swap(arr, storeIndex, high);
        return storeIndex;
    }

    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}`;
      } else if (language === 'c') {
        this.exampleCode = `#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int randomizedPartition(int arr[], int low, int high) {
    int pivotIndex = low + rand() % (high - low + 1);
    int pivotValue = arr[pivotIndex];
    int temp = arr[pivotIndex];
    arr[pivotIndex] = arr[high];
    arr[high] = temp;
    int storeIndex = low;
    for (int i = low; i < high; i++) {
        if (arr[i] < pivotValue) {
            temp = arr[storeIndex];
            arr[storeIndex] = arr[i];
            arr[i] = temp;
            storeIndex++;
        }
    }
    temp = arr[storeIndex];
    arr[storeIndex] = arr[high];
    arr[high] = temp;
    return storeIndex;
}

void randomizedQuickSort(int arr[], int low, int high) {
    if (low < high) {
        int pivotIndex = randomizedPartition(arr, low, high);
        randomizedQuickSort(arr, low, pivotIndex - 1);
        randomizedQuickSort(arr, pivotIndex + 1, high);
    }
}

int main() {
    srand(time(NULL));
    int arr[] = {10, 7, 8, 9, 1, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    randomizedQuickSort(arr, 0, n - 1);
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    return 0;
}`;
      } else if (language === 'python') {
        this.exampleCode = `import random

def randomized_partition(arr, low, high):
    pivot_index = low + random.randint(0, high - low)
    pivot_value = arr[pivot_index]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    store_index = low
    for i in range(low, high):
        if arr[i] < pivot_value:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1
    arr[store_index], arr[high] = arr[high], arr[store_index]
    return store_index

def randomized_quick_sort(arr, low, high):
    if low < high:
        pivot_index = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pivot_index - 1)
        randomized_quick_sort(arr, pivot_index + 1, high)

arr = [10, 7, 8, 9, 1, 5]
randomized_quick_sort(arr, 0, len(arr) - 1)
print(arr)`;
      }
    },

// Add this method to the methods section
generateAINotes() {
// Choose a default topic and subtopic
const topic = "Randomised Algorithms";
const subtopic = "Randomised Algorithms BasicS";

// Call the existing generateNotes method
this.generateNotes(topic, subtopic);
},

// Generates the AI notes with a comprehensive prompt
generatePrompt(topic, subtopic) {
  return `
Generate comprehensive programming notes about ${topic} - ${subtopic}.\n\n
Include the following sections:\n\n
1. Introduction and Basic Concepts\n\n
2. Key Features and Characteristics\n\n
3. Implementation Details\n\n
4. Common Operations and Time Complexity\n\n
5. Real-world Applications\n\n
6. Best Practices and Tips\n\n
Make the content detailed enough for both beginners and advanced programmers.\n
`;
},


// Toggle topic expansion
toggleTopic(topic) {
  this.$set(this.expandedTopics, topic, !this.expandedTopics[topic]);
},

// Generates AI notes for a specific topic
async generateNotes(topic, subtopic) {
  if (!this.groqApiKey) {
    this.error = 'Missing API key. Please provide a valid API key and try again.';
    return;
  }

  this.loading = true;
  this.error = null;
  this.selectedTopic = `${topic} - ${subtopic}`;
  this.aiNotesData = null;

  try {
    const response = await axios.post('https://api.groq.com/openai/v1/chat/completions', {
      model: "mixtral-8x7b-32768",
      messages: [
        {
          role: "user",
          content: this.generatePrompt(topic, subtopic)
        }
      ],
      temperature: 0.7,
      max_tokens: 2000
    }, {
      headers: {
        'Authorization': `Bearer ${this.groqApiKey}`,
        'Content-Type': 'application/json'
      }
    });

    if (!response.data.choices || response.data.choices.length === 0) {
      throw new Error('No response generated. Please try again.');
    }

    const aiResponse = response.data.choices[0].message.content;
    
    // Parse and structure the AI response
    this.aiNotesData = {
      studyNotes: aiResponse,
      keyConcepts: this.extractKeyConcepts(aiResponse),
      interviewQuestions: this.extractInterviewQuestions(aiResponse),
      tutorialLinks: this.generateTutorialLinks(topic, subtopic)
    };
  } catch (error) {
    console.error('Error generating AI notes:', error);
    this.error = error.message || 'Failed to generate notes. Please try again.';
  } finally {
    this.loading = false;
  }
},

// Helper method to extract key concepts
extractKeyConcepts(text) {
  const conceptsMatch = text.match(/Key Features and Characteristics:(.*?)(\n\n|$)/s);
  if (conceptsMatch) {
    return conceptsMatch[1].trim().split('\n')
      .filter(concept => concept.trim() !== '')
      .slice(0, 5);
  }
  return [
    "Definition and Basic Concepts",
    "Core Characteristics",
    "Key Implementation Details",
    "Important Properties",
    "Advanced Techniques"
  ];
},

// Helper method to extract interview questions
extractInterviewQuestions(text) {
  const questionsMatch = text.match(/Common Interview Questions:(.*?)(\n\n|$)/s);
  if (questionsMatch) {
    return questionsMatch[1].trim().split('\n')
      .filter(q => q.trim() !== '')
      .slice(0, 3);
  }
  return [
    "What are the core principles of this topic?",
    "Explain the most important aspects and use cases.",
    "Discuss advanced implementation techniques."
  ];
},

// Generate tutorial links based on topic
generateTutorialLinks(topic, subtopic) {
  return [
    {
      platform: 'YouTube',
      description: `${topic} - ${subtopic} Tutorial`,
      url: `https://www.youtube.com/results?search_query=${encodeURIComponent(topic + ' ' + subtopic)}`
    },
    {
      platform: 'Coursera',
      description: `Learn ${topic} in Depth`,
      url: `https://www.coursera.org/courses?query=${encodeURIComponent(topic)}`
    }
  ];
},

// Copy notes to clipboard
copyNotes() {
  if (this.aiNotesData) {
    const notesText = `
Study Guide: ${this.selectedTopic}

📘 Study Notes:
${this.aiNotesData.studyNotes}

🎯 Key Concepts:
${this.aiNotesData.keyConcepts.map((c, i) => `${i + 1}. ${c}`).join('\n')}

💡 Interview Questions:
${this.aiNotesData.interviewQuestions.map((q, i) => `Q${i + 1}: ${q}`).join('\n')}

🎥 Recommended Tutorials:
${this.aiNotesData.tutorialLinks.map(t => `${t.platform}: ${t.description} - ${t.url}`).join('\n')}
    `;

    navigator.clipboard.writeText(notesText).then(() => {
      alert('Study guide copied to clipboard!');
    }).catch(err => {
      console.error('Failed to copy notes:', err);
      alert('Failed to copy notes. Please try again.');
    });
  }
},

// Download notes as PDF
downloadNotesPDF() {
  if (this.aiNotesData) {
    const doc = new jspdf();
    
    doc.setFontSize(16);
    doc.text(`Study Guide: ${this.selectedTopic}`, 20, 20);
    
    doc.setFontSize(12);
    let yPos = 30;

    const addSection = (title, content) => {
      doc.setFontSize(14);
      doc.setTextColor(0, 0, 255);
      doc.text(title, 20, yPos);
      
      doc.setFontSize(12);
      doc.setTextColor(0, 0, 0);
      const splitContent = doc.splitTextToSize(content, 170);
      doc.text(splitContent, 20, yPos + 10);
      
      yPos += 20 + (splitContent.length * 10);
    };

    addSection('Study Notes', this.aiNotesData.studyNotes);
    
    addSection('Key Concepts', 
      this.aiNotesData.keyConcepts.map((c, i) => `${i + 1}. ${c}`).join('\n')
    );
    
    addSection('Interview Questions', 
      this.aiNotesData.interviewQuestions.map((q, i) => `Q${i + 1}: ${q}`).join('\n')
    );
    
    addSection('Recommended Tutorials', 
      this.aiNotesData.tutorialLinks.map(t => `${t.platform}: ${t.description} - ${t.url}`).join('\n')
    );

    doc.save(`${this.selectedTopic.replace(/\s+/g, '_')}_Study_Guide.pdf`);
  }
}
}
};
</script>
<style scoped>
.matrix-container {
padding: 20px;
background: #000000;
border-radius: 10px;
box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
font-family: 'Arial', sans-serif;
color: #e4e4e4;
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

Generative Study Companion

.type-title {
font-size: 1.2em;
color: #ebe64d;
margin-top: 10px;
}

.characteristics-list {
list-style-type: disc;
padding-left: 40px;
}

.notes-text {
white-space: pre-wrap; /* Preserves whitespace and newlines */
}


.matrix-diagram {
display: block;
margin: 20px auto;
max-width: 100%;
border: 1px solid #ddd;
border-radius: 5px;
}

.example-button {
padding: 10px 20px;
margin: 10px;
border: none;
border-radius: 5px;
background: #007bff;
color: #fff;
cursor: pointer;
font-size: 1em;
transition: background 0.3s;
}

.example-button:hover {
background: #000000;
}

.ai-notes-display {
margin-top: 20px;
background: #313131;
padding: 20px;
border-radius: 10px;
box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.section-title {
font-size: 1.3em;
color: #007bff;
}

.key-concepts-list {
list-style-type: decimal;
padding-left: 40px;
}

.interview-questions {
margin: 10px 0;
}

.tutorial-link {
display: block;
margin: 5px 0;
color: #fbff00;
text-decoration: none;
}

.tutorial-link:hover {
text-decoration: underline;
}

.copy-button, .download-button {
margin-right: 10px;
background: #28a745;
}

.copy-button:hover, .download-button:hover {
background: #218838;
}
</style>