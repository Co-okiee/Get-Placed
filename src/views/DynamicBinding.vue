<template>
    <div class="oop-container">
      <h1 class="main-title">Dynamic Binding and Message Passing</h1>
      <p class="intro">
        In Object-Oriented Programming (OOP), dynamic binding and message passing are two important concepts that enhance flexibility and reusability of code. Dynamic binding allows method calls to be resolved at runtime, while message passing enables communication between objects.
      </p>

      <h2 class="sub-title">Introduction to Dynamic Binding</h2>
      <p class="content">
        Dynamic binding, also known as late binding, occurs when a method call is not resolved until runtime. It is typically achieved through the use of pointers or references to base class objects and is fundamental to polymorphism in C++.
      </p>
  
      <h2 class="sub-title">Key Characteristics of Dynamic Binding</h2>
      <ul class="characteristics-list">
        <li><strong>Late Binding:</strong> The function call is resolved at runtime rather than compile-time.</li>
        <li><strong>Polymorphism:</strong> Dynamic binding is closely associated with runtime polymorphism, where a base class reference or pointer can refer to objects of derived classes.</li>
        <li><strong>Virtual Functions:</strong> In C++, dynamic binding is implemented using virtual functions.</li>
      </ul>
  
      <h2 class="sub-title">Example of Dynamic Binding in C++</h2>
      <p class="content">
        Here is an example demonstrating dynamic binding using virtual functions in C++:
      </p>
      <pre class="code-block">
        <code>
          class Base {
          public:
              virtual void show() {
                  cout << "Base class show function" << endl;
              }
          };

          class Derived : public Base {
          public:
              void show() override {
                  cout << "Derived class show function" << endl;
              }
          };

          int main() {
              Base *ptr = new Derived();
              ptr->show(); // Calls Derived class show function at runtime
              delete ptr;
              return 0;
          }
        </code>
      </pre>

      <h2 class="sub-title">Introduction to Message Passing</h2>
      <p class="content">
        Message passing is a mechanism in OOP that allows objects to communicate with each other by sending and receiving messages. It supports encapsulation and data abstraction by making interactions between objects happen through well-defined interfaces.
      </p>

      <h2 class="sub-title">Characteristics of Message Passing</h2>
      <ul class="characteristics-list">
        <li><strong>Object Communication:</strong> Objects communicate by invoking methods on other objects, sending data and receiving responses.</li>
        <li><strong>Encapsulation:</strong> Message passing hides the internal details of the objects, focusing on the interaction interface.</li>
        <li><strong>Modularity:</strong> Message passing allows independent development of objects, as they only need to know the interface to communicate.</li>
      </ul>

      <h2 class="sub-title">Example of Message Passing in C++</h2>
      <p class="content">
        Here is an example that demonstrates message passing between two objects:
      </p>
      <pre class="code-block">
        <code>
          class A {
          public:
              void sendMessage() {
                  cout << "Message from class A" << endl;
              }
          };

          class B {
          public:
              void receiveMessage(A &obj) {
                  obj.sendMessage(); // Object B communicates with object A
              }
          };

          int main() {
              A objA;
              B objB;
              objB.receiveMessage(objA); // B sends message to A
              return 0;
          }
        </code>
      </pre>

      <h2 class="sub-title">Difference between Static and Dynamic Binding</h2>
      <ul class="characteristics-list">
        <li><strong>Static Binding:</strong> Function call is resolved at compile time.</li>
        <li><strong>Dynamic Binding:</strong> Function call is resolved at runtime, enabling polymorphism.</li>
      </ul>
  
      <h2 class="sub-title">Advantages of Dynamic Binding and Message Passing</h2>
      <p class="content">
        Dynamic binding increases flexibility in code by allowing runtime decisions, while message passing ensures a clear communication mechanism between objects. Both enhance modularity, encapsulation, and code reusability in OOP.
      </p>
  
      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the concepts discussed:</p>
      <div class="diagram-container">
        <img src="path/to/dynamic_binding_diagram.png" alt="Diagram illustrating dynamic binding" />
        <img src="path/to/message_passing_diagram.png" alt="Diagram showing message passing between objects" />
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "OOPConcepts",
  };
  </script>
  
  <style scoped>
  .oop-container {
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
  
  .code-block {
    background-color: #1e1e1e;
    padding: 15px;
    border-radius: 5px;
    font-family: monospace;
    color: #d1d1d1;
    margin-bottom: 20px;
    overflow-x: auto;
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