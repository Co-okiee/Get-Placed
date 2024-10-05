<template>
    <div class="lld-container">
      <h1 class="main-title">Low Level Design (LLD)</h1>
      <p class="intro">
        Low Level Design (LLD) refers to the detailed design phase of a system where the components of the system are designed and detailed specifications are provided. It focuses on the implementation of system components, ensuring that all parts work together as intended.
      </p>

      <h2 class="sub-title">What is Low Level Design or LLD</h2>
      <p class="content">
        LLD is a blueprint for the system architecture and describes how the system will be built. It outlines the specifications of the components, including their interactions and data structures.
      </p>

      <h2 class="sub-title">Data Structures and Algorithms for System Design</h2>
      <p class="content">
        Choosing the right data structures and algorithms is critical in LLD as they impact the system's performance and efficiency. Examples include linked lists, trees, hash tables, and algorithms like sorting and searching.
      </p>

      <h2 class="sub-title">Event-Driven Architecture</h2>
      <p class="content">
        Event-driven architecture is a software architecture pattern that uses events to trigger and communicate between decoupled services. This approach enables scalability and flexibility in system design.
      </p>

      <h2 class="sub-title">Difference between Authentication and Authorization</h2>
      <p class="content">
        <strong>Authentication:</strong> Verifies who you are (e.g., logging in with a username and password). <br>
        <strong>Authorization:</strong> Determines what you are allowed to do (e.g., access control to resources).
      </p>

      <h2 class="sub-title">What is API Gateway</h2>
      <p class="content">
        An API Gateway is a server that acts as an intermediary for requests from clients seeking access to services. It handles tasks such as routing, composition, and protocol translation.
      </p>

      <h2 class="sub-title">What is Data Encryption?</h2>
      <p class="content">
        Data encryption is the process of converting plaintext data into a coded format, making it unreadable to unauthorized users. This ensures data security and privacy during transmission and storage.
      </p>

      <h2 class="sub-title">Design Patterns</h2>
      <p class="content">
        Design patterns are standard solutions to common problems in software design. Examples include Singleton, Factory, and Observer patterns, which help in creating scalable and maintainable code.
      </p>

      <h2 class="sub-title">Code Optimization Techniques</h2>
      <p class="content">
        Code optimization techniques aim to improve code efficiency and performance. Techniques include minimizing memory usage, reducing execution time, and avoiding redundant computations.
      </p>

      <h2 class="sub-title">Unit Testing</h2>
      <p class="content">
        Unit testing involves testing individual components of the software to ensure they work as intended. It helps catch bugs early and improves code quality and reliability.
      </p>

      <h2 class="sub-title">Integration Testing</h2>
      <p class="content">
        Integration testing focuses on verifying the interactions between different modules or services. It ensures that integrated components work together correctly.
      </p>

      <h2 class="sub-title">CI/CD: Continuous Integration and Continuous Delivery</h2>
      <p class="content">
        CI/CD is a set of practices that enable development teams to deliver code changes more frequently and reliably. Continuous Integration (CI) involves automatically testing code changes, while Continuous Delivery (CD) ensures that software is always ready for deployment.
      </p>

      <h2 class="sub-title">Introduction to Modularity and Interfaces In System Design</h2>
      <p class="content">
        Modularity refers to designing a system in separate components (modules) that can be independently created and then used in different systems. Interfaces define how these modules interact with each other, enhancing flexibility and maintainability.
      </p>

      <h2 class="sub-title">Data Partitioning Techniques in System Design</h2>
      <p class="content">
        Data partitioning involves dividing a database into smaller, more manageable pieces. Techniques include horizontal partitioning (splitting rows) and vertical partitioning (splitting columns), which improve performance and scalability.
      </p>

      <h2 class="sub-title">Class Diagrams | UML</h2>
      <p class="content">
        Class diagrams in UML (Unified Modeling Language) are used to represent the static structure of a system. They show the system's classes, attributes, methods, and the relationships between the classes.
      </p>

      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=lld1" target="_blank">Introduction to Low Level Design</a></li>
        <li><a href="https://www.youtube.com/watch?v=lld2" target="_blank">Low Level Design Patterns</a></li>
      </ul>

      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the concepts discussed:</p>
      <div class="diagram-container">
        <img src="path/to/diagram1.png" alt="Class Diagram Example" />
        <img src="path/to/diagram2.png" alt="Event-Driven Architecture" />
        <img src="path/to/diagram3.png" alt="CI/CD Pipeline" />
      </div>
    </div>
</template>

<script>
export default {
  name: "LowLevelDesign",
};
</script>

<style scoped>
.lld-container {
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