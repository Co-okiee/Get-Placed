<template>
    <div class="dl-container">
      <h1 class="main-title">Data Link Layer</h1>
      <p class="intro">
        The Data Link Layer is the second layer of the OSI model. It is responsible for node-to-node data transfer and error detection and correction, ensuring reliable communication over a single link.
      </p>
  
      <h2 class="sub-title">Local Area Network (LAN) Technologies</h2>
      <p class="content">
        LAN technologies enable devices within a limited geographical area to communicate. Common technologies include Ethernet, Wi-Fi, and Token Ring.
      </p>
  
      <h2 class="sub-title">Computer Network | Bridges (Local Internetworking Device)</h2>
      <p class="content">
        Bridges connect multiple network segments, making them function as a single network. They filter traffic and reduce collisions by dividing a large network into smaller segments.
      </p>
  
      <h2 class="sub-title">Internetworking</h2>
      <p class="content">
        Internetworking involves connecting different networks to enable communication. Routers play a vital role in directing data between these networks.
      </p>
  
      <h2 class="sub-title">Framing In Data Link Layer</h2>
      <p class="content">
        Framing is the process of encapsulating network layer packets into frames. Each frame has a header and trailer for error detection and addressing.
      </p>
  
      <h2 class="sub-title">Introduction of MAC Address</h2>
      <p class="content">
        A MAC (Media Access Control) address is a unique identifier assigned to network interfaces for communication on the physical network segment. It consists of 48 bits and is usually represented in hexadecimal.
      </p>
  
      <h2 class="sub-title">MAC Filtering</h2>
      <p class="content">
        MAC filtering allows network administrators to control which devices can access the network based on their MAC addresses, enhancing security.
      </p>
  
      <h2 class="sub-title">Multiple Access Protocols</h2>
      <p class="content">
        These protocols determine how multiple devices share the same communication medium. Common protocols include CSMA/CD, CSMA/CA, and Token Ring.
      </p>
  
      <h2 class="sub-title">Ethernet Frame Format</h2>
      <p class="content">
        An Ethernet frame consists of the following fields: 
        <ul>
          <li>Destination MAC Address</li>
          <li>Source MAC Address</li>
          <li>EtherType/Length</li>
          <li>Payload (Data)</li>
          <li>Frame Check Sequence (FCS)</li>
        </ul>
      </p>
  
      <h2 class="sub-title">EtherChannel</h2>
      <p class="content">
        EtherChannel combines multiple Ethernet links into a single logical link, increasing bandwidth and providing redundancy.
      </p>
  
      <h2 class="sub-title">Difference between Byte Stuffing and Bit Stuffing</h2>
      <p class="content">
        Byte stuffing adds a special byte to the data to indicate a data frame boundary, while bit stuffing inserts a '0' after a sequence of five '1's to ensure a frame boundary.
      </p>
  
      <h2 class="sub-title">Implementing Byte Stuffing using Java</h2>
      <p class="content">
        Here’s a simple example of byte stuffing in Java:
        java
        public class ByteStuffing {
            public static String byteStuff(String data) {
                return data.replace("01111110", "011111110");
            }
        }
        
      </p>
  
      <h2 class="sub-title">Circuit Switching</h2>
      <p class="content">
        Circuit switching establishes a dedicated communication path between two endpoints, commonly used in traditional telephone networks.
      </p>
  
      <h2 class="sub-title">Packet Switching and Delays</h2>
      <p class="content">
        Packet switching breaks data into packets, which travel independently. Delays may occur due to routing and queuing processes.
      </p>
  
      <h2 class="sub-title">Circuit Switching VS Packet Switching</h2>
      <p class="content">
        Circuit switching provides a dedicated path with consistent bandwidth, while packet switching allows for more efficient use of resources, though it may introduce delays.
      </p>
  
      <h2 class="sub-title">Differences between Virtual Circuits & Datagram Networks</h2>
      <p class="content">
        Virtual circuits establish a predefined path for data, while datagram networks send packets independently, allowing for more flexibility.
      </p>
  
      <h2 class="sub-title">Switching Techniques: Message Switching</h2>
      <p class="content">
        Message switching stores entire messages at intermediate nodes before forwarding them, ensuring reliable delivery but introducing delays.
      </p>
  
      <h2 class="sub-title">Types of Switches</h2>
      <p class="content">
        Types of switches include:
        <ul>
          <li>Unmanaged Switches</li>
          <li>Managed Switches</li>
          <li>Layer 2 Switches</li>
          <li>Layer 3 Switches</li>
        </ul>
      </p>
  
      <h2 class="sub-title">Maximum Data Rate (Channel Capacity) for Noiseless and Noisy Channels</h2>
      <p class="content">
        The channel capacity for a noiseless channel is calculated using Shannon's Theorem, while for a noisy channel, it considers the signal-to-noise ratio.
      </p>
  
      <h2 class="sub-title">Hot Spot 2.0</h2>
      <p class="content">
        Hot Spot 2.0 is an advanced Wi-Fi feature that allows for seamless roaming between Wi-Fi networks, improving connectivity for mobile devices.
      </p>
  
      <h2 class="sub-title">Collision Avoidance in Wireless Networks</h2>
      <p class="content">
        Collision avoidance techniques, such as CSMA/CA, are used in wireless networks to minimize packet collisions during transmission.
      </p>
  
      <h2 class="sub-title">Traditional Wireless Mobile Communication</h2>
      <p class="content">
        Traditional wireless communication uses radio waves to transmit data, with various standards like GSM and CDMA for mobile networks.
      </p>
  
      <h2 class="sub-title">Carrier Sense Multiple Access (CSMA)</h2>
      <p class="content">
        CSMA is a network protocol that listens for a carrier signal before transmitting, reducing the chance of collisions.
      </p>
  
      <h2 class="sub-title">Collision Detection in CSMA/CD</h2>
      <p class="content">
        CSMA/CD detects collisions in a shared medium, allowing devices to stop transmitting and retry after a random back-off time.
      </p>
  
      <h2 class="sub-title">Efficiency of CSMA/CD</h2>
      <p class="content">
        The efficiency of CSMA/CD decreases with increased network traffic, as the probability of collisions rises.
      </p>
  
      <h2 class="sub-title">Back-off Algorithm for CSMA/CD</h2>
      <p class="content">
        The back-off algorithm determines how long a device should wait before attempting to retransmit after a collision occurs.
      </p>
  
      <h2 class="sub-title">Controlled Access Protocols</h2>
      <p class="content">
        Controlled access protocols, like Token Ring, ensure that only one device transmits at a time, preventing collisions.
      </p>
  
      <h2 class="sub-title">Virtual LAN (VLAN)</h2>
      <p class="content">
        VLANs segment a network into smaller, isolated groups, improving security and reducing broadcast traffic.
      </p>
  
      <h2 class="sub-title">Inter VLAN Routing by Layer 3 Switch</h2>
      <p class="content">
        Layer 3 switches can route traffic between VLANs, enabling communication while maintaining network segmentation.
      </p>
  
      <h2 class="sub-title">Computer Network | Private VLAN</h2>
      <p class="content">
        Private VLANs enhance security by isolating devices within the same VLAN, limiting communication between them.
      </p>
  
      <h2 class="sub-title">Computer Network | VLAN ACL (VACL)</h2>
      <p class="content">
        VLAN Access Control Lists (VACLs) filter traffic within VLANs based on specified rules, enhancing security.
      </p>
  
      <h2 class="sub-title">Access and Trunk Ports</h2>
      <p class="content">
        Access ports connect to end devices, while trunk ports carry traffic for multiple VLANs between switches.
      </p>
  
      <h2 class="sub-title">Role-Based Access Control</h2>
      <p class="content">
        Role-based access control assigns permissions based on user roles, enhancing security and simplifying management.
      </p>
  
      <h2 class="sub-title">Port Security</h2>
      <p class="content">
        Port security prevents unauthorized devices from connecting to a network port, improving overall network security.
      </p>
  
      <h2 class="sub-title">Inter-Switch Link (ISL) and IEEE 802.1Q</h2>
      <p class="content">
        ISL and IEEE 802.1Q are VLAN tagging protocols that allow switches to identify VLAN traffic across trunk links.
      </p>
  
      <h2 class="sub-title">Dynamic Trunking Protocol (DTP)</h2>
      <p class="content">
        DTP is a Cisco protocol that negotiates trunking between switches, automating the configuration of trunk ports.
      </p>
  
      <h2 class="sub-title">Sliding Window Protocol | Set 1 (Sender Side)</h2>
      <p class="content">
        The sliding window protocol allows the sender to send multiple frames before needing an acknowledgment, enhancing throughput.
      </p>
  
      <h2 class="sub-title">Sliding Window Protocol | Set 2 (Receiver Side)</h2>
      <p class="content">
        On the receiver side, the protocol manages the acknowledgment of received frames and ensures that frames are processed in order.
      </p>
  
      <h2 class="sub-title">Sliding Window Protocol | Set 3 (Selective Repeat)</h2>
      <p class="content">
        Selective Repeat allows the receiver to acknowledge non-contiguous frames, enabling retransmission of only the lost frames.
      </p>
  
      <h2 class="sub-title">Sliding Window Protocols Summary</h2>
      <p class="content">
        Sliding window protocols improve efficiency by allowing multiple frames to be in transit simultaneously, reducing wait times.
      </p>
  
      <h2 class="sub-title">Stop and Wait ARQ</h2>
      <p class="content">
        Stop and Wait ARQ requires the sender to wait for an acknowledgment after sending each frame, which can lead to inefficiencies.
      </p>
  
      <h2 class="sub-title">Difference between Stop and Wait, Go-Back-N, and Selective Repeat</h2>
      <p class="content">
        Stop and Wait sends one frame at a time, Go-Back-N allows multiple frames but retransmits from the last acknowledged frame, while Selective Repeat retransmits only the frames that are lost.
      </p>
  
      <h2 class="sub-title">Manchester Encoding</h2>
      <p class="content">
        Manchester encoding represents binary data with transitions, ensuring reliable clock recovery and reducing errors.
      </p>
  
      <h2 class="sub-title">Error Detection</h2>
      <p class="content">
        Error detection techniques, such as checksums and CRC (Cyclic Redundancy Check), identify errors in transmitted data.
      </p>
  
      <h2 class="sub-title">Hamming Code</h2>
      <p class="content">
        Hamming code is an error correction technique that can detect and correct single-bit errors in data.
      </p>
  
      <h2 class="sub-title">Program to Remotely Power On a PC Over the Internet Using the Wake-on-LAN Protocol</h2>
      <p class="content">
        The Wake-on-LAN protocol allows you to turn on a computer remotely. Here is a simple example in Python:
        python
        import socket
  
        def wake_on_lan(macaddress):
            macaddress = macaddress.replace(":", "")
            magic = bytes.fromhex("FF") * 6 + bytes.fromhex(macaddress) * 16
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(magic, ('&lt;broadcast&gt;', 9))
        
        wake_on_lan('00:11:22:33:44:55')
        
      </p>
  
      <h2 class="sub-title">Basics of Wi-Fi</h2>
      <p class="content">
        Wi-Fi technology allows devices to connect to a network wirelessly, using radio waves to transmit data.
      </p>
  
      <h2 class="sub-title">IEEE 802.11 Mac Frame</h2>
      <p class="content">
        The IEEE 802.11 MAC frame includes fields for frame control, duration, address fields, and data payload, facilitating wireless communication.
      </p>
  
      <h2 class="sub-title">Efficiency Of Token Ring</h2>
      <p class="content">
        Token Ring networks use a token-passing method to control access, which can enhance efficiency by preventing collisions.
      </p>
  
      <h2 class="sub-title">Token Bus (IEEE 802.4)</h2>
      <p class="content">
        Token Bus uses a token-passing protocol over a bus topology, allowing devices to transmit in a controlled manner.
      </p>
  
      <h2 class="sub-title">Multiplexing (Channel Sharing)</h2>
      <p class="content">
        Multiplexing combines multiple signals into one channel, improving efficiency in data transmission.
      </p>
  
      <h2 class="sub-title">Frequency Division and Time Division Multiplexing</h2>
      <p class="content">
        Frequency Division Multiplexing (FDM) allocates different frequency bands for each signal, while Time Division Multiplexing (TDM) assigns time slots for signals, enabling multiple communications over the same medium.
      </p>
  
      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the concepts discussed:</p>
      <div class="diagram-container">
        <img src="src\assets\study_imgs\datalink1.png" alt="Ethernet Frame Format" class="imageedit"/>
        <img src="src\assets\study_imgs\datalink2.jpg" alt="Circuit vs. Packet Switching" class="imageedit" />
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
const topic = "Data Link Layer";
const subtopic = "Data Link Layer Basics";

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
