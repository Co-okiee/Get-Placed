<template>
    <div class="oop-container">
      <h1 class="main-title">Polymorphism</h1>
      <p class="intro">
        Polymorphism is one of the four fundamental principles of Object-Oriented Programming (OOP) in C++. It allows objects to be treated as instances of their parent class, enabling different implementations of a method to be called, depending on the object type.
      </p>

      <h2 class="sub-title">Introduction to Polymorphism</h2>
      <p class="content">
        Polymorphism refers to the ability of a single function or method to operate on different data types or classes. In C++, it is primarily achieved through two types: compile-time and runtime polymorphism.
      </p>
  
      <h2 class="sub-title">Types of Polymorphism</h2>
      <ul class="characteristics-list">
        <li><strong>Compile-time Polymorphism:</strong> Also known as static polymorphism, this is achieved using method overloading and operator overloading.</li>
        <li><strong>Runtime Polymorphism:</strong> Also known as dynamic polymorphism, this is achieved using inheritance and virtual functions.</li>
      </ul>

      <h2 class="sub-title">Compile-Time Polymorphism</h2>
      <p class="content">
        Compile-time polymorphism in C++ occurs when the method that will be invoked is determined at compile time. It is mainly achieved through function overloading and operator overloading.
      </p>
      <div class="example-container">
        <h3 class="example-title">Example: Function Overloading</h3>
        <pre>
          <code class="cpp-code">
          #include &lt;iostream&gt;
          using namespace std;
          class Print {
          public:
              void display(int i) {
                  cout &lt;&lt; "Integer: " &lt;&lt; i &lt;&lt; endl;
              }
              void display(double d) {
                  cout &lt;&lt; "Double: " &lt;&lt; d &lt;&lt; endl;
              }
          };
          int main() {
              Print obj;
              obj.display(5);      // Calls the integer version
              obj.display(3.14);   // Calls the double version
              return 0;
          }
          </code>
        </pre>
      </div>

      <h2 class="sub-title">Runtime Polymorphism</h2>
      <p class="content">
        Runtime polymorphism is achieved using inheritance and virtual functions. The function that will be invoked is determined at runtime based on the type of object being referenced, typically using pointers or references to base class objects.
      </p>
      <div class="example-container">
        <h3 class="example-title">Example: Virtual Functions</h3>
        <pre>
          <code class="cpp-code">
          #include &lt;iostream&gt;
          using namespace std;

          class Base {
          public:
              virtual void show() {
                  cout &lt;&lt; "Base class" &lt;&lt; endl;
              }
          };

          class Derived : public Base {
          public:
              void show() {
                  cout &lt;&lt; "Derived class" &lt;&lt; endl;
              }
          };

          int main() {
              Base *bptr;
              Derived d;
              bptr = &d;
              bptr-&gt;show();  // Calls Derived class version
              return 0;
          }
          </code>
        </pre>
      </div>

      <h2 class="sub-title">Key Differences Between Compile-Time and Runtime Polymorphism</h2>
      <ul class="characteristics-list">
        <li><strong>Compile-Time Polymorphism:</strong> Method is determined during compilation (e.g., function overloading).</li>
        <li><strong>Runtime Polymorphism:</strong> Method is determined at runtime using pointers or references (e.g., virtual functions).</li>
      </ul>

      <h2 class="sub-title">Advantages of Polymorphism</h2>
      <p class="content">
        Polymorphism increases the flexibility and maintainability of code by allowing different objects to be treated as instances of the parent class. This allows for the same function to be called in different ways, depending on the object type.
      </p>

      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=cpp1" target="_blank">Introduction to Polymorphism (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=cpp2" target="_blank">Polymorphism in Hindi</a></li>
      </ul>

      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the concepts discussed:</p>
      <div class="diagram-container">
        <img src="path/to/diagram1.png" alt="Diagram illustrating compile-time and runtime polymorphism" />
        <img src="path/to/diagram2.png" alt="Diagram showing virtual function mechanism" />
      </div>
    </div>
</template>

<script>
export default {
  name: "PolymorphismOOP",
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

.example-container {
  background-color: #1e1e1e;
  padding: 15px;
  border-radius: 5px;
  margin: 20px 0;
}

.cpp-code {
  color: #00ffcc;
  font-size: 1.1em;
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