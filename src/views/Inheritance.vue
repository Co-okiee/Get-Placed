<template>
    <div class="os-container">
      <h1 class="main-title">Inheritance</h1>
      <p class="intro">
        Inheritance is one of the core concepts of Object-Oriented Programming (OOP) in C++. It allows a class (called derived class) to inherit properties and behaviors (methods) from another class (called base class). This promotes code reusability and hierarchical classification.
      </p>
  
      <h2 class="sub-title">Introduction to Inheritance</h2>
      <p class="content">
        Inheritance is a mechanism in C++ where a new class is derived from an existing class. The derived class inherits the attributes and methods of the base class, and it can also have additional features.
      </p>
  
      <h2 class="sub-title">Types of Inheritance</h2>
      <ul class="characteristics-list">
        <li><strong>Single Inheritance:</strong> A class is derived from one base class.</li>
        <li><strong>Multiple Inheritance:</strong> A class is derived from more than one base class.</li>
        <li><strong>Multilevel Inheritance:</strong> A class is derived from a class, which is also derived from another class, forming a chain.</li>
        <li><strong>Hierarchical Inheritance:</strong> Multiple derived classes inherit from a single base class.</li>
        <li><strong>Hybrid Inheritance:</strong> A combination of multiple and hierarchical inheritance.</li>
      </ul>
  
      <h2 class="sub-title">Functions of Inheritance</h2>
      <p class="content">
        Inheritance helps in the following:
        <ul>
          <li>Code Reusability: Allows reuse of code written in the base class without rewriting it.</li>
          <li>Extensibility: Extends the base class by adding new properties and methods in the derived class.</li>
          <li>Maintainability: Easier to manage and update the code since changes made to the base class are automatically inherited by derived classes.</li>
        </ul>
      </p>
  
      <h2 class="sub-title">Real-Time Example of Inheritance</h2>
      <p class="content">
        Consider a class <code>Animal</code> with attributes like <code>name</code> and <code>age</code>. We can derive classes such as <code>Dog</code> and <code>Cat</code> from the <code>Animal</code> class. Both <code>Dog</code> and <code>Cat</code> inherit the properties of <code>Animal</code>, and can also have their specific methods like <code>bark()</code> and <code>meow()</code>, respectively.
      </p>
  
      <h2 class="sub-title">Difference between Single and Multiple Inheritance</h2>
      <ul class="characteristics-list">
        <li><strong>Single Inheritance:</strong> Derived class inherits from only one base class.</li>
        <li><strong>Multiple Inheritance:</strong> Derived class inherits from more than one base class, combining features from all base classes.</li>
      </ul>
  
      <h2 class="sub-title">Base Class and Derived Class Relationship</h2>
      <p class="content">
        The base class provides the foundation for inheritance, defining the attributes and methods that are shared with the derived class. The derived class can inherit, extend, or override these features as needed.
      </p>
  
      <h2 class="sub-title">Access Specifiers in Inheritance</h2>
      <p class="content">
        The accessibility of inherited properties is controlled using access specifiers:
        <ul>
          <li><strong>Public Inheritance:</strong> Public members of the base class remain public in the derived class.</li>
          <li><strong>Protected Inheritance:</strong> Public and protected members of the base class become protected in the derived class.</li>
          <li><strong>Private Inheritance:</strong> Public and protected members of the base class become private in the derived class.</li>
        </ul>
      </p>
  
      <h2 class="sub-title">Example: Inheritance in C++</h2>
      <p class="content">
        Here's an example demonstrating single inheritance in C++:
      </p>
      <pre class="content">
        <code>
          class Animal {
          public:
              string name;
              void speak() {
                  cout << "Animal speaks!" << endl;
              }
          };
  
          class Dog : public Animal {
          public:
              void bark() {
                  cout << "Dog barks!" << endl;
              }
          };
  
          int main() {
              Dog dog;
              dog.name = "Buddy";
              dog.speak();  // Inherited method from Animal
              dog.bark();   // Dog's specific method
              return 0;
          }
        </code>
      </pre>
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=in1" target="_blank">Inheritance in C++ (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=in2" target="_blank">Object-Oriented Programming in C++ (Hindi)</a></li>
      </ul>
  
      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the concept of inheritance:</p>
      <div class="diagram-container">
        <img src="path/to/inheritance_diagram1.png" alt="Single Inheritance Example" />
        <img src="path/to/inheritance_diagram2.png" alt="Multiple Inheritance Example" />
        <img src="path/to/inheritance_diagram3.png" alt="Base and Derived Class Relationship" />
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "InheritanceInCpp",
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