<!-- src/views/Arrays.vue -->
<!-- <template>
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
-->

<template>
  <div class="min-h-screen bg-black p-6">
    <div class="max-w-4xl mx-auto">

      <h1 class="text-4xl font-bold text-center mb-8 text-indigo-400">
        Array Data Structure Notes
      </h1>


      <div v-if="loading" class="flex justify-center items-center min-h-[200px]">
        <div class="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-indigo-500"></div>
      </div>


      <div v-else-if="error" class="bg-red-100 border-l-4 border-red-500 p-4 mb-4">
        <p class="text-red-700">{{ error }}</p>
      </div>


      <div v-else class="space-y-4">
        <div v-for="(note, index) in arrayNotes" :key="index" 
             class="bg-gray-800 rounded-lg shadow-md overflow-hidden">
          

          <button 
            @click="expandedTopics[index] = !expandedTopics[index]"
            class="w-full px-6 py-4 flex justify-between items-center bg-gradient-to-r from-indigo-600 to-indigo-700 hover:from-indigo-700 hover:to-indigo-800 transition-colors duration-200"
          >
            <h2 class="text-xl font-semibold text-white flex items-center gap-2">
              <i class="fas fa-book"></i>
              {{ note.title }}
            </h2>
            <i :class="[expandedTopics[index] ? 'fa-chevron-up' : 'fa-chevron-down', 'fas', 'text-white transition-transform duration-300']"></i>
          </button>

          <!-- Expanded Content -->
          <div v-if="expandedTopics[index]" class="p-6 text-gray-200">

            <div v-if="note.description" class="mb-6 leading-relaxed">
              <p>{{ note.description }}</p>
            </div>


            <div v-for="(list, listIndex) in note.lists" :key="listIndex" class="mb-6">
              <ul class="space-y-2 list-disc list-inside">
                <li v-for="(item, itemIndex) in list" :key="itemIndex">
                  {{ item }}
                </li>
              </ul>
            </div>

    <div v-if="note.code_examples?.length" class="space-y-4">
      <h3 class="text-lg font-semibold text-indigo-400 mb-3 flex items-center gap-2">
        <i class="fas fa-code"></i>
        Code Examples
      </h3>
      <div v-for="(example, exampleIndex) in note.code_examples" 
           :key="exampleIndex" 
           class="relative group">
        <pre
          class="bg-[#1e1e1e] text-[#d4d4d4] p-4 rounded-lg overflow-x-auto font-mono text-sm leading-6"
        ><code class="language-cpp" v-html="highlightCode(example)"></code></pre>
        <button 
          @click="copyCode(example)"
          class="absolute top-2 right-2 opacity-0 group-hover:opacity-100 transition-opacity duration-200 bg-indigo-600 text-white px-3 py-1 rounded text-sm hover:bg-indigo-700"
        >
          Copy
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'

const arrayNotes = ref([])
const expandedTopics = reactive({})
const loading = ref(true)
const error = ref(null)

// Function to format code
const formatCode = (code) => {
  return code
    .replace(/(\s{2,})/g, ' ')  // Replace multiple spaces with a single space
    .trim();                    // Remove leading/trailing whitespace
}

