<template>
  <v-app>
    <v-app-bar app>
      <v-app-bar-nav-icon @click.stop="overlay = !overlay" />
      <v-app-bar-title @click="homeBtn">AutoSearch</v-app-bar-title>
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
    <v-overlay :value="overlay" opacity="0.8">
      <v-navigation-drawer v-model="overlay" absolute color="transparent" style="position:fixed;">
        <v-layout>
          <v-flex>
            <v-toolbar width="100%" absolute dense color="transparent" style="position:fixed;">
              <v-card color="white" light elevation="0">
                <v-icon @click.stop="overlay = !overlay" style="cursor:pointer;" light>{{ leftArrowIcon }}</v-icon>
              </v-card>
              <!-- mdi-arrow-left, mdi-reply -->
            </v-toolbar>
          </v-flex>
          <v-flex absolute fill-height>
            <v-card fluid color="transparent" elevation="0">
              <br />
              <br />
              <v-list>
                <v-list-item style="cursor:pointer">
                  <v-list-item-content>
                    <v-list-item-title>
                      <span class="display-1 text-shadow font-weight-bold">
                        <div>
                          <p id="effect" @click="moveLoginPage()">로그인</p>
                        </div>
                      </span>
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item style="cursor:pointer">
                  <v-list-item-content>
                    <v-list-item-title>
                      <span class="display-1 text-shadow font-weight-bold">
                        <div>
                          <p id="effect">로그아웃</p>
                        </div>
                      </span>
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item style="cursor:pointer">
                  <v-list-item-content>
                    <v-list-item-title>
                      <span class="display-1 text-shadow font-weight-bold">
                        <div>
                          <p id="effect" @click="moveMyPage()">마이페이지</p>
                        </div>
                      </span>
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-card>
          </v-flex>
        </v-layout>
      </v-navigation-drawer>
    </v-overlay>
    <!-- <v-navigation-drawer v-model="drawer" temporary app overflow>
      <v-content>
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
      </v-content>
    </v-navigation-drawer> -->

    <!-- <v-navigation-drawer v-model="left" fixed temporary /> -->

    <v-content>
      <transition name="fade">
        <router-view :key="$route.fullPath"></router-view>
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
import { mdiArrowLeftThick, mdiCrosshairsGps } from "@mdi/js";
// import {
//   mdiCalendarTextOutline,
//   mdiAccountCircle,
//   mdiHelp,
//   mdiLockOpenVariant,
//   mdiLock,
// } from "@mdi/js";
export default {
  name: "App",
  props: {
    source: String,
  },

  components: {
    BottomNav,
  },

  data: () => ({
    overlay: null,
    selected: "이름",
    left: false,
    keyword: "",
    isLogin: false,
    leftArrowIcon: mdiArrowLeftThick,
    gpsIcon: mdiCrosshairsGps,
    loginRoutePath: "/login",
    myPageRoutePath: "/MyPage",
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
        this.$router.push({
          path: "/search",
          query: { keyword: data.keyword, filter: data.filter },
        });
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
    moveLoginPage() {
      this.overlay = false;
      this.$router.push(this.loginRoutePath);
    },
    moveMyPage() {
      this.overlay = false;
      this.$router.push(this.myPageRoutePath);
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
@import url("https://fonts.googleapis.com/css?family=Black+Han+Sans|Do+Hyeon|Jua|Nanum+Gothic|Sunflower:300");
#effect {
  font-family: "Do Hyeon", sans-serif;
}
#effect::before {
  width: 0;
  transition: width 0.1s ease-out;
}

#effect:hover:before {
  content: "";
  width: 80%;
  height: 80%;
  background-image: linear-gradient(to top, rgb(18, 192, 149) 15%, rgba(0, 0, 0, 0) 30%);
  position: absolute;
  left: 0;
  bottom: 10px;
  z-index: -1;
  will-change: width;
  transform: rotate(-2deg);
  transform-origin: left bottom;
  transition-duration: 0.15s;
}
// #effect {
//   text-transform: uppercase;
//   font-size: 36px;
//   color: white;
//   text-decoration: none;
//   position: relative;
// }
// [class^="link-"] {
//   display: inline-block;
// }
// .toolbarSize {
//   width: 30px;
// }
// .link-7 #effect:before {
//   content: "";
//   border-bottom: solid 1px white;
//   position: absolute;
//   bottom: 0;
//   left: 30%;
//   width: 0;
//   -webkit-transform: scale(0);
//   -moz-transform: scale(0);
//   -ms-transform: scale(0);
//   -o-transform: scale(0);
//   transform: scale(0);
// }
// .link-7 #effect:hover:before {
//   border-bottom: solid thin white;
//   width: 40%;
//   -webkit-animation: heartbeat-x 1.7s infinite ease-in;
//   animation: heartbeat-x 1.7s infinite ease-in;
// }

// .link-7 #effect:hover {
//   -webkit-animation: heartbeat 1.7s infinite ease-in;
//   animation: heartbeat 1.7s infinite ease-in;
// }

// @-webkit-keyframes heartbeat {
//   0% {
//     -webkit-transform: scale(1);
//   }
//   10% {
//     -webkit-transform: scale(1.1);
//   }
//   20% {
//     -webkit-transform: scale(1);
//   }
//   30% {
//     -webkit-transform: scale(1.1);
//   }
//   40% {
//     -webkit-transform: scale(1);
//   }
// }

// @-webkit-keyframes heartbeat-x {
//   0% {
//     -webkit-transform: scaleX(0);
//   }
//   10% {
//     -webkit-transform: scaleX(1);
//   }
//   20% {
//     -webkit-transform: scaleX(0);
//   }
//   30% {
//     -webkit-transform: scaleX(1);
//   }
//   40% {
//     -webkit-transform: scaleX(0);
//   }
// }

// @keyframes heartbeat {
//   0% {
//     transform: scale(1);
//   }
//   10% {
//     transform: scale(1.1);
//   }
//   20% {
//     transform: scale(1);
//   }
//   30% {
//     transform: scale(1.1);
//   }
//   40% {
//     transform: scale(1);
//   }
// }

// @keyframes heartbeat-x {
//   0% {
//     transform: scaleX(0);
//   }
//   10% {
//     transform: scaleX(1);
//   }
//   20% {
//     transform: scaleX(0);
//   }
//   30% {
//     transform: scaleX(1);
//   }
//   40% {
//     transform: scaleX(0);
//   }
// }
</style>
