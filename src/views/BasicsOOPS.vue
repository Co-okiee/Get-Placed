<template>
    <div class="cpp-oops-container">
      <h1 class="main-title">Object-Oriented Programming in C++</h1>
      <p class="intro">
        Object-Oriented Programming (OOP) in C++ is a programming paradigm that uses objects and classes to structure software into reusable and efficient components. It promotes concepts like inheritance, polymorphism, and encapsulation to model real-world scenarios.
      </p>
  
      <h2 class="sub-title">Basics of OOP in C++</h2>
      <p class="content">
        OOP revolves around the idea of creating objects which represent real-world entities. The key principles of OOP include:
      </p>
      <ul class="characteristics-list">
        <li><strong>Encapsulation:</strong> Bundling of data (variables) and methods (functions) that operate on the data into a single unit or class.</li>
        <li><strong>Inheritance:</strong> A class can inherit properties and behavior (methods) from another class.</li>
        <li><strong>Polymorphism:</strong> The ability to redefine methods for different object types.</li>
        <li><strong>Abstraction:</strong> Hiding the implementation details and exposing only essential features.</li>
      </ul>
  
      <h2 class="sub-title">Classes in C++</h2>
      <p class="content">
        A class is a blueprint for creating objects. It defines properties (attributes) and methods (functions) that the objects created from the class will have. For example:
      </p>
      <pre class="code-example">
        <code>
          class Car {
            public:
              string brand;
              int year;
              void start() {
                cout &lt;&lt; "The car has started!" &lt;&lt; endl;
              }
          };
        </code>
      </pre>
      <p class="content">
        In this example, the class Car defines two attributes: brand and year, and a method start(). These attributes and methods can be accessed by the objects created from this class.
      </p>
  
      <h2 class="sub-title">Objects in C++</h2>
      <p class="content">
        An object is an instance of a class. Once a class is defined, we can create objects to represent specific real-world entities. For example:
      </p>
      <pre class="code-example">
        <code>
          int main() {
            Car myCar; // Create an object of Car
            myCar.brand = "Toyota";
            myCar.year = 2020;
            myCar.start(); // Call the method
            return 0;
          }
        </code>
      </pre>
      <p class="content">
        In this example, myCar is an object of the Car class. It has its own brand and year properties, and it can call the start() method.
      </p>
  
      <h2 class="sub-title">Inheritance in C++</h2>
      <p class="content">
        Inheritance allows a class to derive properties and methods from another class. For example, a SportsCar class could inherit from the Car class:
      </p>
      <pre class="code-example">
        <code>
          class SportsCar : public Car {
            public:
              bool turbo;
              void showDetails() {
                cout &lt;&lt; "Brand: " &lt;&lt; brand &lt;&lt; ", Year: " &lt;&lt;
                year &lt;&lt; ", Turbo: " &lt;&lt; (turbo ? "Yes" : "No") &lt;&lt; endl;
              }
          };
        </code>
      </pre>
  
      <h2 class="sub-title">Polymorphism in C++</h2>
      <p class="content">
        Polymorphism allows objects of different classes to be treated as objects of a common parent class. It can be achieved through function overloading and overriding. Example of function overriding:
      </p>
      <pre class="code-example">
        <code>
          class Animal {
            public:
              virtual void sound() {
                cout &lt;&lt; "This is an animal sound." &lt;&lt; endl;
              }
          };
  
          class Dog : public Animal {
            public:
              void sound() override {
                cout &lt;&lt; "Bark!" &lt;&lt; endl;
              }
          };
        </code>
      </pre>
  
      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate OOP concepts in C++:</p>
      <div class="diagram-container">
        <img src="path/to/class_diagram.png" alt="Class Diagram in OOP" />
        <img src="path/to/inheritance_diagram.png" alt="Inheritance Example" />
        <img src="path/to/polymorphism_diagram.png" alt="Polymorphism in Action" />
      </div>
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=cpp_oops1" target="_blank">Introduction to OOP in C++</a></li>
        <li><a href="https://www.youtube.com/watch?v=cpp_oops2" target="_blank">Classes and Objects in C++</a></li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "CppOops",
  };
  </script>
  
  <style scoped>
  .cpp-oops-container {
    max-width: 900px;
    margin: 20px auto;
    padding: 20px;
    border-radius: 10px;
    background-color: #1c1c1c;
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
    border: 2px solid #e0ce46;
  }
  
  pre.code-example {
    background-color: #333;
    padding: 15px;
    color: #fff;
    font-family: 'Courier New', monospace;
    font-size: 1em;
    border-radius: 5px;
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