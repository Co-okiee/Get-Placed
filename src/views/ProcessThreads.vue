<template>
    <div class="os-container">
      <h1 class="main-title">Processes and Threads</h1>
      <p class="intro">
        Processes and threads are fundamental concepts in operating systems, playing a crucial role in multitasking and resource management. A process is an instance of a program in execution, while a thread is the smallest unit of processing that can be scheduled by the operating system.
      </p>
  
      <h2 class="sub-title">Threads and Its Types</h2>
      <p class="content">
        A thread is a lightweight process that shares the same memory space as other threads in the same process. The main types of threads include:
      </p>
      <ul class="characteristics-list">
        <li><strong>User Threads:</strong> Managed by user-level libraries and the operating system is unaware of them.</li>
        <li><strong>Kernel Threads:</strong> Managed by the operating system and can be scheduled independently.</li>
      </ul>
  
      <h2 class="sub-title">User-Level Thread vs Kernel-Level Thread</h2>
      <p class="content">
        User-level threads are faster to create and manage because they do not require kernel mode switching. However, kernel-level threads can take advantage of multiple processors.
      </p>
  
      <h2 class="sub-title">Process-based and Thread-based Multitasking</h2>
      <p class="content">
        In process-based multitasking, multiple processes share system resources. In contrast, thread-based multitasking allows multiple threads within the same process to share memory and resources, improving efficiency.
      </p>
  
      <h2 class="sub-title">Multithreading Models</h2>
      <ul class="characteristics-list">
        <li><strong>Many-to-One Model:</strong> Many user threads mapped to a single kernel thread.</li>
        <li><strong>One-to-One Model:</strong> Each user thread maps to a kernel thread.</li>
        <li><strong>Many-to-Many Model:</strong> Many user threads mapped to many kernel threads.</li>
      </ul>
  
      <h2 class="sub-title">Benefits of Multithreading</h2>
      <ul>
        <li>Improved application responsiveness.</li>
        <li>Efficient CPU utilization by overlapping I/O and computation.</li>
        <li>Resource sharing among threads leading to reduced overhead.</li>
      </ul>
  
      <h2 class="sub-title">Zombie Processes and Their Prevention</h2>
      <p class="content">
        A zombie process is a process that has completed execution but still has an entry in the process table. It can be prevented by ensuring that the parent process reads the exit status of the child process using wait() system call.
      </p>
  
      <h2 class="sub-title">Maximum Number of Zombie Processes a System Can Handle</h2>
      <p class="content">
        The maximum number of zombie processes is determined by the system's process table size, which varies between operating systems.
      </p>
  
      <h2 class="sub-title">Remote Procedure Call (RPC)</h2>
      <p class="content">
        RPC is a protocol that allows a program to execute a procedure on a remote server as if it were a local procedure call, enabling communication between processes in different address spaces.
      </p>
  
      <h2 class="sub-title">Memory Management</h2>
      <h3 class="sub-sub-title">Memory Hierarchy Design and its Characteristics</h3>
      <p class="content">
        Memory hierarchy consists of various levels of memory (e.g., cache, RAM, disk) that balance speed, size, and cost, ensuring efficient data access.
      </p>
  
      <h3 class="sub-sub-title">Introduction to Memory and Memory Units</h3>
      <p class="content">
        Memory is the component of a computer that stores data and instructions for immediate access, measured in bytes (B), kilobytes (KB), megabytes (MB), etc.
      </p>
  
      <h3 class="sub-sub-title">Different Types of RAM</h3>
      <ul class="characteristics-list">
        <li><strong>DRAM (Dynamic RAM):</strong> Needs to be refreshed thousands of times per second.</li>
        <li><strong>SRAM (Static RAM):</strong> Faster and more reliable than DRAM, used in cache memory.</li>
      </ul>
  
      <h3 class="sub-sub-title">Buddy System: Memory Allocation Technique</h3>
      <p class="content">
        The buddy system divides memory into partitions to minimize fragmentation and enables efficient allocation and deallocation.
      </p>
  
      <h3 class="sub-sub-title">Partition Allocation Method</h3>
      <ul class="characteristics-list">
        <li><strong>Fixed Partitioning:</strong> Memory is divided into fixed-sized partitions.</li>
        <li><strong>Variable Partitioning:</strong> Memory is divided based on the needs of the processes.</li>
        <li><strong>Non-Contiguous Allocation:</strong> Memory is allocated in non-contiguous blocks to reduce fragmentation.</li>
      </ul>
  
      <h3 class="sub-sub-title">Logical vs Physical Address</h3>
      <p class="content">
        Logical addresses are generated by the CPU, while physical addresses refer to actual locations in memory. The memory management unit (MMU) maps logical addresses to physical addresses.
      </p>
  
      <h3 class="sub-sub-title">Paging</h3>
      <p class="content">
        Paging divides the process's memory into fixed-size pages and maps them to physical memory frames, eliminating fragmentation.
      </p>
  
      <h3 class="sub-sub-title">Requirements of Memory Management System</h3>
      <ul>
        <li>Efficient allocation and deallocation of memory.</li>
        <li>Protection and isolation of processes.</li>
        <li>Support for virtual memory management.</li>
      </ul>
  
      <h3 class="sub-sub-title">Memory Management – Mapping Virtual Addresses to Physical Addresses</h3>
      <p class="content">
        This involves using page tables to translate virtual addresses to physical addresses, ensuring that each process operates within its allocated memory space.
      </p>
  
      <h3 class="sub-sub-title">Page Table Entries</h3>
      <p class="content">
        Page tables store the mapping between virtual pages and physical frames, containing the frame number and status bits (e.g., valid/invalid).
      </p>
  
      <h3 class="sub-sub-title">Virtual Memory</h3>
      <p class="content">
        Virtual memory allows processes to use more memory than physically available by using disk space as an extension of RAM.
      </p>
  
      <h3 class="sub-sub-title">Memory Interleaving</h3>
      <p class="content">
        Memory interleaving distributes memory addresses across multiple memory banks to enhance access speed and reduce bottlenecks.
      </p>
  
      <h3 class="sub-sub-title">Virtual Memory Questions</h3>
      <p class="content">
        Common questions include:
        <ul>
          <li>What is the difference between paging and segmentation?</li>
          <li>How does virtual memory improve system performance?</li>
        </ul>
      </p>
  
      <h3 class="sub-sub-title">Operating System-based Virtualization</h3>
      <p class="content">
        This involves creating virtual instances of hardware resources to run multiple operating systems on a single machine, enhancing resource utilization.
      </p>
  
      <h3 class="sub-sub-title">Inverted Page Table</h3>
      <p class="content">
        An inverted page table is a memory management scheme that uses a single table for mapping all physical frames to their corresponding pages in memory, reducing the size of page tables.
      </p>
  
      <h3 class="sub-sub-title">Swap Space</h3>
      <p class="content">
        Swap space is a reserved portion of disk space used to hold data that cannot fit in RAM, allowing for larger process execution.
      </p>
  
      <h3 class="sub-sub-title">Page Fault Handling</h3>
      <p class="content">
        When a page fault occurs, the operating system pauses the process, retrieves the page from disk, and updates the page table before resuming execution.
      </p>
  
      <h3 class="sub-sub-title">Segmentation</h3>
      <p class="content">
        Segmentation divides memory into variable-sized segments based on the logical structure of a program, providing a more intuitive memory management approach.
      </p>
  
      <h3 class="sub-sub-title">Memory Segmentation in 8086 Microprocessor</h3>
      <p class="content">
        In 8086 microprocessor architecture, memory is segmented to improve access efficiency, allowing different segments for code, data, and stack.
      </p>
  
      <h3 class="sub-sub-title">Program for Next Fit Algorithm in Memory Management</h3>
      <p class="content">
        The next-fit algorithm allocates the next available memory block for a process, reducing the need to search from the beginning.
        <pre><code>
  // Example of Next Fit Algorithm
  void nextFit(int size[], int m, int processSize[], int n) {
      int allocation[n];
      for (int i = 0; i < n; i++) {
          allocation[i] = -1;
      }
      int j = 0; 
      for (int i = 0; i < n; i++) {
          while (j < m) {
              if (size[j] >= processSize[i]) {
                  allocation[i] = j;
                  size[j] -= processSize[i];
                  break;
              }
              j++;
          }
          if (j == m) {
              j = 0;
          }
      }
  }
        </code></pre>
      </p>
  
      <h3 class="sub-sub-title">Overlays in Memory Management</h3>
      <p class="content">
        Overlays allow a program to be divided into smaller segments, loading only necessary segments into memory to run, optimizing memory usage.
      </p>
  
      <h3 class="sub-sub-title">Page Replacement Algorithms</h3>
      <p class="content">
        Page replacement algorithms manage the swapping of pages in and out of physical memory, including:
        <ul>
          <li>Least Recently Used (LRU)</li>
          <li>Optimal Page Replacement</li>
          <li>Least Frequently Used (LFU)</li>
        </ul>
      </p>
  
      <h3 class="sub-sub-title">Program for Page Replacement Algorithms | Set 1 (LRU)</h3>
      <p class="content">
        <pre><code>
  // Example of LRU Page Replacement Algorithm
  void lru(int pages[], int n, int capacity) {
      int pageFaults = 0;
      int memory[capacity];
      for (int i = 0; i < capacity; i++) {
          memory[i] = -1;
      }
      for (int i = 0; i < n; i++) {
          bool found = false;
          for (int j = 0; j < capacity; j++) {
              if (memory[j] == pages[i]) {
                  found = true;
                  break;
              }
          }
          if (!found) {
              memory[pageFaults % capacity] = pages[i];
              pageFaults++;
          }
      }
  }
        </code></pre>
      </p>
  
      <h3 class="sub-sub-title">Program for Optimal Page Replacement Algorithm</h3>
      <p class="content">
        <pre><code>
  // Example of Optimal Page Replacement Algorithm
  int optimal(int pages[], int n, int capacity) {
      int pageFaults = 0;
      int memory[capacity];
      for (int i = 0; i < capacity; i++) {
          memory[i] = -1;
      }
      for (int i = 0; i < n; i++) {
          bool found = false;
          for (int j = 0; j < capacity; j++) {
              if (memory[j] == pages[i]) {
                  found = true;
                  break;
              }
          }
          if (!found) {
              int farthest = -1, index = -1;
              for (int j = 0; j < capacity; j++) {
                  int nextUse = -1;
                  for (int k = i + 1; k < n; k++) {
                      if (memory[j] == pages[k]) {
                          nextUse = k;
                          break;
                      }
                  }
                  if (nextUse == -1) {
                      index = j;
                      break;
                  }
                  if (nextUse > farthest) {
                      farthest = nextUse;
                      index = j;
                  }
              }
              memory[index] = pages[i];
              pageFaults++;
          }
      }
      return pageFaults;
  }
        </code></pre>
      </p>
  
      <h3 class="sub-sub-title">LFU (Least Frequently Used) Cache Implementation</h3>
      <p class="content">
        The LFU cache keeps track of the frequency of page accesses, replacing the least frequently used page when a new page needs to be loaded.
      </p>
  
      <h3 class="sub-sub-title">Second Chance (Clock) Page Replacement Policy</h3>
      <p class="content">
        The second chance algorithm gives pages a second chance to stay in memory if they have been accessed recently, efficiently managing page replacement.
      </p>
  
      <h3 class="sub-sub-title">Techniques to Handle Thrashing</h3>
      <p class="content">
        Thrashing can be minimized through techniques like:
        <ul>
          <li>Increasing the amount of physical memory.</li>
          <li>Using better page replacement algorithms.</li>
          <li>Optimizing application memory usage.</li>
        </ul>
      </p>
  
      <h3 class="sub-sub-title">Allocating Kernel Memory (Buddy System and Slab System)</h3>
      <p class="content">
        The buddy system divides memory into blocks to minimize fragmentation, while the slab system manages memory in fixed-size caches for efficient allocation and deallocation.
      </p>
  
      <h3 class="sub-sub-title">Program for Buddy Memory Allocation Scheme in Operating Systems | Set 1 (Allocation)</h3>
      <p class="content">
        <pre><code>
  // Example of Buddy Memory Allocation
  void buddyAllocate(int size) {
      // Implementation of buddy allocation
      // Pseudo code for buddy system allocation
  }
        </code></pre>
      </p>
  
      <h3 class="sub-sub-title">Program for Buddy Memory Allocation Scheme in Operating Systems | Set 2 (Deallocation)</h3>
      <p class="content">
        <pre><code>
  // Example of Buddy Memory Deallocation
  void buddyDeallocate(int address) {
      // Implementation of buddy deallocation
      // Pseudo code for buddy system deallocation
  }
        </code></pre>
      </p>
  
      <h3 class="sub-sub-title">Static and Dynamic Libraries | Set 1</h3>
      <p class="content">
        Static libraries are linked at compile time, while dynamic libraries are linked at runtime, allowing for smaller executable sizes.
      </p>
  
      <h3 class="sub-sub-title">Working with Shared Libraries | Set 1</h3>
      <p class="content">
        Shared libraries can be used by multiple programs, reducing memory consumption and improving loading times.
      </p>
  
      <h3 class="sub-sub-title">Working with Shared Libraries | Set 2</h3>
      <p class="content">
        Understanding how to create, link, and manage shared libraries is crucial for efficient program development.
      </p>
  
      <h3 class="sub-sub-title">Named Pipe or FIFO with Example C Program</h3>
      <p class="content">
        A named pipe (FIFO) allows for inter-process communication, enabling data transfer between processes.
        <pre><code>
  // Example of Named Pipe in C
  #include &lt;stdio.h&gt;
  #include &lt;stdlib.h&gt;
  #include &lt;unistd.h&gt;
  #include &lt;fcntl.h&gt;
  
  int main() {
      mkfifo("myfifo", 0666);
      char arr[80];
      int fd = open("myfifo", O_WRONLY);
      printf("Enter data: ");
      fgets(arr, 80, stdin);
      write(fd, arr, sizeof(arr));
      close(fd);
      return 0;
  }
        </code></pre>
      </p>
  
      <h3 class="sub-sub-title">Tracing Memory Usage in Linux</h3>
      <p class="content">
        Linux provides tools like <code>top</code>, <code>htop</code>, and <code>free</code> for monitoring memory usage, enabling efficient resource management.
      </p>
  
      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the concepts discussed:</p>
      <div class="diagram-container">
        <img src="src\assets\study_imgs\os_pt1.webp" alt="Diagram illustrating Threads vs Processes" class="imageedit"/>
        <img src="src\assets\study_imgs\os_pt2.png" alt="Memory Management Diagram" class="imageedit"/>
        <!-- <img src="path/to/diagram3.png" alt="Paging and Segmentation Comparison" class="imageedit"/> -->
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
const topic = "Process Threads";
const subtopic = "Process Threads concept";

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
color: #73cdc3;
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