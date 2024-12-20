<template>
    <div class="string-container">
      <h1 class="main-title">Strings</h1>
      <p class="intro">
        A string is a sequence of characters, commonly used to represent text. Strings are fundamental in programming and are used in various applications, such as data manipulation, input/output processing, and more.
      </p>
  
      <h2 class="sub-title">Key Characteristics of Strings</h2>
      <ul class="characteristics-list">
        <li><strong>Immutable or Mutable:</strong> Strings can be immutable (like in Java) or mutable (like in Python).</li>
        <li><strong>Character Indexing:</strong> Individual characters in a string can be accessed by their index, starting from zero.</li>
        <li><strong>Concatenation:</strong> Strings can be combined or concatenated to form new strings.</li>
      </ul>
  
      <h2 class="sub-title">Diagram of a String</h2>
      <img src="@/assets/String.png" alt="String Diagram" class="string-diagram"/>
  
      <h2 class="sub-title">Types of Strings</h2>
      <h3 class="type-title">Immutable String</h3>
      <p>A string that cannot be altered once created. Any changes result in the creation of a new string.</p>
  
      <h3 class="type-title">Mutable String</h3>
      <p>A string that can be modified after creation, commonly used for performance in large data operations.</p>
  
      <h3 class="type-title">Concatenated String</h3>
      <p>A string formed by joining two or more strings together.</p>
  
      <h2 class="sub-title">String Operations</h2>
      <p>Common operations performed on strings include concatenation, substring extraction, and replacing characters or substrings.</p>
  
      <h2 class="sub-title">String Functions</h2>
      <p>String functions include length, upper case, lower case, and trimming whitespace.</p>
  
      <h2 class="sub-title">Examples</h2>
      <p>Click on the buttons below to see examples of strings in different programming languages:</p>
  
      <div class="button-container">
        <button @click="showExample('java')" class="example-button">Example in Java</button>
        <button @click="showExample('c')" class="example-button">Example in C</button>
        <button @click="showExample('python')" class="example-button">Example in Python</button>
      </div>
  
      <pre v-if="exampleCode">
        <code>{{ exampleCode }}</code>
      </pre>
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=abc123" target="_blank">Strings in JavaScript (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=xyz456" target="_blank">Strings in Hindi</a></li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "String",
    data() {
      return {
        exampleCode: "",
      };
    },
    methods: {
      showExample(language) {
        if (language === 'java') {
          this.exampleCode = `// Declaration of a string in Java
  String text = "Hello, World!";
  System.out.println(text.charAt(0)); // Output: H`;
        } else if (language === 'c') {
          this.exampleCode = `// Declaration of a string in C
  char text[] = "Hello, World!";
  printf("%c", text[0]); // Output: H`;
        } else if (language === 'python') {
          this.exampleCode = `# Declaration of a string in Python
  text = "Hello, World!"
  print(text[0])  # Output: H`;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .string-container {
    max-width: 800px;
    margin: 20px auto;
    padding: 20px;
    border-radius: 10px;
    background-color: #121212; /* Dark background color */
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.6);
    font-family: 'Roboto', sans-serif;
    color: #f5f5f5; /* Lighter text color for better readability */
    line-height: 1.6; /* Increased line height for readability */
  }
  
  .main-title {
    font-size: 2.8em; /* Increased font size for main title */
    color: #e3e3e3;
    text-align: center;
    margin-bottom: 30px;
  }
  
  .sub-title {
    font-size: 2em;
    color: #ffcc00; /* Bright color for sub-titles */
    margin-top: 40px;
    padding-bottom: 10px;
  }
  
  .type-title {
    font-size: 1.5em;
    color: #ffcc00; /* Bright color for type titles */
    margin-top: 25px;
  }
  
  .intro {
    font-size: 1.3em; /* Increased font size for intro text */
    margin-bottom: 25px;
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
  
  .string-diagram {
    width: 100%;
    height: auto;
    margin: 30px 0;
    border: 1px solid #555;
    border-radius: 5px;
  }
  
  pre {
    background-color: #1c1c1c;
    padding: 10px;
    border-radius: 5px;
    overflow-x: auto;
    color: #00ff00;
    font-size: 1.2em; /* Adjusted font size for code */
  }
  
  .button-container {
    display: flex;
    justify-content: space-around;
    margin: 30px 0;
  }
  
  .example-button {
    background-color: #ffcc00;
    color: #121212;
    border: none;
    border-radius: 5px;
    padding: 15px 30px;
    font-size: 1.2em;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .example-button:hover {
    background-color: #ffe066;
  }
  
  a {
    color: #ffcc00;
    text-decoration: none;
    font-size: 1.1em;
  }
  
  a:hover {
    text-decoration: underline;
  }
  
  .link-title {
    color: #ffffff;
    margin-top: 30px;
    /*font-size: 1.7em;*/
  }
  </style>
  