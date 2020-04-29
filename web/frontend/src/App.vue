<template>
  <v-app id="inspire" class="viewport">
    <v-app-bar app clipped-left>
      <v-app-bar-nav-icon class="left-drawer" @click.stop="drawer = !drawer" />
      <v-app-bar-title @click="homeBtn" class="left-drawer">AutoSearch</v-app-bar-title>
      <v-spacer />

      <select v-model="selected" class="filter">
        <option>이름</option>
        <option>제조사</option>
      </select>
      <v-text-field flat solo-inverted hide-details label="Search" v-model="keyword" @keyup.enter="search(keyword)"></v-text-field>
      <v-btn @click="search(keyword)">
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-spacer />
      <!-- <v-toolbar-items>
        <v-btn text>홈</v-btn>
        <v-btn text>로그인</v-btn>
      </v-toolbar-items> -->
    </v-app-bar>

    <v-navigation-drawer class="left-drawer" v-model="drawer" :clipped="$vuetify.breakpoint.lgAndUp" app>
      <v-list dense>
        <v-list-item v-if="isLogin">
          <v-list-item-icon>
            <v-icon>mdi-logout-variant</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>로그아웃</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item v-else to="/login">
          <v-list-item-icon>
            <v-icon>mdi-login-variant</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>로그인</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item to="/MyPage">
          <v-list-item-icon>
            <v-icon>mdi-account</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>마이페이지</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <!-- <v-navigation-drawer v-model="left" fixed temporary /> -->

    <v-content>
      <transition name="fade">
        <router-view></router-view>
      </transition>
    </v-content>

    <BottomNav class="bottom-nav" />
    <!-- <v-footer app color="blue-grey" class="white--text">
      <span>SSAFY</span>
      <v-spacer />
      <span>&copy; 2020</span>
    </v-footer> -->
  </v-app>
</template>

<script>
import BottomNav from "./components/BottomNav";
export default {
  name: "App",
  props: {
    source: String,
  },

  components: {
    BottomNav,
  },

  data: () => ({
    drawer: null,
    selected: "이름",
    left: false,
    keyword: "",
    isLogin: false,
  }),
  methods: {
    search(keyword) {
      const data = { keyword: keyword, filter: this.selected };

      // console.log(this.$route);
      console.log("fullpath:", this.$router.currentRoute.path);
      console.log("data, query:", data, this.$route.query.keyword);
      if (this.$router.currentRoute.path == `/search` && this.$route.query.keyword == data.keyword) {
        console.log("refreash");
        this.$router.go(0);
      } else {
        console.log("push to search");
        this.$router.push({ path: "/search", query: { keyword: data.keyword, filter: data.filter } });
      }
    },
    homeBtn() {
      // console.log(this.$router.currentRoute.path);
      if (this.$router.currentRoute.path === "/") {
        this.$router.go(0);
      } else {
        this.$router.push("/");
      }
    },
  },
  // watch: {
  //   keyword: function() {
  //     console.log(this.keyword);
  //   },
  // },
};
</script>

<style lang="scss" scoped>
@media (min-width: 1367px) {
  .bottom-nav {
    display: none;
  }
}
@media (max-width: 1366px) {
  .left-drawer {
    display: none;
  }
}
.filter {
  border: 1px solid black;
}
.slide-fade-enter {
  transform: translateX(10px);
  opacity: 0;
}
.slide-fade-enter-active,
.slide-fade-leave-active {
  transition: opacity 0.5s ease-out;
}
.fade-enter {
  opacity: 0;
}
.fade-enter-active {
  transition: opacity 0.5s ease-out;
}
.fade-leave-active {
  transition: opacity 0.5s ease-out;
}
.fade-leave-to {
  opacity: 0;
}
</style>
