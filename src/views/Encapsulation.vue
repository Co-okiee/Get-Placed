<template>
    <div class="oos-container">
      <h1 class="main-title">Encapsulation</h1>
      <p class="intro">
        Encapsulation is one of the fundamental concepts in Object-Oriented Programming (OOP), which involves bundling the data (variables) and the methods (functions) that operate on the data into a single unit or class. In C++, encapsulation is used to restrict direct access to some of an object's components and can be achieved using access specifiers.
      </p>

      <h2 class="sub-title">Introduction to Encapsulation</h2>
      <p class="content">
        Encapsulation is the process of keeping the internal details (data members) of a class hidden from outside interference or misuse. The data is accessible only through public methods, which help in maintaining the integrity of the object.
      </p>

      <h2 class="sub-title">Encapsulation in C++</h2>
      <ul class="characteristics-list">
        <li><strong>Private Members:</strong> Data and methods declared under private cannot be accessed or modified directly from outside the class.</li>
        <li><strong>Public Methods:</strong> Public methods provide a controlled interface to interact with private members, ensuring data integrity and security.</li>
        <li><strong>Access Control:</strong> C++ uses access specifiers (private, public, protected) to enforce encapsulation.</li>
      </ul>

      <h2 class="sub-title">Classes and Objects</h2>
      <p class="content">
        In C++, encapsulation is achieved through classes, where data members (attributes) are kept private, and member functions (methods) are public, controlling access to the private data.
      </p>
  
      <h2 class="sub-title">Example of Encapsulation in C++</h2>
      <p class="content">
        Below is an example of how encapsulation works in C++. The class <code>Student</code> contains private data members, and public methods provide controlled access to these members.
      </p>

      <pre class="code-snippet">
<code>
class Student {
private:
    string name;
    int age;

public:
    void setName(string studentName) {
        name = studentName;
    }

    void setAge(int studentAge) {
        if (studentAge > 0) {
            age = studentAge;
        }
    }

    string getName() {
        return name;
    }

    int getAge() {
        return age;
    }
};

int main() {
    Student s1;
    s1.setName("Alice");
    s1.setAge(20);
    cout << s1.getName() << " is " << s1.getAge() << " years old." << endl;
    return 0;
}
</code>
      </pre>

      <h2 class="sub-title">Benefits of Encapsulation</h2>
      <ul class="characteristics-list">
        <li><strong>Data Hiding:</strong> Encapsulation provides data hiding, meaning the object's internal representation is hidden from the outside world.</li>
        <li><strong>Modularity:</strong> It allows for modular code where changes in one part of a program do not affect others.</li>
        <li><strong>Maintenance:</strong> It improves code maintainability by separating the internal details of an object from its external usage.</li>
      </ul>

      <h2 class="sub-title">Difference between Encapsulation and Abstraction</h2>
      <ul class="characteristics-list">
        <li><strong>Encapsulation:</strong> Encapsulation is about bundling data and methods that manipulate the data, and keeping the data safe from outside interference.</li>
        <li><strong>Abstraction:</strong> Abstraction is about hiding the complex implementation details and showing only the essential features of an object.</li>
      </ul>

      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the concepts of encapsulation in OOPs:</p>
      <div class="diagram-container">
        <img src="path/to/diagram1.png" alt="Diagram showing encapsulation in C++ class structure" />
        <img src="path/to/diagram2.png" alt="Diagram demonstrating access control using public methods" />
        <img src="path/to/diagram3.png" alt="Encapsulation vs Abstraction comparison diagram" />
      </div>

      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=oops1" target="_blank">Introduction to OOP and Encapsulation in C++</a></li>
        <li><a href="https://www.youtube.com/watch?v=oops2" target="_blank">Encapsulation in Hindi</a></li>
      </ul>
    </div>
  </template>

  <script>
  export default {
    name: "EncapsulationInCpp",
  };
  </script>

  <style scoped>
  .oos-container {
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

  .code-snippet {
    background-color: #333;
    padding: 15px;
    border-radius: 10px;
    color: #fff;
    overflow-x: auto;
    font-family: 'Courier New', Courier, monospace;
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