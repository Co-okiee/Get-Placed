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
        <img src="path/to/diagram1.png" alt="Diagram illustrating Threads vs Processes" />
        <img src="path/to/diagram2.png" alt="Memory Management Diagram" />
        <img src="path/to/diagram3.png" alt="Paging and Segmentation Comparison" />
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "ProcessesAndThreads",
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
  
  .sub-sub-title {
    font-size: 1.8em;
    color: #e0ce46;
    margin-top: 30px;
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