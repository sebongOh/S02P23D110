import Vue from "vue";
import Router from "vue-router";
import main from "./views/content/main";
import result from "./views/content/aiResult";
import search from "./views/content/search";
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
      path: "/result",
      name: "result",
      component: result,
    },
    {
      path: "/search",
      name: "search",
      component: search,
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

// router.beforeEach((to, from, next) => {
//   // console.log(from.params, to.params);
//   console.log("to:", to.path);
//   console.log("from:", from.path);
//   if (from.path === to.path && from.params === to.params) {
//     this.$router.go(0);
//   } else {
//     next();
//   }
// });

export default router;
