<template>
  <div class="track-progress">
    <h1>Track Progress</h1>
    <p v-if="!scores || scores.length === 0">
      No scores available. Take a quiz!
    </p>
    <ul v-else>
      <li v-for="(score, index) in scores" :key="index">
        Quiz {{ index + 1 }}: {{ score }}/{{ totalQuestions }}
      </li>
    </ul>
  </div>
</template>

<script>
import { useUserStore } from "@/store";

export default {
  name: "TrackProgress",
  computed: {
    scores() {
      const store = useUserStore();
      return store.scores[store.user];
    },
    totalQuestions() {
      return 2; // Adjust based on your quiz length
    },
  },
};
</script>
