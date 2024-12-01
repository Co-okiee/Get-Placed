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
          <input v-model="email" type="email" id="email" required />
        </div>
        <div class="form-group">
          <label for="password">Password:</label>
          <input v-model="password" type="password" id="password" required />
        </div>
        <button type="submit" class="signup-btn">Sign Up</button>
      </form>
      <p>Already have an account? <router-link to="/login" class="login-link">Login</router-link></p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      name: '',
      email: '',
      password: '',
    };
  },
  methods: {
    async registerUser() {
      try {
        const response = await axios.post('http://localhost:5000/signup', {
          name: this.name,
          username: this.email,
          password: this.password,
        });
        console.log(response.data.message);
        this.$router.push('/login');
      } catch (error) {
        console.error('Registration error:', error.response.data.error);
        alert(error.response.data.error || 'An error occurred during registration.');
      }
    },
  },
};
</script>

<style scoped>
.signup-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: linear-gradient(135deg, #000000, #000000);
}

.signup-box {
  background-color: rgba(46, 46, 46, 0.9);
  padding: 2.5rem;
  border-radius: 15px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
  width: 320px;
  text-align: center;
  transition: transform 0.2s;
}

.signup-box:hover {
  transform: scale(1.02);
}

h2 {
  margin-bottom: 1.5rem;
  color: #fcfcfc;
}

.form-group {
  margin-bottom: 1.5rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
  color: #ffffff;
}

input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-sizing: border-box;
  transition: border-color 0.3s;
}

input:focus {
  border-color: #4ed5b1;
  outline: none;
}

.signup-btn {
  width: 100%;
  padding: 0.75rem;
  background-color: #4ed5b1;
  color: #ffffff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.2s;
}

.signup-btn:hover {
  background-color: #3abf97;
  transform: translateY(-2px);
}

p {
  margin-top: 1.5rem;
  color: #d1d1d1;
}

.login-link {
  color: #e2dc41;
  text-decoration: none;
}

.login-link:hover {
  text-decoration: underline;
  color: #f1e54d;
}
</style>
