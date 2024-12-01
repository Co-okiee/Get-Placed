<template>
    <div class="oop-container">
      <h1 class="main-title">Dynamic Binding and Message Passing</h1>
      <p class="intro">
        In Object-Oriented Programming (OOP), dynamic binding and message passing are two important concepts that enhance flexibility and reusability of code. Dynamic binding allows method calls to be resolved at runtime, while message passing enables communication between objects.
      </p>

      <h2 class="sub-title">Introduction to Dynamic Binding</h2>
      <p class="content">
        Dynamic binding, also known as late binding, occurs when a method call is not resolved until runtime. It is typically achieved through the use of pointers or references to base class objects and is fundamental to polymorphism in C++.
      </p>
  
      <h2 class="sub-title">Key Characteristics of Dynamic Binding</h2>
      <ul class="characteristics-list">
        <li><strong>Late Binding:</strong> The function call is resolved at runtime rather than compile-time.</li>
        <li><strong>Polymorphism:</strong> Dynamic binding is closely associated with runtime polymorphism, where a base class reference or pointer can refer to objects of derived classes.</li>
        <li><strong>Virtual Functions:</strong> In C++, dynamic binding is implemented using virtual functions.</li>
      </ul>
  
      <h2 class="sub-title">Example of Dynamic Binding in C++</h2>
      <p class="content">
        Here is an example demonstrating dynamic binding using virtual functions in C++:
      </p>
      <pre class="code-block">
        <code>
          class Base {
          public:
              virtual void show() {
                  cout << "Base class show function" << endl;
              }
          };

          class Derived : public Base {
          public:
              void show() override {
                  cout << "Derived class show function" << endl;
              }
          };

          int main() {
              Base *ptr = new Derived();
              ptr->show(); // Calls Derived class show function at runtime
              delete ptr;
              return 0;
          }
        </code>
      </pre>

      <h2 class="sub-title">Introduction to Message Passing</h2>
      <p class="content">
        Message passing is a mechanism in OOP that allows objects to communicate with each other by sending and receiving messages. It supports encapsulation and data abstraction by making interactions between objects happen through well-defined interfaces.
      </p>

      <h2 class="sub-title">Characteristics of Message Passing</h2>
      <ul class="characteristics-list">
        <li><strong>Object Communication:</strong> Objects communicate by invoking methods on other objects, sending data and receiving responses.</li>
        <li><strong>Encapsulation:</strong> Message passing hides the internal details of the objects, focusing on the interaction interface.</li>
        <li><strong>Modularity:</strong> Message passing allows independent development of objects, as they only need to know the interface to communicate.</li>
      </ul>

      <h2 class="sub-title">Example of Message Passing in C++</h2>
      <p class="content">
        Here is an example that demonstrates message passing between two objects:
      </p>
      <pre class="code-block">
        <code>
          class A {
          public:
              void sendMessage() {
                  cout << "Message from class A" << endl;
              }
          };

          class B {
          public:
              void receiveMessage(A &obj) {
                  obj.sendMessage(); // Object B communicates with object A
              }
          };

          int main() {
              A objA;
              B objB;
              objB.receiveMessage(objA); // B sends message to A
              return 0;
          }
        </code>
      </pre>

      <h2 class="sub-title">Difference between Static and Dynamic Binding</h2>
      <ul class="characteristics-list">
        <li><strong>Static Binding:</strong> Function call is resolved at compile time.</li>
        <li><strong>Dynamic Binding:</strong> Function call is resolved at runtime, enabling polymorphism.</li>
      </ul>
  
      <h2 class="sub-title">Advantages of Dynamic Binding and Message Passing</h2>
      <p class="content">
        Dynamic binding increases flexibility in code by allowing runtime decisions, while message passing ensures a clear communication mechanism between objects. Both enhance modularity, encapsulation, and code reusability in OOP.
      </p>
  
      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the concepts discussed:</p>
      <div class="diagram-container">
        <img src="path/to/dynamic_binding_diagram.png" alt="Diagram illustrating dynamic binding" />
        <img src="path/to/message_passing_diagram.png" alt="Diagram showing message passing between objects" />
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
  name: "dynamic binding",
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
"Dynamic Binding and Message Passing": [
  "Dynamic Binding Basics", 
  "Late Binding", 
  "Runtime Binding", 
  "Dynamic Binding in Polymorphism", 
  "Message Passing Basics", 
  "Communication Between Objects", 
  "Method Invocation", 
  "Message Passing in Object-Oriented Design", 
  "Dynamic Binding and Message Passing in Distributed Systems", 
  "Examples of Dynamic Binding and Message Passing"
]
      },
      
      // Expanded topics state
      expandedTopics: {}
    };
  
  },
  
    methods: {
    
    // Add this method to the methods section
  generateAINotes() {
  // Choose a default topic and subtopic
  const topic = "Dynamic Binding and Message Passing";
  const subtopic = "Dynamic Binding and Message Passing BasicS";
  
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