<template>
    <div class="misc-container">
      <h1 class="main-title">Miscellaneous Networking and Virtualization Concepts</h1>
      <p class="intro">
        This section explores various networking and virtualization concepts that are vital in understanding modern computing environments.
      </p>
  
      <h2 class="sub-title">Onion Routing</h2>
      <p class="content">
        Onion routing is a technique for anonymous communication over a computer network. Messages are encapsulated in layers of encryption, resembling the layers of an onion. The data is routed through a series of nodes, each removing a layer of encryption to reveal the next node, ensuring privacy and anonymity for users.
      </p>
      <img src="path/to/onion-routing-diagram.png" alt="Onion Routing Diagram" class="diagram" />
  
      <h2 class="sub-title">Types of Server Virtualization</h2>
      <ul class="characteristics-list">
        <li><strong>Full Virtualization:</strong> Emulates the underlying hardware, allowing multiple operating systems to run concurrently.</li>
        <li><strong>Paravirtualization:</strong> The guest OS is modified to interact with the hypervisor directly for better performance.</li>
        <li><strong>OS-Level Virtualization:</strong> The host OS runs multiple isolated user-space instances (containers).</li>
      </ul>
  
      <h2 class="sub-title">Cloud Computing</h2>
      <p class="content">
        Cloud computing provides on-demand access to a shared pool of configurable computing resources, allowing for rapid provisioning and release with minimal management effort. 
        <strong>Characteristics of Virtualization:</strong> 
        Scalability, flexibility, and cost-effectiveness are primary characteristics of cloud computing.
      </p>
  
      <h2 class="sub-title">On-Premises Cost Estimates of Virtualization</h2>
      <p class="content">
        On-premises virtualization incurs costs associated with hardware, software licenses, maintenance, and personnel. Companies must consider these factors when calculating total cost of ownership (TCO).
      </p>
  
      <h2 class="sub-title">Hardware-Based Virtualization</h2>
      <p class="content">
        This approach uses hardware features (such as Intel VT or AMD-V) to enable multiple operating systems to run on a single physical machine, enhancing performance and resource utilization.
      </p>
  
      <h2 class="sub-title">Operating System-Based Virtualization</h2>
      <p class="content">
        This type relies on the host operating system to create and manage virtual environments. It is often more lightweight than hardware-based virtualization, allowing for quick deployments.
      </p>
  
      <h2 class="sub-title">Digital Subscriber Line (DSL)</h2>
      <p class="content">
        DSL is a high-speed internet connection that transmits data over traditional telephone lines, allowing for simultaneous voice and data transmission. It is widely used for residential internet access.
      </p>
  
      <h2 class="sub-title">Image Steganography</h2>
      <p class="content">
        Image steganography is the practice of hiding information within an image file. It can be used for secure communications by embedding secret data in a way that is not easily detectable.
      </p>
  
      <h2 class="sub-title">Network Neutrality</h2>
      <p class="content">
        Network neutrality is the principle that internet service providers must treat all data on the internet equally, without discriminating or charging differently by user, content, or website.
      </p>
  
      <h2 class="sub-title">Basics of NS2 and OTcl/Tcl Script</h2>
      <p class="content">
        NS2 (Network Simulator 2) is a discrete event simulator used for networking research. OTcl is an object-oriented extension of Tcl, used for scripting in NS2 simulations to configure network protocols and behaviors.
      </p>
  
      <h2 class="sub-title">Voice over Internet Protocol (VoIP)</h2>
      <p class="content">
        VoIP technology allows for voice communication and multimedia sessions over the Internet. It converts voice signals into digital packets for transmission, enabling phone calls over the Internet.
      </p>
  
      <h2 class="sub-title">Cisco Router Modes</h2>
      <p class="content">
        Cisco routers have several operational modes including User mode, Privileged mode, Global Configuration mode, and Interface Configuration mode, each allowing different levels of command access and configuration capabilities.
      </p>
  
      <h2 class="sub-title">Cisco Router Basic Commands</h2>
      <ul class="characteristics-list">
        <li><strong>show running-config:</strong> Displays the current configuration of the router.</li>
        <li><strong>configure terminal:</strong> Enters global configuration mode.</li>
        <li><strong>ping:</strong> Tests connectivity to another network device.</li>
      </ul>
  
      <h2 class="sub-title">Backing Up Cisco IOS Router Image</h2>
      <p class="content">
        To back up a Cisco IOS router image, use the command <code>copy flash tftp</code> to transfer the image from the router's flash memory to a TFTP server.
      </p>
  
      <h2 class="sub-title">Basic Configuration of Adaptive Security Appliance (ASA)</h2>
      <p class="content">
        ASA is used for network security. Basic configurations include defining interfaces, setting up security levels, and configuring routing protocols.
      </p>
  
      <h2 class="sub-title">Adaptive Security Appliance (ASA) Features</h2>
      <ul class="characteristics-list">
        <li><strong>Firewall:</strong> Provides stateful inspection of traffic.</li>
        <li><strong>VPN Support:</strong> Allows secure remote access to internal resources.</li>
        <li><strong>Intrusion Prevention:</strong> Monitors network traffic for malicious activity.</li>
      </ul>
  
      <h2 class="sub-title">Default Flow of Traffic (ASA)</h2>
      <p class="content">
        By default, traffic from a lower security level to a higher security level is allowed, while traffic in the opposite direction is denied unless explicitly permitted.
      </p>
  
      <h2 class="sub-title">Cisco ASA Redistribution Example</h2>
      <p class="content">
        Redistribution allows routing information from different protocols to be shared. For example, to redistribute OSPF into EIGRP, use the command <code>redistribute ospf 1 metric 100</code>.
      </p>
  
      <h2 class="sub-title">Telnet and SSH on Adaptive Security Appliance (ASA)</h2>
      <p class="content">
        Telnet provides unencrypted access to the ASA, while SSH offers secure encrypted access. Configuration requires enabling the respective protocol and specifying user credentials.
      </p>
  
      <h2 class="sub-title">Near Field Communication (NFC)</h2>
      <p class="content">
        NFC is a short-range wireless technology that allows for data transfer between devices within close proximity, often used in contactless payments and data sharing.
      </p>
  
      <h2 class="sub-title">Relabel-to-Front Algorithm</h2>
      <p class="content">
        The relabel-to-front algorithm is a method for maintaining a list where elements can be moved to the front when accessed, optimizing access times in data structures.
      </p>
  
      <h2 class="sub-title">Berkeley’s Algorithm</h2>
      <p class="content">
        Berkeley’s algorithm is a method for synchronizing time across distributed systems, where a coordinator collects timestamps from various nodes and calculates an average time to set on each node.
      </p>
  
      <h2 class="sub-title">Cristian’s Algorithm</h2>
      <p class="content">
        Cristian’s algorithm is another time synchronization method that involves a time server providing its time to a requesting client, which adjusts its clock based on the received time and network delays.
      </p>
  
      <h2 class="sub-title">Universal Serial Bus (USB) in Computer Network</h2>
      <p class="content">
        USB is a standard for connecting peripherals to a computer. It allows for data transfer and power supply through a single interface, facilitating easy connections for various devices.
      </p>
  
      <h2 class="sub-title">Type-C Port in Computer Network</h2>
      <p class="content">
        The USB Type-C port is a universal connector that supports higher power delivery and faster data transfer rates compared to previous USB versions, enhancing connectivity across devices.
      </p>
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=example1" target="_blank">Onion Routing Explained</a></li>
        <li><a href="https://www.youtube.com/watch?v=example2" target="_blank">Introduction to VoIP</a></li>
        <li><a href="https://www.youtube.com/watch?v=example3" target="_blank">Cisco Router Basics</a></li>
      </ul>
  
      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the concepts discussed:</p>
      <div class="diagram-container">
        <img src="path/to/onion-routing-diagram.png" alt="Onion Routing Diagram" />
        <img src="path/to/server-virtualization-diagram.png" alt="Types of Server Virtualization" />
        <img src="path/to/voip-diagram.png" alt="Voice over IP Diagram" />
        <img src="path/to/nfc-diagram.png" alt="Near Field Communication Diagram" />
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "MiscellaneousNetworking",
  };
  </script>
  
  <style scoped>
  .misc-container {
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