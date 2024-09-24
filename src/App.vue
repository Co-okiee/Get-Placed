<script setup>
import { RouterView } from "vue-router";
</script>

<template>
  <RouterView v-slot="{ Component }">
    <transition name="fade" mode="out-in" :duration="{ enter: 300, leave: 200 }">
      <!-- Dynamic component rendering based on the route -->
      <component :is="Component" />
    </transition>
  </RouterView>
</template>

<style>
/* Define the slide-right animation (as in your original) */
.slide-right-enter-active,
.slide-right-leave-active {
  transition: transform 0.2s ease;
}
.slide-right-enter-from,
.slide-right-leave-to {
  transform: translateX(100%);
}

/* Optionally, you can add a fade transition */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
</style>
