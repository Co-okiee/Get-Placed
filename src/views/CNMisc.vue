<template>
    <div class="misc-container">
      <h1 class="main-title">Miscellaneous Networking and Virtualization Concepts</h1>
      <p class="intro">
        This section explores various networking and virtualization concepts that are vital in understanding modern computing environments.
      </p>
  
      <h2 class="sub-title">Onion Routing</h2>
      <p class="content">
        Onion routing is a technique for anonymous communication over a computer network. Messages are encapsulated in layers of encryption, resembling the layers of an onion. The data is routed through a series of nodes, each removing a layer of encryption to reveal the next node, ensuring privacy and anonymity for users.
      </p>
      <img src="src\assets\study_imgs\devices1.jpeg" alt="Onion Routing Diagram" class="imageedit"/>
  
      <h2 class="sub-title">Types of Server Virtualization</h2>
      <ul class="characteristics-list">
        <li><strong>Full Virtualization:</strong> Emulates the underlying hardware, allowing multiple operating systems to run concurrently.</li>
        <li><strong>Paravirtualization:</strong> The guest OS is modified to interact with the hypervisor directly for better performance.</li>
        <li><strong>OS-Level Virtualization:</strong> The host OS runs multiple isolated user-space instances (containers).</li>
      </ul>
  
      <h2 class="sub-title">Cloud Computing</h2>
      <p class="content">
        Cloud computing provides on-demand access to a shared pool of configurable computing resources, allowing for rapid provisioning and release with minimal management effort. 
        <strong>Characteristics of Virtualization:</strong> 
        Scalability, flexibility, and cost-effectiveness are primary characteristics of cloud computing.
      </p>
  
      <h2 class="sub-title">On-Premises Cost Estimates of Virtualization</h2>
      <p class="content">
        On-premises virtualization incurs costs associated with hardware, software licenses, maintenance, and personnel. Companies must consider these factors when calculating total cost of ownership (TCO).
      </p>
  
      <h2 class="sub-title">Hardware-Based Virtualization</h2>
      <p class="content">
        This approach uses hardware features (such as Intel VT or AMD-V) to enable multiple operating systems to run on a single physical machine, enhancing performance and resource utilization.
      </p>
  
      <h2 class="sub-title">Operating System-Based Virtualization</h2>
      <p class="content">
        This type relies on the host operating system to create and manage virtual environments. It is often more lightweight than hardware-based virtualization, allowing for quick deployments.
      </p>
  
      <h2 class="sub-title">Digital Subscriber Line (DSL)</h2>
      <p class="content">
        DSL is a high-speed internet connection that transmits data over traditional telephone lines, allowing for simultaneous voice and data transmission. It is widely used for residential internet access.
      </p>
  
      <h2 class="sub-title">Image Steganography</h2>
      <p class="content">
        Image steganography is the practice of hiding information within an image file. It can be used for secure communications by embedding secret data in a way that is not easily detectable.
      </p>
  
      <h2 class="sub-title">Network Neutrality</h2>
      <p class="content">
        Network neutrality is the principle that internet service providers must treat all data on the internet equally, without discriminating or charging differently by user, content, or website.
      </p>
  
      <h2 class="sub-title">Basics of NS2 and OTcl/Tcl Script</h2>
      <p class="content">
        NS2 (Network Simulator 2) is a discrete event simulator used for networking research. OTcl is an object-oriented extension of Tcl, used for scripting in NS2 simulations to configure network protocols and behaviors.
      </p>
  
      <h2 class="sub-title">Voice over Internet Protocol (VoIP)</h2>
      <p class="content">
        VoIP technology allows for voice communication and multimedia sessions over the Internet. It converts voice signals into digital packets for transmission, enabling phone calls over the Internet.
      </p>
  
      <h2 class="sub-title">Cisco Router Modes</h2>
      <p class="content">
        Cisco routers have several operational modes including User mode, Privileged mode, Global Configuration mode, and Interface Configuration mode, each allowing different levels of command access and configuration capabilities.
      </p>
  
      <h2 class="sub-title">Cisco Router Basic Commands</h2>
      <ul class="characteristics-list">
        <li><strong>show running-config:</strong> Displays the current configuration of the router.</li>
        <li><strong>configure terminal:</strong> Enters global configuration mode.</li>
        <li><strong>ping:</strong> Tests connectivity to another network device.</li>
      </ul>
  
      <h2 class="sub-title">Backing Up Cisco IOS Router Image</h2>
      <p class="content">
        To back up a Cisco IOS router image, use the command <code>copy flash tftp</code> to transfer the image from the router's flash memory to a TFTP server.
      </p>
  
      <h2 class="sub-title">Basic Configuration of Adaptive Security Appliance (ASA)</h2>
      <p class="content">
        ASA is used for network security. Basic configurations include defining interfaces, setting up security levels, and configuring routing protocols.
      </p>
  
      <h2 class="sub-title">Adaptive Security Appliance (ASA) Features</h2>
      <ul class="characteristics-list">
        <li><strong>Firewall:</strong> Provides stateful inspection of traffic.</li>
        <li><strong>VPN Support:</strong> Allows secure remote access to internal resources.</li>
        <li><strong>Intrusion Prevention:</strong> Monitors network traffic for malicious activity.</li>
      </ul>
  
      <h2 class="sub-title">Default Flow of Traffic (ASA)</h2>
      <p class="content">
        By default, traffic from a lower security level to a higher security level is allowed, while traffic in the opposite direction is denied unless explicitly permitted.
      </p>
  
      <h2 class="sub-title">Cisco ASA Redistribution Example</h2>
      <p class="content">
        Redistribution allows routing information from different protocols to be shared. For example, to redistribute OSPF into EIGRP, use the command <code>redistribute ospf 1 metric 100</code>.
      </p>
  
      <h2 class="sub-title">Telnet and SSH on Adaptive Security Appliance (ASA)</h2>
      <p class="content">
        Telnet provides unencrypted access to the ASA, while SSH offers secure encrypted access. Configuration requires enabling the respective protocol and specifying user credentials.
      </p>
  
      <h2 class="sub-title">Near Field Communication (NFC)</h2>
      <p class="content">
        NFC is a short-range wireless technology that allows for data transfer between devices within close proximity, often used in contactless payments and data sharing.
      </p>
  
      <h2 class="sub-title">Relabel-to-Front Algorithm</h2>
      <p class="content">
        The relabel-to-front algorithm is a method for maintaining a list where elements can be moved to the front when accessed, optimizing access times in data structures.
      </p>
  
      <h2 class="sub-title">Berkeley’s Algorithm</h2>
      <p class="content">
        Berkeley’s algorithm is a method for synchronizing time across distributed systems, where a coordinator collects timestamps from various nodes and calculates an average time to set on each node.
      </p>
  
      <h2 class="sub-title">Cristian’s Algorithm</h2>
      <p class="content">
        Cristian’s algorithm is another time synchronization method that involves a time server providing its time to a requesting client, which adjusts its clock based on the received time and network delays.
      </p>
  
      <h2 class="sub-title">Universal Serial Bus (USB) in Computer Network</h2>
      <p class="content">
        USB is a standard for connecting peripherals to a computer. It allows for data transfer and power supply through a single interface, facilitating easy connections for various devices.
      </p>
  
      <h2 class="sub-title">Type-C Port in Computer Network</h2>
      <p class="content">
        The USB Type-C port is a universal connector that supports higher power delivery and faster data transfer rates compared to previous USB versions, enhancing connectivity across devices.
      </p>
  
      
  
      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the concepts discussed:</p>
      <div class="diagram-container">
        <img src="src\assets\study_imgs\devices2.jpg" alt="Types of Server Virtualization" class="imageedit" />
        <img src="src\assets\study_imgs\devices3.jpg" alt="Voice over IP Diagram" class="imageedit"/>
        <img src="src\assets\study_imgs\devices4.jpg" alt="Near Field Communication Diagram" class="imageedit"/>
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
  name: "misc",
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
  "Miscellaneous": [
    "Introduction to Networking Concepts",
    "OSI vs TCP/IP Models",
    "IP Addressing and Subnetting",
    "DNS and Domain Name Resolution",
    "Network Topologies and Their Applications",
    "Basic Networking Commands (ping, tracert, ipconfig)",
    "Virtual Private Network (VPN)",
    "Cloud Networking and Virtualization",
    "Quality of Service (QoS)",
    "Network Design Principles",
    "Network Security Best Practices",
    "Introduction to IPv6",
    "Troubleshooting Network Connectivity",
    "Network Performance Metrics (Latency, Throughput, Packet Loss)",
    "Software-Defined Networking (SDN)",
    "Network Automation Tools",
    "Introduction to Network Monitoring Tools",
    "Network Management Protocols (SNMP, NetFlow)",
    "Network Architecture and Scaling",
    "IoT and Networking"
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
  const topic = "Misclleneous";
  const subtopic = "Misclleneous BasicS";
  
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