<template>
    <div class="os-container">
      <h1 class="main-title">Operating Systems</h1>
      <p class="intro">
        An operating system (OS) is software that manages computer hardware and software resources and provides common services for computer programs. It acts as an intermediary between users and the computer hardware.
      </p>
  
      <h2 class="sub-title">Introduction of Operating System</h2>
      <p class="content">
        The operating system is the most fundamental program that runs on a computer, managing both hardware and software resources.
      </p>
  
      <h2 class="sub-title">Types of Operating Systems</h2>
      <ul class="characteristics-list">
        <li><strong>Batch Operating Systems:</strong> Execute jobs in batches without user interaction.</li>
        <li><strong>Time-Sharing Operating Systems:</strong> Allow multiple users to interact with the computer at the same time.</li>
        <li><strong>Distributed Operating Systems:</strong> Manage a group of distinct computers and make them appear as a single coherent system.</li>
        <li><strong>Real-Time Operating Systems:</strong> Respond to inputs immediately to ensure timely processing.</li>
      </ul>
  
      <h2 class="sub-title">Functions of Operating System</h2>
      <p class="content">
        The primary functions include process management, memory management, file system management, and device management.
      </p>
  
      <h2 class="sub-title">Real-Time Systems</h2>
      <p class="content">
        Real-time systems are designed to process data as it comes in, typically without any buffering delay. They are crucial in environments where time is a critical factor.
      </p>
      
      <h2 class="sub-title">Tasks in Real-Time Systems</h2>
      <p class="content">
        Tasks in real-time systems must be completed within specified time constraints, ensuring reliable performance in applications like embedded systems, robotics, and process control.
      </p>
      
      <h2 class="sub-title">Difference between Multitasking, Multithreading, and Multiprocessing</h2>
      <ul class="characteristics-list">
        <li><strong>Multitasking:</strong> Multiple tasks are executed by the CPU concurrently.</li>
        <li><strong>Multithreading:</strong> Multiple threads within a single process are executed concurrently.</li>
        <li><strong>Multiprocessing:</strong> Multiple processes run simultaneously on different processors.</li>
      </ul>
  
      <h2 class="sub-title">Types of Computer Memory (RAM and ROM)</h2>
      <p class="content">
        <strong>RAM (Random Access Memory):</strong> Volatile memory used to store data temporarily for quick access. <br>
        <strong>ROM (Read-Only Memory):</strong> Non-volatile memory that contains essential system instructions.
      </p>
  
      <h2 class="sub-title">Difference between 32-bit and 64-bit Operating Systems</h2>
      <p class="content">
        A 64-bit OS can handle more memory (RAM) than a 32-bit OS, allowing for better performance in applications that require large amounts of data.
      </p>
  
      <h2 class="sub-title">What Happens When We Turn on the Computer?</h2>
      <p class="content">
        When the computer is powered on, it goes through a series of steps known as the boot process, including the POST (Power-On Self Test) and loading the OS from the bootable device.
      </p>
      
      <h2 class="sub-title">Boot Block</h2>
      <p class="content">
        The boot block is the first sector of the storage device that the operating system reads when booting the system, containing the boot loader that initializes the system.
      </p>
  
      <h2 class="sub-title">UEFI (Unified Extensible Firmware Interface)</h2>
      <p class="content">
        UEFI is a modern replacement for BIOS, providing a more flexible interface between the operating system and firmware, along with enhanced security features.
      </p>
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=os1" target="_blank">Introduction to Operating Systems (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=os2" target="_blank">Operating Systems in Hindi</a></li>
      </ul>
  
      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the concepts discussed:</p>
      <div class="diagram-container">
        <img src="path/to/diagram1.png" alt="Diagram illustrating the OS boot process" />
        <img src="path/to/diagram2.png" alt="Diagram showing memory types" />
        <img src="path/to/diagram3.png" alt="Comparison of 32-bit and 64-bit architecture" />
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "OperatingSystems",
  };
  </script>
  
  <style scoped>
  .os-container {
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
  