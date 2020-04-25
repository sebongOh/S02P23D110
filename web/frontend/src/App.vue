<template>
  <v-app id="inspire">
    <v-navigation-drawer v-model="drawerRight" app clipped right>
      <v-list dense>
        <v-list-item @click.stop="right = !right">
          <v-list-item-action>
            <v-icon>mdi-exit-to-app</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>right drawer</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar app clipped-right color="blue-grey" dark>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <!-- <router-link to='/'></router-link> -->
      <v-toolbar-title @click="homeBtn">SearchAuto</v-toolbar-title>
      <v-spacer />
      <v-text-field
        flat
        solo-inverted
        hide-details
        prepend-inner-icon="fa-search"
        label="Search"
        class="hidden-sm-and-down"
        v-model="keyword"
        @keyup.enter="search"
      ></v-text-field>
      <v-btn @click="search">검색</v-btn>
      <v-spacer />
      <v-app-bar-nav-icon @click.stop="drawerRight = !drawerRight" />
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" :clipped="$vuetify.breakpoint.lgAndUp" app>
      <v-list dense>
        <template v-for="item in items">
          <v-layout v-if="item.heading" :key="item.heading" row align-center>
            <v-flex xs6>
              <v-subheader v-if="item.heading">{{ item.heading }}</v-subheader>
            </v-flex>
            <v-flex xs6 class="text-xs-center">
              <a href="#!" class="body-2 black--text">EDIT</a>
            </v-flex>
          </v-layout>
          <v-list-group
            v-else-if="item.children"
            :key="item.text"
            v-model="item.model"
            :prepend-icon="item.model ? item.icon : item['icon-alt']"
            append-icon
          >
            <template v-slot:activator>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>{{ item.text }}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </template>
            <v-list-item v-for="(child, i) in item.children" :key="i" @click="search(child.name)">
              <v-list-item-action v-if="child.icon"></v-list-item-action>
              <v-list-item-avatar>
                <img :src="child.imgUrl" alt />
              </v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-title>{{child.name}}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-group>
          <v-list-item v-else :key="item.name">
            <v-list-item-action>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>{{ item.name }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </template>
      </v-list>
    </v-navigation-drawer>

    <!-- <v-navigation-drawer v-model="left" fixed temporary /> -->

    <v-content>
      <p>autosearch</p>
      <router-view></router-view>
    </v-content>

    <v-navigation-drawer v-model="right" fixed right temporary />

    <v-footer app color="blue-grey" class="white--text">
      <span>SSAFY</span>
      <v-spacer />
      <span>&copy; 2020</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: "App",
  props: {
    source: String
  },

  components: {},

  data: () => ({
    drawer: null,
    drawerRight: null,
    right: false,
    left: false,
    keyword: "",
    items: [
      {
        icon: "keyboard-arrow-up",
        "icon-alt": "keyboard-arrow-down",
        text: "국산차",
        model: true,
        children: [
          {
            name: "현대",
            imgUrl:
              "https://imgauto-phinf.pstatic.net/20180529_88/auto_1527592677868AxMTJ_PNG/20180529201748_nbVe4EOk.png?type=f40_40"
          }, //현대
          {
            name: "기아",
            imgUrl:
              "https://imgauto-phinf.pstatic.net/20170707_181/auto_149940895782493s0w_PNG/20170707152915_q71wMr3r.png?type=f40_40"
          }, //기아
          {
            name: "쌍용",
            imgUrl:
              "https://imgauto-phinf.pstatic.net/20170707_181/auto_149940895782493s0w_PNG/20170707152915_q71wMr3r.png?type=f40_40"
          }, //쌍용
          {
            name: "르노삼성",
            imgUrl:
              "https://imgauto-phinf.pstatic.net/20170707_188/auto_14994089761732i2AM_PNG/20170707152934_4UQVPJ4f.png?type=f40_40"
          }, //르노삼성
          {
            name: "제네시스",
            imgUrl:
              "https://imgauto-phinf.pstatic.net/20200210_194/auto_158131011533438Psz_PNG/20200210134830_T0xCqY1D.png?type=f40_40"
          } //제네시스
        ]
      },
      {
        icon: "keyboard-arrow-up",
        "icon-alt": "keyboard-arrow-down",
        text: "해외차",
        model: false,
        children: [
          {
            name: "쉐보레",
            imgUrl:
              "https://imgauto-phinf.pstatic.net/20200210_175/auto_15813076774623FdaV_PNG/20200210130752_EvOsbnkP.png?type=f40_40"
          }, // 쉐보레)
          {
            name: "벤츠",
            imgUrl:
              "https://imgauto-phinf.pstatic.net/20170707_151/auto_1499404806991Xuw2o_PNG/20170707142004_4ANaTv3h.png?type=f40_40"
          }, //벤츠
          {
            name: "BMW",
            imgUrl:
              "https://imgauto-phinf.pstatic.net/20200310_214/auto_1583815678479PKzIr_PNG/20200310134752_3hMT5CTc.png?type=f40_40"
          }, //bmw
          {
            name: "아우디",
            imgUrl:
              "https://imgauto-phinf.pstatic.net/20170707_207/auto_1499404828979BICft_PNG/20170707142026_ovRGcdML.png?type=f40_40"
          }, //아우디
          {
            name: "폭스바겐",
            imgUrl:
              "https://imgauto-phinf.pstatic.net/20200422_10/auto_15875288567367G6VE_PNG/20200422131406_lmRMWJht.png?type=f40_40"
          }, //폭스바겐
          {
            name: "재규어",
            imgUrl:
              "https://imgauto-phinf.pstatic.net/20200210_83/auto_1581307501553E0yRR_PNG/20200210130456_nFc7LE10.png?type=f40_40"
          }, //재규어
          {
            name: "랜드로버",
            imgUrl:
              "https://imgauto-phinf.pstatic.net/20170707_56/auto_1499407965482n6u8s_PNG/20170707151243_JgB80ept.png?type=f40_40"
          }, //랜드로버
          {
            name: "볼보",
            imgUrl:
              "https://imgauto-phinf.pstatic.net/20170707_20/auto_1499407892646zwj3j_PNG/20170707151130_ECGx0tRI.png?type=f40_40"
          }, //볼보
          {
            name: "미니",
            imgUrl:
              "https://imgauto-phinf.pstatic.net/20170718_248/auto_1500352107292eUlzC_PNG/20170718132824_jfupLnkX.png?type=f40_40"
          }, //미니
          {
            name: "토요타",
            imgUrl:
              "https://imgauto-phinf.pstatic.net/20170707_157/auto_1499408657856g9GA0_PNG/20170707152416_RYNsQlax.png?type=f40_40"
          }, //토요타
          {
            name: "렉서스",
            imgUrl:
              "https://imgauto-phinf.pstatic.net/20170707_52/auto_14994086479909zBvg_PNG/20170707152405_Q81trl9v.png?type=f40_40"
          }, //렉서스
          {
            name: "혼다",
            imgUrl:
              "https://imgauto-phinf.pstatic.net/20170707_163/auto_1499412516283v1k4a_PNG/20170707162834_NTGXoypb.png?type=f40_40"
          }, //혼다
          {
            name: "닛산",
            imgUrl:
              "https://imgauto-phinf.pstatic.net/20170707_205/auto_1499412137135mBn5U_PNG/20170707162215_NaaURKNg.png?type=f40_40"
          } //닛산
        ]
      }
    ]
  }),
  methods: {
    search(keyword) {
      const data = keyword;

      // console.log(this.$route);
      console.log("fullpath:", this.$router.currentRoute.path);
      console.log("data, query:", data, this.$route.query.keyword);
      if (
        this.$router.currentRoute.path == `/search` &&
        this.$route.query.keyword == data
      ) {
        console.log("refreash");
        this.$router.go(0);
      } else {
        console.log("push to search");
        this.$router.push({ path: "/search", query: { keyword: data } });
      }
    },
    homeBtn() {
      // console.log(this.$router.currentRoute.path);
      if (this.$router.currentRoute.path === "/") {
        this.$router.go(0);
      } else {
        this.$router.push("/");
      }
    }
  },
  watch: {
    keyword: function() {
      console.log(this.keyword);
    }
  }
};
</script>
