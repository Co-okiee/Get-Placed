<template>
    <div class="os-container">
      <h1 class="main-title">Abstraction</h1>
      <p class="intro">
        Abstraction in Object-Oriented Programming (OOP) is the concept of hiding the complex implementation details and exposing only the essential features of an object. It helps in reducing the complexity of the system and enhances code readability and maintenance.
      </p>

      <h2 class="sub-title">Introduction to Abstraction in OOP</h2>
      <p class="content">
        Abstraction is a fundamental principle of OOP, which allows you to represent real-world complexities in a simplified form by only showing the necessary data and hiding the implementation details. In C++, this is usually done using classes and abstract classes.
      </p>
  
      <h2 class="sub-title">Levels of Abstraction in C++</h2>
      <ul class="characteristics-list">
        <li><strong>High-Level Abstraction:</strong> Focuses on the "what" a system does, ignoring the details of "how" it is done. This is often represented by abstract classes or interfaces.</li>
        <li><strong>Low-Level Abstraction:</strong> Involves more specific and detailed information about how tasks are accomplished, often hidden from the user.</li>
      </ul>
  
      <h2 class="sub-title">Purpose of Abstraction</h2>
      <p class="content">
        The main goal of abstraction is to manage complexity by breaking down a system into simpler parts. It allows developers to focus on the interactions between objects rather than their internal implementation.
      </p>
  
      <h2 class="sub-title">Real-World Example of Abstraction</h2>
      <p class="content">
        Consider a car. You only need to know how to drive a car (high-level abstraction) without worrying about how the engine works internally (low-level abstraction). Similarly, in C++, classes hide internal details and show only the necessary functionalities.
      </p>

      <h2 class="sub-title">Implementation of Abstraction in C++</h2>
      <p class="content">
        In C++, abstraction is implemented using abstract classes and interfaces. An abstract class contains at least one pure virtual function, which means the function has no implementation and must be implemented in derived classes.
      </p>

      <h2 class="sub-title">Example of Abstraction in C++</h2>
      <p class="content">
        Below is an example of how abstraction can be implemented in C++ using an abstract class:
      </p>

      <pre class="code-snippet">
<code>
class Vehicle {
  public:
    virtual void start() = 0;  // Pure virtual function
};

class Car : public Vehicle {
  public:
    void start() {
      cout << "Car started." << endl;
    }
};

int main() {
  Vehicle* v = new Car();
  v->start();
  delete v;
}
</code>
      </pre>
  
      <h2 class="sub-title">Difference between Abstraction and Encapsulation</h2>
      <ul class="characteristics-list">
        <li><strong>Abstraction:</strong> Focuses on hiding complexity by showing only the essential details of an object. For example, only showing the start() function of a Car class without exposing how it works internally.</li>
        <li><strong>Encapsulation:</strong> Refers to bundling data and methods together inside a class, and controlling access to that data through access modifiers like private, protected, and public.</li>
      </ul>

      <h2 class="sub-title">Benefits of Abstraction in OOP</h2>
      <p class="content">
        Abstraction in C++ offers several benefits:
        <ul class="characteristics-list">
          <li>Improves code maintainability by separating the interface from the implementation.</li>
          <li>Increases code reusability since abstract classes can be extended by multiple derived classes.</li>
          <li>Makes the system more modular, allowing for easier updates and modifications.</li>
        </ul>
      </p>
  
      <h2 class="sub-title">Difference between Abstract Class and Interface</h2>
      <ul class="characteristics-list">
        <li><strong>Abstract Class:</strong> Can have both implemented and pure virtual functions. It can also have member variables.</li>
        <li><strong>Interface (Pure Abstract Class):</strong> Contains only pure virtual functions and no member variables.</li>
      </ul>
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=cpp-abstraction1" target="_blank">Abstraction in C++ (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=cpp-abstraction2" target="_blank">Object-Oriented Programming in C++ (Hindi)</a></li>
      </ul>
  
      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the concepts discussed:</p>
      <div class="diagram-container">
        <img src="path/to/diagram1.png" alt="Diagram illustrating abstraction layers in a system" />
        <img src="path/to/diagram2.png" alt="Diagram showing the difference between abstraction and encapsulation" />
        <img src="path/to/diagram3.png" alt="Hierarchy of classes with an abstract class at the top" />
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "AbstractionInOOP",
  };
  </script>
  
  <style scoped>
  .os-container {
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