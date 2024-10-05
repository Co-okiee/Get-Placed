<template>
    <div class="system-structure-container">
      <h1 class="main-title">System Structure</h1>
      <p class="intro">
        System structure in operating systems refers to the organization of various components that facilitate effective communication and resource management. Understanding system structure helps in grasping how operating systems function.
      </p>
  
      <h2 class="sub-title">Microkernel</h2>
      <p class="content">
        A microkernel is a minimalistic kernel that only includes essential functionalities like communication between processes and basic memory management. Other services, like device drivers and file systems, run in user space.
      </p>
      <img src="path/to/microkernel-diagram.png" alt="Microkernel Architecture" class="system-diagram" />
  
      <h2 class="sub-title">Kernel I/O Subsystem (I/O System)</h2>
      <p class="content">
        The I/O subsystem manages input and output devices and their communication with the operating system. It abstracts the complexity of device handling through drivers and provides a uniform interface for application developers.
      </p>
      <img src="path/to/io-subsystem-diagram.png" alt="Kernel I/O Subsystem" class="system-diagram" />
  
      <h2 class="sub-title">Monolithic Kernel and Key Differences from Microkernel</h2>
      <p class="content">
        A monolithic kernel includes all operating system services within one large block of code that runs in a single address space. This approach can offer better performance but may become complex and harder to maintain.
      </p>
      <ul class="characteristics-list">
        <li><strong>Microkernel:</strong> Minimal services, runs most services in user space, better fault isolation.</li>
        <li><strong>Monolithic Kernel:</strong> All services in kernel space, potentially faster, but less modular.</li>
      </ul>
      <img src="path/to/monolithic-vs-microkernel-diagram.png" alt="Monolithic vs Microkernel" class="system-diagram" />
  
      <h2 class="sub-title">Introduction of System Call</h2>
      <p class="content">
        A system call is a mechanism used by an application to request services from the operating system. It acts as an interface between user programs and the OS, allowing user-level applications to perform operations like file manipulation and process control.
      </p>
      <img src="path/to/system-call-diagram.png" alt="System Call Diagram" class="system-diagram" />
  
      <h2 class="sub-title">Get/Set Process Resource Limits in C</h2>
      <p class="content">
        The resource limits of a process can be controlled using the <code>getrlimit</code> and <code>setrlimit</code> functions in C. These functions allow you to retrieve and modify resource limits like CPU time, file size, and more.
      </p>
      <pre>
<code>
#include &lt;sys/resource.h&gt;

struct rlimit limit;
// Get the current limit
getrlimit(RLIMIT_CPU, &amp;limit);
// Set a new limit
limit.rlim_cur = 10; // Set limit to 10 seconds
setrlimit(RLIMIT_CPU, &amp;limit);
</code>
</pre>

      <h2 class="sub-title">Dual Mode Operations in OS</h2>
      <p class="content">
        Dual mode operation allows the operating system to operate in two modes: user mode and kernel mode. In user mode, processes have restricted access to system resources, while in kernel mode, the operating system can execute any instruction and access any resource.
      </p>
      <img src="path/to/dual-mode-diagram.png" alt="Dual Mode Operations" class="system-diagram" />
  
      <h2 class="sub-title">Privileged and Non-Privileged Instructions</h2>
      <p class="content">
        Privileged instructions can only be executed in kernel mode and include tasks like changing memory management settings. Non-privileged instructions can be executed in user mode and include basic arithmetic and control instructions.
      </p>
      <ul class="characteristics-list">
        <li><strong>Privileged Instructions:</strong> Execute in kernel mode, control critical system functions.</li>
        <li><strong>Non-Privileged Instructions:</strong> Execute in user mode, limited to user-level operations.</li>
      </ul>
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=example1" target="_blank">System Structure Overview (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=example2" target="_blank">System Structure in Hindi</a></li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "SystemStructure",
  };
  </script>
  
  <style scoped>
  .system-structure-container {
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
  
  .system-diagram {
    width: 100%;
    height: auto;
    margin: 20px 0;
    border: 1px solid #444;
    border-radius: 5px;
  }
  
  pre {
    background-color: #1f1f1f;
    padding: 10px;
    border-radius: 5px;
    overflow-x: auto;
    color: #00ff00;
    font-size: 1.2em;
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