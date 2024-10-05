<template>
    <div class="compression-container">
      <h1 class="main-title">Compression Techniques</h1>
      <p class="intro">
        Compression techniques reduce the size of data for storage and transmission, helping to save space and speed up data transfer. They can be classified into lossless and lossy compression methods.
      </p>

      <h2 class="sub-title">Introduction to Compression Techniques</h2>
      <p class="content">
        Compression is essential in data storage and communication. It allows for efficient use of resources while maintaining data integrity in lossless techniques.
      </p>

      <h2 class="sub-title">LZW (Lempel–Ziv–Welch) Compression Technique</h2>
      <p class="content">
        LZW is a lossless data compression algorithm that replaces repeated occurrences of data with references to a single copy. This technique is widely used in GIF images and UNIX file compression.
      </p>
      <h3 class="example-title">Example of LZW Compression</h3>
      <p class="content">
        For the input string "ABABABA," LZW builds a dictionary that encodes sequences as follows:
        <br><strong>AB</strong> → 1
        <br><strong>A</strong> → 2
        <br><strong>B</strong> → 3
        <br><strong>ABAB</strong> → 4
        <br>Encoded output: 1, 2, 4, 2
      </p>

      <h2 class="sub-title">Data Compression With Arithmetic Coding</h2>
      <p class="content">
        Arithmetic coding compresses data by representing the entire message as a single number between 0 and 1. It assigns shorter codes to more frequent symbols and longer codes to less frequent ones.
      </p>
      <h3 class="example-title">Example of Arithmetic Coding</h3>
      <p class="content">
        For a message with symbols A (50%), B (30%), and C (20%), the range for A could be 0 to 0.5, for B 0.5 to 0.8, and for C 0.8 to 1. This method effectively compresses the data based on the frequency of the symbols.
      </p>

      <h2 class="sub-title">Shannon-Fano Algorithm for Data Compression</h2>
      <p class="content">
        The Shannon-Fano algorithm is a method of lossless data compression. It assigns binary codes to symbols based on their probabilities, ensuring that more frequent symbols have shorter codes.
      </p>
      <h3 class="example-title">Example of Shannon-Fano Encoding</h3>
      <p class="content">
        Given symbols A (0.4), B (0.3), C (0.2), D (0.1), the algorithm would produce:
        <br><strong>A:</strong> 0
        <br><strong>B:</strong> 10
        <br><strong>C:</strong> 110
        <br><strong>D:</strong> 111
      </p>

      <h2 class="sub-title">Comparison of Compression Techniques</h2>
      <p class="content">
        Each technique has its strengths:
        <ul>
          <li><strong>LZW:</strong> Simple and effective for repetitive data.</li>
          <li><strong>Arithmetic Coding:</strong> More efficient for non-uniform distributions of symbols.</li>
          <li><strong>Shannon-Fano:</strong> Easier to implement, though less efficient than Huffman coding.</li>
        </ul>
      </p>

      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=compression1" target="_blank">Introduction to Data Compression Techniques (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=compression2" target="_blank">Compression Algorithms Explained in Hindi</a></li>
      </ul>

      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the concepts discussed:</p>
      <div class="diagram-container">
        <img src="path/to/lzw_diagram.png" alt="LZW Compression Diagram" />
        <img src="path/to/arithmetic_coding_diagram.png" alt="Arithmetic Coding Diagram" />
        <img src="path/to/shannon_fano_diagram.png" alt="Shannon-Fano Algorithm Diagram" />
      </div>
    </div>
</template>

<script>
export default {
    name: "CompressionTechniques",
};
</script>

<style scoped>
.compression-container {
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