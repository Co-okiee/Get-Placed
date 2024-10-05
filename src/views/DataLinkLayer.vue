<template>
    <div class="dl-container">
      <h1 class="main-title">Data Link Layer</h1>
      <p class="intro">
        The Data Link Layer is the second layer of the OSI model. It is responsible for node-to-node data transfer and error detection and correction, ensuring reliable communication over a single link.
      </p>
  
      <h2 class="sub-title">Local Area Network (LAN) Technologies</h2>
      <p class="content">
        LAN technologies enable devices within a limited geographical area to communicate. Common technologies include Ethernet, Wi-Fi, and Token Ring.
      </p>
  
      <h2 class="sub-title">Computer Network | Bridges (Local Internetworking Device)</h2>
      <p class="content">
        Bridges connect multiple network segments, making them function as a single network. They filter traffic and reduce collisions by dividing a large network into smaller segments.
      </p>
  
      <h2 class="sub-title">Internetworking</h2>
      <p class="content">
        Internetworking involves connecting different networks to enable communication. Routers play a vital role in directing data between these networks.
      </p>
  
      <h2 class="sub-title">Framing In Data Link Layer</h2>
      <p class="content">
        Framing is the process of encapsulating network layer packets into frames. Each frame has a header and trailer for error detection and addressing.
      </p>
  
      <h2 class="sub-title">Introduction of MAC Address</h2>
      <p class="content">
        A MAC (Media Access Control) address is a unique identifier assigned to network interfaces for communication on the physical network segment. It consists of 48 bits and is usually represented in hexadecimal.
      </p>
  
      <h2 class="sub-title">MAC Filtering</h2>
      <p class="content">
        MAC filtering allows network administrators to control which devices can access the network based on their MAC addresses, enhancing security.
      </p>
  
      <h2 class="sub-title">Multiple Access Protocols</h2>
      <p class="content">
        These protocols determine how multiple devices share the same communication medium. Common protocols include CSMA/CD, CSMA/CA, and Token Ring.
      </p>
  
      <h2 class="sub-title">Ethernet Frame Format</h2>
      <p class="content">
        An Ethernet frame consists of the following fields: 
        <ul>
          <li>Destination MAC Address</li>
          <li>Source MAC Address</li>
          <li>EtherType/Length</li>
          <li>Payload (Data)</li>
          <li>Frame Check Sequence (FCS)</li>
        </ul>
      </p>
  
      <h2 class="sub-title">EtherChannel</h2>
      <p class="content">
        EtherChannel combines multiple Ethernet links into a single logical link, increasing bandwidth and providing redundancy.
      </p>
  
      <h2 class="sub-title">Difference between Byte Stuffing and Bit Stuffing</h2>
      <p class="content">
        Byte stuffing adds a special byte to the data to indicate a data frame boundary, while bit stuffing inserts a '0' after a sequence of five '1's to ensure a frame boundary.
      </p>
  
      <h2 class="sub-title">Implementing Byte Stuffing using Java</h2>
      <p class="content">
        Here’s a simple example of byte stuffing in Java:
        java
        public class ByteStuffing {
            public static String byteStuff(String data) {
                return data.replace("01111110", "011111110");
            }
        }
        
      </p>
  
      <h2 class="sub-title">Circuit Switching</h2>
      <p class="content">
        Circuit switching establishes a dedicated communication path between two endpoints, commonly used in traditional telephone networks.
      </p>
  
      <h2 class="sub-title">Packet Switching and Delays</h2>
      <p class="content">
        Packet switching breaks data into packets, which travel independently. Delays may occur due to routing and queuing processes.
      </p>
  
      <h2 class="sub-title">Circuit Switching VS Packet Switching</h2>
      <p class="content">
        Circuit switching provides a dedicated path with consistent bandwidth, while packet switching allows for more efficient use of resources, though it may introduce delays.
      </p>
  
      <h2 class="sub-title">Differences between Virtual Circuits & Datagram Networks</h2>
      <p class="content">
        Virtual circuits establish a predefined path for data, while datagram networks send packets independently, allowing for more flexibility.
      </p>
  
      <h2 class="sub-title">Switching Techniques: Message Switching</h2>
      <p class="content">
        Message switching stores entire messages at intermediate nodes before forwarding them, ensuring reliable delivery but introducing delays.
      </p>
  
      <h2 class="sub-title">Types of Switches</h2>
      <p class="content">
        Types of switches include:
        <ul>
          <li>Unmanaged Switches</li>
          <li>Managed Switches</li>
          <li>Layer 2 Switches</li>
          <li>Layer 3 Switches</li>
        </ul>
      </p>
  
      <h2 class="sub-title">Maximum Data Rate (Channel Capacity) for Noiseless and Noisy Channels</h2>
      <p class="content">
        The channel capacity for a noiseless channel is calculated using Shannon's Theorem, while for a noisy channel, it considers the signal-to-noise ratio.
      </p>
  
      <h2 class="sub-title">Hot Spot 2.0</h2>
      <p class="content">
        Hot Spot 2.0 is an advanced Wi-Fi feature that allows for seamless roaming between Wi-Fi networks, improving connectivity for mobile devices.
      </p>
  
      <h2 class="sub-title">Collision Avoidance in Wireless Networks</h2>
      <p class="content">
        Collision avoidance techniques, such as CSMA/CA, are used in wireless networks to minimize packet collisions during transmission.
      </p>
  
      <h2 class="sub-title">Traditional Wireless Mobile Communication</h2>
      <p class="content">
        Traditional wireless communication uses radio waves to transmit data, with various standards like GSM and CDMA for mobile networks.
      </p>
  
      <h2 class="sub-title">Carrier Sense Multiple Access (CSMA)</h2>
      <p class="content">
        CSMA is a network protocol that listens for a carrier signal before transmitting, reducing the chance of collisions.
      </p>
  
      <h2 class="sub-title">Collision Detection in CSMA/CD</h2>
      <p class="content">
        CSMA/CD detects collisions in a shared medium, allowing devices to stop transmitting and retry after a random back-off time.
      </p>
  
      <h2 class="sub-title">Efficiency of CSMA/CD</h2>
      <p class="content">
        The efficiency of CSMA/CD decreases with increased network traffic, as the probability of collisions rises.
      </p>
  
      <h2 class="sub-title">Back-off Algorithm for CSMA/CD</h2>
      <p class="content">
        The back-off algorithm determines how long a device should wait before attempting to retransmit after a collision occurs.
      </p>
  
      <h2 class="sub-title">Controlled Access Protocols</h2>
      <p class="content">
        Controlled access protocols, like Token Ring, ensure that only one device transmits at a time, preventing collisions.
      </p>
  
      <h2 class="sub-title">Virtual LAN (VLAN)</h2>
      <p class="content">
        VLANs segment a network into smaller, isolated groups, improving security and reducing broadcast traffic.
      </p>
  
      <h2 class="sub-title">Inter VLAN Routing by Layer 3 Switch</h2>
      <p class="content">
        Layer 3 switches can route traffic between VLANs, enabling communication while maintaining network segmentation.
      </p>
  
      <h2 class="sub-title">Computer Network | Private VLAN</h2>
      <p class="content">
        Private VLANs enhance security by isolating devices within the same VLAN, limiting communication between them.
      </p>
  
      <h2 class="sub-title">Computer Network | VLAN ACL (VACL)</h2>
      <p class="content">
        VLAN Access Control Lists (VACLs) filter traffic within VLANs based on specified rules, enhancing security.
      </p>
  
      <h2 class="sub-title">Access and Trunk Ports</h2>
      <p class="content">
        Access ports connect to end devices, while trunk ports carry traffic for multiple VLANs between switches.
      </p>
  
      <h2 class="sub-title">Role-Based Access Control</h2>
      <p class="content">
        Role-based access control assigns permissions based on user roles, enhancing security and simplifying management.
      </p>
  
      <h2 class="sub-title">Port Security</h2>
      <p class="content">
        Port security prevents unauthorized devices from connecting to a network port, improving overall network security.
      </p>
  
      <h2 class="sub-title">Inter-Switch Link (ISL) and IEEE 802.1Q</h2>
      <p class="content">
        ISL and IEEE 802.1Q are VLAN tagging protocols that allow switches to identify VLAN traffic across trunk links.
      </p>
  
      <h2 class="sub-title">Dynamic Trunking Protocol (DTP)</h2>
      <p class="content">
        DTP is a Cisco protocol that negotiates trunking between switches, automating the configuration of trunk ports.
      </p>
  
      <h2 class="sub-title">Sliding Window Protocol | Set 1 (Sender Side)</h2>
      <p class="content">
        The sliding window protocol allows the sender to send multiple frames before needing an acknowledgment, enhancing throughput.
      </p>
  
      <h2 class="sub-title">Sliding Window Protocol | Set 2 (Receiver Side)</h2>
      <p class="content">
        On the receiver side, the protocol manages the acknowledgment of received frames and ensures that frames are processed in order.
      </p>
  
      <h2 class="sub-title">Sliding Window Protocol | Set 3 (Selective Repeat)</h2>
      <p class="content">
        Selective Repeat allows the receiver to acknowledge non-contiguous frames, enabling retransmission of only the lost frames.
      </p>
  
      <h2 class="sub-title">Sliding Window Protocols Summary</h2>
      <p class="content">
        Sliding window protocols improve efficiency by allowing multiple frames to be in transit simultaneously, reducing wait times.
      </p>
  
      <h2 class="sub-title">Stop and Wait ARQ</h2>
      <p class="content">
        Stop and Wait ARQ requires the sender to wait for an acknowledgment after sending each frame, which can lead to inefficiencies.
      </p>
  
      <h2 class="sub-title">Difference between Stop and Wait, Go-Back-N, and Selective Repeat</h2>
      <p class="content">
        Stop and Wait sends one frame at a time, Go-Back-N allows multiple frames but retransmits from the last acknowledged frame, while Selective Repeat retransmits only the frames that are lost.
      </p>
  
      <h2 class="sub-title">Manchester Encoding</h2>
      <p class="content">
        Manchester encoding represents binary data with transitions, ensuring reliable clock recovery and reducing errors.
      </p>
  
      <h2 class="sub-title">Error Detection</h2>
      <p class="content">
        Error detection techniques, such as checksums and CRC (Cyclic Redundancy Check), identify errors in transmitted data.
      </p>
  
      <h2 class="sub-title">Hamming Code</h2>
      <p class="content">
        Hamming code is an error correction technique that can detect and correct single-bit errors in data.
      </p>
  
      <h2 class="sub-title">Program to Remotely Power On a PC Over the Internet Using the Wake-on-LAN Protocol</h2>
      <p class="content">
        The Wake-on-LAN protocol allows you to turn on a computer remotely. Here is a simple example in Python:
        python
        import socket
  
        def wake_on_lan(macaddress):
            macaddress = macaddress.replace(":", "")
            magic = bytes.fromhex("FF") * 6 + bytes.fromhex(macaddress) * 16
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(magic, ('&lt;broadcast&gt;', 9))
        
        wake_on_lan('00:11:22:33:44:55')
        
      </p>
  
      <h2 class="sub-title">Basics of Wi-Fi</h2>
      <p class="content">
        Wi-Fi technology allows devices to connect to a network wirelessly, using radio waves to transmit data.
      </p>
  
      <h2 class="sub-title">IEEE 802.11 Mac Frame</h2>
      <p class="content">
        The IEEE 802.11 MAC frame includes fields for frame control, duration, address fields, and data payload, facilitating wireless communication.
      </p>
  
      <h2 class="sub-title">Efficiency Of Token Ring</h2>
      <p class="content">
        Token Ring networks use a token-passing method to control access, which can enhance efficiency by preventing collisions.
      </p>
  
      <h2 class="sub-title">Token Bus (IEEE 802.4)</h2>
      <p class="content">
        Token Bus uses a token-passing protocol over a bus topology, allowing devices to transmit in a controlled manner.
      </p>
  
      <h2 class="sub-title">Multiplexing (Channel Sharing)</h2>
      <p class="content">
        Multiplexing combines multiple signals into one channel, improving efficiency in data transmission.
      </p>
  
      <h2 class="sub-title">Frequency Division and Time Division Multiplexing</h2>
      <p class="content">
        Frequency Division Multiplexing (FDM) allocates different frequency bands for each signal, while Time Division Multiplexing (TDM) assigns time slots for signals, enabling multiple communications over the same medium.
      </p>
  
      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the concepts discussed:</p>
      <div class="diagram-container">
        <img src="path/to/diagram1.png" alt="Ethernet Frame Format" />
        <img src="path/to/diagram2.png" alt="MAC Address Structure" />
        <img src="path/to/diagram3.png" alt="Circuit vs. Packet Switching" />
        <img src="path/to/diagram4.png" alt="VLAN Configuration" />
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "DataLinkLayer",
  };
  </script>
  
  <style scoped>
  .dl-container {
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