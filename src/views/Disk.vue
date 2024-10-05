<template>
    <div class="disk-management-container">
      <h1 class="main-title">Disk Management</h1>
      <p class="intro">
        Disk management is the process of managing disk drives in a computer system, which includes managing file systems, directory structures, and allocating space on storage devices.
      </p>

      <h2 class="sub-title">File Systems</h2>
      <p class="content">
        A file system is a method used by the operating system to manage files on a disk. It provides a way to store, organize, and retrieve files.
      </p>
      <img src="@/assets/file-system-diagram.png" alt="File System Structure Diagram" class="diagram"/>

      <h2 class="sub-title">Unix File System</h2>
      <p class="content">
        The Unix File System (UFS) organizes files in a hierarchical structure, where everything is treated as a file, including devices and processes. UFS uses inodes to manage files and directories.
      </p>
      <img src="@/assets/unix-file-system-diagram.png" alt="Unix File System Structure" class="diagram"/>

      <h2 class="sub-title">Implementing Directory Management using Shell Script</h2>
      <p class="content">
        Directory management can be automated using shell scripts. For example, a script can be written to create, delete, and list directories.
      </p>
      <pre>
        <code>
          #!/bin/bash
          echo "1. Create Directory"
          echo "2. Delete Directory"
          echo "3. List Directories"
          read -p "Choose an option: " option
          case $option in
              1) read -p "Enter directory name: " dirname
                 mkdir "$dirname"
                 ;;
              2) read -p "Enter directory name: " dirname
                 rmdir "$dirname"
                 ;;
              3) ls -d */
                 ;;
              *) echo "Invalid option!"
                 ;;
          esac
        </code>
      </pre>

      <h2 class="sub-title">File Directory | Path Name</h2>
      <p class="content">
        A file directory contains files and subdirectories, and the path name specifies the location of a file within the directory hierarchy. Absolute and relative paths are two types of path names.
      </p>

      <h2 class="sub-title">Structures of Directory</h2>
      <p class="content">
        Directory structures can be classified as single-level, two-level, and hierarchical. Each structure has its advantages and disadvantages in terms of organization and access speed.
      </p>

      <h2 class="sub-title">File Allocation Methods</h2>
      <ul class="characteristics-list">
        <li><strong>Contiguous Allocation:</strong> Files are stored in consecutive blocks.</li>
        <li><strong>Linked Allocation:</strong> Each file consists of a linked list of blocks.</li>
        <li><strong>Indexed Allocation:</strong> An index block contains pointers to the file blocks.</li>
      </ul>

      <h2 class="sub-title">File Access Methods</h2>
      <ul class="characteristics-list">
        <li><strong>Sequential Access:</strong> Files are read in order.</li>
        <li><strong>Random Access:</strong> Any block can be accessed directly.</li>
      </ul>

      <h2 class="sub-title">Secondary Memory</h2>
      <p class="content">
        Secondary memory refers to non-volatile storage devices, such as hard drives, that retain data even when the computer is powered off. It is used for long-term storage of data and applications.
      </p>

      <h2 class="sub-title">Secondary Memory – Hard Disk Drive</h2>
      <p class="content">
        A Hard Disk Drive (HDD) is a common type of secondary memory that uses magnetic storage to read and write data. It consists of spinning disks and read/write heads.
      </p>
      <img src="@/assets/hard-disk-drive.png" alt="Hard Disk Drive Diagram" class="diagram"/>

      <h2 class="sub-title">Disk Scheduling Algorithms</h2>
      <p class="content">
        Disk scheduling algorithms determine the order in which disk I/O requests are processed. Common algorithms include FCFS, SSTF, SCAN, and C-SCAN.
      </p>

      <h2 class="sub-title">Program for SSTF Disk Scheduling Algorithm</h2>
      <p class="content">Below is a simple implementation of the Shortest Seek Time First (SSTF) disk scheduling algorithm:</p>
      <pre>
        <code>
          def SSTF(requests, head):
              seek_sequence = []
              while requests:
                  closest = min(requests, key=lambda x: abs(x - head))
                  seek_sequence.append(closest)
                  head = closest
                  requests.remove(closest)
              return seek_sequence

          requests = [98, 183, 37, 122, 14, 124, 65, 67]
          head = 53
          print("Seek Sequence:", SSTF(requests, head))
        </code>
      </pre>

      <h2 class="sub-title">What Exactly Spooling is All About?</h2>
      <p class="content">
        Spooling (Simultaneous Peripheral Operations Online) is a process where data is temporarily held in a buffer while being transferred between devices, allowing the CPU to perform other tasks concurrently.
      </p>

      <h2 class="sub-title">Difference between Spooling and Buffering</h2>
      <p class="content">
        <strong>Spooling:</strong> Involves managing data input/output operations for devices, allowing tasks to be performed in parallel. <br>
        <strong>Buffering:</strong> Temporarily holds data in memory to smooth out differences in data processing rates between two devices.
      </p>

      <h2 class="sub-title">Free Space Management</h2>
      <p class="content">
        Free space management keeps track of available disk space, ensuring that new files can be allocated efficiently. It uses bitmap or linked list methods to manage free blocks.
      </p>

      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=disk-management" target="_blank">Disk Management Overview (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=dm-in-hindi" target="_blank">Disk Management in Hindi</a></li>
      </ul>
    </div>
</template>

<script>
export default {
  name: "DiskManagement",
};
</script>

<style scoped>
.disk-management-container {
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

.diagram {
  width: 100%;
  height: auto;
  margin: 30px 0;
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