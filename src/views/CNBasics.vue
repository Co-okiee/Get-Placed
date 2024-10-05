<template>
    <div class="network-container">
      <h1 class="main-title">Basics of Computer Networking</h1>
      <p class="intro">
        Computer networking is the practice of connecting computers and other devices to share resources and information. It enables communication and data exchange among devices.
      </p>
  
      <h2 class="sub-title">The Internet and the Web</h2>
      <p class="content">
        The Internet is a global network of interconnected computers that communicate using standardized protocols. The Web is a collection of information accessible through the Internet, typically using web browsers.
      </p>
  
      <h2 class="sub-title">Internet and Web Programming: Behind the Scenes</h2>
      <p class="content">
        Internet programming involves creating applications that run on the web. This includes using languages like HTML, CSS, and JavaScript for front-end development and PHP, Python, or Java for back-end services.
      </p>
  
      <h2 class="sub-title">The New Internet | Internet of Everything</h2>
      <p class="content">
        The Internet of Everything (IoE) extends the concept of the Internet by connecting people, processes, data, and things. It enhances the interaction among these elements, enabling smarter and more efficient systems.
      </p>
  
      <h2 class="sub-title">Unknown Facts of Networking</h2>
      <p class="content">
        Networking has fascinating facts, such as the first message sent over the ARPANET in 1969, which was supposed to be "LOGIN" but crashed the network after just two letters were transmitted.
      </p>
  
      <h2 class="sub-title">Network Goals</h2>
      <p class="content">
        The primary goals of networking include resource sharing, data communication, reliability, scalability, and providing security.
      </p>
  
      <h2 class="sub-title">Line Configuration in Computer Networks</h2>
      <p class="content">
        Line configuration refers to how devices are connected in a network. Common configurations include point-to-point and multipoint configurations.
      </p>
  
      <h2 class="sub-title">Transmission Modes in Computer Networks</h2>
      <ul class="characteristics-list">
        <li><strong>Simplex:</strong> Communication is unidirectional (one way).</li>
        <li><strong>Half-Duplex:</strong> Communication is bidirectional but not simultaneous (one at a time).</li>
        <li><strong>Full Duplex:</strong> Communication is bidirectional and simultaneous (both ways at once).</li>
      </ul>
  
      <h2 class="sub-title">Types of Transmission Media</h2>
      <ul class="characteristics-list">
        <li><strong>Twisted Pair Cable:</strong> Consists of pairs of wires twisted together, commonly used in LANs.</li>
        <li><strong>Coaxial Cable:</strong> Contains a central conductor and is used for cable TV and Internet connections.</li>
        <li><strong>Fiber Optic Cable:</strong> Uses light to transmit data, providing high speed and bandwidth over long distances.</li>
      </ul>
  
      <h2 class="sub-title">Unicast, Broadcast, and Multicast</h2>
      <p class="content">
        <strong>Unicast:</strong> One-to-one communication. <br>
        <strong>Broadcast:</strong> One-to-all communication. <br>
        <strong>Multicast:</strong> One-to-many communication, where data is sent to a group of interested receivers.
      </p>
  
      <h2 class="sub-title">Introduction to Basic Networking Terminology</h2>
      <p class="content">
        Understanding basic networking terms such as IP address, subnet mask, router, and switch is essential for anyone working with networks.
      </p>
  
      <h2 class="sub-title">Network Topologies</h2>
      <ul class="characteristics-list">
        <li><strong>Star Topology:</strong> All devices are connected to a central hub.</li>
        <li><strong>Bus Topology:</strong> All devices share a single communication line.</li>
        <li><strong>Ring Topology:</strong> Devices are connected in a circular configuration.</li>
      </ul>
  
      <h2 class="sub-title">Types of Area Networks – LAN, MAN, and WAN</h2>
      <p class="content">
        <strong>LAN (Local Area Network):</strong> Covers a small geographical area, like a single building. <br>
        <strong>MAN (Metropolitan Area Network):</strong> Covers a city or a large campus. <br>
        <strong>WAN (Wide Area Network):</strong> Covers a broad area, potentially worldwide.
      </p>
  
      <h2 class="sub-title">Telecom Networks</h2>
      <p class="content">
        Telecom networks provide communication services through various technologies, including cellular, satellite, and fiber optics, enabling voice, video, and data transmission.
      </p>
  
      <h2 class="sub-title">Access Networks</h2>
      <p class="content">
        Access networks connect end-users to the broader telecommunications network. They can be wired (DSL, fiber) or wireless (Wi-Fi, cellular).
      </p>
  
      <h2 class="sub-title">TCP/IP Model</h2>
      <p class="content">
        The TCP/IP model consists of four layers: Application, Transport, Internet, and Network Access. It defines how data is transmitted over the network.
      </p>
  
      <h2 class="sub-title">Layers of OSI Model</h2>
      <p class="content">
        The OSI model consists of seven layers: Application, Presentation, Session, Transport, Network, Data Link, and Physical. It standardizes networking protocols to ensure interoperability.
      </p>
  
      <h2 class="sub-title">Introduction to Active Directory Domain Service</h2>
      <p class="content">
        Active Directory (AD) is a directory service for Windows domain networks, providing authentication, authorization, and centralized management of network resources.
      </p>
  
      <h2 class="sub-title">Advantages and Disadvantages of Computer Networking</h2>
      <ul class="characteristics-list">
        <li><strong>Advantages:</strong> Resource sharing, increased communication speed, and enhanced security through centralized management.</li>
        <li><strong>Disadvantages:</strong> Complexity in network management, security vulnerabilities, and dependency on network infrastructure.</li>
      </ul>
  
      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the concepts discussed:</p>
      <div class="diagram-container">
        <img src="path/to/network_topologies.png" alt="Diagram illustrating different network topologies" />
        <img src="path/to/tcp_ip_model.png" alt="Diagram showing TCP/IP model layers" />
        <img src="path/to/osi_model.png" alt="Diagram showing OSI model layers" />
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "BasicsOfComputerNetworking",
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