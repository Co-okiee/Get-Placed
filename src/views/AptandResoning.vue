<template>
    <div class="prep-container">
      <h1 class="main-title">Aptitude and Reasoning</h1>
      <p class="intro">
        Aptitude and reasoning skills are essential for competitive exams, placement tests, and various job interviews. Mastering these concepts will enhance problem-solving abilities and logical thinking.
      </p>
  
      <h2 class="sub-title">Key Areas of Aptitude</h2>
      <ul class="key-areas-list">
        <li><strong>Quantitative Aptitude:</strong> Deals with arithmetic, algebra, geometry, and trigonometry problems.</li>
        <li><strong>Logical Reasoning:</strong> Involves pattern recognition, logical deductions, and analogies.</li>
        <li><strong>Verbal Ability:</strong> Focuses on reading comprehension, sentence correction, and grammar.</li>
      </ul>
  
      <h2 class="sub-title">Types of Aptitude Questions</h2>
      <h3 class="type-title">Arithmetic Ability</h3>
      <p>Questions on basic arithmetic operations like addition, subtraction, multiplication, division, percentages, etc.</p>
  
      <h3 class="type-title">Logical Reasoning</h3>
      <p>Questions involving puzzles, coding-decoding, syllogism, and seating arrangement.</p>
  
      <h3 class="type-title">Data Interpretation</h3>
      <p>Questions based on interpreting data from charts, graphs, and tables.</p>
  
      <h2 class="sub-title">Important Formulas</h2>
      <p>Memorizing these formulas will help you quickly solve aptitude questions:</p>
      <ul class="formula-list">
        <li><strong>Simple Interest:</strong> \(SI = \frac{P \times R \times T}{100}\)</li>
        <li><strong>Compound Interest:</strong> \(A = P \left(1 + \frac{R}{100}\right)^T\)</li>
        <li><strong>Time, Speed, Distance:</strong> \(Speed = \frac{Distance}{Time}\)</li>
        <li><strong>Profit and Loss:</strong> \(Profit\% = \frac{Profit}{Cost Price} \times 100\)</li>
      </ul>
  
      <h2 class="sub-title">Logical Reasoning Puzzles</h2>
      <p>Examples of common reasoning puzzles:</p>
      <ul class="puzzle-list">
        <li>Find the missing number in a series.</li>
        <li>Solve the seating arrangement puzzle.</li>
        <li>Determine relationships from family tree diagrams.</li>
      </ul>
  
      <h2 class="sub-title">Examples</h2>
      <p>Click on the buttons below to see examples of aptitude questions in different categories:</p>
  
      <div class="button-container">
        <button @click="showExample('quantitative')" class="example-button">Quantitative Example</button>
        <button @click="showExample('logical')" class="example-button">Logical Reasoning Example</button>
        <button @click="showExample('verbal')" class="example-button">Verbal Ability Example</button>
      </div>
  
      <pre v-if="exampleCode">
        <code>{{ exampleCode }}</code>
      </pre>
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=example1" target="_blank">Quantitative Aptitude (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=example2" target="_blank">Logical Reasoning in Hindi</a></li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "AptitudeAndReasoning",
    data() {
      return {
        exampleCode: "",
      };
    },
    methods: {
      showExample(category) {
        if (category === 'quantitative') {
          this.exampleCode = `// Quantitative Aptitude Example
  // Find the Simple Interest on a sum of Rs. 1000 at 5% per annum for 3 years.
  let principal = 1000;
  let rate = 5;
  let time = 3;
  let simpleInterest = (principal * rate * time) / 100;
  console.log("Simple Interest: ", simpleInterest);`;
        } else if (category === 'logical') {
          this.exampleCode = `// Logical Reasoning Example
  // A is older than B, B is older than C. Who is the youngest?
  if (A > B && B > C) {
    console.log("C is the youngest.");
  }`;
        } else if (category === 'verbal') {
          this.exampleCode = `// Verbal Ability Example
  // Identify the error in the sentence:
  // She have completed her assignment.
  let correctSentence = "She has completed her assignment.";
  console.log(correctSentence);`;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .prep-container {
    max-width: 800px;
    margin: 20px auto;
    padding: 20px;
    border-radius: 10px;
    background-color: #121212; /* Dark theme */
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
  }
  
  .type-title {
    font-size: 1.8em;
    color: #e0ce46;
    margin-top: 25px;
  }
  
  .intro, .key-areas-list, .formula-list, .puzzle-list {
    font-size: 1.3em;
    margin-bottom: 25px;
  }
  
  .pre {
    background-color: #1f1f1f;
    padding: 10px;
    border-radius: 5px;
    overflow-x: auto;
    color: #00ff00;
  }
  
  .button-container {
    display: flex;
    justify-content: space-around;
    margin: 30px 0;
  }
  
  .example-button {
  background-color: #e0ce46; /* Button color */
  color: #121212; /* Text color */
  border: none;
  border-radius: 5px;
  padding: 8px 15px; /* Reduced padding for smaller button size */
  font-size: 1.2em; /* Reduced font size for buttons */
  cursor: pointer;
  transition: background-color 0.3s;
}

.example-button:hover {
  background-color: #f6f361; /* Change color on hover */
}

  
  a {
    color: #ddc452;
    text-decoration: none;
    font-size: 1.2em;
  }
  
  a:hover {
    text-decoration: underline;
  }
  
  .link-title {
    color: #ffffff;
    margin-top: 20px;
    font-size: 1.5em;
  }
  </style>
  