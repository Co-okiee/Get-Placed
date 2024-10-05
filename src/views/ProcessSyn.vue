<template>
    <div class="ps-container">
      <h1 class="main-title">Process Synchronization</h1>
      <p class="intro">
        Process synchronization is a mechanism that ensures that multiple processes can operate concurrently without conflict. It is essential for ensuring data consistency and preventing race conditions in a multi-threaded environment.
      </p>
  
      <h2 class="sub-title">Introduction to Process Synchronization</h2>
      <p class="content">
        In operating systems, processes may need to share resources. Synchronization is required to prevent conflicts when multiple processes access shared resources simultaneously.
      </p>
  
      <h2 class="sub-title">Critical Section</h2>
      <p class="content">
        The critical section is a segment of code that accesses shared resources. Only one process should be allowed to execute in its critical section at a time to prevent data inconsistency.
      </p>
      <img src="path/to/critical-section-diagram.png" alt="Critical Section Diagram" />
  
      <h2 class="sub-title">Inter Process Communication (IPC)</h2>
      <p class="content">
        IPC is a set of methods used for communication between processes. It allows processes to exchange data and signals.
      </p>
  
      <h2 class="sub-title">Interprocess Communication: Methods</h2>
      <ul class="characteristics-list">
        <li><strong>Shared Memory:</strong> Processes communicate by accessing a common memory space.</li>
        <li><strong>Message Queues:</strong> Processes send and receive messages via a queue.</li>
      </ul>
  
      <h2 class="sub-title">IPC through Shared Memory</h2>
      <p class="content">
        Shared memory is one of the fastest IPC methods. Processes share a segment of memory and communicate through it.
      </p>
  
      <h2 class="sub-title">IPC using Message Queues</h2>
      <p class="content">
        Message queues allow processes to communicate asynchronously. Messages are placed in a queue and can be retrieved by processes.
      </p>
  
      <h2 class="sub-title">Message-based Communication in IPC</h2>
      <p class="content">
        This method involves sending messages between processes. It provides a way to communicate without sharing memory directly.
      </p>
  
      <h2 class="sub-title">Communication Between Two Processes Using Signals in C</h2>
      <p class="content">
        Signals are a limited form of IPC that allows processes to send notifications. For example, a process can notify another process to terminate using a signal.
      </p>
      <pre>
        <code>
          #include &lt;signal.h&gt;
          // Signal handler function
          void handleSignal(int signal) {
              // Handle the signal
          }
        </code>
      </pre>
  
      <h2 class="sub-title">Semaphores in Operating System</h2>
      <p class="content">
        A semaphore is a synchronization primitive used to control access to shared resources. It uses two operations: wait (P) and signal (V).
      </p>
  
      <h2 class="sub-title">Mutex vs. Semaphore</h2>
      <p class="content">
        A mutex allows only one thread to access a resource at a time, while a semaphore can allow multiple threads to access a set number of resources.
      </p>
  
      <h2 class="sub-title">Process Synchronization: Monitors</h2>
      <p class="content">
        Monitors are high-level synchronization constructs that allow safe access to shared resources by encapsulating them with lock mechanisms.
      </p>
  
      <h2 class="sub-title">Peterson’s Algorithm for Mutual Exclusion</h2>
      <h3 class="type-title">Set 1 (Basic C Implementation)</h3>
      <pre>
        <code>
          // Basic implementation of Peterson's Algorithm
          void peterson(int process) {
              int other = 1 - process;
              flag[process] = true; 
              turn = process; 
              while (flag[other] && turn == process);
          }
        </code>
      </pre>
  
      <h3 class="type-title">Set 2 (CPU Cycles and Memory Fence)</h3>
      <p class="content">
        This set emphasizes the importance of memory fences to prevent CPU optimizations from affecting the execution order.
      </p>
  
      <h3 class="type-title">Peterson’s Algorithm (Using Processes and Shared Memory)</h3>
      <p class="content">
        Here, we demonstrate the algorithm using processes that communicate through shared memory.
      </p>
  
      <h2 class="sub-title">Dekker’s Algorithm</h2>
      <p class="content">
        Dekker's algorithm is another solution for mutual exclusion that ensures that only one of the processes can enter the critical section at a time.
      </p>
  
      <h2 class="sub-title">Bakery Algorithm</h2>
      <p class="content">
        The Bakery algorithm ensures that processes enter their critical sections in a first-come-first-serve basis by assigning a number to each process.
      </p>
  
      <h2 class="sub-title">Producer-Consumer Problem Using Semaphores</h2>
      <h3 class="type-title">Set 1</h3>
      <p class="content">
        The producer-consumer problem is a classic synchronization problem that illustrates how to synchronize producer and consumer processes using semaphores.
      </p>
  
      <h2 class="sub-title">Dining Philosopher Problem Using Semaphores</h2>
      <p class="content">
        This problem illustrates the challenges of resource sharing among multiple processes and how to resolve deadlocks.
      </p>
  
      <h2 class="sub-title">Dining-Philosophers Solution Using Monitors</h2>
      <p class="content">
        Using monitors, this solution addresses the dining philosophers problem while avoiding deadlocks.
      </p>
  
      <h2 class="sub-title">Readers-Writers Problem</h2>
      <h3 class="type-title">Set 1 (Introduction and Readers Preference Solution)</h3>
      <p class="content">
        The readers-writers problem addresses synchronization between processes that read and write shared data. In the reader's preference solution, readers get priority.
      </p>
  
      <h3 class="type-title">Reader-Writers Solution Using Monitors</h3>
      <p class="content">
        Monitors can be used to solve the readers-writers problem effectively, ensuring both reader and writer integrity.
      </p>
  
      <h2 class="sub-title">Sleeping Barber Problem</h2>
      <p class="content">
        This problem illustrates the synchronization of multiple processes in a barbershop scenario, ensuring efficient service without wastage.
      </p>
  
      <h2 class="sub-title">Lock Variable Synchronization Mechanism</h2>
      <p class="content">
        Lock variables are used to control access to shared resources in order to ensure mutual exclusion.
      </p>
  
      <h2 class="sub-title">Mutex Lock for Linux Thread Synchronization</h2>
      <p class="content">
        Mutex locks are used in Linux for thread synchronization, ensuring that only one thread can access a critical section at a time.
      </p>
  
      <h2 class="sub-title">Priority Inversion: What the Heck!</h2>
      <p class="content">
        Priority inversion occurs when a lower-priority task holds a resource needed by a higher-priority task, causing unexpected delays.
      </p>
  
      <h2 class="sub-title">What’s the Difference Between Priority Inversion and Priority Inheritance?</h2>
      <p class="content">
        Priority inheritance is a technique to prevent priority inversion by temporarily raising the priority of the lower-priority task holding a needed resource.
      </p>
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=ps1" target="_blank">Introduction to Process Synchronization (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=ps2" target="_blank">Process Synchronization in Hindi</a></li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "ProcessSynchronization",
  };
  </script>
  
  <style scoped>
  .ps-container {
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
  
  .content {
    font-size: 1.2em;
    margin-bottom: 20px;
  }
  
  .characteristics-list {
    margin: 10px 0;
    padding-left: 20px;
    font-size: 1.2em;
  }
  
  li {
    margin-bottom: 15px;
    line-height: 1.6;
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