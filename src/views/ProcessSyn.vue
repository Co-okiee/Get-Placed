<template>
    <div class="ps-container">
      <h1 class="main-title">Process Synchronization</h1>
      <p class="intro">
        Process synchronization is a mechanism that ensures that multiple processes can operate concurrently without conflict. It is essential for ensuring data consistency and preventing race conditions in a multi-threaded environment.
      </p>
  
      <h2 class="sub-title">Introduction to Process Synchronization</h2>
      <p class="content">
        In operating systems, processes may need to share resources. Synchronization is required to prevent conflicts when multiple processes access shared resources simultaneously.
      </p>
  
      <h2 class="sub-title">Critical Section</h2>
      <p class="content">
        The critical section is a segment of code that accesses shared resources. Only one process should be allowed to execute in its critical section at a time to prevent data inconsistency.
      </p>
      <img src="path/to/critical-section-diagram.png" alt="Critical Section Diagram" />
  
      <h2 class="sub-title">Inter Process Communication (IPC)</h2>
      <p class="content">
        IPC is a set of methods used for communication between processes. It allows processes to exchange data and signals.
      </p>
  
      <h2 class="sub-title">Interprocess Communication: Methods</h2>
      <ul class="characteristics-list">
        <li><strong>Shared Memory:</strong> Processes communicate by accessing a common memory space.</li>
        <li><strong>Message Queues:</strong> Processes send and receive messages via a queue.</li>
      </ul>
  
      <h2 class="sub-title">IPC through Shared Memory</h2>
      <p class="content">
        Shared memory is one of the fastest IPC methods. Processes share a segment of memory and communicate through it.
      </p>
  
      <h2 class="sub-title">IPC using Message Queues</h2>
      <p class="content">
        Message queues allow processes to communicate asynchronously. Messages are placed in a queue and can be retrieved by processes.
      </p>
  
      <h2 class="sub-title">Message-based Communication in IPC</h2>
      <p class="content">
        This method involves sending messages between processes. It provides a way to communicate without sharing memory directly.
      </p>
  
      <h2 class="sub-title">Communication Between Two Processes Using Signals in C</h2>
      <p class="content">
        Signals are a limited form of IPC that allows processes to send notifications. For example, a process can notify another process to terminate using a signal.
      </p>
      <pre>
        <code>
          #include &lt;signal.h&gt;
          // Signal handler function
          void handleSignal(int signal) {
              // Handle the signal
          }
        </code>
      </pre>
  
      <h2 class="sub-title">Semaphores in Operating System</h2>
      <p class="content">
        A semaphore is a synchronization primitive used to control access to shared resources. It uses two operations: wait (P) and signal (V).
      </p>
  
      <h2 class="sub-title">Mutex vs. Semaphore</h2>
      <p class="content">
        A mutex allows only one thread to access a resource at a time, while a semaphore can allow multiple threads to access a set number of resources.
      </p>
  
      <h2 class="sub-title">Process Synchronization: Monitors</h2>
      <p class="content">
        Monitors are high-level synchronization constructs that allow safe access to shared resources by encapsulating them with lock mechanisms.
      </p>
  
      <h2 class="sub-title">Peterson’s Algorithm for Mutual Exclusion</h2>
      <h3 class="type-title">Set 1 (Basic C Implementation)</h3>
      <pre>
        <code>
          // Basic implementation of Peterson's Algorithm
          void peterson(int process) {
              int other = 1 - process;
              flag[process] = true; 
              turn = process; 
              while (flag[other] && turn == process);
          }
        </code>
      </pre>
  
      <h3 class="type-title">Set 2 (CPU Cycles and Memory Fence)</h3>
      <p class="content">
        This set emphasizes the importance of memory fences to prevent CPU optimizations from affecting the execution order.
      </p>
  
      <h3 class="type-title">Peterson’s Algorithm (Using Processes and Shared Memory)</h3>
      <p class="content">
        Here, we demonstrate the algorithm using processes that communicate through shared memory.
      </p>
  
      <h2 class="sub-title">Dekker’s Algorithm</h2>
      <p class="content">
        Dekker's algorithm is another solution for mutual exclusion that ensures that only one of the processes can enter the critical section at a time.
      </p>
  
      <h2 class="sub-title">Bakery Algorithm</h2>
      <p class="content">
        The Bakery algorithm ensures that processes enter their critical sections in a first-come-first-serve basis by assigning a number to each process.
      </p>
  
      <h2 class="sub-title">Producer-Consumer Problem Using Semaphores</h2>
      <h3 class="type-title">Set 1</h3>
      <p class="content">
        The producer-consumer problem is a classic synchronization problem that illustrates how to synchronize producer and consumer processes using semaphores.
      </p>
  
      <h2 class="sub-title">Dining Philosopher Problem Using Semaphores</h2>
      <p class="content">
        This problem illustrates the challenges of resource sharing among multiple processes and how to resolve deadlocks.
      </p>
  
      <h2 class="sub-title">Dining-Philosophers Solution Using Monitors</h2>
      <p class="content">
        Using monitors, this solution addresses the dining philosophers problem while avoiding deadlocks.
      </p>
  
      <h2 class="sub-title">Readers-Writers Problem</h2>
      <h3 class="type-title">Set 1 (Introduction and Readers Preference Solution)</h3>
      <p class="content">
        The readers-writers problem addresses synchronization between processes that read and write shared data. In the reader's preference solution, readers get priority.
      </p>
  
      <h3 class="type-title">Reader-Writers Solution Using Monitors</h3>
      <p class="content">
        Monitors can be used to solve the readers-writers problem effectively, ensuring both reader and writer integrity.
      </p>
  
      <h2 class="sub-title">Sleeping Barber Problem</h2>
      <p class="content">
        This problem illustrates the synchronization of multiple processes in a barbershop scenario, ensuring efficient service without wastage.
      </p>
  
      <h2 class="sub-title">Lock Variable Synchronization Mechanism</h2>
      <p class="content">
        Lock variables are used to control access to shared resources in order to ensure mutual exclusion.
      </p>
  
      <h2 class="sub-title">Mutex Lock for Linux Thread Synchronization</h2>
      <p class="content">
        Mutex locks are used in Linux for thread synchronization, ensuring that only one thread can access a critical section at a time.
      </p>
  
      <h2 class="sub-title">Priority Inversion: What the Heck!</h2>
      <p class="content">
        Priority inversion occurs when a lower-priority task holds a resource needed by a higher-priority task, causing unexpected delays.
      </p>
  
      <h2 class="sub-title">What’s the Difference Between Priority Inversion and Priority Inheritance?</h2>
      <p class="content">
        Priority inheritance is a technique to prevent priority inversion by temporarily raising the priority of the lower-priority task holding a needed resource.
      </p>
  
     
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
const topic = "Process Synchronization";
const subtopic = "Process Synchronization BasicS";

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