<!-- App.vue -->
<template>
  <div class="min-h-screen bg-white px-4 py-8 md:px-8 lg:px-16">
    <div class="container mx-auto max-w-7xl">
      <div class="bg-white rounded-3xl shadow-2xl border border-gray-100 overflow-hidden">
        <!-- Colorful Gradient Header -->
        <div class="bg-gradient-to-r from-blue-600 to-indigo-700 p-6 text-white">
          <div class="flex items-center justify-between">
            <div class="flex items-center">
              <BookIcon class="mr-4 w-12 h-12 text-yellow-300" />
              <h1 class="text-4xl font-extrabold tracking-tight flex items-center">
                AI Learning Companion
                <span class="ml-3 text-sm bg-yellow-400 text-blue-900 px-2 py-1 rounded-full">
                  Beta
                </span>
              </h1>
            </div>
            <div class="hidden md:block text-blue-100">
              Discover, Learn, and Master Data Structures
            </div>
          </div>
        </div>

        <!-- Main Content Area -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 p-6">
          <!-- Interactive Topics Sidebar -->
          <div class="bg-gray-50 rounded-2xl p-5 border border-gray-200 shadow-sm">
            <div class="mb-6 flex items-center">
              <RocketIcon class="w-7 h-7 mr-3 text-blue-600" />
              <h2 class="text-2xl font-bold text-gray-800">Learning Paths</h2>
            </div>

            <div class="space-y-3">
              <div 
                v-for="(subtopics, topic) in topics" 
                :key="topic" 
                class="topic-group"
              >
                <button 
                  @click="toggleTopic(topic)"
                  class="w-full text-left flex justify-between items-center p-4 rounded-xl transition-all duration-300 
                  hover:bg-gradient-to-r hover:from-blue-100 hover:to-indigo-100
                  focus:outline-none focus:ring-2 focus:ring-blue-300"
                  :class="{
                    'bg-gradient-to-r from-blue-100 to-indigo-100 text-blue-800 shadow-md': expandedTopics[topic],
                    'text-gray-700 bg-white hover:bg-gray-50': !expandedTopics[topic]
                  }"
                >
                  <span class="font-semibold">{{ topic }}</span>
                  <ChevronRightIcon 
                    v-if="!expandedTopics[topic]" 
                    class="w-6 h-6 text-gray-500 transform transition-transform" 
                  />
                  <ChevronDownIcon 
                    v-else 
                    class="w-6 h-6 text-blue-600 transform transition-transform" 
                  />
                </button>

                <transition 
                  enter-active-class="transition duration-300 ease-out"
                  enter-from-class="opacity-0 -translate-y-2"
                  enter-to-class="opacity-100 translate-y-0"
                  leave-active-class="transition duration-200 ease-in"
                  leave-from-class="opacity-100 translate-y-0"
                  leave-to-class="opacity-0 -translate-y-2"
                >
                  <div 
                    v-if="expandedTopics[topic]" 
                    class="bg-white rounded-b-xl shadow-sm border border-gray-100 p-2 mt-1 space-y-1"
                  >
                    <button 
                      v-for="subtopic in subtopics" 
                      :key="subtopic"
                      @click="generateNotes(topic, subtopic)"
                      class="w-full text-left px-4 py-3 rounded-lg text-sm transition-all duration-200 
                      hover:bg-gradient-to-r hover:from-blue-50 hover:to-indigo-50 
                      hover:text-blue-800 hover:shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-200"
                      :class="{
                        'bg-gradient-to-r from-blue-100 to-indigo-100 text-blue-900 shadow-sm': selectedTopic === `${topic} - ${subtopic}`
                      }"
                    >
                      {{ subtopic }}
                    </button>
                  </div>
                </transition>
              </div>
            </div>
          </div>

          <!-- Notes Display Area -->
          <div class="md:col-span-2 bg-white rounded-2xl border border-gray-200 p-6 shadow-sm">
            <div class="mb-6 flex items-center justify-between">
              <h2 class="text-3xl font-bold text-gray-800">
                {{ selectedTopic || 'Select a Learning Path' }}
              </h2>
              <button 
                v-if="notes"
                @click="copyToClipboard" 
                class="text-blue-600 hover:bg-blue-50 p-3 rounded-full transition-all duration-300 
                focus:outline-none focus:ring-2 focus:ring-blue-300 flex items-center"
              >
                <CopyIcon class="w-6 h-6" />
                <span class="ml-2 text-sm hidden md:block">Copy Notes</span>
              </button>
            </div>

            <!-- Loading State -->
            <div v-if="loading" class="flex items-center justify-center h-64">
              <div class="animate-pulse flex space-x-4">
                <div class="rounded-full bg-blue-400 h-12 w-12"></div>
                <div class="flex-1 space-y-4 py-1">
                  <div class="h-4 bg-blue-400 rounded w-3/4"></div>
                  <div class="space-y-3">
                    <div class="h-4 bg-blue-400 rounded"></div>
                    <div class="h-4 bg-blue-400 rounded w-5/6"></div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Notes Content -->
            <div 
              v-else-if="notes" 
              class="prose max-w-none bg-gray-50 p-6 rounded-xl border border-gray-200"
            >
              <div class="whitespace-pre-wrap">{{ notes }}</div>
            </div>

            <!-- Empty State -->
            <div 
              v-else 
              class="h-64 flex flex-col items-center justify-center text-center text-gray-400"
            >
              <RocketIcon class="w-20 h-20 mb-4 text-blue-300" />
              <p class="text-2xl font-medium">
                Choose a topic to start your learning journey!
              </p>
              <p class="mt-2 text-gray-500 text-sm">
                Explore comprehensive programming notes across various topics
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import { 
  BookIcon, 
  RocketIcon, 
  ChevronRightIcon, 
  ChevronDownIcon, 
  CopyIcon 
} from 'lucide-vue-next'

