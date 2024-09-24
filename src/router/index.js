import { createRouter, createWebHistory } from "vue-router";

// Import necessary components
import HomeView from "../views/Home.vue"; 
import NotFound from "../views/NotFound.vue";
import NotAllowed from "../views/NotAllowed.vue";
import Login from "../views/Login.vue";
import Signup from "../views/Signup.vue";
import Dashboard from "../views/Dashboard.vue";
import Study from "../views/Study.vue"; 
import DataStructures from "../views/DataStructures.vue"; 
import Home from "../views/Home.vue";
/* Uncomment and import these if needed
import Algorithms from "../views/Algorithms.vue";
import OperatingSystems from "../views/OperatingSystems.vue";
import Databases from "../views/Databases.vue";
import Oops from "../views/Oops.vue";
import Aptitude from "../views/Aptitude.vue";
import Networking from "../views/Networking.vue";
import SystemDesign from "../views/SystemDesign.vue";
*/

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "homeview", // Renamed from 'dashboard' to 'home'
      component: Dashboard, // Dashboard will be the home component
    },
    {
      path: "/study",
      name: "study",
      component: Study,
    },
    {
      path: "/data-structures",
      name: "data-structures",
      component: DataStructures,
    },
    /* Uncomment and add routes for these if needed
    {
      path: "/algorithms",
      name: "algorithms",
      component: Algorithms,
    },
    {
      path: "/operating-systems",
      name: "operating-systems",
      component: OperatingSystems,
    },
    {
      path: "/databases",
      name: "databases",
      component: Databases,
    },
    {
      path: "/oops",
      name: "oops",
      component: Oops,
    },
    {
      path: "/aptitude",
      name: "aptitude",
      component: Aptitude,
    },
    {
      path: "/networking",
      name: "networking",
      component: Networking,
    },
    {
      path: "/system-design",
      name: "system-design",
      component: SystemDesign,
    },
    */
    {
      path: "/login",
      name: "login",
      component: Login,
    },
    {
      path: "/home",
      name: "home",
      component: Home,
    },
    {
      path: "/signup",
      name: "signup",
      component: Signup,
    },
    {
        path: "/question/:id",
        name: "question",
        component: () => import("../views/Question.vue"), // make sure this component exists
    },
    {
      path: "/:pathMatch(.*)*",
      name: "notfound",
      component: NotFound,
    }
  ],
});

export default router;
