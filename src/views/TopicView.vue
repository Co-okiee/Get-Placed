<template>
    <div class="topic-container">
      <div class="navigation-header">
        <button @click="goBack" class="back-button">
          <span class="back-icon">←</span>
          Back to Topics
        </button>
      </div>
  
      <div class="content-navigation">
        <button 
          v-for="type in contentTypes" 
          :key="type.id"
          @click="setContentType(type.id)"
          :class="['nav-button', contentType === type.id ? 'active' : '']"
        >
          {{ type.label }}
        </button>
      </div>
  
      <topic-content 
        :topic="topic"
        :content-type="contentType"
      />
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  import TopicContent from '@/components/TopicContent.vue';
  
  export default {
    name: 'TopicView',
    components: {
      TopicContent
    },
    props: {
      topic: {
        type: String,
        required: true
      }
    },
    setup() {
      const contentType = ref('overview');
      const contentTypes = [
        { id: 'overview', label: 'Overview' },
        { id: 'implementation', label: 'Implementation' },
        { id: 'practice', label: 'Practice Problems' }
      ];
  
      const setContentType = (type) => {
        contentType.value = type;
      };
  
      const goBack = () => {
        router.push({ name: 'dataStructures' });
      };
  
      return {
        contentType,
        contentTypes,
        setContentType,
        goBack
      };
    }
  };
  </script>
  
  <style scoped>
  .topic-container {
    max-width: 800px;
    margin: 20px auto;
    padding: 20px;
    background-color: #121212;
    border-radius: 10px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.6);
  }
  
  .navigation-header {
    margin-bottom: 20px;
  }
  
  .back-button {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    background: white;
    border: 1px solid #e2e8f0;
    padding: 0.75rem 1.5rem;
    border-radius: 8px;
    color: #1e293b;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s ease;
  }
  
  .back-button:hover {
    background: #f1f5f9;
    transform: translateX(-4px);
  }
  
  .back-icon {
    font-size: 1.2rem;
  }
  
  .content-navigation {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-bottom: 30px;
  }
  
  .nav-button {
    background-color: #1f1f1f;
    color: #e0e0e0;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    cursor: pointer;
    transition: all 0.3s ease;
  }
  
  .nav-button.active {
    background-color: #ffcc00;
    color: #121212;
  }
  
  .nav-button:hover {
    background-color: #ffcc00;
    color: #121212;
  }
  </style>