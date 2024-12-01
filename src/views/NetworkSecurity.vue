<template>
    <div class="network-security-container">
      <h1 class="main-title">Network Security and Cryptography Layer</h1>
      <p class="intro">
        Network Security encompasses the policies, practices, and technologies aimed at protecting networks and data from unauthorized access, attacks, and damage. Cryptography is a critical component of network security that provides confidentiality, integrity, and authenticity of data.
      </p>

      <h2 class="sub-title">The CIA Triad</h2>
      <p class="content">
        The CIA triad is a model for understanding the core principles of information security: Confidentiality, Integrity, and Availability. 
      </p>

      <h2 class="sub-title">Introduction to Firewall</h2>
      <p class="content">
        A firewall is a network security device that monitors and controls incoming and outgoing network traffic based on predetermined security rules.
      </p>

      <h2 class="sub-title">Types of Firewalls and Possible Attacks</h2>
      <ul class="characteristics-list">
        <li><strong>Packet-Filtering Firewalls:</strong> Examine packets and allow or deny them based on source/destination IP addresses and ports.</li>
        <li><strong>Stateful Inspection Firewalls:</strong> Track the state of active connections and make decisions based on the context of the traffic.</li>
        <li><strong>Proxy Firewalls:</strong> Intercept and inspect traffic before it reaches the intended destination.</li>
      </ul>

      <h2 class="sub-title">Firewall Methodologies</h2>
      <p class="content">
        Firewalls can employ various methodologies including filtering, proxying, and stateful inspection to manage network traffic effectively.
      </p>

      <h2 class="sub-title">Zone-Based Firewall</h2>
      <p class="content">
        A zone-based firewall segregates the network into multiple zones and applies security policies to control traffic between these zones.
      </p>

      <h2 class="sub-title">Zone-Based Firewall Configuration</h2>
      <p class="content">
        Configuration involves defining zones, associating interfaces with zones, and applying policies to govern traffic flow.
      </p>

      <h2 class="sub-title">How to Set Up a Firewall in Linux?</h2>
      <p class="content">
        To set up a firewall in Linux, tools like iptables or firewalld can be used. Basic commands involve defining rules for incoming and outgoing traffic.
      </p>

      <h2 class="sub-title">Message Authentication Codes (MAC)</h2>
      <p class="content">
        MACs provide a way to ensure the integrity and authenticity of a message through a shared secret key.
      </p>

      <h2 class="sub-title">How Message Authentication Code Works?</h2>
      <p class="content">
        MACs work by combining the message and a secret key to produce a fixed-size hash that is sent along with the message. The recipient can verify the integrity by computing the MAC again.
      </p>

      <h2 class="sub-title">HMAC Algorithm</h2>
      <p class="content">
        HMAC (Hash-based Message Authentication Code) uses a cryptographic hash function and a secret key to provide both data integrity and authenticity.
      </p>

      <h2 class="sub-title">Password Authentication Protocol (PAP)</h2>
      <p class="content">
        PAP is a simple authentication protocol that transmits passwords in plaintext, making it vulnerable to interception.
      </p>

      <h2 class="sub-title">Basic Network Attacks</h2>
      <ul class="characteristics-list">
        <li><strong>Denial of Service (DoS):</strong> Attacks aimed at making a network service unavailable.</li>
        <li><strong>Vishing:</strong> Voice phishing that exploits phone calls to deceive victims into providing personal information.</li>
        <li><strong>Birthday Attack:</strong> A type of cryptographic attack that exploits the mathematics behind the probability of collisions in hash functions.</li>
      </ul>

      <h2 class="sub-title">System Security</h2>
      <p class="content">
        System security involves measures taken to protect a system from unauthorized access or damage, ensuring data integrity and confidentiality.
      </p>

      <h2 class="sub-title">Private Browsing</h2>
      <p class="content">
        Private browsing modes in web browsers prevent the storage of browsing history and cookies, offering users an extra layer of privacy.
      </p>

      <h2 class="sub-title">Threat Modelling</h2>
      <p class="content">
        Threat modelling is the process of identifying potential threats to a system and defining measures to mitigate these threats.
      </p>

      <h2 class="sub-title">DFD Based Threat Modelling | Set 1</h2>
      <p class="content">
        Data Flow Diagrams (DFDs) help visualize data flow in a system, aiding in identifying potential vulnerabilities.
      </p>

      <h2 class="sub-title">DFD Based Threat Modelling | Set 2</h2>
      <p class="content">
        Further DFD analysis allows for a deeper understanding of interactions and vulnerabilities within a system.
      </p>

      <h2 class="sub-title">Types of Viruses</h2>
      <ul class="characteristics-list">
        <li><strong>File Infector Virus:</strong> Attaches itself to executable files.</li>
        <li><strong>Macro Virus:</strong> Infects documents and templates.</li>
        <li><strong>Polymorphic Virus:</strong> Changes its code to avoid detection.</li>
      </ul>

      <h2 class="sub-title">Denial of Service and Prevention</h2>
      <p class="content">
        Preventative measures against DoS attacks include rate limiting, traffic analysis, and robust firewall configurations.
      </p>

      <h2 class="sub-title">Denial of Service (DDoS) Attack</h2>
      <p class="content">
        DDoS attacks involve multiple compromised systems attacking a single target, making it difficult to mitigate.
      </p>

      <h2 class="sub-title">Unicode</h2>
      <p class="content">
        Unicode is a standardized encoding system for text that ensures consistency across different platforms and languages.
      </p>

      <h2 class="sub-title">RC4 Encryption Algorithm</h2>
      <p class="content">
        RC4 is a stream cipher known for its simplicity and speed but is considered less secure compared to modern algorithms.
      </p>

      <h2 class="sub-title">RSA Algorithm in Cryptography</h2>
      <p class="content">
        RSA is a widely used asymmetric encryption algorithm based on the mathematical difficulty of factoring large integers.
      </p>

      <h2 class="sub-title">RSA Algorithm using Multiple Precision Arithmetic Library</h2>
      <p class="content">
        Using libraries allows for handling very large integers necessary for RSA encryption and decryption processes.
      </p>

      <h2 class="sub-title">Weak RSA Decryption with Chinese-Remainder Theorem</h2>
      <p class="content">
        The Chinese-Remainder Theorem can be used to improve the efficiency of RSA decryption under certain conditions.
      </p>

      <h2 class="sub-title">How to Solve RSA Algorithm Problems?</h2>
      <p class="content">
        RSA problems typically involve generating keys, encrypting messages, and decrypting them using the private key.
      </p>

      <h2 class="sub-title">Hash Functions in System Security</h2>
      <p class="content">
        Hash functions create fixed-size hash values from variable-size data, ensuring data integrity and verifying authenticity.
      </p>

      <h2 class="sub-title">DNA Cryptography</h2>
      <p class="content">
        DNA cryptography utilizes the unique properties of DNA sequences to create secure cryptographic keys.
      </p>

      <h2 class="sub-title">RC5 Encryption Algorithm</h2>
      <p class="content">
        RC5 is a block cipher known for its variable block size, key size, and number of rounds, providing flexibility and security.
      </p>

      <h2 class="sub-title">ElGamal Encryption Algorithm</h2>
      <p class="content">
        ElGamal is an asymmetric key encryption algorithm based on the Diffie-Hellman key exchange, offering security through randomness.
      </p>

      <h2 class="sub-title">Caesar Cipher</h2>
      <p class="content">
        The Caesar Cipher is a simple substitution cipher that shifts letters in the alphabet by a fixed number of places.
      </p>

      <h2 class="sub-title">Cryptography Introduction</h2>
      <p class="content">
        Cryptography is the practice of securing communication and information through encoding and decoding messages.
      </p>

      <h2 class="sub-title">Cryptography | Traditional Symmetric Ciphers</h2>
      <p class="content">
        Traditional symmetric ciphers use the same key for both encryption and decryption, such as DES and AES.
      </p>

      <h2 class="sub-title">Block Cipher Modes of Operation</h2>
      <p class="content">
        Modes like ECB, CBC, and CTR define how block ciphers process data, affecting security and efficiency.
      </p>

      <h2 class="sub-title">Cryptography | Development of Cryptography</h2>
      <p class="content">
        Cryptography has evolved from simple manual techniques to complex algorithms designed to secure digital communication.
      </p>

      <h2 class="sub-title">Difference between AES and DES Ciphers</h2>
      <p class="content">
        AES is a more secure and efficient algorithm than DES, which has become outdated due to its shorter key length.
      </p>

      <h2 class="sub-title">Transforming a Plain Text Message to Cipher Text</h2>
      <p class="content">
        Transforming involves applying a cipher algorithm to plaintext, resulting in ciphertext that is unreadable without decryption.
      </p>

      <h2 class="sub-title">What is Cryptocurrency?</h2>
      <p class="content">
        Cryptocurrency is a digital or virtual currency that uses cryptography for security and operates on a decentralized network.
      </p>

      <h2 class="sub-title">Introduction to Crypto-Terminologies</h2>
      <p class="content">
        Understanding key terms such as blockchain, wallets, and mining is crucial for comprehending the cryptocurrency landscape.
      </p>

      <h2 class="sub-title">Quantum Cryptography</h2>
      <p class="content">
        Quantum cryptography leverages quantum mechanics to create secure communication channels resistant to eavesdropping.
      </p>

      <h2 class="sub-title">End-to-End Encryption (E2EE) in Computer Networks</h2>
      <p class="content">
        E2EE ensures that data transmitted between two endpoints is encrypted, preventing interception by third parties.
      </p>

      <h2 class="sub-title">IP Security (IPSec)</h2>
      <p class="content">
        IPSec is a framework for securing Internet Protocol (IP) communications through encryption and authentication.
      </p>

      <h2 class="sub-title">What is Packet Sniffing?</h2>
      <p class="content">
        Packet sniffing involves capturing and analyzing packets transmitted over a network, often used for network troubleshooting and security monitoring.
      </p>

      <h2 class="sub-title">Introduction to Sniffers</h2>
      <p class="content">
        Sniffers are tools that capture and analyze network traffic, which can be used for both legitimate and malicious purposes.
      </p>

      <h2 class="sub-title">Data Encryption Standard (DES) | Set 1</h2>
      <p class="content">
        DES is a symmetric-key algorithm that encrypts data in 64-bit blocks using a 56-bit key.
      </p>

      <h2 class="sub-title">End-to-End Encryption (E2EE) in Computer Network</h2>
      <p class="content">
        E2EE provides secure data transmission by ensuring that only the communicating users can read the messages.
      </p>

      <h2 class="sub-title">Types of Security Attacks | Active and Passive Attacks</h2>
      <p class="content">
        Active attacks involve modifying the data in transit, while passive attacks involve eavesdropping without altering the data.
      </p>

      <h2 class="sub-title">Types of Wireless and Mobile Device Attacks</h2>
      <ul class="characteristics-list">
        <li><strong>Man-in-the-Middle Attack:</strong> An attacker intercepts and potentially alters communication between two parties.</li>
        <li><strong>Evil Twin Attack:</strong> A rogue Wi-Fi access point mimicking a legitimate one to steal sensitive information.</li>
      </ul>

      <h2 class="sub-title">Types of Email Attacks</h2>
      <ul class="characteristics-list">
        <li><strong>Phishing:</strong> Fraudulent emails trick users into revealing personal information.</li>
        <li><strong>Spear Phishing:</strong> Targeted phishing attacks aimed at specific individuals.</li>
      </ul>

      <h2 class="sub-title">Sybil Attack</h2>
      <p class="content">
        A Sybil attack occurs when a single adversary creates multiple identities to gain a disproportionately large influence on a network.
      </p>

      <h2 class="sub-title">Malware and Its Types</h2>
      <ul class="characteristics-list">
        <li><strong>Virus:</strong> Attaches to files and spreads when those files are executed.</li>
        <li><strong>Worm:</strong> Self-replicating malware that spreads across networks.</li>
        <li><strong>Trojan Horse:</strong> Disguises itself as legitimate software to gain unauthorized access.</li>
      </ul>

      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the concepts discussed:</p>
      <div class="diagram-container">
        <img src="path/to/diagram1.png" alt="Diagram illustrating the CIA triad" />
        <img src="path/to/diagram2.png" alt="Diagram showing firewall types" />
        <img src="path/to/diagram3.png" alt="Diagram of encryption algorithms" />
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
const topic = "Network Security";
const subtopic = "Network security BasicS";

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