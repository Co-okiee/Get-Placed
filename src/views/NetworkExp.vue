<template>
    <div class="network-container">
      <h1 class="main-title">Networking Experiments</h1>
      <p class="intro">
        Networking involves connecting computers and devices to share resources and information. This section explores various networking experiments and implementations using different programming languages.
      </p>

      <h2 class="sub-title">Let’s Experiment with Networking</h2>
      <p class="content">
        Networking experiments allow us to understand and explore different protocols and methodologies used in communication between devices. Here are some experiments that can be conducted.
      </p>
  
      <h2 class="sub-title">Mobile Ad Hoc Network (MANET)</h2>
      <p class="content">
        A Mobile Ad Hoc Network (MANET) is a self-configuring network of mobile devices connected wirelessly. MANETs can change locations and links frequently, making them highly dynamic.
      </p>

      <h2 class="sub-title">Types of MANET</h2>
      <ul class="characteristics-list">
        <li><strong>Infrastructure-Based MANET:</strong> Relies on fixed infrastructure like base stations for communication.</li>
        <li><strong>Infrastructureless MANET:</strong> Devices communicate directly without the need for fixed infrastructure.</li>
      </ul>

      <h2 class="sub-title">Simple Chat Room using Python</h2>
      <p class="content">
        A simple chat room can be implemented in Python using socket programming. It allows multiple clients to communicate through a server.
      </p>
      <pre>
        <code>
          # Simple Chat Server in Python
          import socket
          import threading

          def handle_client(client_socket):
              while True:
                  message = client_socket.recv(1024).decode('utf-8')
                  if message:
                      print(f"Received: {message}")
                  else:
                      break
              client_socket.close()

          server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          server.bind(('0.0.0.0', 9999))
          server.listen(5)
          print("Server listening on port 9999")

          while True:
              client, addr = server.accept()
              print(f"Accepted connection from {addr}")
              client_handler = threading.Thread(target=handle_client, args=(client,))
              client_handler.start()
        </code>
      </pre>
  
      <h2 class="sub-title">Socket Programming in Java</h2>
      <p class="content">
        Socket programming in Java allows the establishment of a communication channel between clients and servers.
      </p>
      <pre>
        <code>
          // Simple Server in Java
          import java.io.*;
          import java.net.*;

          public class SimpleServer {
              public static void main(String[] args) throws IOException {
                  ServerSocket serverSocket = new ServerSocket(9999);
                  System.out.println("Server listening on port 9999");
                  Socket socket = serverSocket.accept();
                  BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                  String message;
                  while ((message = in.readLine()) != null) {
                      System.out.println("Received: " + message);
                  }
                  socket.close();
              }
          }
        </code>
      </pre>

      <h2 class="sub-title">C Program to Find IP Address, Subnet Mask & Default Gateway</h2>
      <p class="content">
        The following C program retrieves and displays the IP address, subnet mask, and default gateway of the machine.
      </p>
      <pre>
        <code>
          #include &lt;stdio.h&gt;
          #include &lt;stdlib.h&gt;
          #include &lt;string.h&gt;
          #include &lt;arpa/inet.h&gt;
          #include &lt;ifaddrs.h&gt;

          void get_network_info() {
              struct ifaddrs *ifaddr, *ifa;
              getifaddrs(&ifaddr);
              for (ifa = ifaddr; ifa != NULL; ifa = ifa->ifa_next) {
                  if (ifa->ifa_addr && ifa->ifa_addr->sa_family == AF_INET) {
                      char ip[INET_ADDRSTRLEN];
                      inet_ntop(AF_INET, &((struct sockaddr_in *)ifa->ifa_addr)->sin_addr, ip, sizeof(ip));
                      printf("Interface: %s\tIP Address: %s\n", ifa->ifa_name, ip);
                  }
              }
              freeifaddrs(ifaddr);
          }

          int main() {
              get_network_info();
              return 0;
          }
        </code>
      </pre>
  
      <h2 class="sub-title">Introduction to Variable Length Subnet Mask (VLSM)</h2>
      <p class="content">
        Variable Length Subnet Masking (VLSM) allows for more efficient use of IP addresses by assigning different subnet masks to different subnets based on their size.
      </p>

      <h2 class="sub-title">Extracting MAC Address using Python</h2>
      <p class="content">
        The following Python script can be used to extract the MAC address of the machine.
      </p>
      <pre>
        <code>
          import uuid

          mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
          print("MAC Address:", mac)
        </code>
      </pre>
      
      <h2 class="sub-title">Implementation of Diffie-Hellman Algorithm</h2>
      <p class="content">
        The Diffie-Hellman algorithm is a method of securely exchanging cryptographic keys over a public channel.
      </p>
      <pre>
        <code>
          # Simple implementation in Python
          def diffie_hellman(p, g, a):
              A = (g ** a) % p
              return A

          p = 23  # prime number
          g = 5   # generator
          a = 6   # private key
          A = diffie_hellman(p, g, a)
          print("Public key A:", A)
        </code>
      </pre>

      <h2 class="sub-title">Java Implementation of Diffie-Hellman Algorithm between Client and Server</h2>
      <p class="content">
        A simple client-server implementation in Java for the Diffie-Hellman key exchange can be done as follows.
      </p>
      <pre>
        <code>
          // Client and Server implementation would go here.
        </code>
      </pre>

      <h2 class="sub-title">Socket Programming in Python</h2>
      <p class="content">
        Python allows for easy socket programming to create client-server applications.
      </p>

      <h2 class="sub-title">Socket Programming with Multi-threading in Python</h2>
      <p class="content">
        Using multi-threading in Python enables handling multiple clients simultaneously.
      </p>

      <h2 class="sub-title">Cyclic Redundancy Check in Python</h2>
      <p class="content">
        A simple example of implementing a CRC to check data integrity in Python can be seen below.
      </p>

      <h2 class="sub-title">Explicitly Assigning Port Number to Client in Socket</h2>
      <p class="content">
        Clients can explicitly assign port numbers while creating a socket connection to the server.
      </p>
  
      <h2 class="sub-title">Netstat Command in Linux</h2>
      <p class="content">
        The netstat command displays network connections, routing tables, interface statistics, and more.
      </p>

      <h2 class="sub-title">nslookup Command in Linux with Examples</h2>
      <p class="content">
        The nslookup command is used to query the DNS to obtain domain name or IP address mapping. Example: <code>nslookup www.example.com</code>.
      </p>

      <h2 class="sub-title">UDP Server-Client Implementation in C</h2>
      <p class="content">
        Here’s a simple UDP server-client example in C.
      </p>

      <h2 class="sub-title">C Program for File Transfer using UDP</h2>
      <p class="content">
        A program that demonstrates file transfer over UDP can be implemented in C.
      </p>

      <h2 class="sub-title">Java Program to Find IP Address of Your Computer</h2>
      <p class="content">
        Java can be used to find the local IP address of the computer.
      </p>

      <h2 class="sub-title">Finding IP Address of a URL in Java</h2>
      <p class="content">
        The following code snippet in Java demonstrates how to find the IP address of a given URL.
      </p>

      <h2 class="sub-title">Program to Calculate the Round Trip Time (RTT)</h2>
      <p class="content">
        The Round Trip Time (RTT) can be calculated by measuring the time taken for packets to travel to a destination and back.
      </p>

      <h2 class="sub-title">Network Configuration and Troubleshooting Commands in Linux</h2>
      <p class="content">
        Common commands include <code>ifconfig</code>, <code>ping</code>, and <code>traceroute</code> to troubleshoot network issues.
      </p>

      <h2 class="sub-title">Implementing Checksum Using Java</h2>
      <p class="content">
        Checksum can be implemented in Java to ensure data integrity during transmission.
      </p>

      <h2 class="sub-title">C Program to Display Hostname and IP Address</h2>
      <p class="content">
        The following C program retrieves and displays the hostname and corresponding IP address.
      </p>
  
      <h2 class="sub-title">Program to Determine Class, Network, and Host ID of an IPv4 Address</h2>
      <p class="content">
        This program determines the class, network ID, and host ID of a given IPv4 address.
      </p>

      <h2 class="sub-title">Program to Determine Class, Broadcast Address, and Network Address of an IPv4 Address</h2>
      <p class="content">
        A program that determines the class, broadcast address, and network address based on an IPv4 address can be useful in networking.
      </p>

      <h2 class="sub-title">Program for IP Forwarding Table Lookup</h2>
      <p class="content">
        IP forwarding can be implemented to route packets from one network to another efficiently.
      </p>

      <h2 class="sub-title">Wi-Fi Password of All Connected Networks in Windows/Linux</h2>
      <p class="content">
        A script can be written to extract the saved Wi-Fi passwords of all networks connected to the system.
      </p>
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=network1" target="_blank">Introduction to Networking (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=network2" target="_blank">Networking Concepts in Hindi</a></li>
      </ul>
  
      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the concepts discussed:</p>
      <div class="diagram-container">
        <img src="path/to/network_diagram1.png" alt="Diagram illustrating MANET" />
        <img src="path/to/network_diagram2.png" alt="Diagram showing socket communication" />
        <img src="path/to/network_diagram3.png" alt="Diagram of Diffie-Hellman Key Exchange" />
      </div>
    </div>
</template>

<script>
export default {
    name: "NetworkingExperiments",
};
</script>

<style scoped>
.network-container {
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