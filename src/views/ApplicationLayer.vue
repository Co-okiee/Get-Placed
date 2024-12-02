<template>
    <div class="app-container">
      <h1 class="main-title">Application Layer</h1>
      <p class="intro">
        The Application Layer is the topmost layer of the OSI model, responsible for providing network services directly to end-user applications. It enables software applications to communicate over a network.
      </p>
  
      <h2 class="sub-title">Protocols in Application Layer</h2>
      <ul class="characteristics-list">
        <li><strong>Simple Mail Transfer Protocol (SMTP):</strong> A protocol used for sending emails between servers.</li>
        <li><strong>DNS (Domain Name System):</strong> Translates domain names into IP addresses.</li>
        <li><strong>Dynamic Host Configuration Protocol (DHCP):</strong> Dynamically assigns IP addresses to devices on a network.</li>
        <li><strong>File Transfer Protocol (FTP):</strong> Used for transferring files between a client and a server.</li>
        <li><strong>Simple Network Management Protocol (SNMP):</strong> A protocol for managing devices on IP networks.</li>
      </ul>
  
      <h2 class="sub-title">Why Does DNS Use UDP and Not TCP?</h2>
      <p class="content">
        DNS primarily uses UDP for its queries because it is faster and requires less overhead than TCP. Most DNS queries are small and do not require the reliability that TCP provides, making UDP a better choice for these operations.
      </p>
  
      <h2 class="sub-title">Address Resolution in DNS</h2>
      <p class="content">
        Address resolution is the process of translating a domain name into its corresponding IP address through the DNS, allowing users to access websites by name instead of by numerical address.
      </p>
  
      <h2 class="sub-title">DNS Spoofing or DNS Cache Poisoning</h2>
      <p class="content">
        DNS spoofing is a technique where an attacker corrupts the DNS cache to redirect users to malicious sites. This can compromise security and privacy by misleading users.
      </p>
  
      <h2 class="sub-title">Types of DNS Attacks and Tactics for Security</h2>
      <p class="content">
        Common types of DNS attacks include DNS spoofing, DDoS attacks, and amplification attacks. Implementing measures such as DNSSEC (Domain Name System Security Extensions) can help mitigate these risks.
      </p>
  
      <h2 class="sub-title">What’s the Difference Between http:// and https://?</h2>
      <p class="content">
        The primary difference is that HTTPS (HyperText Transfer Protocol Secure) provides a secure communication channel over the Internet through encryption, while HTTP does not.
      </p>
  
      <h2 class="sub-title">What’s the Difference Between HTML and HTTP?</h2>
      <p class="content">
        HTML (HyperText Markup Language) is a markup language used to create web pages, while HTTP is a protocol used for transferring data over the web.
      </p>
  
      <h2 class="sub-title">HTTP Non-Persistent & Persistent Connection</h2>
      <p class="content">
        Non-persistent connections open a new TCP connection for each request/response pair, while persistent connections keep the connection open for multiple requests, reducing latency.
      </p>
  
      <h2 class="sub-title">Asynchronous Transfer Mode (ATM)</h2>
      <p class="content">
        ATM is a network technology that uses fixed-size cells for data transmission, ensuring consistent performance and support for various data types, including voice and video.
      </p>
  
      <h2 class="sub-title">What is Local Host?</h2>
      <p class="content">
        Local host refers to the computer that is currently being used. It is typically accessed via the loopback IP address (127.0.0.1), which allows network applications to communicate with the local machine.
      </p>
  
      <h2 class="sub-title">DHCP Relay Agent</h2>
      <p class="content">
        A DHCP relay agent forwards DHCP requests and replies between clients and servers, especially when the server is on a different subnet from the client.
      </p>
  
      <h2 class="sub-title">How DHCP Server Dynamically Assigns IP Address to a Host?</h2>
      <p class="content">
        The DHCP server assigns IP addresses dynamically through a process that includes discovering available addresses, offering an address to a client, and acknowledging the allocation, allowing devices to connect to the network easily.
      </p>
  
      <h2 class="sub-title">What’s the Difference Between The Internet and The Web?</h2>
      <p class="content">
        The Internet is the global network of interconnected computers, while the Web (World Wide Web) is a collection of information accessed via the Internet, using HTTP to transfer data.
      </p>
  
      <h2 class="sub-title">Multipurpose Internet Mail Extensions (MIME)</h2>
      <p class="content">
        MIME extends the format of email messages to support text in character sets other than ASCII, as well as attachments of audio, video, and image files.
      </p>
  
      <h2 class="sub-title">Computer Network | MIME Media Types</h2>
      <p class="content">
        MIME media types define the nature and format of a document, file, or byte stream. This helps in identifying the type of data being sent over the Internet, ensuring it is handled correctly by applications.
      </p>
  
      <h2 class="sub-title">Quality of Service and Multimedia</h2>
      <p class="content">
        Quality of Service (QoS) ensures that multimedia applications, like video and audio streaming, receive sufficient bandwidth and low latency for optimal performance, prioritizing their data over other types.
      </p>
  
      <h2 class="sub-title">Web Caching and the Conditional GET Statements</h2>
      <p class="content">
        Web caching stores copies of web pages to reduce load times for subsequent requests. Conditional GET statements help browsers determine if a cached version is up-to-date, minimizing unnecessary data transfer.
      </p>
  

  
      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the concepts discussed:</p>
      <div class="diagram-container">
        <img src="src\assets\study_imgs\application1.png" alt="Overview of DNS Resolution Process" class="imageedit"/>
        <img src="src\assets\study_imgs\application2.webp" alt="Difference between HTTP and HTTPS" class="imageedit"/>
        <img src="src\assets\study_imgs\application3.png" alt="DHCP Address Assignment Process" class="imageedit"/>
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
const topic = "Application Layer";
const subtopic = "Application Layer Basics";

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