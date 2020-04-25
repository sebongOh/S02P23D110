import Vue from "vue";
import Router from "vue-router";
import main from "./views/content/main";
import login from "./views/login";
import signUp from "./views/signUp";
import myInformation from "./views/myInformation";
import leave from "./views/leave";
// import store from "./vuex/store";

Vue.use(Router);

const router = new Router({
  routes: [
    {
      path: "/",
      name: "main",
      component: main,
    },
    {
      path: "/login",
      name: "login",
      component: login,
    },
    {
      path: "/signUp",
      name: "signUp",
      component: signUp,
    },
    {
      path: "/myInformation",
      name: "myInformation",
      component: myInformation,
    },
    {
      path: "/leave",
      name: "leave",
      component: leave,
    },
  ],
});

// router.beforeEach((to, from, next) => {
//     console.group('to: ', to);
//     console.log('from: ', from);
//     console.log('next: ', next);
//     console.groupEnd();
//     if (to.name === 'Login' || to.name === 'Join' || to.name === 'FindPassword' || to.name === 'NotFound') {
//         console.log('before ', store.state.showNav);
//         store.commit('toggleNav', false);
//         console.log('after ', store.state.showNav);
//     } else {
//         store.commit('toggleNav', true);
//     }

//     next();
// });

export default router;
