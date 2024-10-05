<template>
    <div class="hld-container">
      <h1 class="main-title">High-Level Design (HLD)</h1>
      <p class="intro">
        High-Level Design (HLD) is an essential phase in system design, focusing on defining the system's architecture, components, modules, and interfaces in a structured way. It outlines how the system will function and interact with external systems.
      </p>

      <h2 class="sub-title">What is High-Level Design?</h2>
      <p class="content">
        HLD provides an overview of the system architecture and helps to establish the relationships between components. It serves as a blueprint for the development process, ensuring all stakeholders understand the system's layout.
      </p>
  
      <h2 class="sub-title">Availability in System Design</h2>
      <p class="content">
        Availability refers to the system's ability to remain operational and accessible when required. High availability designs often incorporate redundancy and failover mechanisms to minimize downtime.
      </p>

      <h2 class="sub-title">Consistency in System Design</h2>
      <p class="content">
        Consistency ensures that all users see the same data at the same time, regardless of when or where they access the system. Maintaining consistency is crucial for systems handling critical transactions.
      </p>
  
      <h2 class="sub-title">Reliability in System Design</h2>
      <p class="content">
        Reliability refers to the system's ability to function correctly over time. Reliable systems incorporate error detection, redundancy, and recovery mechanisms to maintain functionality under varying conditions.
      </p>
  
      <h2 class="sub-title">CAP Theorem</h2>
      <p class="content">
        The CAP theorem states that in a distributed data store, it's impossible to guarantee all three of the following simultaneously: Consistency, Availability, and Partition Tolerance. Designers must prioritize which two attributes to focus on based on system requirements.
      </p>

      <h2 class="sub-title">Difference between Process and Thread</h2>
      <ul class="characteristics-list">
        <li><strong>Process:</strong> A process is an independent program in execution, with its own memory space.</li>
        <li><strong>Thread:</strong> A thread is a lightweight process that shares the same memory space but operates independently within a process.</li>
      </ul>
  
      <h2 class="sub-title">Difference between Concurrency and Parallelism</h2>
      <ul class="characteristics-list">
        <li><strong>Concurrency:</strong> Refers to the ability of the system to manage multiple tasks simultaneously, allowing them to progress without necessarily being executed at the same time.</li>
        <li><strong>Parallelism:</strong> Involves executing multiple tasks at the exact same time, often using multiple processors.</li>
      </ul>
  
      <h2 class="sub-title">Load Balancer</h2>
      <p class="content">
        A load balancer distributes incoming network traffic across multiple servers, ensuring no single server becomes overwhelmed, improving responsiveness and availability.
      </p>

      <h2 class="sub-title">Consistent Hashing</h2>
      <p class="content">
        Consistent hashing is a strategy for distributing data across multiple nodes while minimizing reorganization when nodes are added or removed. It's particularly useful for scalable distributed systems.
      </p>

      <h2 class="sub-title">Content Delivery Network (CDN) in System Design</h2>
      <p class="content">
        A CDN is a network of servers distributed geographically to deliver web content more efficiently by caching it closer to users. This reduces latency and improves load times for users accessing content from different locations.
      </p>

      <h2 class="sub-title">Caching in System Design</h2>
      <p class="content">
        Caching stores frequently accessed data in a temporary storage location to improve retrieval speed and reduce load on the primary data source, enhancing system performance.
      </p>

      <h2 class="sub-title">Cache Eviction Policies</h2>
      <p class="content">
        Cache eviction policies determine how data is removed from the cache when it reaches its capacity. Common policies include Least Recently Used (LRU), First-In-First-Out (FIFO), and Least Frequently Used (LFU).
      </p>

      <h2 class="sub-title">Message Queues</h2>
      <p class="content">
        Message queues facilitate asynchronous communication between different components of a system, allowing them to exchange data without requiring direct connections. This enhances system resilience and scalability.
      </p>

      <h2 class="sub-title">Communication Protocols in System Design</h2>
      <p class="content">
        Communication protocols define the rules and conventions for data exchange between components. Examples include HTTP for web traffic and MQTT for IoT applications, ensuring reliable and efficient communication.
      </p>

      <h2 class="sub-title">Network Protocols and Proxies in System Design</h2>
      <p class="content">
        Network protocols govern how data is transmitted over networks. Proxies serve as intermediaries, managing requests between clients and servers, enhancing security, load balancing, and data caching.
      </p>

      <h2 class="sub-title">Unified Modeling Language (UML)</h2>
      <p class="content">
        UML is a standardized modeling language used to visualize the design of a system. It provides various diagrams (e.g., class diagrams, sequence diagrams) that help in understanding system architecture and interactions.
      </p>
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=hld1" target="_blank">Understanding High-Level Design (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=hld2" target="_blank">High-Level Design Concepts in Hindi</a></li>
      </ul>
  
      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the concepts discussed:</p>
      <div class="diagram-container">
        <img src="path/to/diagram1.png" alt="Diagram illustrating High-Level Design" />
        <img src="path/to/diagram2.png" alt="Diagram showing the CAP theorem" />
        <img src="path/to/diagram3.png" alt="Diagram of Load Balancing Architecture" />
      </div>
    </div>
</template>
  
<script>
export default {
    name: "HighLevelDesign",
};
</script>
  
<style scoped>
.hld-container {
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