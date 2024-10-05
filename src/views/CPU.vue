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
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=os1" target="_blank">Introduction to CPU Scheduling (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=os2" target="_blank">CPU Scheduling in Hindi</a></li>
      </ul>
  
      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the concepts discussed:</p>
      <div class="diagram-container">
        <img src="path/to/diagram1.png" alt="Diagram illustrating CPU scheduling algorithms" />
        <img src="path/to/diagram2.png" alt="Diagram showing process states" />
        <img src="path/to/diagram3.png" alt="Comparison of scheduling algorithms" />
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "CPUScheduling",
  };
  </script>
  
  <style scoped>
  .cpu-scheduling-container {
    max-width: 900px;
    margin: 20px auto;
    padding: 20px;
    border-radius: 10px;
    background-color: #121212;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.6);
    font-family: 'Roboto', sans-serif;
    color: #e0e0e0;
    line-height: 1.6;
  }
  
  .main-title {
    font-size: 2.8em;
    color: #ffcc00;
    text-align: center;
    margin-bottom: 30px;
  }
  
  .sub-title {
    font-size: 2.2em;
    color: #e0ce46;
    margin-top: 40px;
    padding-bottom: 10px;
  }
  
  .type-title {
    font-size: 1.8em;
    color: #e0ce46;
    margin-top: 30px;
  }
  
  .content {
    font-size: 1.2em;
    margin-bottom: 20px;
  }
  
  .diagram-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    margin: 20px 0;
  }
  
  .diagram-container img {
    max-width: 100%;
    height: auto;
    margin-bottom: 10px;
    border: 2px solid #e0ce46; /* border color for diagrams */
  }
  
  a {
    color: #ddc452;
    text-decoration: none;
    font-size: 1.1em;
  }
  
  a:hover {
    text-decoration: underline;
  }
  
  .link-title {
    color: #ffffff;
    margin-top: 30px;
  }
  </style>