<template>
    <div class="memory-management-container">
      <h1 class="main-title">Memory Management</h1>
      <p class="intro">
        Memory management is a crucial function of an operating system that involves managing computer memory, allocating space for programs, and ensuring efficient memory usage.
      </p>
  
      <h2 class="sub-title">Memory Hierarchy Design and its Characteristics</h2>
      <p class="content">
        Memory hierarchy refers to the structure of different memory types in a computer, designed to provide fast access to data while maximizing storage efficiency. The main characteristics include speed, cost, size, and volatility.
      </p>
  
      <h2 class="sub-title">Introduction to Memory and Memory Units</h2>
      <p class="content">
        Memory is an essential component of a computer system, comprising various types of storage that hold data and instructions. Common units of memory include bytes, kilobytes (KB), megabytes (MB), gigabytes (GB), and terabytes (TB).
      </p>
  
      <h2 class="sub-title">Different Types of RAM (Random Access Memory)</h2>
      <ul class="characteristics-list">
        <li><strong>DRAM (Dynamic RAM):</strong> Needs to be refreshed thousands of times per second.</li>
        <li><strong>SRAM (Static RAM):</strong> Faster and more reliable but more expensive; used for cache memory.</li>
        <li><strong>SDRAM (Synchronous DRAM):</strong> Synchronized with the CPU clock for better performance.</li>
      </ul>
  
      <h2 class="sub-title">Buddy System: Memory Allocation Technique</h2>
      <p class="content">
        The buddy system divides memory into partitions to try and minimize fragmentation. It allocates memory in blocks that are powers of two, making it easier to manage.
      </p>
  
      <h2 class="sub-title">Memory Management | Partition Allocation Method</h2>
      <p class="content">
        Memory management strategies can be broadly classified into partition allocation methods, which include fixed and variable partitioning, allowing for efficient memory usage.
      </p>
  
      <h2 class="sub-title">Fixed (or Static) Partitioning in Operating System</h2>
      <p class="content">
        In fixed partitioning, memory is divided into fixed-size partitions. Each process is allocated a specific partition, which can lead to internal fragmentation.
      </p>
  
      <h2 class="sub-title">Variable (or Dynamic) Partitioning in Operating System</h2>
      <p class="content">
        Variable partitioning allows processes to be allocated only the amount of memory they need, reducing wastage but requiring more complex memory management.
      </p>
  
      <h2 class="sub-title">Non-Contiguous Allocation in Operating System</h2>
      <p class="content">
        Non-contiguous allocation allows processes to be stored in different areas of memory, which helps utilize memory more efficiently and reduces fragmentation.
      </p>
  
      <h2 class="sub-title">Logical vs Physical Address in Operating System</h2>
      <p class="content">
        A logical address is generated by the CPU, while a physical address is the actual location in memory. The operating system maps logical addresses to physical addresses.
      </p>
  
      <h2 class="sub-title">Paging</h2>
      <p class="content">
        Paging is a memory management scheme that eliminates the need for contiguous allocation of physical memory, thus avoiding external fragmentation.
      </p>
  
      <h2 class="sub-title">Requirements of Memory Management System</h2>
      <ul class="characteristics-list">
        <li>Efficient memory allocation and deallocation.</li>
        <li>Minimizing fragmentation.</li>
        <li>Ensuring protection and sharing of memory.</li>
        <li>Managing virtual memory.</li>
      </ul>
  
      <h2 class="sub-title">Memory Management – Mapping Virtual Address to Physical Addresses</h2>
      <p class="content">
        Memory management includes mapping virtual addresses generated by processes to physical addresses in RAM, allowing for efficient memory usage.
      </p>
  
      <h2 class="sub-title">Page Table Entries</h2>
      <p class="content">
        Page table entries (PTEs) are data structures used in paging to store the mapping between virtual addresses and physical addresses, including information about the frame number and status.
      </p>
  
      <h2 class="sub-title">Virtual Memory</h2>
      <p class="content">
        Virtual memory extends the available memory on a system by using disk space to simulate additional RAM, allowing larger processes to run than the physical memory would otherwise permit.
      </p>
  
      <h2 class="sub-title">Memory Interleaving</h2>
      <p class="content">
        Memory interleaving is a technique that improves access speed by distributing memory addresses across multiple memory modules, allowing simultaneous access to different modules.
      </p>
  
      <h2 class="sub-title">Virtual Memory Questions</h2>
      <p class="content">
        <strong>Q: What is the purpose of virtual memory?</strong> <br>
        A: To enable the execution of processes that may not fit into the physical memory available.
      </p>
  
      <h2 class="sub-title">Operating System Based Virtualization</h2>
      <p class="content">
        OS-level virtualization allows multiple instances of an OS to run on a single physical machine, providing isolation and resource management for applications.
      </p>
  
      <h2 class="sub-title">Inverted Page Table</h2>
      <p class="content">
        An inverted page table is a memory management structure that maintains a single table for all physical frames, improving efficiency for large address spaces.
      </p>
  
      <h2 class="sub-title">Swap Space</h2>
      <p class="content">
        Swap space is a portion of the hard disk used to extend the system's memory by temporarily holding inactive pages of memory.
      </p>
  
      <h2 class="sub-title">Page Fault Handling</h2>
      <p class="content">
        When a program accesses a page that is not in memory, a page fault occurs, requiring the OS to retrieve the page from disk, which involves various handling strategies to minimize performance impact.
      </p>
  
      <h2 class="sub-title">Segmentation</h2>
      <p class="content">
        Segmentation is a memory management technique that divides memory into segments based on logical divisions such as functions or objects.
      </p>
  
      <h2 class="sub-title">Memory Segmentation in 8086 Microprocessor</h2>
      <p class="content">
        The 8086 microprocessor uses segmentation to address memory, allowing programs to access more memory than the addressable range of the processor.
      </p>
  
      <h2 class="sub-title">Program for Next Fit Algorithm in Memory Management</h2>
      <pre><code>
  // Example of Next Fit Algorithm
  int nextFit(int blockSize[], int m, int processSize[], int n) {
      int allocation[n];
      for (int i = 0; i < n; i++) allocation[i] = -1;
  
      int j = 0;
      for (int i = 0; i < n; i++) {
          while (j < m) {
              if (blockSize[j] >= processSize[i]) {
                  allocation[i] = j;
                  blockSize[j] -= processSize[i];
                  j = (j + 1) % m;
                  break;
              }
              j = (j + 1) % m;
          }
      }
      return allocation;
  }
      </code></pre>
  
      <h2 class="sub-title">Overlays in Memory Management</h2>
      <p class="content">
        Overlays allow a program to execute that is larger than the available memory by loading only the necessary parts into memory when required.
      </p>
  
      <h2 class="sub-title">Page Replacement Algorithms</h2>
      <p class="content">
        Page replacement algorithms determine which memory pages to remove when new pages need to be loaded. Key algorithms include LRU, FIFO, and Optimal Page Replacement.
      </p>
  
      <h2 class="sub-title">Program for Page Replacement Algorithms | Set 1 (LRU)</h2>
      <pre><code>
  // Example of LRU Page Replacement Algorithm
  int pageFaults(int pages[], int n, int capacity) {
      int pageFaults = 0;
      int memory[capacity];
      int index[capacity];
      int count = 0;
  
      for (int i = 0; i < capacity; i++) {
          memory[i] = -1;
      }
  
      for (int i = 0; i < n; i++) {
          int j;
          for (j = 0; j < capacity; j++) {
              if (memory[j] == pages[i]) break;
          }
  
          if (j == capacity) {
              if (count < capacity) {
                  memory[count++] = pages[i];
              } else {
                  int lruIndex = -1, lruTime = -1;
                  for (j = 0; j < capacity; j++) {
                      if (index[j] < lruTime || lruTime == -1) {
                          lruTime = index[j];
                          lruIndex = j;
                      }
                  }
                  memory[lruIndex] = pages[i];
              }
              pageFaults++;
          }
          index[j] = i;
      }
      return pageFaults;
  }
      </code></pre>
  
      <h2 class="sub-title">Program for Optimal Page Replacement Algorithm</h2>
      <pre><code>
  // Example of Optimal Page Replacement Algorithm
  int optimalPageReplacement(int pages[], int n, int capacity) {
      int memory[capacity];
      bool isPresent[capacity];
      int pageFaults = 0;
  
      for (int i = 0; i < capacity; i++) {
          memory[i] = -1;
          isPresent[i] = false;
      }
  
      for (int i = 0; i < n; i++) {
          int j;
          for (j = 0; j < capacity; j++) {
              if (memory[j] == pages[i]) {
                  isPresent[j] = true;
                  break;
              }
          }
  
          if (j == capacity) {
              int farthest = -1, replaceIndex = -1;
              for (j = 0; j < capacity; j++) {
                  if (!isPresent[j]) {
                      replaceIndex = j;
                      break;
                  }
                  int index = findFarthestIndex(pages, n, memory[j], i);
                  if (index > farthest) {
                      farthest = index;
                      replaceIndex = j;
                  }
              }
              memory[replaceIndex] = pages[i];
              pageFaults++;
          }
      }
      return pageFaults;
  }
  
  int findFarthestIndex(int pages[], int n, int page, int currentIndex) {
      for (int i = currentIndex; i < n; i++) {
          if (pages[i] == page) {
              return i;
          }
      }
      return n;
  }
      </code></pre>
  
      <h2 class="sub-title">LFU (Least Frequently Used) Cache Implementation</h2>
      <p class="content">
        LFU cache replacement algorithm keeps track of how often a page is accessed and replaces the least frequently used pages.
      </p>
  
      <h2 class="sub-title">Second Chance (or Clock) Page Replacement Policy</h2>
      <p class="content">
        The Second Chance algorithm is an enhancement to FIFO that gives pages a second chance based on their reference bit before replacement.
      </p>
  
      <h2 class="sub-title">Techniques to Handle Thrashing</h2>
      <p class="content">
        Thrashing occurs when excessive paging reduces performance. Techniques to manage this include increasing the number of frames allocated to processes and optimizing memory access patterns.
      </p>
  
      <h2 class="sub-title">Allocating Kernel Memory (Buddy System and Slab System)</h2>
      <p class="content">
        The buddy system and slab system are strategies for managing kernel memory allocation, helping to minimize fragmentation and improve allocation speed.
      </p>
  
      <h2 class="sub-title">Program for Buddy Memory Allocation Scheme in Operating Systems | Set 1 (Allocation)</h2>
      <pre><code>
  // Example of Buddy Memory Allocation Scheme
  void* buddyAlloc(int size) {
      // Implementation of buddy allocation
  }
      </code></pre>
  
      <h2 class="sub-title">Program for Buddy Memory Allocation Scheme in Operating Systems | Set 2 (Deallocation)</h2>
      <pre><code>
  // Example of Buddy Memory Deallocation
  void buddyFree(void* ptr) {
      // Implementation of buddy deallocation
  }
      </code></pre>
  
      <h2 class="sub-title">Static and Dynamic Libraries | Set 1</h2>
      <p class="content">
        Static libraries are linked at compile time, while dynamic libraries are linked at runtime, allowing for more flexible memory usage.
      </p>
  
      <h2 class="sub-title">Working with Shared Libraries | Set 1</h2>
      <p class="content">
        Shared libraries allow multiple programs to use the same library in memory, reducing memory consumption and improving performance.
      </p>
  
      <h2 class="sub-title">Working with Shared Libraries | Set 2</h2>
      <p class="content">
        Examples of using shared libraries include loading libraries dynamically in C/C++ using dlopen() and dlsym().
      </p>
  
      <h2 class="sub-title">Named Pipe or FIFO with Example C Program</h2>
      <pre><code>
  // Example of Named Pipe in C
  #include &lt;stdio.h&gt;
  #include &lt;stdlib.h&gt;
  #include &lt;unistd.h&gt;
  
  int main() {
      // Create a named pipe (FIFO)
      mkfifo("myfifo", 0666);
      char str[80];
      // Write to FIFO
      write(fd, str, sizeof(str));
      // Read from FIFO
      read(fd, str, sizeof(str));
      printf("Received: %s\n", str);
      return 0;
  }
      </code></pre>
  
      <h2 class="sub-title">Tracing Memory Usage in Linux</h2>
      <p class="content">
        Tools like top, htop, and vmstat can be used to trace memory usage in Linux systems, providing insights into resource utilization.
      </p>
  
      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the concepts discussed:</p>
      <div class="diagram-container">
        <img src="path/to/memory_hierarchy.png" alt="Memory Hierarchy Diagram" />
        <img src="path/to/paging_diagram.png" alt="Paging Diagram" />
        <img src="path/to/segmentation_diagram.png" alt="Segmentation Diagram" />
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "MemoryManagement",
  };
  </script>
  
  <style scoped>
  .memory-management-container {
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