<template>
    <div class="network-container">
      <h1 class="main-title">Basics of Computer Networking</h1>
      <p class="intro">
        Computer networking is the practice of connecting computers and other devices to share resources and information. It enables communication and data exchange among devices.
      </p>
  
      <h2 class="sub-title">The Internet and the Web</h2>
      <p class="content">
        The Internet is a global network of interconnected computers that communicate using standardized protocols. The Web is a collection of information accessible through the Internet, typically using web browsers.
      </p>
  
      <h2 class="sub-title">Internet and Web Programming: Behind the Scenes</h2>
      <p class="content">
        Internet programming involves creating applications that run on the web. This includes using languages like HTML, CSS, and JavaScript for front-end development and PHP, Python, or Java for back-end services.
      </p>
  
      <h2 class="sub-title">The New Internet | Internet of Everything</h2>
      <p class="content">
        The Internet of Everything (IoE) extends the concept of the Internet by connecting people, processes, data, and things. It enhances the interaction among these elements, enabling smarter and more efficient systems.
      </p>
  
      <h2 class="sub-title">Unknown Facts of Networking</h2>
      <p class="content">
        Networking has fascinating facts, such as the first message sent over the ARPANET in 1969, which was supposed to be "LOGIN" but crashed the network after just two letters were transmitted.
      </p>
  
      <h2 class="sub-title">Network Goals</h2>
      <p class="content">
        The primary goals of networking include resource sharing, data communication, reliability, scalability, and providing security.
      </p>
  
      <h2 class="sub-title">Line Configuration in Computer Networks</h2>
      <p class="content">
        Line configuration refers to how devices are connected in a network. Common configurations include point-to-point and multipoint configurations.
      </p>
  
      <h2 class="sub-title">Transmission Modes in Computer Networks</h2>
      <ul class="characteristics-list">
        <li><strong>Simplex:</strong> Communication is unidirectional (one way).</li>
        <li><strong>Half-Duplex:</strong> Communication is bidirectional but not simultaneous (one at a time).</li>
        <li><strong>Full Duplex:</strong> Communication is bidirectional and simultaneous (both ways at once).</li>
      </ul>
  
      <h2 class="sub-title">Types of Transmission Media</h2>
      <ul class="characteristics-list">
        <li><strong>Twisted Pair Cable:</strong> Consists of pairs of wires twisted together, commonly used in LANs.</li>
        <li><strong>Coaxial Cable:</strong> Contains a central conductor and is used for cable TV and Internet connections.</li>
        <li><strong>Fiber Optic Cable:</strong> Uses light to transmit data, providing high speed and bandwidth over long distances.</li>
      </ul>
  
      <h2 class="sub-title">Unicast, Broadcast, and Multicast</h2>
      <p class="content">
        <strong>Unicast:</strong> One-to-one communication. <br>
        <strong>Broadcast:</strong> One-to-all communication. <br>
        <strong>Multicast:</strong> One-to-many communication, where data is sent to a group of interested receivers.
      </p>
  
      <h2 class="sub-title">Introduction to Basic Networking Terminology</h2>
      <p class="content">
        Understanding basic networking terms such as IP address, subnet mask, router, and switch is essential for anyone working with networks.
      </p>
  
      <h2 class="sub-title">Network Topologies</h2>
      <ul class="characteristics-list">
        <li><strong>Star Topology:</strong> All devices are connected to a central hub.</li>
        <li><strong>Bus Topology:</strong> All devices share a single communication line.</li>
        <li><strong>Ring Topology:</strong> Devices are connected in a circular configuration.</li>
      </ul>
  
      <h2 class="sub-title">Types of Area Networks – LAN, MAN, and WAN</h2>
      <p class="content">
        <strong>LAN (Local Area Network):</strong> Covers a small geographical area, like a single building. <br>
        <strong>MAN (Metropolitan Area Network):</strong> Covers a city or a large campus. <br>
        <strong>WAN (Wide Area Network):</strong> Covers a broad area, potentially worldwide.
      </p>
  
      <h2 class="sub-title">Telecom Networks</h2>
      <p class="content">
        Telecom networks provide communication services through various technologies, including cellular, satellite, and fiber optics, enabling voice, video, and data transmission.
      </p>
  
      <h2 class="sub-title">Access Networks</h2>
      <p class="content">
        Access networks connect end-users to the broader telecommunications network. They can be wired (DSL, fiber) or wireless (Wi-Fi, cellular).
      </p>
  
      <h2 class="sub-title">TCP/IP Model</h2>
      <p class="content">
        The TCP/IP model consists of four layers: Application, Transport, Internet, and Network Access. It defines how data is transmitted over the network.
      </p>
  
      <h2 class="sub-title">Layers of OSI Model</h2>
      <p class="content">
        The OSI model consists of seven layers: Application, Presentation, Session, Transport, Network, Data Link, and Physical. It standardizes networking protocols to ensure interoperability.
      </p>
  
      <h2 class="sub-title">Introduction to Active Directory Domain Service</h2>
      <p class="content">
        Active Directory (AD) is a directory service for Windows domain networks, providing authentication, authorization, and centralized management of network resources.
      </p>
  
      <h2 class="sub-title">Advantages and Disadvantages of Computer Networking</h2>
      <ul class="characteristics-list">
        <li><strong>Advantages:</strong> Resource sharing, increased communication speed, and enhanced security through centralized management.</li>
        <li><strong>Disadvantages:</strong> Complexity in network management, security vulnerabilities, and dependency on network infrastructure.</li>
      </ul>
  
      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the concepts discussed:</p>
      <div class="diagram-container">
        <img src="src\assets\study_imgs\cnbasics1.jpeg" alt="Diagram illustrating different network topologies" class="imageedit"/>
        <img src="src\assets\study_imgs\cnbasics2.webp" alt="Diagram showing TCP/IP model layers" class="imageedit"/>
      </div>
      <h2 class="sub-title">Generative Study Companion</h2>
  <div class="ai-notes-section">
    <button 
      @click="generateAINotes" 
      class="example-button ai-notes-button" 
      :disabled="isGenerating"
    >
      {{ isGenerating ? 'Generating  Study Guide...' : 'Generate Study Guide' }}
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
name: "basicsoop",
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
"Data Link Layer": [
  "Data Link Layer Basics", 
  "Functions of Data Link Layer", 
  "Framing", 
  "Error Detection and Correction", 
  "Flow Control", 
  "HDLC (High-Level Data Link Control)", 
  "PPP (Point-to-Point Protocol)", 
  "ARQ (Automatic Repeat Request)", 
  "MAC (Media Access Control) Sublayer", 
  "Ethernet Frame Format", 
  "Access Control Mechanisms", 
  "Types of Errors in Data Link Layer", 
  "Link Layer Switching and Bridging", 
  "Error Recovery Techniques"
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
const topic = "Computer Networks";
const subtopic = "Computer Networks Basics";

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