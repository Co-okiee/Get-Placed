<template>
    <div class="disk-management-container">
      <h1 class="main-title">Disk Management</h1>
      <p class="intro">
        Disk management is the process of managing disk drives in a computer system, which includes managing file systems, directory structures, and allocating space on storage devices.
      </p>

      <h2 class="sub-title">File Systems</h2>
      <p class="content">
        A file system is a method used by the operating system to manage files on a disk. It provides a way to store, organize, and retrieve files.
      </p>
      <img src="src\assets\study_imgs\os_disk1.webp" alt="File System Structure Diagram" class="diagram imageedit"/>

      <h2 class="sub-title">Unix File System</h2>
      <p class="content">
        The Unix File System (UFS) organizes files in a hierarchical structure, where everything is treated as a file, including devices and processes. UFS uses inodes to manage files and directories.
      </p>
      <img src="src\assets\study_imgs\os_disk2.png" alt="Unix File System Structure" class="diagram imageedit"/>

      <h2 class="sub-title">Implementing Directory Management using Shell Script</h2>
      <p class="content">
        Directory management can be automated using shell scripts. For example, a script can be written to create, delete, and list directories.
      </p>
      <pre>
        <code>
          #!/bin/bash
          echo "1. Create Directory"
          echo "2. Delete Directory"
          echo "3. List Directories"
          read -p "Choose an option: " option
          case $option in
              1) read -p "Enter directory name: " dirname
                 mkdir "$dirname"
                 ;;
              2) read -p "Enter directory name: " dirname
                 rmdir "$dirname"
                 ;;
              3) ls -d */
                 ;;
              *) echo "Invalid option!"
                 ;;
          esac
        </code>
      </pre>

      <h2 class="sub-title">File Directory | Path Name</h2>
      <p class="content">
        A file directory contains files and subdirectories, and the path name specifies the location of a file within the directory hierarchy. Absolute and relative paths are two types of path names.
      </p>

      <h2 class="sub-title">Structures of Directory</h2>
      <p class="content">
        Directory structures can be classified as single-level, two-level, and hierarchical. Each structure has its advantages and disadvantages in terms of organization and access speed.
      </p>

      <h2 class="sub-title">File Allocation Methods</h2>
      <ul class="characteristics-list">
        <li><strong>Contiguous Allocation:</strong> Files are stored in consecutive blocks.</li>
        <li><strong>Linked Allocation:</strong> Each file consists of a linked list of blocks.</li>
        <li><strong>Indexed Allocation:</strong> An index block contains pointers to the file blocks.</li>
      </ul>

      <h2 class="sub-title">File Access Methods</h2>
      <ul class="characteristics-list">
        <li><strong>Sequential Access:</strong> Files are read in order.</li>
        <li><strong>Random Access:</strong> Any block can be accessed directly.</li>
      </ul>

      <h2 class="sub-title">Secondary Memory</h2>
      <p class="content">
        Secondary memory refers to non-volatile storage devices, such as hard drives, that retain data even when the computer is powered off. It is used for long-term storage of data and applications.
      </p>

      <h2 class="sub-title">Secondary Memory – Hard Disk Drive</h2>
      <p class="content">
        A Hard Disk Drive (HDD) is a common type of secondary memory that uses magnetic storage to read and write data. It consists of spinning disks and read/write heads.
      </p>
      <img src="src\assets\study_imgs\os_disk3.jpg" alt="Hard Disk Drive Diagram" class="diagram imageedit"/>

      <h2 class="sub-title">Disk Scheduling Algorithms</h2>
      <p class="content">
        Disk scheduling algorithms determine the order in which disk I/O requests are processed. Common algorithms include FCFS, SSTF, SCAN, and C-SCAN.
      </p>

      <h2 class="sub-title">Program for SSTF Disk Scheduling Algorithm</h2>
      <p class="content">Below is a simple implementation of the Shortest Seek Time First (SSTF) disk scheduling algorithm:</p>
      <pre>
        <code>
          def SSTF(requests, head):
              seek_sequence = []
              while requests:
                  closest = min(requests, key=lambda x: abs(x - head))
                  seek_sequence.append(closest)
                  head = closest
                  requests.remove(closest)
              return seek_sequence

          requests = [98, 183, 37, 122, 14, 124, 65, 67]
          head = 53
          print("Seek Sequence:", SSTF(requests, head))
        </code>
      </pre>

      <h2 class="sub-title">What Exactly Spooling is All About?</h2>
      <p class="content">
        Spooling (Simultaneous Peripheral Operations Online) is a process where data is temporarily held in a buffer while being transferred between devices, allowing the CPU to perform other tasks concurrently.
      </p>

      <h2 class="sub-title">Difference between Spooling and Buffering</h2>
      <p class="content">
        <strong>Spooling:</strong> Involves managing data input/output operations for devices, allowing tasks to be performed in parallel. <br>
        <strong>Buffering:</strong> Temporarily holds data in memory to smooth out differences in data processing rates between two devices.
      </p>

      <h2 class="sub-title">Free Space Management</h2>
      <p class="content">
        Free space management keeps track of available disk space, ensuring that new files can be allocated efficiently. It uses bitmap or linked list methods to manage free blocks.
      </p>

 
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
const topic = "Disk Management";
const subtopic = "Disk Management";

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
color: #89dbce;
margin-top: 10px;
}

.imageedit {
  margin: 10px; /* Adds space around each image */
  padding: 5px; /* Optional: Adds inner space within the image border */
  border: 1px solid #ccc; /* Optional: Adds a border for better visibility */
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