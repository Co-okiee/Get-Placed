<template>
    <div class="cpu-scheduling-container">
      <h1 class="main-title">CPU Scheduling</h1>
      <p class="intro">
        CPU scheduling is a crucial aspect of operating systems that manages the execution of processes by allocating CPU time. Efficient CPU scheduling enhances system performance and responsiveness.
      </p>
  
      <h2 class="sub-title">Process</h2>
      <h3 class="type-title">Introduction and Different States</h3>
      <p class="content">
        A process is a program in execution. It goes through various states: new, ready, running, waiting, and terminated.
      </p>
  
      <h3 class="type-title">States of a Process</h3>
      <ul>
        <li><strong>New:</strong> The process is being created.</li>
        <li><strong>Ready:</strong> The process is waiting to be assigned to a CPU.</li>
        <li><strong>Running:</strong> The process is currently being executed.</li>
        <li><strong>Waiting:</strong> The process is waiting for some event to occur (e.g., I/O completion).</li>
        <li><strong>Terminated:</strong> The process has finished execution.</li>
      </ul>
  
      <h2 class="sub-title">Process Table and Process Control Block (PCB)</h2>
      <p class="content">
        The Process Table is a data structure that holds information about all processes. The PCB contains essential details such as the process state, program counter, CPU registers, memory management information, and I/O status information.
      </p>
  
      <h2 class="sub-title">Process Scheduler</h2>
      <p class="content">
        The process scheduler is responsible for determining which process runs at any given time, ensuring efficient CPU utilization and process management.
      </p>
  
      <h2 class="sub-title">CPU Scheduling</h2>
      <p class="content">
        CPU scheduling is the method by which processes are assigned to the CPU. Different scheduling algorithms determine how processes are prioritized for CPU access.
      </p>
  
      <h2 class="sub-title">Preemptive and Non-Preemptive Scheduling</h2>
      <p class="content">
        <strong>Preemptive Scheduling:</strong> The operating system can interrupt a currently running process to start or resume another. <br />
        <strong>Non-Preemptive Scheduling:</strong> Once a process is in the running state, it cannot be interrupted until it completes its execution.
      </p>
  
      <h2 class="sub-title">Measure the Time Spent in Context Switch</h2>
      <p class="content">
        Context switching time is the time taken to save the state of the currently running process and load the state of the next process. This overhead can impact system performance.
      </p>
  
      <h2 class="sub-title">Difference Between Dispatcher and Scheduler</h2>
      <ul>
        <li><strong>Dispatcher:</strong> A module that gives control of the CPU to the process selected by the scheduler.</li>
        <li><strong>Scheduler:</strong> Determines which process will run at a given time.</li>
      </ul>
  
      <h2 class="sub-title">FCFS Scheduling</h2>
      <h3 class="type-title">Set 1</h3>
      <p class="content">
        First-Come, First-Served (FCFS) is the simplest CPU scheduling algorithm that processes requests in the order they arrive.
      </p>
      <h3 class="type-title">Set 2</h3>
      <pre><code>
  // Example of FCFS Scheduling
  processQueue = [P1, P2, P3]
  for each process in processQueue:
    execute process
    calculate waiting time
  </code></pre>
  
      <h2 class="sub-title">Convoy Effect in Operating Systems</h2>
      <p class="content">
        The convoy effect occurs when shorter processes wait for a long process to finish, leading to inefficient CPU utilization.
      </p>
  
      <h2 class="sub-title">Belady’s Anomaly</h2>
      <p class="content">
        Belady's anomaly is a phenomenon where increasing the number of page frames results in an increase in the number of page faults for certain page replacement algorithms.
      </p>
  
      <h2 class="sub-title">Shortest Job First (SJF) Scheduling</h2>
      <h3 class="type-title">Set 1 (Non-Preemptive)</h3>
      <p class="content">
        SJF schedules processes based on their burst time, with the shortest burst time being executed first.
      </p>
      <h3 class="type-title">Set 2 (Preemptive)</h3>
      <pre><code>
  // Example of Preemptive SJF Scheduling
  while processes remain:
    choose process with shortest remaining time
    execute process
  </code></pre>
  
      <h2 class="sub-title">Shortest Job First Scheduling with Predicted Burst Time</h2>
      <p class="content">
        When burst time can be predicted, SJF can efficiently manage the queue, reducing average waiting time.
      </p>
  
      <h2 class="sub-title">Longest Remaining Time First (LRTF) Program</h2>
      <p class="content">
        LRTF is a preemptive version of SJF that selects the process with the longest remaining time for execution.
      </p>
      <pre><code>
  // Example of LRTF Scheduling
  while processes remain:
    choose process with longest remaining time
    execute process
  </code></pre>
  
      <h2 class="sub-title">Round Robin Scheduling</h2>
      <p class="content">
        Round Robin scheduling allocates a fixed time slice to each process in the ready queue, cycling through them until all processes are complete.
      </p>
      
      <h2 class="sub-title">Selfish Round Robin Scheduling</h2>
      <p class="content">
        In selfish round robin, processes may not yield control voluntarily, potentially leading to starvation for lower-priority processes.
      </p>
  
      <h2 class="sub-title">Round Robin Scheduling with Different Arrival Times</h2>
      <p class="content">
        Managing processes that arrive at different times can complicate round robin scheduling, requiring careful management of the ready queue.
      </p>
  
      <h2 class="sub-title">Priority Scheduling</h2>
      <p class="content">
        Priority scheduling assigns priority levels to processes, allowing higher priority processes to preempt lower priority ones.
      </p>
  
      <h2 class="sub-title">Program for Preemptive Priority CPU Scheduling</h2>
      <pre><code>
  // Example of Preemptive Priority Scheduling
  while processes remain:
    choose highest priority process
    execute process
  </code></pre>
  
      <h2 class="sub-title">Priority Scheduling with Different Arrival Times – Set 2</h2>
      <p class="content">
        Managing priorities effectively requires consideration of arrival times to ensure fair allocation of CPU time.
      </p>
  
      <h2 class="sub-title">Starvation and Aging in Operating Systems</h2>
      <p class="content">
        Starvation occurs when a process is perpetually denied the resources it needs to execute. Aging is a technique used to gradually increase the priority of waiting processes to prevent starvation.
      </p>
  
      <h2 class="sub-title">Highest Response Ratio Next (HRRN) Scheduling</h2>
      <p class="content">
        HRRN scheduling selects processes based on the ratio of waiting time to service time, favoring processes that have waited the longest relative to their burst time.
      </p>
  
      <h2 class="sub-title">Multilevel Queue Scheduling</h2>
      <p class="content">
        Multilevel queue scheduling divides processes into different queues based on priority or type, each with its scheduling algorithm.
      </p>
  
      <h2 class="sub-title">Multilevel Feedback Queue Scheduling</h2>
      <p class="content">
        Multilevel feedback queue scheduling allows processes to move between queues based on their behavior and needs, promoting responsiveness.
      </p>
  
      <h2 class="sub-title">Lottery Process Scheduling</h2>
      <p class="content">
        Lottery scheduling allocates CPU time using a random lottery system, giving each process a certain number of tickets based on priority.
      </p>
  
      <h2 class="sub-title">Multiple-Processor Scheduling</h2>
      <p class="content">
        In multiple-processor scheduling, processes are distributed among several processors, improving system throughput and performance.
      </p>
  
  
      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the concepts discussed:</p>
      <div class="diagram-container">
        <img src="path/to/diagram1.png" alt="Diagram illustrating CPU scheduling algorithms" />
        <img src="path/to/diagram2.png" alt="Diagram showing process states" />
        <img src="path/to/diagram3.png" alt="Comparison of scheduling algorithms" />
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
const topic = "CPU Scheduling";
const subtopic = "CPU Scheduling";

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