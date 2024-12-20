<!-- src/views/PatternSearching.vue -->
<template>
    <div class="algorithm-container">
      <h1 class="main-title">Pattern Searching</h1>
      <p class="intro">
        Pattern searching is a fundamental problem in computer science and string processing, where the goal is to find occurrences of a "pattern" string within a larger "text" string. Efficient pattern searching algorithms are crucial for applications like text editing, search engines, and DNA sequencing.
      </p>
  
      <h2 class="sub-title">Key Concepts in Pattern Searching</h2>
      <ul class="characteristics-list">
        <li><strong>Text:</strong> The larger string in which we want to find occurrences of the pattern.</li>
        <li><strong>Pattern:</strong> The smaller string that we are searching for within the text.</li>
        <li><strong>Search Algorithms:</strong> Various algorithms can be employed for pattern searching, each with different efficiencies and use cases.</li>
      </ul>
  
      <h2 class="sub-title">Diagram for Pattern Searching</h2>
      <img src="@/assets/pattern-searching-diagram.png" alt="Pattern Searching Diagram" class="algorithm-diagram"/>
  
      <h2 class="sub-title">Example Algorithms</h2>
      <p>Select a category of pattern searching algorithms to see examples:</p>
  
      <div class="button-container">
        <button @click="showAlgorithm('naive')" class="example-button">Naive Pattern Searching</button>
        <button @click="showAlgorithm('kmp')" class="example-button">KMP Algorithm</button>
        <button @click="showAlgorithm('bm')" class="example-button">Boyer-Moore Algorithm</button>
      </div>
  
      <pre v-if="algorithmExample">
        <code>{{ algorithmExample }}</code>
      </pre>
  
      <h2 class="sub-title">Types of Pattern Searching Algorithms</h2>
      <h3 class="type-title">Naive Pattern Searching</h3>
      <p>This approach checks for the pattern at every position in the text, resulting in a straightforward but inefficient method.</p>
  
      <h3 class="type-title">KMP Algorithm</h3>
      <p>The Knuth-Morris-Pratt (KMP) algorithm preprocesses the pattern to create a partial match table, allowing it to skip unnecessary comparisons.</p>
  
      <h3 class="type-title">Boyer-Moore Algorithm</h3>
      <p>The Boyer-Moore algorithm uses a heuristic to skip sections of the text based on the last occurrence of characters in the pattern, making it faster in practice.</p>
  
      <h2 class="sub-title">Advantages of Pattern Searching</h2>
      <ul>
        <li>Efficient searching in large texts with minimal computational overhead.</li>
        <li>Useful for various applications, including text processing, data retrieval, and bioinformatics.</li>
        <li>Reduces the need for exhaustive searches, enhancing performance in string matching.</li>
      </ul>
  
      <h2 class="sub-title">Disadvantages of Pattern Searching</h2>
      <ul>
        <li>Some algorithms may have high worst-case time complexity, depending on the input.</li>
        <li>Not all algorithms are efficient for every type of pattern or text structure.</li>
        <li>Preprocessing time for some algorithms may be non-trivial, impacting their overall efficiency.</li>
      </ul>
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=3W8hN4WblYc" target="_blank">Pattern Searching (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=W9rX1nAxPPE" target="_blank">Pattern Searching in Hindi</a></li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "PatternSearching",
    data() {
      return {
        algorithmExample: "",
      };
    },
    methods: {
      showAlgorithm(type) {
        if (type === 'naive') {
          this.algorithmExample = `// Example of Naive Pattern Searching Algorithm
  for (int i = 0; i <= n - m; i++) {
    int j;
    for (j = 0; j < m; j++)
      if (text[i + j] != pattern[j])
        break;
    if (j == m)
      print("Pattern found at index " + i);
  }`;
        } else if (type === 'kmp') {
          this.algorithmExample = `// Example of KMP Algorithm
  void KMPSearch(string text, string pattern) {
    int M = pattern.length();
    int N = text.length();
    int lps[M];
    computeLPSArray(pattern, M, lps);
    int i = 0; // index for text
    int j = 0; // index for pattern
    while (N - i >= M) {
      if (pattern[j] == text[i]) {
        j++;
        i++;
      }
      if (j == M) {
        print("Pattern found at index " + (i - j));
        j = lps[j - 1];
      } else if (i < N && pattern[j] != text[i]) {
        if (j != 0)
          j = lps[j - 1];
        else
          i++;
      }
    }
  }`;
        } else if (type === 'bm') {
          this.algorithmExample = `// Example of Boyer-Moore Algorithm
  void search(string text, string pattern) {
    int m = pattern.length();
    int n = text.length();
    int badChar[256];
    preprocessBadChar(pattern, badChar);
    int s = 0; // s is shift of the pattern with respect to text
    while (s <= n - m) {
      int j = m - 1;
      while (j >= 0 && pattern[j] == text[s + j])
        j--;
      if (j < 0) {
        print("Pattern found at index " + s);
        s += (s + m < n) ? m - badChar[text[s + m]] : 1;
      } else
        s += max(1, j - badChar[text[s + j]]);
    }
  }`;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .algorithm-container {
    max-width: 800px;
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
    color: #f8f8f8;
    text-align: center;
    margin-bottom: 30px;
  }
  
  .sub-title {
    font-size: 2em;
    color: #e0ce46;
    margin-top: 40px;
    padding-bottom: 10px;
  }
  
  .type-title {
    font-size: 1.5em;
    color: #e0ce46;
    margin-top: 25px;
  }
  
  .intro {
    font-size: 1.3em;
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
  
  .algorithm-diagram {
    width: 100%;
    height: auto;
    margin: 30px 0;
    border: 1px solid #444;
    border-radius: 5px;
  }
  
  pre {
    background-color: #1f1f1f;
    padding: 10px;
    border-radius: 5px;
    overflow-x: auto;
    color: #00ff00;
    font-size: 1.2em;
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