<template>
  <div class="network-layer-container">
    <h1 class="main-title">Network Layer in Computer Networks</h1>
    <p class="intro">
      The Network Layer is a crucial component of the OSI (Open Systems Interconnection) model, responsible for logical addressing, routing, and packet forwarding across different networks.
    </p>

    <h2 class="sub-title">Core Functions of the Network Layer</h2>
    <ul class="characteristics-list">
      <li><strong>Logical Addressing:</strong> Assigns unique IP addresses to devices for identification and location tracking across networks.</li>
      <li><strong>Routing:</strong> Determines the most efficient path for data packets to travel from source to destination.</li>
      <li><strong>Packet Forwarding:</strong> Transfers data packets between different network segments based on logical addressing.</li>
      <li><strong>Fragmentation and Reassembly:</strong> Breaks large data packets into smaller units for transmission and reassembles them at the destination.</li>
    </ul>

    <h2 class="sub-title">Key Protocols in the Network Layer</h2>
    <ul class="characteristics-list">
      <li><strong>Internet Protocol (IP):</strong> The fundamental protocol for addressing and routing packets across networks.
        <ul>
          <li>IPv4: 32-bit addressing scheme</li>
          <li>IPv6: 128-bit addressing scheme with enhanced features</li>
        </ul>
      </li>
      <li><strong>Internet Control Message Protocol (ICMP):</strong> Used for diagnostic and control purposes, including ping and traceroute.</li>
      <li><strong>Address Resolution Protocol (ARP):</strong> Maps IP addresses to physical (MAC) addresses.</li>
      <li><strong>Dynamic Host Configuration Protocol (DHCP):</strong> Automatically assigns IP addresses to network devices.</li>
    </ul>

    <h2 class="sub-title">IP Addressing Mechanisms</h2>
    <p class="content">
      IP addressing provides a systematic way to identify and locate devices on a network. It involves network and host portions, subnet masks, and various addressing classes.
    </p>

    <h2 class="sub-title">Routing Algorithms</h2>
    <ul class="characteristics-list">
      <li><strong>Distance Vector Routing:</strong> Routers share their routing table with neighboring routers, updating based on hop count.</li>
      <li><strong>Link State Routing:</strong> Routers maintain a complete topology map of the network, calculating the shortest path.</li>
      <li><strong>Path Vector Routing:</strong> Used in interdomain routing, maintaining path information to avoid routing loops.</li>
    </ul>

    <h2 class="sub-title">Network Address Translation (NAT)</h2>
    <p class="content">
      NAT allows multiple devices on a local network to share a single public IP address, enhancing security and addressing IPv4 address exhaustion.
    </p>

    <h2 class="sub-title">Subnetting and CIDR</h2>
    <p class="content">
      Subnetting divides a network into smaller, more manageable subnetworks. Classless Inter-Domain Routing (CIDR) provides flexible IP address allocation.
    </p>

    <h2 class="sub-title">Quality of Service (QoS) in Network Layer</h2>
    <p class="content">
      QoS mechanisms prioritize certain types of network traffic to ensure performance for critical applications like VoIP and video streaming.
    </p>

    <h2 class="sub-title">Network Layer Security Challenges</h2>
    <ul class="characteristics-list">
      <li><strong>IP Spoofing:</strong> Attackers disguise their IP address to impersonate trusted sources.</li>
      <li><strong>Routing Attacks:</strong> Manipulation of routing tables to redirect or intercept network traffic.</li>
      <li><strong>Denial of Service (DoS):</strong> Overwhelming network resources to disrupt services.</li>
    </ul>

    <h2 class="sub-title">Emerging Trends in Network Layer</h2>
    <ul class="characteristics-list">
      <li><strong>Software-Defined Networking (SDN):</strong> Separates network control logic from underlying hardware.</li>
      <li><strong>IPv6 Adoption:</strong> Gradual transition to address the limitations of IPv4.</li>
      <li><strong>Enhanced Security Protocols:</strong> Development of more robust encryption and authentication mechanisms.</li>
    </ul>

    <h2 class="sub-title">Diagrams</h2>
    <div class="diagram-container">
      <img src="src\assets\study_imgs\networklayer3.avif" alt="Network Layer in OSI Model" class="imageedit"/>
      <img src="src\assets\study_imgs\networklayer2.png" alt="Routing Algorithms Comparison" class="imageedit"/>
    </div>
   
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
"Network Security": [
  "Network Security Basics",
  "Confidentiality, Integrity, and Availability (CIA Triad)",
  "Cryptography Basics",
  "Symmetric and Asymmetric Encryption",
  "Public Key Infrastructure (PKI)",
  "Digital Signatures and Certificates",
  "SSL/TLS (Secure Sockets Layer/Transport Layer Security)",
  "VPN (Virtual Private Network)",
  "Firewalls and Types of Firewalls",
  "Intrusion Detection and Prevention Systems (IDS/IPS)",
  "Access Control",
  "Authentication Protocols",
  "Network Security Attacks",
  "Denial of Service (DoS) and Distributed Denial of Service (DDoS) Attacks",
  "Network Sniffing and Spoofing",
  "Security Protocols (IPSec, SSL/TLS, SSH)",
  "Security Best Practices for Networks"
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
const topic = "Network Layer";
const subtopic = "Network Layer BasicS";

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