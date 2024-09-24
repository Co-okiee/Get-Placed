<template>
    <div class="login">
      <h2>Login</h2>
      <form @submit.prevent="loginUser">
        <div>
          <label for="email">Email:</label>
          <input v-model="email" type="email" id="email" required />
        </div>
        <div>
          <label for="password">Password:</label>
          <input v-model="password" type="password" id="password" required />
        </div>
        <button type="submit">Login</button>
      </form>
      <p>Don't have an account? <router-link to="/signup">Sign Up</router-link></p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        email: '',
        password: '',
      };
    },
    methods: {
      loginUser() {
        // Add your login logic here, e.g., API call to authenticate user
        console.log('Logging in with:', this.email, this.password);
        // Example API call (replace with actual API endpoint):
        // axios.post('api/login', { email: this.email, password: this.password })
        //   .then(response => {
        //     // Handle successful login
        //   })
        //   .catch(error => {
        //     // Handle login error
        //   });
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add your styles here */
  </style>
  