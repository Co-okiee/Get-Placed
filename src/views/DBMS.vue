<template>
    <div class="dbms-container">
      <h1 class="main-title">Database Management Systems (DBMS)</h1>
      <p class="intro">
        A Database Management System (DBMS) is a software suite designed to store, retrieve, manage, and manipulate data efficiently. It provides an interface for users and applications to interact with databases while ensuring data security, integrity, and consistency. DBMS supports various operations, including data storage, querying, updating, and administration of databases.
      </p>
  
      <h2 class="sub-title">Introduction</h2>
      <p class="content">
        A DBMS acts as an intermediary between end-users and the database. It is responsible for data retrieval, transaction processing, ensuring that data remains consistent and organized, and protecting it from unauthorized access. DBMS systems are crucial in a wide range of applications such as banking, airlines, universities, and more.
      </p>
  
      <h2 class="sub-title">Entity Relationship Model</h2>
      <p class="content">
        The Entity-Relationship (ER) Model is a high-level data model that defines the data elements (entities) and relationships among them. It is used to visually represent the database's logical structure. Entities can be things, persons, or concepts, and relationships define how entities are linked together.
      </p>
      <div class="diagram-container">
        <img src="path/to/er_diagram.png" alt="ER Diagram example showing entities and their relationships" />
        <p class="diagram-caption">Example of an ER diagram showing entities like Student, Course, and Instructor with relationships like enrollment and assignment.</p>
      </div>
  
      <h2 class="sub-title">Relational Model</h2>
      <p class="content">
        The relational model represents data in the form of tables (also called relations). Each table consists of rows (records or tuples) and columns (fields or attributes). In this model, every row in the table is a unique entry and is identified by a primary key. Relationships between tables are established using foreign keys.
      </p>
      <div class="diagram-container">
        <img src="path/to/relational_model.png" alt="Relational Model Diagram" />
        <p class="diagram-caption">A Relational Model representing a 'Student' and 'Course' table, where 'Student_ID' acts as a primary key in the Student table and a foreign key in the Course table.</p>
      </div>
  
      <h2 class="sub-title">Relational Algebra</h2>
      <p class="content">
        Relational Algebra is a procedural query language that works on the relational model. It provides a set of operations such as selection, projection, union, set difference, and join, which are used to query and manipulate data in relational databases. For example, the 'selection' operator filters rows, while the 'projection' operator selects specific columns.
      </p>
      <div class="diagram-container">
        <img src="path/to/relational_algebra_operations.png" alt="Relational Algebra operations" />
        <p class="diagram-caption">Various relational algebra operations like selection (σ), projection (π), and join (⋈) used to manipulate relations in a database.</p>
      </div>
  
      <h2 class="sub-title">Functional Dependencies</h2>
      <p class="content">
        A functional dependency is a relationship between two attributes in a relation. It specifies that the value of one attribute is determined by the value of another attribute. For example, in a 'Student' table, the 'Roll Number' can uniquely identify a 'Student Name.' Functional dependencies are crucial in database normalization to eliminate redundancy.
      </p>
  
      <h2 class="sub-title">Normalization</h2>
      <p class="content">
        Normalization is the process of organizing data to reduce redundancy and improve data integrity. The most common normal forms include 1NF (First Normal Form), 2NF (Second Normal Form), 3NF (Third Normal Form), and BCNF (Boyce-Codd Normal Form). Each step in normalization ensures that data is stored logically, minimizing duplication and dependency issues.
      </p>
      <div class="diagram-container">
        <img src="path/to/normalization.png" alt="Normalization process example" />
        <p class="diagram-caption">An example of Normalization from 1NF to 3NF, showing how tables are restructured to minimize redundancy and dependency.</p>
      </div>
  
      <h2 class="sub-title">Transactions and Concurrency Control</h2>
      <p class="content">
        A transaction is a sequence of operations performed as a single logical unit of work. For a transaction to be reliable, it must satisfy ACID properties: Atomicity, Consistency, Isolation, and Durability. Concurrency control mechanisms like locking, timestamp ordering, and multiversion concurrency control (MVCC) ensure that transactions are executed without conflicting with each other, maintaining database integrity.
      </p>
  
      <h2 class="sub-title">Indexing, B and B+ Trees</h2>
      <p class="content">
        Indexing is used to speed up data retrieval by reducing the number of disk accesses. B-trees and B+ trees are popular data structures used in databases to maintain sorted data and allow for efficient insertion, deletion, and searching. B+ trees are a variation of B-trees where all records are stored at the leaf level, making it highly efficient for range queries.
      </p>
      <div class="diagram-container">
        <img src="path/to/b_tree_diagram.png" alt="B+ Tree diagram" />
        <p class="diagram-caption">Example of a B+ Tree data structure used for indexing in databases, which helps in faster data retrieval and range queries.</p>
      </div>
  
      <h2 class="sub-title">File Organization</h2>
      <p class="content">
        File organization refers to how data is stored in the database at the physical level. Common types of file organization include heap files (unordered), sequential files (ordered), and indexed files. Each file organization type has different characteristics regarding access speed and storage efficiency.
      </p>
  
      <h2 class="sub-title">Advanced Topics</h2>
      <p class="content">
        Some advanced topics in DBMS include distributed databases, where data is stored across multiple locations, and NoSQL databases, which are used for handling unstructured or semi-structured data. Other topics include database security, object-oriented databases, and big data systems, which deal with massive amounts of data and complex data models.
      </p>
  
  
      <h2 class="sub-title">SQL Tutorial</h2>
      <ul class="characteristics-list">
        <li><a href="https://www.sqltutorial.org/" target="_blank">SQL Tutorial</a></li>
        <li><a href="https://www.w3schools.com/sql/" target="_blank">W3Schools SQL Tutorial</a></li>
        <li><a href="https://www.codecademy.com/learn/learn-sql" target="_blank">Codecademy SQL Course</a></li>
      </ul>
  
  
      <h2 class="sub-title">Advantages of DBMS</h2>
      <ul class="characteristics-list">
        <li>Reduces data redundancy and inconsistency.</li>
        <li>Enhances data security through access controls and encryption.</li>
        <li>Allows concurrent access to data by multiple users.</li>
        <li>Ensures data integrity by enforcing data constraints.</li>
      </ul>
  
      <h2 class="sub-title">Disadvantages of DBMS</h2>
      <ul class="characteristics-list">
        <li>Complexity in database design and maintenance.</li>
        <li>High initial investment for setting up DBMS software and hardware.</li>
        <li>Requires skilled personnel to manage and maintain the system.</li>
        <li>Performance overhead due to abstraction layers in DBMS.</li>
      </ul>
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=dbms1" target="_blank">Introduction to DBMS (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=dbms2" target="_blank">DBMS Overview in Hindi</a></li>
        <li><a href="https://www.youtube.com/watch?v=dbms3" target="_blank">Advanced DBMS Concepts</a></li>
      </ul>
  
      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the key DBMS concepts discussed:</p>
      <div class="diagram-container">
        <img src="path/to/er_diagram.png" alt="ER Diagram" />
        <img src="path/to/b_tree_diagram.png" alt="B+ Tree Diagram" />
        <img src="path/to/normalization.png" alt="Normalization process" />
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "DatabaseManagementSystem",
  };
  </script>
  
  <style scoped>
  .dbms-container {
    max-width: 1000px;
    margin: 20px auto;
    padding: 20px;
    border-radius: 10px;
    background-color: #1e1e1e;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.8);
    font-family: 'Roboto', sans-serif;
    color: #f5f5f5;
    line-height: 1.8;
  }
  
  .main-title {
    font-size: 3em;
    color: #ffcc00;
    text-align: center;
    margin-bottom: 30px;
  }
  
  .sub-title {
    font-size: 2.4em;
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
    border: 2px solid #e0ce46;
  }
  
  p.diagram-caption {
    font-size: 0.9em;
    color: #aaaaaa;
    margin-top: -10px;
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