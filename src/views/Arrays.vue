<!-- src/views/Arrays.vue -->
<template>
  <div class="array-container">
    <h1 class="main-title">Arrays</h1>
    <p class="intro">
      An array is a collection of items stored at contiguous memory locations. It is used to store multiple values in a single variable, instead of declaring separate variables for each value. Arrays can store items of the same data type.
    </p>
    
    <h2 class="sub-title">Key Characteristics of Arrays</h2>
    <ul class="characteristics-list">
      <li><strong>Fixed size:</strong> The size of an array is defined at the time of creation and cannot be changed.</li>
      <li><strong>Homogeneous elements:</strong> All elements in an array are of the same data type.</li>
      <li><strong>Random access:</strong> Elements can be accessed directly using their index.</li>
    </ul>

    <h2 class="sub-title">Diagram of an Array</h2>
    <img src="@/assets/7-2.png" alt="Array Diagram" class="array-diagram"/>

    <h2 class="sub-title">Declaration Syntax</h2>
    <p>Select a programming language to see the declaration syntax:</p>
    
    <div class="button-container">
      <button @click="showDeclaration('java')" class="example-button">Java</button>
      <button @click="showDeclaration('c')" class="example-button">C</button>
      <button @click="showDeclaration('python')" class="example-button">Python</button>
    </div>

    <pre v-if="declarationCode">
      <code>{{ declarationCode }}</code>
    </pre>

    <h2 class="sub-title">Types of Arrays</h2>
    <h3 class="type-title">One-Dimensional Arrays</h3>
    <p>A one-dimensional array is a linear array that can store a sequence of elements. Each element can be accessed using a single index.</p>
    
    <h3 class="type-title">Multi-Dimensional Arrays</h3>
    <p>Multi-dimensional arrays are arrays of arrays, allowing for storage of data in multiple dimensions. The most common example is a two-dimensional array (matrix).</p>

    <h2 class="sub-title">Advantages of Arrays</h2>
    <ul>
      <li>Arrays allow efficient access to elements using indices.</li>
      <li>They provide a systematic way to store and manage collections of data.</li>
      <li>Memory allocation is contiguous, which improves cache performance.</li>
    </ul>

    <h2 class="sub-title">Disadvantages of Arrays</h2>
    <ul>
      <li>The size of an array is fixed and cannot be altered after creation.</li>
      <li>Insertion and deletion of elements can be time-consuming as it may require shifting elements.</li>
      <li>They can waste memory if the allocated size is not fully utilized.</li>
    </ul>

    <h2 class="sub-title">Useful Links</h2>
    <h3 class="link-title">YouTube Tutorials</h3>
    <ul>
      <li><a href="https://www.youtube.com/watch?v=0qF0_JB2Kaw" target="_blank">Arrays in JavaScript (English)</a></li>
      <li><a href="https://www.youtube.com/watch?v=9z9gElc6D5s" target="_blank">Arrays in Hindi</a></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "Arrays",
  data() {
    return {
      declarationCode: "",
    };
  },
  methods: {
    showDeclaration(language) {
      if (language === 'java') {
        this.declarationCode = `// Declaration of an array in Java
int[] numbers = {10, 20, 30, 40, 50};`;
      } else if (language === 'c') {
        this.declarationCode = `// Declaration of an array in C
int numbers[] = {10, 20, 30, 40, 50};`;
      } else if (language === 'python') {
        this.declarationCode = `# Declaration of an array in Python
numbers = [10, 20, 30, 40, 50]`;
      }
    },
  },
};
</script>

<style scoped>
.array-container {
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
  border-radius: 10px;
  background-color: #121212; /* Dark background color */
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.6);
  font-family: 'Roboto', sans-serif; /* Updated font */
  color: #e0e0e0; /* Light text color for better readability */
  line-height: 1.6; /* Increased line height for better readability */
}

.main-title {
  font-size: 2.8em; /* Larger font size for main title */
  color: #f8f8f8; /* Bright color for the main title */
  text-align: center;
  margin-bottom: 30px; /* Increased margin for better spacing */
}

.sub-title {
  font-size: 2em; /* Larger font size for sub-titles */
  color: #e0ce46; /* Bright color for sub-titles */
  margin-top: 40px; /* Increased margin for better spacing */
  padding-bottom: 10px; /* Space below the sub-title */
}

.type-title {
  font-size: 1.5em; /* Larger font size for type titles */
  color: #e0ce46; /* Bright color for type titles */
  margin-top: 25px; /* Margin for type titles */
}

.intro {
  font-size: 1.3em; /* Increased font size for intro text */
  margin-bottom: 25px; /* Increased margin for better spacing */
}

.characteristics-list {
  margin: 10px 0;
  padding-left: 20px;
  font-size: 1.2em; /* Increased font size for list items */
}

li {
  margin-bottom: 15px; /* Increased margin for list items */
  line-height: 1.6; /* Increased line height for better readability */
}

.array-diagram {
  width: 100%;
  height: auto;
  margin: 30px 0; /* Increased margin for better spacing */
  border: 1px solid #444; /* Darker border for image */
  border-radius: 5px;
}

pre {
  background-color: #1f1f1f; /* Darker background for code */
  padding: 10px;
  border-radius: 5px;
  overflow-x: auto; /* Allow horizontal scrolling for long code */
  color: #00ff00; /* Green text color for code */
  font-size: 1.2em; /* Increased font size for code */
}

.button-container {
  display: flex;
  justify-content: space-around; /* Space buttons evenly */
  margin: 30px 0; /* Increased margin for better spacing */
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
  color: #ddc452; /* Link color */
  text-decoration: none; /* Remove underline */
  font-size: 1.1em; /* Increased font size for links */
}

a:hover {
  text-decoration: underline; /* Underline on hover */
}

.link-title {
  color: #ffffff; /* Bright color for link titles */
  margin-top: 30px; /* Increased margin for better spacing */
}
</style>
