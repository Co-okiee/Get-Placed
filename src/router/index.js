import { createRouter, createWebHistory } from "vue-router";

// Import necessary components
import Dashboard from "../views/Dashboard.vue"; // Dashboard will be the home component
import Study from "../views/Study.vue"; // Study page component
import DataStructures from "../views/DataStructures.vue"; // Data Structures page component
import Arrays from "../views/Arrays.vue"; // Arrays page component
import Matrix from "../views/Matrix.vue";
import Strings from "../views/Strings.vue"; // Matrix page component
import Login from "../views/Login.vue"; // Login page component
import Signup from "../views/Signup.vue"; // Signup page component
import NotFound from "../views/NotFound.vue"; // Not Found page component
import CompanyCodingPage from "../views/CompanyCodingPage.vue"; // Component for company coding questions
import QuizOptions from "../views/QuizOptions.vue"; // Component for quiz options
import TopicWise from "../views/TopicWise.vue"; // Topic Wise Quiz page component
import ArrayQuiz from "../views/ArrayQuiz.vue"; // Array Quiz page component
import LinkedLists from "../views/LinkedLists.vue";
import Stack from "../views/Stack.vue";
import Queue from "../views/Queue.vue";
import Tree from "../views/Tree.vue";
import Graph from "../views/Graph.vue";
import Hashing from "../views/Hashing.vue";
import Heap from "../views/Heap.vue";
import ADS from "../views/ADS.vue";
import Map from "../views/Map.vue";
import Set from "../views/Set.vue";

// Create router instance
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/", // Home path
      name: "home",
      component: Dashboard, // Dashboard will be the home component
    },
    {
      path: "/study",
      name: "study",
      component: Study, // Study page component
    },
    {
      path: "/data-structures",
      name: "data-structures",
      component: DataStructures, // Data Structures page component
    },
    {
      path: "/arrays",
      name: "arrays",
      component: Arrays, // Arrays page component
    },
    {
      path: '/matrix', // Add this route for the Matrix component
      name: 'matrix',
      component: Matrix,
    },
    {
      path: '/strings', // Add this route for the Matrix component
      name: 'strings',
      component: Strings,
    },
    {
      path: '/linkedlists', // Add this route for the Matrix component
      name: 'linkedlists',
      component: LinkedLists,
    },
    {
      path: '/stack', // Add this route for the Matrix component
      name: 'stack',
      component: Stack,
    },
    {
      path: '/queue', // Add this route for the Matrix component
      name: 'queue',
      component: Queue,
    },
    {
      path: '/tree', // Add this route for the Matrix component
      name: 'tree',
      component: Tree,
    },
    {
      path: '/heap', // Add this route for the Matrix component
      name: 'heap',
      component: Heap,
    },
    {
      path: '/hashing', // Add this route for the Matrix component
      name: 'hashing',
      component: Hashing,
    },
    {
      path: '/graph', // Add this route for the Matrix component
      name: 'graph',
      component: Graph,
    },
    {
      path: '/set', // Add this route for the Matrix component
      name: 'set',
      component: Set,
    },
    {
      path: '/map', // Add this route for the Matrix component
      name: 'map',
      component: Map,
    },
    
    {
      path: '/ADS', // Add this route for the Matrix component
      name: 'ADS',
      component: ADS,
    },
    {
      path: "/topic-wise-quiz",
      name: "topic-wise-quiz",
      component: TopicWise, // Topic Wise Quiz page component
    },
    {
      path: "/array-quiz",
      name: "array-quiz",
      component: ArrayQuiz, // Array Quiz page component
    },
    
    {
      path: "/login",
      name: "login",
      component: Login, // Login page component
    },
    {
      path: "/signup",
      name: "signup",
      component: Signup, // Signup page component
    },
    {
      path: "/question/:id", // Dynamic route for questions
      name: "question",
      component: () => import("../views/Question.vue"), // Lazy-loaded Question component
    },
    {
      path: "/quiz-options",
      name: "quiz-options", // Route name for QuizOptions
      component: QuizOptions, // Component for quiz options
    },
    {
      path: "/company-coding",
      name: "company-coding", // Route for company coding questions
      component: CompanyCodingPage, // Component for company coding questions
    },
    {
      path: "/:pathMatch(.*)*", // Catch-all route for 404 Not Found
      name: "notfound",
      component: NotFound, // Not Found page component
    },
  ],
});

// Export the router instance
export default router;
