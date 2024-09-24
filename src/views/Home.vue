<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useCounterStore } from '../stores/counter';
import { getRemoteData, shuffle } from '../lib/utils';
import StarButton from '../components/StartButton.vue';

const store = useCounterStore();
const router = useRouter();

const loading = ref(false);
const error = ref(false);

function startQuiz() {
  console.log('Start Quiz button clicked'); // Debugging log
  store.resetScore();
  store.increment();
  store.setQuestionIndex(0);

  // Navigate to the first question
  router.push('/question/0');
}

onMounted(async () => {
  store.resetQuiz();

  if (import.meta.env.VITE_APP_USE_LOCALDATA === 'true') return;

  loading.value = true;

  try {
    const data = await getRemoteData();
    let raw_questions = data.results || null;

    if (raw_questions) {
      raw_questions = raw_questions.map((item, index) => {
        const answers = [item.correct_answer, ...item.incorrect_answers];
        let choices = answers.map((ans, i) => ({
          id: i,
          text: ans,
        }));

        shuffle(choices);

        return {
          ...item,
          answers,
          id: index,
          text: item.question,
          answer: 0,
          choices,
        };
      });

      store.setQuizData(raw_questions);
    }
  } catch (err) {
    console.error('Error fetching data:', err); // Debugging log
    error.value = true;
  } finally {
    loading.value = false;
  }
});
</script>

<template>
  <div class="container">
    <div v-if="!loading && !error">
      <StarButton @click="startQuiz">Start Quiz</StarButton>
    </div>
    <p v-if="loading">Fetching trivia questions....</p>
    <p v-if="error">Oops, something went wrong!</p>
  </div>
</template>

<style scoped>
.container {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
