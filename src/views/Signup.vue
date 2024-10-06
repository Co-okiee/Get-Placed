<template>
  <div class="signup-container">
    <div class="signup-box">
      <h2>Sign Up</h2>
      <form @submit.prevent="registerUser">
        <div class="form-group">
          <label for="name">Name:</label>
          <input v-model="name" type="text" id="name" required />
        </div>
        <div class="form-group">
          <label for="email">Email:</label>
          <input v-model="email" type="email" id="email" required /> <!-- Fixed id -->
        </div>
        <div class="form-group">
          <label for="password">Password:</label>
          <input v-model="password" type="password" id="password" required />
        </div>
        <button type="submit" class="signup-btn">Sign Up</button>
      </form>
      <p>Already have an account? <router-link to="/login">Login</router-link></p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'; // Ensure axios is imported

export default {
  data() {
    return {
      name: '', // Added name field to data
      email: '',
      password: '',
    };
  },
  methods: {
    async registerUser() {
      try {
        const response = await axios.post('http://localhost:5000/signup', {
          name: this.name,       // Sending the name in the request body
          username: this.email,  // Assuming username is the email
          password: this.password,
        });
        // Handle successful registration
        console.log(response.data.message);
        this.$router.push('/login'); // Redirect to login page after successful signup
      } catch (error) {
        // Handle registration error
        console.error('Registration error:', error.response.data.error);
        alert(error.response.data.error || 'An error occurred during registration.');
      }
    },
  },
};
</script>

<style scoped>
/* Centering the signup box */
.signup-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #000000;
}

.signup-box {
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

.signup-btn {
  width: 100%;
  padding: 0.75rem;
  background-color: #4ed5b1;
  color: rgb(255, 255, 255);
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.signup-btn:hover {
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
