<template>
    <div class="deadlock-container">
      <h1 class="main-title">Deadlock</h1>
      <p class="intro">
        Deadlock is a condition in computer systems where two or more processes cannot proceed because each is waiting for the other to release a resource. This situation leads to a standstill in resource allocation and system performance.
      </p>
  
      <h2 class="sub-title">Deadlock Introduction</h2>
      <p class="content">
        A deadlock occurs when processes are unable to continue execution because they are each waiting for resources held by the other. This is often described with the resource allocation model.
      </p>
      
      <h2 class="sub-title">Deadlock Detection and Recovery</h2>
      <p class="content">
        Detection algorithms can identify deadlocks by examining resource allocation states. Recovery methods involve terminating or rolling back processes to break the deadlock.
      </p>
  
      <h2 class="sub-title">Deadlock, Starvation, and Livelock</h2>
      <p class="content">
        - *Deadlock*: A state where processes are blocked because each is holding a resource the other needs.
        - *Starvation*: A scenario where a process is perpetually denied necessary resources.
        - *Livelock*: Similar to deadlock, but processes continuously change state without making progress.
      </p>
  
      <h2 class="sub-title">Deadlock Prevention and Avoidance</h2>
      <p class="content">
        Deadlock prevention techniques ensure that at least one of the necessary conditions for deadlock cannot hold, while avoidance strategies dynamically allocate resources based on safe states.
      </p>
  
      <h2 class="sub-title">Banker’s Algorithm</h2>
      <p class="content">
        The Banker’s Algorithm is used for resource allocation in systems with multiple processes. It checks the safety of resource allocation before proceeding.
      </p>
  
      <h2 class="sub-title">Resource Allocation Graph (RAG)</h2>
      <p class="content">
        A Resource Allocation Graph is a directed graph that represents the allocation of resources to processes, helping to visualize potential deadlocks.
      </p>
      
      <h2 class="sub-title">Methods of Resource Allocation to Processes by Operating System</h2>
      <p class="content">
        Operating systems manage resources through various methods, including priority scheduling, round-robin, and the aforementioned Banker’s Algorithm.
      </p>
      
      <h2 class="sub-title">Program for Banker’s Algorithm</h2>
      <pre>
  <code>
  // Sample code for Banker’s Algorithm
  class BankersAlgorithm {
      ...
  }
  </code>
      </pre>
  
      <h2 class="sub-title">Banker’s Algorithm: Print All the Safe States (or Safe Sequences)</h2>
      <p class="content">
        This section outlines how to determine all the safe sequences that can occur in a system.
      </p>
      <pre>
  <code>
  // Sample code for printing safe sequences
  class BankersAlgorithm {
      ...
  }
  </code>
      </pre>
  
      <h2 class="sub-title">Deadlock Detection Algorithm</h2>
      <p class="content">
        Algorithms like Wait-For Graph and Resource Allocation Graph are used to detect deadlocks in the system.
      </p>
      
      <h2 class="sub-title">Program for Deadlock-Free Condition in Operating System</h2>
      <pre>
  <code>
  // Sample code to ensure deadlock-free conditions
  class DeadlockFree {
      ...
  }
  </code>
      </pre>
  
      <h2 class="sub-title">Deadlock Detection in Distributed Systems</h2>
      <p class="content">
        Deadlocks in distributed systems are complex due to the lack of centralized control, requiring specific detection algorithms like Chandy-Misra's algorithm.
      </p>
  
      <h2 class="sub-title">Techniques Used in Centralized Approach of Deadlock Detection in Distributed Systems</h2>
      <p class="content">
        Techniques such as centralized resource allocation graphs and wait-for graphs are employed to manage and detect deadlocks in distributed systems.
      </p>
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=example1" target="_blank">Deadlock Overview (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=example2" target="_blank">Deadlock in Hindi</a></li>
      </ul>
  
      <h2 class="sub-title">Diagrams</h2>
      <p>Below are diagrams illustrating the concepts discussed:</p>
      <div class="diagram-container">
        <img src="path/to/deadlock.png" alt="Diagram illustrating a deadlock situation" />
        <img src="path/to/bankers_algorithm.png" alt="Diagram showing the Banker’s Algorithm flow" />
        <img src="path/to/rag.png" alt="Resource Allocation Graph example" />
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "Deadlock",
  };
  </script>
  
  <style scoped>
  .deadlock-container {
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