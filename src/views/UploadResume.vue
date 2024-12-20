<template>
  <div class="container">
    <div class="upload-section">
      <h1>Upload Your Resume</h1>
      <div class="file-upload">
        <input type="file" @change="handleFileUpload" accept=".pdf,.doc,.docx" />
        <button @click="uploadResume" :disabled="!selectedFile || isUploading">
          <span v-if="!isUploading">Upload</span>
          <span v-else>Uploading...</span>
        </button>
      </div>
      <p v-if="uploadStatus" :class="statusClass">{{ uploadStatus }}</p>
    </div>

    <div class="info-section">
      <h2>How It Works</h2>
      <p>
        Upload your resume in PDF, DOC, or DOCX format. Based on the keywords 
        extracted from your resume, we will generate interview questions tailored to your skills.
      </p>
      <p class="note">
        Note: Ensure your file is under 5MB and contains the necessary details about your technical expertise.
      </p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedFile: null, // Selected file from input
      keywords: [], // Store extracted keywords
      uploadStatus: "", // Store status message
      statusClass: "", // Dynamic class for status message styling
      isUploading: false, // State for showing a loader
    };
  },
  methods: {
    handleFileUpload(event) {
      this.selectedFile = event.target.files[0];

      if (this.selectedFile) {
        const fileExtension = this.selectedFile.name.split(".").pop().toLowerCase();
        const allowedExtensions = ["pdf", "doc", "docx"];

        if (!allowedExtensions.includes(fileExtension)) {
          this.selectedFile = null;
          this.uploadStatus = "Unsupported file type. Please upload a PDF, DOC, or DOCX file.";
          this.statusClass = "error"; // Set error class
        } else if (this.selectedFile.size > 5 * 1024 * 1024) { // 5MB size limit
          this.selectedFile = null;
          this.uploadStatus = "File size exceeds the 5MB limit. Please upload a smaller file.";
          this.statusClass = "error"; // Set error class
        } else {
          this.uploadStatus = `Selected file: ${this.selectedFile.name}`;
          this.statusClass = "success"; // Set success class
        }
      }
    },
    async uploadResume() {
      if (this.selectedFile) {
        this.isUploading = true; // Start loader
        const formData = new FormData();
        formData.append("resume", this.selectedFile);

        try {
          const response = await fetch("http://127.0.0.1:5001/upload", {
            method: "POST",
            body: formData,
          });

          if (response.ok) {
            const data = await response.json();
            this.keywords = data.keywords; // Assuming API returns extracted keywords
            console.log("Extracted Keywords:", this.keywords); // Debugging
            this.uploadStatus = "Resume uploaded successfully!";
            this.statusClass = "success"; // Set success class

            // Redirect to VideoCapture and pass keywords as query params
            this.$router.push({
              name: "-capturvideoe",
              query: { keywords: JSON.stringify(this.keywords) }, // Pass keywords as a query parameter
            });
          } else {
            const errorText = await response.text();
            this.uploadStatus = `Failed to upload resume: ${errorText}`;
            this.statusClass = "error"; // Set error class
          }
        } catch (error) {
          this.uploadStatus = `Error uploading resume: ${error.message}`;
          this.statusClass = "error"; // Set error class
        } finally {
          this.isUploading = false; // Stop loader
        }
      } else {
        this.uploadStatus = "Please select a file before uploading.";
        this.statusClass = "error"; // Set error class
      }
    },
  },
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: "Roboto", sans-serif;
  padding: 20px;
  background-color: #f9f9f9;
  min-height: 100vh;
  color: #333;
}

.upload-section {
  text-align: center;
  margin-bottom: 30px;
}

.file-upload {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 15px;
}

input[type="file"] {
  font-size: 16px;
  padding: 10px;
  border: 2px dashed #007bff;
  border-radius: 5px;
  cursor: pointer;
  background-color: #fff;
  outline: none;
  transition: border-color 0.3s ease;
}

input[type="file"]:hover {
  border-color: #0056b3;
}

button {
  background-color: #007bff;
  color: #fff;
  font-size: 16px;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

button:hover:enabled {
  background-color: #0056b3;
}

.statusClass {
  margin-top: 10px;
  font-size: 14px;
}

.success {
  color: green;
  font-weight: bold;
}

.error {
  color: red;
  font-weight: bold;
}

.info-section {
  margin-top: 20px;
  text-align: center;
}

.info-section p {
  font-size: 16px;
  margin: 10px 0;
  line-height: 1.6;
}

.note {
  color: #777;
  font-size: 14px;
}
</style>