<template>
    <div class="transport-container">
      <h1 class="main-title">Transport Layer</h1>
      <p class="intro">
        The Transport Layer is a crucial component of the networking stack, responsible for providing communication services directly to the application processes running on different hosts.
      </p>
  
      <h2 class="sub-title">Transport Layer Responsibilities</h2>
      <p class="content">
        The main responsibilities of the Transport Layer include:
        <ul>
          <li>Segmentation and reassembly of data</li>
          <li>End-to-end communication</li>
          <li>Flow control</li>
          <li>Error detection and correction</li>
          <li>Multiplexing and demultiplexing of data streams</li>
        </ul>
      </p>
  
      <h2 class="sub-title">Multiplexing and Demultiplexing in Transport Layer</h2>
      <p class="content">
        Multiplexing allows multiple applications to share a single network connection by assigning different ports, while demultiplexing ensures that the data is sent to the correct application at the destination.
      </p>
  
      <h2 class="sub-title">User Datagram Protocol (UDP)</h2>
      <p class="content">
        UDP is a connectionless protocol that provides a simple method for sending data with minimal overhead. It is suitable for applications that require fast transmission, such as video streaming or online gaming, but do not need guaranteed delivery.
      </p>
  
      <h2 class="sub-title">TCP Connection Establishment</h2>
      <p class="content">
        TCP establishes a connection using the 3-Way Handshake process, ensuring both sender and receiver are ready for data transmission.
      </p>
  
      <h2 class="sub-title">TCP 3-Way Handshake Process</h2>
      <p class="content">
        The 3-Way Handshake consists of three steps:
        <ol>
          <li><strong>SYN:</strong> The client sends a SYN (synchronize) packet to the server to request a connection.</li>
          <li><strong>SYN-ACK:</strong> The server responds with a SYN-ACK (synchronize-acknowledgment) packet to acknowledge the request.</li>
          <li><strong>ACK:</strong> The client sends an ACK packet back to the server, establishing the connection.</li>
        </ol>
        <img src="path/to/tcp_handshake_diagram.png" alt="TCP 3-Way Handshake Diagram" />
      </p>
  
      <h2 class="sub-title">TCP Timers</h2>
      <p class="content">
        TCP uses several timers to manage connections, including:
        <ul>
          <li><strong>Retransmission Timer:</strong> Used to determine when to retransmit unacknowledged segments.</li>
          <li><strong>Keep-Alive Timer:</strong> Used to check if the connection is still active.</li>
          <li><strong>Persistence Timer:</strong> Used to manage data transmission when the sender is blocked.</li>
        </ul>
      </p>
  
      <h2 class="sub-title">TCP Connection Termination</h2>
      <p class="content">
        TCP connections are terminated through a four-step process, involving the exchange of FIN (finish) and ACK packets between the sender and receiver.
      </p>
  
      <h2 class="sub-title">TCP Sequence Number | Wrap Around Concept</h2>
      <p class="content">
        TCP uses sequence numbers to keep track of the order of data segments. The wrap-around concept allows sequence numbers to reset after reaching the maximum limit, ensuring that older segments are identified correctly.
      </p>
  
      <h2 class="sub-title">P2P (Peer To Peer) File Sharing</h2>
      <p class="content">
        P2P file sharing allows users to share files directly with one another without the need for a centralized server, utilizing both TCP and UDP for data transmission.
      </p>
  
      <h2 class="sub-title">Congestion Control</h2>
      <p class="content">
        Congestion control techniques are vital for maintaining efficient data flow and preventing network overload. TCP employs several methods for congestion control, including:
        <ul>
          <li><strong>AIMD:</strong> Additive Increase Multiplicative Decrease</li>
          <li><strong>Slow Start:</strong> Gradually increases transmission rate until congestion is detected.</li>
        </ul>
      </p>
  
      <h2 class="sub-title">TCP Congestion Control</h2>
      <p class="content">
        TCP employs various congestion control techniques to adaptively adjust the rate of data transmission based on network conditions, ensuring smooth and efficient communication.
      </p>
  
      <h2 class="sub-title">Congestion Control Techniques</h2>
      <p class="content">
        Common congestion control techniques include:
        <ul>
          <li><strong>Leaky Bucket Algorithm:</strong> Controls the amount of data transmitted over a network by regulating the flow.</li>
          <li><strong>Token Bucket Algorithm:</strong> Allows bursts of traffic while maintaining an average rate.</li>
        </ul>
      </p>
  
      <h2 class="sub-title">Error Control in TCP</h2>
      <p class="content">
        TCP provides error control through techniques such as checksums, acknowledgments, and retransmission of lost segments to ensure data integrity.
      </p>
  
      <h2 class="sub-title">TCP Flags</h2>
      <p class="content">
        TCP flags are control bits in the TCP header that indicate specific control information, such as:
        <ul>
          <li>SYN - Synchronize</li>
          <li>ACK - Acknowledgment</li>
          <li>FIN - Finish</li>
          <li>RST - Reset</li>
        </ul>
      </p>
  
      <h2 class="sub-title">TCP | Services and Segment Structure</h2>
      <p class="content">
        TCP provides reliable, ordered, and error-checked delivery of data. The TCP segment structure includes:
        <ul>
          <li>Source Port</li>
          <li>Destination Port</li>
          <li>Sequence Number</li>
          <li>Acknowledgment Number</li>
          <li>Flags</li>
          <li>Window Size</li>
          <li>Checksum</li>
          <li>Urgent Pointer</li>
          <li>Data</li>
        </ul>
        <img src="path/to/tcp_segment_structure.png" alt="TCP Segment Structure Diagram" />
      </p>
  
      <h2 class="sub-title">TCP Server-Client Implementation in C</h2>
      <p class="content">
        Below is a simple example of a TCP server and client implementation in C:
        <pre>
          // TCP Server Example
          #include &lt;stdio.h&gt;
          #include &lt;stdlib.h&gt;
          #include &lt;string.h&gt;
          #include &lt;sys/socket.h&gt;
          #include &lt;netinet/in.h&gt;
  
          int main() {
              int server_fd, new_socket;
              struct sockaddr_in address;
              int opt = 1;
              int addrlen = sizeof(address);
              char buffer[1024] = {0};
  
              server_fd = socket(AF_INET, SOCK_STREAM, 0);
              setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));
              address.sin_family = AF_INET;
              address.sin_addr.s_addr = INADDR_ANY;
              address.sin_port = htons(8080);
  
              bind(server_fd, (struct sockaddr *)&address, sizeof(address));
              listen(server_fd, 3);
              new_socket = accept(server_fd, (struct sockaddr )&address, (socklen_t)&addrlen);
              read(new_socket, buffer, 1024);
              printf("%s\n", buffer);
              return 0;
          }
        </pre>
      </p>
  
      <h2 class="sub-title">TCP and UDP Server Using Select</h2>
      <p class="content">
        The select() function allows a program to monitor multiple file descriptors to see if any of them are ready for I/O operations. Below is a simplified example:
        <pre>
          // Example for TCP and UDP server using select
          // Include necessary headers
        </pre>
        <p>This example demonstrates handling both TCP and UDP connections.</p>
      </p>
  
      <h2 class="sub-title">Servers</h2>
      <p class="content">
        Servers play a vital role in networking, handling requests from clients and providing services. Common types of servers include:
        <ul>
          <li><strong>Web Servers:</strong> Serve web pages to clients.</li>
          <li><strong>File Servers:</strong> Manage file storage and access.</li>
          <li><strong>Database Servers:</strong> Provide data storage and retrieval services.</li>
        </ul>
      </p>
  
  
      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the concepts discussed:</p>
      <div class="diagram-container">
        <img src="path/to/tcp_congestion_control.png" alt="TCP Congestion Control Diagram" />
        <img src="path/to/udp_overview.png" alt="User Datagram Protocol Overview Diagram" />
        <img src="path/to/multiplexing_demultiplexing.png" alt="Multiplexing and Demultiplexing Diagram" />
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
name: "Transport-layer",
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
"Transport Layer": [
  "Transport Layer Basics",
  "Functions of Transport Layer",
  "TCP (Transmission Control Protocol)",
  "UDP (User Datagram Protocol)",
  "Connection-Oriented vs Connectionless Communication",
  "Flow Control in Transport Layer",
  "Congestion Control in Transport Layer",
  "Port Numbers and Sockets",
  "Reliability and Error Detection in Transport Layer",
  "TCP Header Format",
  "UDP Header Format",
  "Three-Way Handshake (TCP)",
  "Transport Layer Protocols",
  "Application Layer and Transport Layer Interaction",
  "Transport Layer Security (TLS)"
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
const topic = "Transport layer";
const subtopic = "Transport layer BasicS";

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