// Function to highlight code with syntax highlighting
const highlightCode = (code) => {
  // Format the code first
  let formattedCode = code
    .replace(/\/\//g, '\n//')  // Add line break before comments
    .replace(/;/g, ';\n')      // Add line break after semicolons
    .replace(/{/g, '{\n')      // Add line break after opening braces
    .replace(/}/g, '\n}')      // Add line break before closing braces
    .split('\n')               // Split into lines
    .map(line => line.trim())  // Trim each line
    .filter(line => line)      // Remove empty lines
    .join('\n');               // Join back with newlines

  // Apply syntax highlighting
  return formattedCode
    .replace(
      /(\/\/.*)|(\b(int|void|return|new|import|class|public|private|static)\b)|\b(\d+)\b|(\[|\])|(\{|\})|(\(|\))|(".*?")|('.*?')/g,
      (match) => {
        if (match.startsWith('//')) {
          return `<span class="code-comment">${match}</span>`;
        } else if (['int', 'void', 'return', 'new', 'import', 'class', 'public', 'private', 'static'].includes(match)) {
          return `<span class="code-keyword">${match}</span>`;
        } else if (/^\d+$/.test(match)) {
          return `<span class="code-number">${match}</span>`;
        } else if (['[', ']', '{', '}', '(', ')'].includes(match)) {
          return `<span class="code-bracket">${match}</span>`;
        } else if (match.startsWith('"') || match.startsWith("'")) {
          return `<span class="code-string">${match}</span>`;
        }
        return match;
      }
    );
}

// Function to copy code to clipboard
const copyCode = async (code) => {
  try {
    await navigator.clipboard.writeText(code)
    // You could add a toast notification here to inform the user
  } catch (err) {
    console.error('Failed to copy code:', err)
  }
}

// Fetch array notes from the API
const fetchArrayNotes = async () => {
  try {
    loading.value = true
    const response = await fetch('http://localhost:5000/fetch-array-notes')
    if (!response.ok) {
      throw new Error('Failed to fetch data')
    }
    arrayNotes.value = await response.json()
    arrayNotes.value.forEach((_, index) => {
      expandedTopics[index] = false
    })
  } catch (err) {
    error.value = 'Error loading array notes: ' + err.message
    console.error('Error:', err)
  } finally {
    loading.value = false
  }
}

// Run fetch function when the component is mounted
onMounted(() => {
  fetchArrayNotes()
})
</script>

<style scoped>
/* Import Roboto Font */
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

body {
  font-family: 'Roboto', sans-serif;
  background-color: #000000;
  color: #dcdcdc;
  display: flex;
  flex-direction: column;
  justify-content: left;
  align-items: left;
  min-height: 100vh;
  margin: 0;
}

/* Centered and yellow headings */
h1, h2, h3 {
  font-weight: 700;
  color: yellow;
  text-align: center;
  margin-bottom: 1rem;
}

/* Text readability */
p, ul, li {
  font-weight: 400;
  line-height: 1.6;
  color: #dcdcdc;
  text-align: left;
  margin: 0.5rem 0;
}

/* Center buttons with opacity */
button {
  background-color: #f63b3b;  /* Blue button color */
  color: white;
  font-weight: 500;
  padding: 0.8rem 1.5rem;
  margin: 1rem;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  opacity: 0.9;  /* Make buttons slightly opaque */
  transition: opacity 0.3s ease;
}

/* Button hover effect */
button:hover {
  opacity: 1;  /* Full opacity on hover */
  background-color: #000000;  /* Darken color on hover */
}

/* Code block styles */
pre {
  background-color: #1e1e1e;
  font-family: 'Fira Code', 'Consolas', monospace;
  padding: 1.5rem;
  border-radius: 8px;
  border: 1px solid #333;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
  overflow-x: auto;
  white-space: pre;
  line-height: 1.6;
  word-break: break-word;
  tab-size: 4;
}

/* Color scheme for code */
.code-comment {
  color: #6A9955; /* Green for comments */
}

.code-keyword {
  color: #FFCC00; /* Yellow for keywords */
}

.code-string {
  color: #FF6666; /* Red for strings */
}

.code-number {
  color: #66FF66; /* Light green for numbers */
}

.code-bracket {
  color: #FFD700; /* Gold for brackets */
}

/* Hover effect for code blocks */
pre:hover {
  box-shadow: 0 0 15px rgba(99, 102, 241, 0.2);
  transition: box-shadow 0.3s ease;
}

/* Line numbers (optional) */
.line-number {
  display: inline-block;
  width: 1.5rem;
  margin-right: 1rem;
  color: #858585;
  text-align: right;
  user-select: none;
}

/* Scrollbar visibility */
pre::-webkit-scrollbar {
  width: 14px;
  height: 14px;
}

pre::-webkit-scrollbar-track {
  background-color: #333333;
}

pre::-webkit-scrollbar-thumb {
  background-color: #555555;
  border: 3px solid #333333;
  border-radius: 7px;
}

pre::-webkit-scrollbar-thumb:hover {
  background-color: #4f4f4f;
}

/* Optional grid background for code blocks */
pre {
  background-image: linear-gradient(transparent 50%, rgba(255, 255, 255, .02) 50%);
  background-size: 3em 3em;
  background-origin: content-box;
}

/* Center everything in the body */
body {
  text-align: left;
  display: flex;
  flex-direction: column;
  align-items: left;
  justify-content: left;
}

/* Button hover and transition effects */
button {
  transition: background-color 0.3s ease, opacity 0.3s ease;
}
</style>