// Topics configuration
const topics = {
    "Arrays": ["Introduction to Arrays", "Array Operations", "Multi-dimensional Arrays", "Array Algorithms"],
    "Matrix": ["Matrix Basics", "Matrix Operations", "Special Matrices", "Matrix Applications"],
    "Advanced Data Structures": ["AVL Trees", "Red-Black Trees", "B-Trees", "Segment Trees"],
    "Strings": ["String Basics", "String Algorithms", "Pattern Matching", "String Manipulation"],
    "Linked Lists": ["Singly Linked Lists", "Doubly Linked Lists", "Circular Linked Lists", "Applications"],
    "Stack": ["Stack Operations", "Stack Applications", "Stack Implementations", "Advanced Concepts"],
    "Queue": ["Queue Operations", "Types of Queues", "Queue Applications", "Priority Queues"],
    "Trees": ["Binary Trees", "BST", "Tree Traversals", "Tree Applications"],
    "Heap": ["Min Heap", "Max Heap", "Heap Operations", "Heap Applications"],
    "Hashing": ["Hash Functions", "Collision Resolution", "Hash Tables", "Applications"],
    "Graph": ["Graph Representation", "Graph Traversals", "Shortest Paths", "Graph Algorithms"],
    "Set": ["Set Operations", "Set Implementation", "MultiSet", "Set Applications"],
    "Map": ["Map Basics", "HashMap", "TreeMap", "Map Applications"]
}

// API Configuration
const GROQ_API_KEY = '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'

// Generate prompt function
const generatePrompt = (topic: string, subtopic: string) => `
Generate comprehensive programming notes about ${topic} - ${subtopic}. 
Include the following sections:
1. Introduction and Basic Concepts
2. Key Features and Characteristics
3. Implementation Details
4. Common Operations and Time Complexity
5. Real-world Applications
6. Best Practices and Tips
7. Common Interview Questions

Make the content detailed enough for both beginners and advanced programmers.
`

// Reactive state
const selectedTopic = ref('')
const notes = ref('')
const loading = ref(false)
const error = ref<string | null>(null)
const expandedTopics = reactive<Record<string, boolean>>({})

// Toggle topic expansion
const toggleTopic = (topic: string) => {
    expandedTopics[topic] = !expandedTopics[topic]
}

// Generate notes function
const generateNotes = async (topic: string, subtopic: string) => {
    // Reset previous state
    loading.value = true
    error.value = null
    notes.value = ''
    selectedTopic.value = `${topic} - ${subtopic}`

    try {
        const response = await fetch('https://api.groq.com/openai/v1/chat/completions', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${GROQ_API_KEY}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                model: 'mixtral-8x7b-32768',
                messages: [
                    {
                        role: 'user',
                        content: generatePrompt(topic, subtopic)
                    }
                ],
                temperature: 0.7,
                max_tokens: 2000
            })
        })

        if (!response.ok) {
            throw new Error('Failed to fetch notes. Please check your API key.')
        }

        const data = await response.json()
        
        if (!data.choices || data.choices.length === 0) {
            throw new Error('No response generated. Please try again.')
        }

        notes.value = data.choices[0].message.content
    } catch (err) {
        error.value = err instanceof Error ? err.message : 'An unknown error occurred'
        console.error('Error:', err)
    } finally {
        loading.value = false
    }
}

// Copy notes to clipboard
const copyToClipboard = () => {
    navigator.clipboard.writeText(notes.value)
        .then(() => {
            alert('Notes copied to clipboard!')
        })
        .catch(err => {
            console.error('Failed to copy:', err)
        })
}
</script>

