<template>
    <div class="geometric-container">
      <h1 class="main-title">Geometric Algorithms</h1>
      <p class="intro">
        Geometric algorithms are techniques used for solving problems related to geometric objects such as points, lines, polygons, and other shapes.
      </p>
  
      <h2 class="sub-title">Key Characteristics of Geometric Algorithms</h2>
      <ul class="characteristics-list">
        <li><strong>Spatial Data Structures:</strong> Utilizes data structures like trees and graphs to manage geometric data efficiently.</li>
        <li><strong>Efficiency:</strong> Aims to minimize computational time and resource usage in processing geometric queries.</li>
        <li><strong>Applications:</strong> Widely used in computer graphics, robotics, geographic information systems (GIS), and more.</li>
      </ul>
  
      <h2 class="sub-title">Diagram of Geometric Algorithms</h2>
      <img src="@/assets/geometric-algorithms.png" alt="Geometric Algorithms Diagram" class="geometric-diagram"/>
  
      <h2 class="sub-title">Types of Geometric Algorithms</h2>
      <h3 class="type-title">Convex Hull</h3>
      <p>A minimal polygon that encloses a set of points in a plane.</p>
  
      <h3 class="type-title">Line Intersection</h3>
      <p>Algorithms to determine the points where two or more lines intersect.</p>
  
      <h3 class="type-title">Polygon Triangulation</h3>
      <p>Dividing a polygon into triangles to simplify computations.</p>
  
      <h2 class="sub-title">Geometric Algorithm Functions</h2>
      <p>Key functions include computing distances, finding intersections, and performing transformations on geometric objects.</p>
  
      <h2 class="sub-title">Examples</h2>
      <p>Click on the buttons below to see examples of geometric algorithms in different programming languages:</p>
  
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
        <li><a href="https://www.youtube.com/watch?v=geometric1" target="_blank">Geometric Algorithms in Java (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=geometric2" target="_blank">Geometric Algorithms in Hindi</a></li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "GeometricAlgorithms",
    data() {
      return {
        exampleCode: "",
      };
    },
    methods: {
      showExample(language) {
        if (language === 'java') {
          this.exampleCode = `import java.awt.geom.Line2D;
  
  public class LineIntersection {
      public static void main(String[] args) {
          Line2D line1 = new Line2D.Double(1, 1, 4, 4);
          Line2D line2 = new Line2D.Double(1, 4, 4, 1);
          if (line1.intersectsLine(line2)) {
              System.out.println("Lines intersect.");
          } else {
              System.out.println("Lines do not intersect.");
          }
      }
  }`;
        } else if (language === 'c') {
          this.exampleCode = `#include <stdio.h>
  
  struct Point {
      int x, y;
  };
  
  int orientation(struct Point p, struct Point q, struct Point r) {
      int val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y);
      return (val == 0) ? 0 : (val > 0) ? 1 : 2;
  }`;
        } else if (language === 'python') {
          this.exampleCode = `def convex_hull(points):
      points = sorted(points)
      # Logic for computing convex hull
      return points
  points = [(0, 0), (1, 1), (2, 2)]
  print(convex_hull(points))`;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .geometric-container {
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
  
  .geometric-diagram {
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
  