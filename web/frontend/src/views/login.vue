<template>
  <div class="text-center">
    <h1>로그인</h1>

    <v-card class="mx-auto" max-width="500">
      <v-card-title class="title font-weight-regular justify-space-between">
        <span>Hello World!</span>
        <v-avatar color="primary lighten-2" class="subheading white--text" size="24"></v-avatar>
      </v-card-title>

      <v-window>
        <v-card-text>
          <v-text-field label="아이디" value v-model="identify"></v-text-field>
          <span
            class="caption grey--text text--darken-1"
          >This is the id you will use to login to your account</span>
        </v-card-text>
        <v-card-text>
          <v-text-field label="비밀번호" type="password" v-model="password"></v-text-field>
          <span class="caption grey--text text--darken-1">Please enter a password for your account</span>
        </v-card-text>
        <div class="pa-4 text-center">
          <v-img
            class="mb-4"
            contain
            height="128"
            src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTaN-ujXAbXuBt9dV8akS1Mgu2_L-nadEpxGUPsvPs_V4ObLIfj&usqp=CAU"
          ></v-img>
          <h3 class="title font-weight-light mb-2">Welcome to AutoSearch</h3>
          <span class="caption grey--text">Thanks for Login!</span>
        </div>
      </v-window>

      <v-divider></v-divider>

      <v-card-actions>
        <v-btn text @click="back">Back</v-btn>
        <v-spacer></v-spacer>
        <v-btn color="primary" depressed @click="login()">Login</v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import UserApi from "../apis/UserApi";
import Swal from "sweetalert2";
export default {
  data: () => ({
    tiles: [
      { img: "keep.png", title: "Keep" },
      { img: "inbox.png", title: "Inbox" },
      { img: "hangouts.png", title: "Hangouts" },
      { img: "messenger.png", title: "Messenger" },
      { img: "google.png", title: "Google+" }
    ],
    step: 1,
    identify: "",
    password: ""
    // idValid:false,
    // passwordValid:false,
  }),
  methods: {
    // changeInput(event, type) {
    //   this.enterInput(event.target.value, type);
    // },
    back() {
      this.$router.go(-1);
    },
    login() {
      let { identify, password } = this;
      let data = {
        identify,
        password
      };
      console.log(identify, password);
      UserApi.requestLogin(
        data,
        res => {
          let id = res.data.id;
          let identify = res.data.identify;
          let name = res.data.name;
          let nickname = res.data.nickname;
          let image = res.data.image;
          // let likelist = res.data.object.likelist;
          sessionStorage.setItem("id", id);
          sessionStorage.setItem("identify", identify);
          sessionStorage.setItem("name", name);
          sessionStorage.setItem("nickname", nickname);
          sessionStorage.setItem("image", image);
          //sessionStorage.setItem("likelist", likelist);
          // this.getNotice();
          // this.$router.push('/main');
          //요청이 끝나면 버튼 활성화
          this.$router.push("/");
        },
        error => {
          this.password = "";
          Swal.fire({
            icon: "error",
            title: "로그인 실패",
            text: "아이디 혹은 비밀번호가 틀렸습니다"
          });
          console.log(error);
        }
      );
    }
  },
  watch: {
    watchLoginColomn: function() {
      // if (this.identify.length >= 9){
      //   this.idValid = true;
      // };
      // if (this.identify.length >= 9){
      //   this.idValid = true;
      // }
      console.log(this.identify);
      console.log(this.password);
    }
  }
};
</script>
