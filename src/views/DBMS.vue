<template>
    <div class="dbms-container">
      <h1 class="main-title">Database Management Systems (DBMS)</h1>
      <p class="intro">
        A Database Management System (DBMS) is a software suite designed to store, retrieve, manage, and manipulate data efficiently. It provides an interface for users and applications to interact with databases while ensuring data security, integrity, and consistency. DBMS supports various operations, including data storage, querying, updating, and administration of databases.
      </p>
  
      <h2 class="sub-title">Introduction</h2>
      <p class="content">
        A DBMS acts as an intermediary between end-users and the database. It is responsible for data retrieval, transaction processing, ensuring that data remains consistent and organized, and protecting it from unauthorized access. DBMS systems are crucial in a wide range of applications such as banking, airlines, universities, and more.
      </p>
  
      <h2 class="sub-title">Entity Relationship Model</h2>
      <p class="content">
        The Entity-Relationship (ER) Model is a high-level data model that defines the data elements (entities) and relationships among them. It is used to visually represent the database's logical structure. Entities can be things, persons, or concepts, and relationships define how entities are linked together.
      </p>
      <div class="diagram-container">
        <img src="src\assets\Entity-Relationship-Diagram-.jpg" alt="ER Diagram example showing entities and their relationships" class="imageedit" />
        <p class="diagram-caption">Example of an ER diagram.</p>
      </div>
  
      <h2 class="sub-title">Relational Model</h2>
      <p class="content">
        The relational model represents data in the form of tables (also called relations). Each table consists of rows (records or tuples) and columns (fields or attributes). In this model, every row in the table is a unique entry and is identified by a primary key. Relationships between tables are established using foreign keys.
      </p>
      <div class="diagram-container">
        <img src="src\assets\dbms2.png" alt="Relational Model Diagram" class="imageedit" />
        <p class="diagram-caption">A Relational Model representing a 'Student' and 'Course' table, where 'Student_ID' acts as a primary key in the Student table and a foreign key in the Course table.</p>
      </div>
  
      <h2 class="sub-title">Relational Algebra</h2>
      <p class="content">
        Relational Algebra is a procedural query language that works on the relational model. It provides a set of operations such as selection, projection, union, set difference, and join, which are used to query and manipulate data in relational databases. For example, the 'selection' operator filters rows, while the 'projection' operator selects specific columns.
      </p>
      <div class="diagram-container">
        <img src="src\assets\study_imgs\dbms3.webp" alt="Relational Algebra operations" class="imageedit" />
        <p class="diagram-caption">Various relational algebra operations like selection (σ), projection (π), and join (⋈) used to manipulate relations in a database.</p>
      </div>
  
      <h2 class="sub-title">Functional Dependencies</h2>
      <p class="content">
        A functional dependency is a relationship between two attributes in a relation. It specifies that the value of one attribute is determined by the value of another attribute. For example, in a 'Student' table, the 'Roll Number' can uniquely identify a 'Student Name.' Functional dependencies are crucial in database normalization to eliminate redundancy.
      </p>
  
      <h2 class="sub-title">Normalization</h2>
      <p class="content">
        Normalization is the process of organizing data to reduce redundancy and improve data integrity. The most common normal forms include 1NF (First Normal Form), 2NF (Second Normal Form), 3NF (Third Normal Form), and BCNF (Boyce-Codd Normal Form). Each step in normalization ensures that data is stored logically, minimizing duplication and dependency issues.
      </p>
      <div class="diagram-container">
        <img src="src\assets\study_imgs\dbms6.jpg" alt="Normalization process example" class="imageedit" />
        <p class="diagram-caption">An example of Normalization from 1NF to 3NF, showing how tables are restructured to minimize redundancy and dependency.</p>
      </div>
  
      <h2 class="sub-title">Transactions and Concurrency Control</h2>
      <p class="content">
        A transaction is a sequence of operations performed as a single logical unit of work. For a transaction to be reliable, it must satisfy ACID properties: Atomicity, Consistency, Isolation, and Durability. Concurrency control mechanisms like locking, timestamp ordering, and multiversion concurrency control (MVCC) ensure that transactions are executed without conflicting with each other, maintaining database integrity.
      </p>
  
      <h2 class="sub-title">Indexing, B and B+ Trees</h2>
      <p class="content">
        Indexing is used to speed up data retrieval by reducing the number of disk accesses. B-trees and B+ trees are popular data structures used in databases to maintain sorted data and allow for efficient insertion, deletion, and searching. B+ trees are a variation of B-trees where all records are stored at the leaf level, making it highly efficient for range queries.
      </p>
      <div class="diagram-container">
        <img src="src\assets\study_imgs\dbms5.jpg" alt="diagram" class="imageedit" />
        <p class="diagram-caption">Example of a B+ Tree data structure used for indexing in databases, which helps in faster data retrieval and range queries.</p>
      </div>
  
      <h2 class="sub-title">File Organization</h2>
      <p class="content">
        File organization refers to how data is stored in the database at the physical level. Common types of file organization include heap files (unordered), sequential files (ordered), and indexed files. Each file organization type has different characteristics regarding access speed and storage efficiency.
      </p>
  
      <h2 class="sub-title">Advanced Topics</h2>
      <p class="content">
        Some advanced topics in DBMS include distributed databases, where data is stored across multiple locations, and NoSQL databases, which are used for handling unstructured or semi-structured data. Other topics include database security, object-oriented databases, and big data systems, which deal with massive amounts of data and complex data models.
      </p>
  
  
      <h2 class="sub-title">SQL Tutorial</h2>
      <ul class="characteristics-list">
        <li><a href="https://www.sqltutorial.org/" target="_blank">SQL Tutorial</a></li>
        <li><a href="https://www.w3schools.com/sql/" target="_blank">W3Schools SQL Tutorial</a></li>
        <li><a href="https://www.codecademy.com/learn/learn-sql" target="_blank">Codecademy SQL Course</a></li>
      </ul>
  
  
      <h2 class="sub-title">Advantages of DBMS</h2>
      <ul class="characteristics-list">
        <li>Reduces data redundancy and inconsistency.</li>
        <li>Enhances data security through access controls and encryption.</li>
        <li>Allows concurrent access to data by multiple users.</li>
        <li>Ensures data integrity by enforcing data constraints.</li>
      </ul>B+ Tree 
  
      <h2 class="sub-title">Disadvantages of DBMS</h2>
      <ul class="characteristics-list">
        <li>Complexity in database design and maintenance.</li>
        <li>High initial investment for setting up DBMS software and hardware.</li>
        <li>Requires skilled personnel to manage and maintain the system.</li>
        <li>Performance overhead due to abstraction layers in DBMS.</li>
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
  
  // Add this method to the methods section
generateAINotes() {
// Choose a default topic and subtopic
const topic = "Scalability";
const subtopic = "Scalability BasicS";

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

.main-title {
font-size: 4em;
color: #ccc;
text-align: center;
}

.sub-title {
font-size: 1.5em;
color: #0d9bbb;
margin-top: 20px;
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

.imageedit {
  padding: 10px; /* Adds inner spacing for a cleaner appearance */
  border: 1px solid #ccc; /* Optional: Adds a subtle border for clarity */
  width: 600px; /* Adjusted size for larger images */
  height: auto; /* Maintains the aspect ratio */
  display: block; /* Centers the image within its container */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Optional: Adds a soft shadow */
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