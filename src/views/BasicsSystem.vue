<template>
  <div class="sd-container">
    <h1 class="main-title">Basics of System Design</h1>
    <p class="intro">
      System design is the process of defining the architecture, components, modules, interfaces, and data for a system to satisfy specified requirements. It is crucial in developing scalable and efficient software systems.
    </p>

    <h2 class="sub-title">What is System Design?</h2>
    <p class="content">
      System design involves creating a blueprint for the system that outlines its structure, functionality, and how components interact with each other. It aims to meet user requirements while ensuring performance, reliability, and scalability.
    </p>

    <h2 class="sub-title">Functional vs Non-Functional Requirements</h2>
    <ul class="characteristics-list">
      <li><strong>Functional Requirements:</strong> Define what the system should do, specifying tasks, services, and functions.</li>
      <li><strong>Non-Functional Requirements:</strong> Describe how the system performs its functions, including performance metrics, usability, reliability, and security.</li>
    </ul>

    <h2 class="sub-title">What are the Components of System Design?</h2>
    <p class="content">
      Key components include:
    </p>
    <ul>
      <li><strong>Architecture:</strong> The overall structure of the system.</li>
      <li><strong>Modules:</strong> Independent components that encapsulate functionality.</li>
      <li><strong>Interfaces:</strong> Points of interaction between different modules.</li>
      <li><strong>Data Flow:</strong> The movement of data between modules.</li>
    </ul>

    <h2 class="sub-title">System Design Life Cycle | SDLC (Design)</h2>
    <p class="content">
      The SDLC for system design includes phases such as:
    </p>
    <ul>
      <li><strong>Requirement Analysis:</strong> Gathering and analyzing requirements.</li>
      <li><strong>System Design:</strong> Creating the system architecture and interfaces.</li>
      <li><strong>Implementation:</strong> Developing and integrating components.</li>
      <li><strong>Testing:</strong> Validating functionality and performance.</li>
      <li><strong>Deployment:</strong> Releasing the system to users.</li>
    </ul>

    <h2 class="sub-title">System Design Strategy</h2>
    <p class="content">
      Effective system design strategies include:
    </p>
    <ul>
      <li><strong>Top-Down Design:</strong> Starting with the high-level overview and breaking it down into sub-systems.</li>
      <li><strong>Bottom-Up Design:</strong> Building smaller modules first and integrating them into a larger system.</li>
      <li><strong>Modular Design:</strong> Creating independent, interchangeable modules to simplify development and maintenance.</li>
    </ul>

    <h2 class="sub-title">Database Sharding – System Design Interview Concept</h2>
      <p class="content">
        Database sharding involves partitioning data across multiple databases to improve performance and scalability. Each shard contains a subset of the total data, allowing the system to handle larger volumes of data more efficiently.
      </p>
  
      <h2 class="sub-title">System Design – Horizontal and Vertical Scaling</h2>
      <p class="content">
        <strong>Horizontal Scaling:</strong> Adding more machines to handle increased load (scaling out). <br>
        <strong>Vertical Scaling:</strong> Adding more resources (CPU, RAM) to a single machine (scaling up). <br>
        Both methods have their advantages and challenges in terms of cost, performance, and system architecture.
      </p>
  
      <h2 class="sub-title">Load Balancer in System Design</h2>
      <p class="content">
        A load balancer distributes incoming network traffic across multiple servers to ensure no single server becomes overwhelmed. This enhances reliability, improves response times, and provides redundancy in case of server failure.
      </p>
  
      <h2 class="sub-title">Routing Requests through Load Balancer</h2>
      <p class="content">
        Requests can be routed through a load balancer using various algorithms, such as round-robin, least connections, and IP hash. These methods determine how requests are distributed among the available servers, optimizing resource utilization.
      </p>
      
      <h2 class="sub-title">Latency and Throughput in System Design</h2>
      <p class="content">
        <strong>Latency:</strong> The time it takes for a request to travel from the client to the server and back. <br>
        <strong>Throughput:</strong> The number of requests processed by the system in a given time frame. Balancing latency and throughput is essential for performance optimization.
      </p>
      
      <h2 class="sub-title">Object-Oriented Analysis and Design</h2>
      <p class="content">
        Object-oriented analysis and design (OOAD) focuses on modeling a system using objects, which encapsulate data and behavior. It promotes reusability, scalability, and maintainability through the principles of encapsulation, inheritance, and polymorphism.
      </p>
      
      <h2 class="sub-title">Difference between Structured and Object-Oriented Analysis</h2>
      <p class="content">
        <strong>Structured Analysis:</strong> Focuses on processes and data flow, emphasizing functional requirements. <br>
        <strong>Object-Oriented Analysis:</strong> Centers on identifying objects and their interactions, prioritizing real-world modeling and data encapsulation.
      </p>
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=sd1" target="_blank">Introduction to System Design (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=sd2" target="_blank">System Design Fundamentals in Hindi</a></li>
      </ul>
  
      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the concepts discussed:</p>
      <div class="diagram-container">
        <img src="path/to/system-design-overview.png" alt="System Design Overview" />
        <img src="path/to/load-balancer-diagram.png" alt="Load Balancer Diagram" />
        <img src="path/to/scaling-diagram.png" alt="Scaling Diagram" />
      </div>
    </div>
</template>

<script>
export default {
  name: "BasicsOfSystemDesign",
};
</script>

<style scoped>
.sd-container {
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