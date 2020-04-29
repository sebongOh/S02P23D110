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
    items: [
      {
        icon: "keyboard-arrow-up",
        "icon-alt": "keyboard-arrow-down",
        text: "국산차",
        model: true,
        children: [
          {
            name: "현대",
            imgUrl: "https://imgauto-phinf.pstatic.net/20180529_88/auto_1527592677868AxMTJ_PNG/20180529201748_nbVe4EOk.png?type=f40_40",
          }, //현대
          {
            name: "기아",
            imgUrl: "https://imgauto-phinf.pstatic.net/20170707_181/auto_149940895782493s0w_PNG/20170707152915_q71wMr3r.png?type=f40_40",
          }, //기아
          {
            name: "쌍용",
            imgUrl: "https://imgauto-phinf.pstatic.net/20170707_290/auto_14994089867715m7Kc_PNG/20170707152945_ov1NwuMf.png?type=f40_40",
          }, //쌍용
          {
            name: "르노삼성",
            imgUrl: "https://imgauto-phinf.pstatic.net/20170707_188/auto_14994089761732i2AM_PNG/20170707152934_4UQVPJ4f.png?type=f40_40",
          }, //르노삼성
          {
            name: "제네시스",
            imgUrl: "https://imgauto-phinf.pstatic.net/20200210_194/auto_158131011533438Psz_PNG/20200210134830_T0xCqY1D.png?type=f40_40",
          }, //제네시스
        ],
      },
      {
        icon: "keyboard-arrow-up",
        "icon-alt": "keyboard-arrow-down",
        text: "해외차",
        model: false,
        children: [
          {
            name: "쉐보레",
            imgUrl: "https://imgauto-phinf.pstatic.net/20200210_175/auto_15813076774623FdaV_PNG/20200210130752_EvOsbnkP.png?type=f40_40",
          }, // 쉐보레)
          {
            name: "벤츠",
            imgUrl: "https://imgauto-phinf.pstatic.net/20170707_151/auto_1499404806991Xuw2o_PNG/20170707142004_4ANaTv3h.png?type=f40_40",
          }, //벤츠
          {
            name: "BMW",
            imgUrl: "https://imgauto-phinf.pstatic.net/20200310_214/auto_1583815678479PKzIr_PNG/20200310134752_3hMT5CTc.png?type=f40_40",
          }, //bmw
          {
            name: "아우디",
            imgUrl: "https://imgauto-phinf.pstatic.net/20170707_207/auto_1499404828979BICft_PNG/20170707142026_ovRGcdML.png?type=f40_40",
          }, //아우디
          {
            name: "폭스바겐",
            imgUrl: "https://imgauto-phinf.pstatic.net/20200422_10/auto_15875288567367G6VE_PNG/20200422131406_lmRMWJht.png?type=f40_40",
          }, //폭스바겐
          {
            name: "재규어",
            imgUrl: "https://imgauto-phinf.pstatic.net/20200210_83/auto_1581307501553E0yRR_PNG/20200210130456_nFc7LE10.png?type=f40_40",
          }, //재규어
          {
            name: "랜드로버",
            imgUrl: "https://imgauto-phinf.pstatic.net/20170707_56/auto_1499407965482n6u8s_PNG/20170707151243_JgB80ept.png?type=f40_40",
          }, //랜드로버
          {
            name: "볼보",
            imgUrl: "https://imgauto-phinf.pstatic.net/20170707_20/auto_1499407892646zwj3j_PNG/20170707151130_ECGx0tRI.png?type=f40_40",
          }, //볼보
          {
            name: "미니",
            imgUrl: "https://imgauto-phinf.pstatic.net/20170718_248/auto_1500352107292eUlzC_PNG/20170718132824_jfupLnkX.png?type=f40_40",
          }, //미니
          {
            name: "토요타",
            imgUrl: "https://imgauto-phinf.pstatic.net/20170707_157/auto_1499408657856g9GA0_PNG/20170707152416_RYNsQlax.png?type=f40_40",
          }, //토요타
          {
            name: "렉서스",
            imgUrl: "https://imgauto-phinf.pstatic.net/20170707_52/auto_14994086479909zBvg_PNG/20170707152405_Q81trl9v.png?type=f40_40",
          }, //렉서스
          {
            name: "혼다",
            imgUrl: "https://imgauto-phinf.pstatic.net/20170707_163/auto_1499412516283v1k4a_PNG/20170707162834_NTGXoypb.png?type=f40_40",
          }, //혼다
          {
            name: "닛산",
            imgUrl: "https://imgauto-phinf.pstatic.net/20170707_205/auto_1499412137135mBn5U_PNG/20170707162215_NaaURKNg.png?type=f40_40",
          }, //닛산
        ],
      },
    ],
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
