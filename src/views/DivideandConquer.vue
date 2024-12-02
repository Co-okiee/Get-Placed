<!-- src/views/DivideAndConquer.vue -->
<template>
  <div class="divide-conquer-container">
    <h1 class="main-title">Divide and Conquer Algorithms</h1>
    <p class="intro">
      Divide and Conquer is an algorithm design paradigm that breaks a problem down into smaller sub-problems, solves each sub-problem recursively, and then combines their solutions to solve the original problem.
    </p>

    <h2 class="sub-title">Types of Divide and Conquer Algorithms</h2>

    <h3 class="type-title">1. Merge Sort</h3>
    <p>Merge Sort splits the array into two halves, recursively sorts them, and then merges the sorted halves to form a completely sorted array.</p>
    

    <h3 class="type-title">2. Quick Sort</h3>
    <p>Quick Sort selects a pivot element and partitions the array into sub-arrays where elements less than the pivot go to one side, and elements greater go to the other. The process is repeated recursively for both sub-arrays.</p>
    

    <h3 class="type-title">3. Binary Search</h3>
    <p>Binary Search repeatedly divides the sorted array in half, eliminating the half in which the target element cannot be, until the target element is found or the search space is empty.</p>
   
    <h3 class="type-title">4. Strassen’s Matrix Multiplication</h3>
    <p>Strassen's algorithm multiplies two matrices using a divide and conquer approach, reducing the number of multiplication operations compared to standard matrix multiplication.</p>
    

    <h3 class="type-title">5. Closest Pair of Points</h3>
    <p>The Closest Pair of Points algorithm recursively divides the set of points into halves, finds the closest pairs in each half, and then checks across the dividing line for any closer pairs.</p>
    
    <h3 class="type-title">6. Karatsuba Multiplication</h3>
    <p>Karatsuba’s algorithm is an efficient way to multiply two large numbers by splitting them into smaller parts, multiplying those parts, and combining the results.</p>
    

    <h3 class="type-title">7. Matrix Chain Multiplication</h3>
    <p>This algorithm determines the optimal order to multiply matrices to minimize the number of scalar multiplications.</p>
    
    <img src="@/assets/divide.png" alt="Divide and Conquer Diagram" class="algorithm-diagram imageedit"/>
    <h2 class="sub-title">Declaration Syntax</h2>
    <p>Select a programming language to see the implementation of a Divide and Conquer algorithm:</p>

    <div class="button-container">
      <button @click="showDeclaration('java')" class="example-button">Java</button>
      <button @click="showDeclaration('c')" class="example-button">C</button>
      <button @click="showDeclaration('python')" class="example-button">Python</button>
    </div>

    <pre v-if="declarationCode">
      <code>{{ declarationCode }}</code>
    </pre>

    <h2 class="sub-title">Advantages of Divide and Conquer Algorithms</h2>
    <ul>
      <li>Divide and Conquer breaks complex problems into smaller, easier-to-manage sub-problems.</li>
      <li>It enables efficient recursive solutions that often outperform iterative approaches.</li>
    </ul>

    <h2 class="sub-title">Disadvantages of Divide and Conquer Algorithms</h2>
    <ul>
      <li>It can sometimes lead to higher space complexity due to recursion.</li>
      <li>Some divide and conquer algorithms are harder to implement and understand than their iterative counterparts.</li>
    </ul>


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
    showDeclaration(language) {
      if (language === 'java') {
        this.declarationCode = `// Merge Sort in Java
void mergeSort(int arr[], int l, int r) {
  if (l < r) {
    int m = l + (r - l) / 2;
    mergeSort(arr, l, m);
    mergeSort(arr, m + 1, r);
    merge(arr, l, m, r);
  }
}

void merge(int arr[], int l, int m, int r) {
  int n1 = m - l + 1;
  int n2 = r - m;
  int L[] = new int[n1];
  int R[] = new int[n2];
  for (int i = 0; i < n1; ++i)
    L[i] = arr[l + i];
  for (int j = 0; j < n2; ++j)
    R[j] = arr[m + 1 + j];
  int i = 0, j = 0;
  int k = l;
  while (i < n1 && j < n2) {
    if (L[i] <= R[j]) {
      arr[k] = L[i];
      i++;
    } else {
      arr[k] = R[j];
      j++;
    }
    k++;
  }
  while (i < n1) {
    arr[k] = L[i];
    i++;
    k++;
  }
  while (j < n2) {
    arr[k] = R[j];
    j++;
    k++;
  }
}`;
      } else if (language === 'c') {
        this.declarationCode = `// Merge Sort in C
void mergeSort(int arr[], int l, int r) {
  if (l < r) {
    int m = l + (r - l) / 2;
    mergeSort(arr, l, m);
    mergeSort(arr, m + 1, r);
    merge(arr, l, m, r);
  }
}

void merge(int arr[], int l, int m, int r) {
  int n1 = m - l + 1;
  int n2 = r - m;
  int L[n1], R[n2];
  for (int i = 0; i < n1; i++)
    L[i] = arr[l + i];
  for (int j = 0; j < n2; j++)
    R[j] = arr[m + 1 + j];
  int i = 0, j = 0, k = l;
  while (i < n1 && j < n2) {
    if (L[i] <= R[j]) {
      arr[k] = L[i];
      i++;
    } else {
      arr[k] = R[j];
      j++;
    }
    k++;
  }
  while (i < n1) {
    arr[k] = L[i];
    i++;
    k++;
  }
  while (j < n2) {
    arr[k] = R[j];
    j++;
    k++;
  }
}`;
      } else if (language === 'python') {
        this.declarationCode = `# Merge Sort in Python
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1`;
      }
    },

// Add this method to the methods section
generateAINotes() {
// Choose a default topic and subtopic
const topic = "Divide and Conquer";
const subtopic = "Divide and Conquer BasicS";

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