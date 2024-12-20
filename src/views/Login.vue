<template>
  <div class="login">
    <h1>Login</h1>
    <form @submit.prevent="handleLogin">
      <input
        type="text"
        v-model="username"
        placeholder="Enter your username"
        required
      />
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
import { useUserStore } from "@/store";

export default {
  name: "Login",
  data() {
    return {
      username: "",
    };
  },
  methods: {
    handleLogin() {
      const store = useUserStore();
      store.login(this.username);
      this.$router.push({ name: "quiz" });
    },
  },
};
</script>
