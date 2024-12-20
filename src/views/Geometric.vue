<template>
  <div class="geometric-container">
    <h1 class="main-title">Geometric Algorithms</h1>
    <p class="intro">
      Geometric algorithms are techniques used for solving problems related to geometric objects such as points, lines, polygons, and other shapes.
    </p>

    <h2 class="sub-title">Key Characteristics of Geometric Algorithms</h2>
    <ul class="characteristics-list">
      <li><strong>Spatial Data Structures:</strong> Utilizes data structures like trees and graphs to manage geometric data efficiently.</li>
      <li><strong>Efficiency:</strong> Aims to minimize computational time and resource usage in processing geometric queries.</li>
      <li><strong>Applications:</strong> Widely used in computer graphics, robotics, geographic information systems (GIS), and more.</li>
    </ul>

    <h2 class="sub-title">Diagram of Geometric Algorithms</h2>
   
    <h2 class="sub-title">Types of Geometric Algorithms</h2>
    <h3 class="type-title">Convex Hull</h3>
    <p>A minimal polygon that encloses a set of points in a plane.</p>

    <h3 class="type-title">Line Intersection</h3>
    <p>Algorithms to determine the points where two or more lines intersect.</p>

    <h3 class="type-title">Polygon Triangulation</h3>
    <p>Dividing a polygon into triangles to simplify computations.</p>

    <h2 class="sub-title">Geometric Algorithm Functions</h2>
    <p>Key functions include computing distances, finding intersections, and performing transformations on geometric objects.</p>

    <h2 class="sub-title">Examples</h2>
    <p>Click on the buttons below to see examples of geometric algorithms in different programming languages:</p>

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
        this.exampleCode = `import java.awt.geom.Line2D;

public class LineIntersection {
    public static void main(String[] args) {
        Line2D line1 = new Line2D.Double(1, 1, 4, 4);
        Line2D line2 = new Line2D.Double(1, 4, 4, 1);
        if (line1.intersectsLine(line2)) {
            System.out.println("Lines intersect.");
        } else {
            System.out.println("Lines do not intersect.");
        }
    }
}`;
      } else if (language === 'c') {
        this.exampleCode = `#include <stdio.h>

struct Point {
    int x, y;
};

int orientation(struct Point p, struct Point q, struct Point r) {
    int val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y);
    return (val == 0) ? 0 : (val > 0) ? 1 : 2;
}`;
      } else if (language === 'python') {
        this.exampleCode = `def convex_hull(points):
    points = sorted(points)
    # Logic for computing convex hull
    return points
points = [(0, 0), (1, 1), (2, 2)]
print(convex_hull(points))`;
      }
    },

// Add this method to the methods section
generateAINotes() {
// Choose a default topic and subtopic
const topic = "Geometric Algorithms";
const subtopic = "Geometric Algorithms BasicS";

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