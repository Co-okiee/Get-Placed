<template>
  <div class="login-container">
    <div class="login-box">
      <h2>Login</h2>
      <form @submit.prevent="loginUser">
        <div class="form-group">
          <label for="email">Email:</label>
          <input v-model="email" type="email" id="email" required />
        </div>
        <div class="form-group">
          <label for="password">Password:</label>
          <input v-model="password" type="password" id="password" required />
        </div>
        <button type="submit" class="login-btn">Login</button>
      </form>
      <p v-if="username">Welcome, {{ username }}!</p> <!-- Display the username if logged in -->
      <p>Don't have an account? <router-link to="/signup">Sign Up</router-link></p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      username:'',
      password: '',
      name: '',  // For storing user's name
      user_id: '' // For storing user's ID
    };
  },
  methods: {
    async loginUser() {
      try {
        // Send a POST request to the Flask login route
        const response = await axios.post('http://localhost:5000/login', {
          username: this.email,     // Sending email instead of username
          password: this.password
        });

        // Assuming the Flask API sends back user_id, name, and username
        this.username = response.data.username;
        this.name = response.data.name;
        this.user_id = response.data.user_id;

        // Save data to localStorage for later use
        localStorage.setItem('username', this.username);
        localStorage.setItem('name', this.name);
        localStorage.setItem('user_id', this.user_id);

        // Redirect to the dashboard after login
        this.$router.push('/');
      } catch (error) {
        if (error.response && error.response.data.error) {
          alert(error.response.data.error);
        } else {
          alert('Login failed! Please try again.');
        }
      }
    },
  },
  mounted() {
    // Retrieve stored values from localStorage when the component is mounted
    this.username = localStorage.getItem('username') || '';
    this.name = localStorage.getItem('name') || '';
    this.user_id = localStorage.getItem('user_id') || '';
    console.log("Retrieved user_id:", this.user_id);
    if (!this.user_id) {
   console.error("Error: user_id is not defined.");
   alert("Failed to get user_id. Please log in again.");
   return;  // Exit the function if user_id is not available
}

  }

};
</script>

<style scoped>
/* Centering the login box */
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #000000;
}

.login-box {
  background-color: #2e2c2c;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 300px;
  text-align: center;
}

h2 {
  margin-bottom: 1.5rem;
  color: #fcfcfc;
}

.form-group {
  margin-bottom: 1rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
  color: #ffffff;
}

input {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-sizing: border-box;
}

.login-btn {
  width: 100%;
  padding: 0.75rem;
  background-color: #4ed5b1;
  color: rgb(255, 255, 255);
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.login-btn:hover {
  background-color: #000000;
}

p {
  margin-top: 1rem;
  color: #939292;
}

a {
  color: #e2dc41;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}
</style>
