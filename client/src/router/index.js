import { createRouter, createWebHashHistory } from "vue-router";
import Survey from "../views/Survey.vue";
import Statistics from "../views/Statistics.vue";

const routes = [
  {
    path: "/:id",
    name: "Survey",
    component: Survey,
  },
  
  {
    path: "/statistics/:id",
    name: "Statistics",
    component: Statistics,
  },
  
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
