<template>
    <div class="transport-container">
      <h1 class="main-title">Transport Layer</h1>
      <p class="intro">
        The Transport Layer is a crucial component of the networking stack, responsible for providing communication services directly to the application processes running on different hosts.
      </p>
  
      <h2 class="sub-title">Transport Layer Responsibilities</h2>
      <p class="content">
        The main responsibilities of the Transport Layer include:
        <ul>
          <li>Segmentation and reassembly of data</li>
          <li>End-to-end communication</li>
          <li>Flow control</li>
          <li>Error detection and correction</li>
          <li>Multiplexing and demultiplexing of data streams</li>
        </ul>
      </p>
  
      <h2 class="sub-title">Multiplexing and Demultiplexing in Transport Layer</h2>
      <p class="content">
        Multiplexing allows multiple applications to share a single network connection by assigning different ports, while demultiplexing ensures that the data is sent to the correct application at the destination.
      </p>
  
      <h2 class="sub-title">User Datagram Protocol (UDP)</h2>
      <p class="content">
        UDP is a connectionless protocol that provides a simple method for sending data with minimal overhead. It is suitable for applications that require fast transmission, such as video streaming or online gaming, but do not need guaranteed delivery.
      </p>
  
      <h2 class="sub-title">TCP Connection Establishment</h2>
      <p class="content">
        TCP establishes a connection using the 3-Way Handshake process, ensuring both sender and receiver are ready for data transmission.
      </p>
  
      <h2 class="sub-title">TCP 3-Way Handshake Process</h2>
      <p class="content">
        The 3-Way Handshake consists of three steps:
        <ol>
          <li><strong>SYN:</strong> The client sends a SYN (synchronize) packet to the server to request a connection.</li>
          <li><strong>SYN-ACK:</strong> The server responds with a SYN-ACK (synchronize-acknowledgment) packet to acknowledge the request.</li>
          <li><strong>ACK:</strong> The client sends an ACK packet back to the server, establishing the connection.</li>
        </ol>
        <img src="path/to/tcp_handshake_diagram.png" alt="TCP 3-Way Handshake Diagram" />
      </p>
  
      <h2 class="sub-title">TCP Timers</h2>
      <p class="content">
        TCP uses several timers to manage connections, including:
        <ul>
          <li><strong>Retransmission Timer:</strong> Used to determine when to retransmit unacknowledged segments.</li>
          <li><strong>Keep-Alive Timer:</strong> Used to check if the connection is still active.</li>
          <li><strong>Persistence Timer:</strong> Used to manage data transmission when the sender is blocked.</li>
        </ul>
      </p>
  
      <h2 class="sub-title">TCP Connection Termination</h2>
      <p class="content">
        TCP connections are terminated through a four-step process, involving the exchange of FIN (finish) and ACK packets between the sender and receiver.
      </p>
  
      <h2 class="sub-title">TCP Sequence Number | Wrap Around Concept</h2>
      <p class="content">
        TCP uses sequence numbers to keep track of the order of data segments. The wrap-around concept allows sequence numbers to reset after reaching the maximum limit, ensuring that older segments are identified correctly.
      </p>
  
      <h2 class="sub-title">P2P (Peer To Peer) File Sharing</h2>
      <p class="content">
        P2P file sharing allows users to share files directly with one another without the need for a centralized server, utilizing both TCP and UDP for data transmission.
      </p>
  
      <h2 class="sub-title">Congestion Control</h2>
      <p class="content">
        Congestion control techniques are vital for maintaining efficient data flow and preventing network overload. TCP employs several methods for congestion control, including:
        <ul>
          <li><strong>AIMD:</strong> Additive Increase Multiplicative Decrease</li>
          <li><strong>Slow Start:</strong> Gradually increases transmission rate until congestion is detected.</li>
        </ul>
      </p>
  
      <h2 class="sub-title">TCP Congestion Control</h2>
      <p class="content">
        TCP employs various congestion control techniques to adaptively adjust the rate of data transmission based on network conditions, ensuring smooth and efficient communication.
      </p>
  
      <h2 class="sub-title">Congestion Control Techniques</h2>
      <p class="content">
        Common congestion control techniques include:
        <ul>
          <li><strong>Leaky Bucket Algorithm:</strong> Controls the amount of data transmitted over a network by regulating the flow.</li>
          <li><strong>Token Bucket Algorithm:</strong> Allows bursts of traffic while maintaining an average rate.</li>
        </ul>
      </p>
  
      <h2 class="sub-title">Error Control in TCP</h2>
      <p class="content">
        TCP provides error control through techniques such as checksums, acknowledgments, and retransmission of lost segments to ensure data integrity.
      </p>
  
      <h2 class="sub-title">TCP Flags</h2>
      <p class="content">
        TCP flags are control bits in the TCP header that indicate specific control information, such as:
        <ul>
          <li>SYN - Synchronize</li>
          <li>ACK - Acknowledgment</li>
          <li>FIN - Finish</li>
          <li>RST - Reset</li>
        </ul>
      </p>
  
      <h2 class="sub-title">TCP | Services and Segment Structure</h2>
      <p class="content">
        TCP provides reliable, ordered, and error-checked delivery of data. The TCP segment structure includes:
        <ul>
          <li>Source Port</li>
          <li>Destination Port</li>
          <li>Sequence Number</li>
          <li>Acknowledgment Number</li>
          <li>Flags</li>
          <li>Window Size</li>
          <li>Checksum</li>
          <li>Urgent Pointer</li>
          <li>Data</li>
        </ul>
        <img src="path/to/tcp_segment_structure.png" alt="TCP Segment Structure Diagram" />
      </p>
  
      <h2 class="sub-title">TCP Server-Client Implementation in C</h2>
      <p class="content">
        Below is a simple example of a TCP server and client implementation in C:
        <pre>
          // TCP Server Example
          #include &lt;stdio.h&gt;
          #include &lt;stdlib.h&gt;
          #include &lt;string.h&gt;
          #include &lt;sys/socket.h&gt;
          #include &lt;netinet/in.h&gt;
  
          int main() {
              int server_fd, new_socket;
              struct sockaddr_in address;
              int opt = 1;
              int addrlen = sizeof(address);
              char buffer[1024] = {0};
  
              server_fd = socket(AF_INET, SOCK_STREAM, 0);
              setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));
              address.sin_family = AF_INET;
              address.sin_addr.s_addr = INADDR_ANY;
              address.sin_port = htons(8080);
  
              bind(server_fd, (struct sockaddr *)&address, sizeof(address));
              listen(server_fd, 3);
              new_socket = accept(server_fd, (struct sockaddr )&address, (socklen_t)&addrlen);
              read(new_socket, buffer, 1024);
              printf("%s\n", buffer);
              return 0;
          }
        </pre>
      </p>
  
      <h2 class="sub-title">TCP and UDP Server Using Select</h2>
      <p class="content">
        The select() function allows a program to monitor multiple file descriptors to see if any of them are ready for I/O operations. Below is a simplified example:
        <pre>
          // Example for TCP and UDP server using select
          // Include necessary headers
        </pre>
        <p>This example demonstrates handling both TCP and UDP connections.</p>
      </p>
  
      <h2 class="sub-title">Servers</h2>
      <p class="content">
        Servers play a vital role in networking, handling requests from clients and providing services. Common types of servers include:
        <ul>
          <li><strong>Web Servers:</strong> Serve web pages to clients.</li>
          <li><strong>File Servers:</strong> Manage file storage and access.</li>
          <li><strong>Database Servers:</strong> Provide data storage and retrieval services.</li>
        </ul>
      </p>
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=transport1" target="_blank">Introduction to Transport Layer</a></li>
        <li><a href="https://www.youtube.com/watch?v=transport2" target="_blank">Transport Layer Protocols Explained</a></li>
      </ul>
  
      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the concepts discussed:</p>
      <div class="diagram-container">
        <img src="path/to/tcp_congestion_control.png" alt="TCP Congestion Control Diagram" />
        <img src="path/to/udp_overview.png" alt="User Datagram Protocol Overview Diagram" />
        <img src="path/to/multiplexing_demultiplexing.png" alt="Multiplexing and Demultiplexing Diagram" />
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "TransportLayer",
  };
  </script>
  
  <style scoped>
  .transport-container {
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