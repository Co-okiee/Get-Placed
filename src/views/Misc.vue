<template>
    <div class="miscellaneous-container">
      <h1 class="main-title">Miscellaneous</h1>
      <p class="intro">
        This section provides insights into various important aspects of UNIX and Linux systems, including commands, process management, and shell scripting.
      </p>
  
      <h2 class="sub-title">Introduction to UNIX System</h2>
      <p class="content">
        UNIX is a powerful multiuser operating system that supports multitasking. Originally developed in the 1960s and 70s, UNIX has influenced many operating systems, including Linux.
      </p>
      <p class="content">
        The key features of UNIX include its hierarchical file system, support for multiple users, and built-in networking capabilities. It uses a command-line interface for user interaction, which allows for efficient control of system operations.
      </p>
  
      <h2 class="sub-title">Important Linux Commands</h2>
      <ul class="characteristics-list">
        <li><strong>leave:</strong> Exit from the current shell or script.</li>
        <li><strong>diff:</strong> Compare files line by line and show the differences.</li>
        <li><strong>cal:</strong> Display a calendar for a given month or year.</li>
        <li><strong>ncal:</strong> Display a calendar in a different format.</li>
        <li><strong>locate:</strong> Find files in the system by name.</li>
        <li><strong>ln:</strong> Create links between files (hard and soft links).</li>
      </ul>
  
      <h2 class="sub-title">Process States and Transitions in a UNIX Process</h2>
      <p class="content">
        A UNIX process can be in one of several states: 
      </p>
      <ul>
        <li><strong>Running:</strong> The process is currently executing.</li>
        <li><strong>Waiting:</strong> The process is waiting for some event to occur (like I/O completion).</li>
        <li><strong>Stopped:</strong> The process has been stopped, usually by a signal.</li>
        <li><strong>Zombie:</strong> The process has completed execution but still has an entry in the process table.</li>
      </ul>
      <img src="path/to/process_states_diagram.png" alt="Process States and Transitions" class="process-diagram"/>
  
      <h2 class="sub-title">Introduction to Linux Shell and Shell Scripting</h2>
      <p class="content">
        The Linux shell is a command-line interface that allows users to interact with the operating system. It interprets commands entered by the user and communicates with the kernel.
      </p>
      <p class="content">
        Shell scripting is writing a series of commands for the shell to execute. Here’s a simple example:
      </p>
      <pre>
        <code>
  #!/bin/bash
  echo "Hello, World!"
        </code>
      </pre>
  
      <h2 class="sub-title">‘crontab’ in Linux with Examples</h2>
      <p class="content">
        The <code>crontab</code> command in Linux is used to schedule tasks to run automatically at specified intervals. The basic syntax is:
      </p>
      <pre>
        <code>
  * * * * * command_to_run
        </code>
      </pre>
      <p class="content">
        For example, to run a script every day at 2 AM:
      </p>
      <pre>
        <code>
  0 2 * * * /path/to/script.sh
        </code>
      </pre>
  
      <h2 class="sub-title">In-depth and Maxdepth in Linux find() Command</h2>
      <p class="content">
        The <code>find</code> command is used to search for files and directories in a directory hierarchy. You can limit the search depth using <code>-depth</code> and <code>-maxdepth</code> options.
      </p>
      <p class="content">
        Example to find all files in the current directory up to 2 levels deep:
      </p>
      <pre>
        <code>
  find . -maxdepth 2 -type f
        </code>
      </pre>
      <p class="content">
        Example using <code>-depth</code> to process each directory's contents before the directory itself:
      </p>
      <pre>
        <code>
  find . -depth -name "*.txt"
        </code>
      </pre>
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=unix_intro" target="_blank">Introduction to UNIX (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=linux_shell" target="_blank">Linux Shell Basics (English)</a></li>
      </ul>
  
      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the concepts discussed:</p>
      <div class="diagram-container">
        <img src="path/to/diagram1.png" alt="Diagram illustrating UNIX process states" />
        <img src="path/to/diagram2.png" alt="Diagram showing Linux shell scripting" />
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "Miscellaneous",
  };
  </script>
  
  <style scoped>
  .miscellaneous-container {
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
  
  .process-diagram {
    width: 100%;
    height: auto;
    margin: 30px 0;
    border: 1px solid #444;
    border-radius: 5px;
  }
  </style>