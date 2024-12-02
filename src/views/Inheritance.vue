<template>
    <div class="os-container">
      <h1 class="main-title">Inheritance</h1>
      <p class="intro">
        Inheritance is one of the core concepts of Object-Oriented Programming (OOP) in C++. It allows a class (called derived class) to inherit properties and behaviors (methods) from another class (called base class). This promotes code reusability and hierarchical classification.
      </p>
  
      <h2 class="sub-title">Introduction to Inheritance</h2>
      <p class="content">
        Inheritance is a mechanism in C++ where a new class is derived from an existing class. The derived class inherits the attributes and methods of the base class, and it can also have additional features.
      </p>
  
      <h2 class="sub-title">Types of Inheritance</h2>
      <ul class="characteristics-list">
        <li><strong>Single Inheritance:</strong> A class is derived from one base class.</li>
        <li><strong>Multiple Inheritance:</strong> A class is derived from more than one base class.</li>
        <li><strong>Multilevel Inheritance:</strong> A class is derived from a class, which is also derived from another class, forming a chain.</li>
        <li><strong>Hierarchical Inheritance:</strong> Multiple derived classes inherit from a single base class.</li>
        <li><strong>Hybrid Inheritance:</strong> A combination of multiple and hierarchical inheritance.</li>
      </ul>
  
      <h2 class="sub-title">Functions of Inheritance</h2>
      <p class="content">
        Inheritance helps in the following:
        <ul>
          <li>Code Reusability: Allows reuse of code written in the base class without rewriting it.</li>
          <li>Extensibility: Extends the base class by adding new properties and methods in the derived class.</li>
          <li>Maintainability: Easier to manage and update the code since changes made to the base class are automatically inherited by derived classes.</li>
        </ul>
      </p>
  
      <h2 class="sub-title">Real-Time Example of Inheritance</h2>
      <p class="content">
        Consider a class <code>Animal</code> with attributes like <code>name</code> and <code>age</code>. We can derive classes such as <code>Dog</code> and <code>Cat</code> from the <code>Animal</code> class. Both <code>Dog</code> and <code>Cat</code> inherit the properties of <code>Animal</code>, and can also have their specific methods like <code>bark()</code> and <code>meow()</code>, respectively.
      </p>
  
      <h2 class="sub-title">Difference between Single and Multiple Inheritance</h2>
      <ul class="characteristics-list">
        <li><strong>Single Inheritance:</strong> Derived class inherits from only one base class.</li>
        <li><strong>Multiple Inheritance:</strong> Derived class inherits from more than one base class, combining features from all base classes.</li>
      </ul>
  
      <h2 class="sub-title">Base Class and Derived Class Relationship</h2>
      <p class="content">
        The base class provides the foundation for inheritance, defining the attributes and methods that are shared with the derived class. The derived class can inherit, extend, or override these features as needed.
      </p>
  
      <h2 class="sub-title">Access Specifiers in Inheritance</h2>
      <p class="content">
        The accessibility of inherited properties is controlled using access specifiers:
        <ul>
          <li><strong>Public Inheritance:</strong> Public members of the base class remain public in the derived class.</li>
          <li><strong>Protected Inheritance:</strong> Public and protected members of the base class become protected in the derived class.</li>
          <li><strong>Private Inheritance:</strong> Public and protected members of the base class become private in the derived class.</li>
        </ul>
      </p>
  
      <h2 class="sub-title">Example: Inheritance in C++</h2>
      <p class="content">
        Here's an example demonstrating single inheritance in C++:
      </p>
      <pre class="content">
        <code>
          class Animal {
          public:
              string name;
              void speak() {
                  cout << "Animal speaks!" << endl;
              }
          };
  
          class Dog : public Animal {
          public:
              void bark() {
                  cout << "Dog barks!" << endl;
              }
          };
  
          int main() {
              Dog dog;
              dog.name = "Buddy";
              dog.speak();  // Inherited method from Animal
              dog.bark();   // Dog's specific method
              return 0;
          }
        </code>
      </pre>
  
  
      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the concept of inheritance:</p>
      <div class="diagram-container">
        <img src="path/to/inheritance_diagram1.png" alt="Single Inheritance Example" />
        <img src="path/to/inheritance_diagram2.png" alt="Multiple Inheritance Example" />
        <img src="path/to/inheritance_diagram3.png" alt="Base and Derived Class Relationship" />
      </div>
    
      <h2 class="sub-title">AI-Powered Study Companion</h2>
  <div class="ai-notes-section">
    <button 
      @click="generateAINotes" 
      class="example-button ai-notes-button" 
      :disabled="isGenerating"
    >
      {{ isGenerating ? 'Generating AI Study Guide...' : 'Generate AI Study Guide' }}
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
  name: "inheritance",
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
      topics: {
"Inheritance": ["Inheritance Basics", "Types of Inheritance", "Single Inheritance", "Multiple Inheritance", "Multilevel Inheritance", "Hierarchical Inheritance", "Constructor in Inheritance", "Inheritance and Method Overriding"]
      },
      
      // Expanded topics state
      expandedTopics: {}
    };
  
  },
  
    methods: {
    
    // Add this method to the methods section
  generateAINotes() {
  // Choose a default topic and subtopic
  const topic = "Inheritance";
  const subtopic = "Inheritance Basics";
  
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
  font-size: 2em;
  color: #007bff;
  text-align: center;
  }
  
  .sub-title {
  font-size: 1.5em;
  color: #0056b3;
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