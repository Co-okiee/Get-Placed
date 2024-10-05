<template>
    <div class="db-container">
      <h1 class="main-title">Databases in Designing Systems</h1>
      <p class="intro">
        Databases are crucial components in system design, allowing for the structured storage, retrieval, and management of data. They can be classified into various types, such as SQL and NoSQL, each catering to different application needs.
      </p>

      <h2 class="sub-title">Which Database to Choose While Designing a System – SQL or NoSQL</h2>
      <p class="content">
        Choosing between SQL (relational) and NoSQL (non-relational) databases depends on the application requirements. SQL databases are suited for complex queries and transactions, while NoSQL databases excel in scalability and flexibility for unstructured data.
      </p>
      
      <h2 class="sub-title">File and Database Storage Systems in System Design</h2>
      <p class="content">
        File storage systems allow for unstructured data storage, while database storage systems offer structured data management, enabling efficient data retrieval, indexing, and querying capabilities.
      </p>
  
      <h2 class="sub-title">Database Replication in System Design</h2>
      <p class="content">
        Database replication involves copying and maintaining database objects in multiple databases to enhance data availability and reliability, ensuring continuous access even in case of failures.
      </p>
      
      <h2 class="sub-title">Block, Object, and File Storage</h2>
      <p class="content">
        - <strong>Block Storage:</strong> Divides data into blocks and stores it in separate locations, suitable for high-performance applications.<br>
        - <strong>Object Storage:</strong> Manages data as objects with unique identifiers, enabling scalability and metadata management.<br>
        - <strong>File Storage:</strong> Organizes data in a hierarchical file and folder structure, making it easy to access and manage.
      </p>
  
      <h2 class="sub-title">Normalization Process in DBMS</h2>
      <p class="content">
        Normalization is the process of organizing data in a database to reduce redundancy and improve data integrity. It involves dividing large tables into smaller, related tables and defining relationships between them.
      </p>
      
      <h2 class="sub-title">Denormalization in Databases</h2>
      <p class="content">
        Denormalization is the intentional process of combining tables to improve read performance at the cost of additional storage and potential data redundancy. It is often used in read-heavy applications where speed is critical.
      </p>
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=db1" target="_blank">Understanding SQL vs NoSQL Databases</a></li>
        <li><a href="https://www.youtube.com/watch?v=db2" target="_blank">Database Replication Explained</a></li>
      </ul>
  
      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the concepts discussed:</p>
      <div class="diagram-container">
        <img src="path/to/diagram1.png" alt="Diagram showing SQL vs NoSQL databases" />
        <img src="path/to/diagram2.png" alt="Diagram illustrating database replication" />
        <img src="path/to/diagram3.png" alt="Normalization process in DBMS" />
      </div>
    </div>
</template>
  
<script>
export default {
    name: "DatabasesInDesigningSystems",
};
</script>
  
<style scoped>
.db-container {
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