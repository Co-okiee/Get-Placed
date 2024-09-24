<template>
    <div class="signup">
      <h2>Sign Up</h2>
      <form @submit.prevent="registerUser">
        <div>
          <label for="name">Name:</label>
          <input v-model="name" type="text" id="name" required />
        </div>
        <div>
          <label for="email">Email:</label>
          <input v-model="email" type="email" id="email" required />
        </div>
        <div>
          <label for="password">Password:</label>
          <input v-model="password" type="password" id="password" required />
        </div>
        <button type="submit">Sign Up</button>
      </form>
      <p>Already have an account? <router-link to="/login">Login</router-link></p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        name: '',
        email: '',
        password: '',
      };
    },
    methods: {
      registerUser() {
        // Add your signup logic here, e.g., API call to register user
        console.log('Registering with:', this.name, this.email, this.password);
        // Example API call (replace with actual API endpoint):
        // axios.post('api/register', { name: this.name, email: this.email, password: this.password })
        //   .then(response => {
        //     // Handle successful registration
        //   })
        //   .catch(error => {
        //     // Handle registration error
        //   });
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add your styles here */
  </style>
  