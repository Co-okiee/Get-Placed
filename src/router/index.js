import { createRouter, createWebHistory } from "vue-router";

// Import necessary components
import Dashboard from "../views/Dashboard.vue"; // Dashboard as home component
import Study from "../views/Study.vue"; // Study page component
import DataStructures from "../views/DataStructures.vue"; // Data Structures page component
import Arrays from "../views/Arrays.vue"; // Arrays page component
import Matrix from "../views/Matrix.vue"; // Matrix page component
import Login from "../views/Login.vue"; // Login page component
import Signup from "../views/Signup.vue"; // Signup page component
import NotFound from "../views/NotFound.vue"; // Not Found page component
import CompanyCodingPage from "../views/CompanyCodingPage.vue"; // Company coding questions component
import QuizOptions from "../views/QuizOptions.vue"; // Quiz options component
import TopicWise from "../views/TopicWise.vue"; // Topic Wise Quiz component
import ArrayQuiz from "../views/ArrayQuiz.vue"; // Array Quiz component
import MockInterview from "../views/MockInterview.vue"; // Mock Interview component
import UploadResume from "../views/UploadResume.vue"; // Upload Resume component
import VideoCapture from "../views/VideoCapture.vue"; // Video Capture component
import TrackProgress from "../views/TrackProgress.vue"; // Track Progress component

// Create router instance
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/", // Home path
      name: "home",
      component: Dashboard, // Dashboard as the home component
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
      path: "/mock-interview",
      name: "mock-interview",
      component: MockInterview, // Mock Interview page component
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
      path: "/matrix",
      name: "matrix",
      component: Matrix, // Matrix page component
    },
    {
      path: "/upload-resume",
      name: "upload-resume",
      component: UploadResume, // Upload Resume component
    },
    {
      path: "/video-capture",
      name: "video-capture",
      component: VideoCapture, // Video Capture component
    },
    {
      path: "/topic-wise-quiz",
      name: "topic-wise-quiz",
      component: TopicWise, // Topic Wise Quiz page component
    },
    {
      path: "/quiz-options",
      name: "quiz-options",
      component: QuizOptions, // Quiz Options component
    },
    {
      path: "/company-coding",
      name: "company-coding",
      component: CompanyCodingPage, // Company Coding Questions component
    },
    {
      path: "/array-quiz",
      name: "array-quiz",
      component: ArrayQuiz, // Array Quiz component
    },
    {
      path: "/question/:id", // Dynamic route for questions
      name: "question",
      component: () => import("../views/Question.vue"), // Lazy-loaded Question component
    },
    {
      path: "/track-progress", // New route for Track Progress
      name: "track-progress",
      component: TrackProgress, // Track Progress component
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
