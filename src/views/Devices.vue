<template>
    <div class="network-container">
      <h1 class="main-title">Network Devices</h1>
      <p class="intro">
        Network devices are physical devices that mediate communication between computer networks. They play a crucial role in establishing, managing, and directing network traffic, ensuring efficient and secure data transfer.
      </p>

      <h2 class="sub-title">Types of Network Devices</h2>
      <ul class="characteristics-list">
        <li><strong>Hub:</strong> A basic networking device that connects multiple Ethernet devices, making them act as a single network segment.</li>
        <li><strong>Repeater:</strong> Amplifies signals in a network to extend the transmission distance between devices.</li>
        <li><strong>Bridge:</strong> Connects two or more networks and filters traffic between them at the data link layer (Layer 2).</li>
        <li><strong>Switch:</strong> A multiport device that forwards data packets between devices within the same network segment based on MAC addresses.</li>
        <li><strong>Router:</strong> Connects different networks and directs data packets between them using IP addresses.</li>
        <li><strong>Gateway:</strong> A device that connects two different networks and translates communication protocols.</li>
      </ul>
  
      <h2 class="sub-title">Inside a Router</h2>
      <p class="content">
        A router contains hardware and software components, including interfaces, routing protocols, and a routing table, allowing it to analyze and direct traffic efficiently.
      </p>
      <img src="path/to/router_diagram.png" alt="Diagram showing the internal structure of a router" class="diagram" />

      <h2 class="sub-title">Bridges (Local Internetworking Device)</h2>
      <p class="content">
        Bridges connect two or more network segments and help to reduce traffic on a LAN by dividing collision domains, thus improving overall network performance.
      </p>
  
      <h2 class="sub-title">Switch Functions at Layer 2</h2>
      <p class="content">
        Switches operate at the data link layer (Layer 2) of the OSI model, using MAC addresses to forward data only to the intended recipient, which enhances network efficiency.
      </p>
  
      <h2 class="sub-title">Collision Domain and Broadcast Domain</h2>
      <p class="content">
        A collision domain is a network segment where data packets can collide, causing packet loss. A broadcast domain is the set of devices that can receive broadcast packets sent by any device within the same network.
      </p>
  
      <h2 class="sub-title">Root Bridge Election in Spanning Tree Protocol</h2>
      <p class="content">
        In Spanning Tree Protocol (STP), the root bridge is elected based on the lowest bridge ID. This ensures a loop-free network topology by designating a central point for data traffic.
      </p>
      <img src="path/to/spanning_tree_diagram.png" alt="Diagram illustrating Root Bridge Election in STP" class="diagram" />
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=network1" target="_blank">Understanding Network Devices</a></li>
        <li><a href="https://www.youtube.com/watch?v=network2" target="_blank">Router and Switch Configuration</a></li>
      </ul>
  
      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the concepts discussed:</p>
      <div class="diagram-container">
        <img src="path/to/diagram1.png" alt="Diagram illustrating different types of network devices" />
        <img src="path/to/diagram2.png" alt="Diagram showing the structure of a bridge" />
        <img src="path/to/diagram3.png" alt="Comparison of collision domain and broadcast domain" />
      </div>
    </div>
</template>

<script>
export default {
  name: "NetworkDevices",
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