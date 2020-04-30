<template>
  <div>
    <NavBar></NavBar>
    <v-container fluid>
      <v-layout wrap lg6 md6 sm6 xs12>
        <v-card class="mx-auto justify-center text-center" elevation="1">
          <v-card-title
            class="display-1 justify-center text-center font-weight-regular "
          >
            Login
          </v-card-title>

          <v-card-text>
            <v-text-field
              label="아이디"
              value
              v-model="identify"
            ></v-text-field>
          </v-card-text>
          <v-card-text>
            <v-text-field
              label="비밀번호"
              type="password"
              v-model="password"
            ></v-text-field>
          </v-card-text>

          <v-divider></v-divider>

          <v-card-actions>
            <v-btn text @click="back">Back</v-btn>
            <v-spacer></v-spacer>
            <v-btn color="primary" depressed @click="login()">Login</v-btn>
          </v-card-actions>
        </v-card>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import UserApi from "../apis/UserApi";
import Swal from "sweetalert2";
import NavBar from "../components/NavBar";
export default {
  components: {
    NavBar,
  },
  data: () => ({
    tiles: [
      { img: "keep.png", title: "Keep" },
      { img: "inbox.png", title: "Inbox" },
      { img: "hangouts.png", title: "Hangouts" },
      { img: "messenger.png", title: "Messenger" },
      { img: "google.png", title: "Google+" },
    ],
    step: 1,
    identify: "",
    password: "",
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
        password,
      };
      console.log(identify, password);
      UserApi.requestLogin(
        data,
        (res) => {
          let id = res.data.id;
          let identify = res.data.identify;
          let name = res.data.name;
          let nickname = res.data.nickname;
          let image = res.data.image;
          UserApi.requestLike(
            id,
            (res) => {
              console.log("내가 좋아요 한 데이터 :: ", res.data);
              let mylikecar = res.data;
              console.log("mylikecar ::", mylikecar);
              sessionStorage.setItem("mylikecars", JSON.stringify(mylikecar));
              console.log(mylikecar);
            },
            (error) => {
              console.log(error);
            }
          );
          // let likelist = res.data.object.likelist;
          sessionStorage.setItem("id", id);
          sessionStorage.setItem("identify", identify);
          sessionStorage.setItem("name", name);
          sessionStorage.setItem("nickname", nickname);
          sessionStorage.setItem("image", image);
          sessionStorage.setItem("token", true);

          //sessionStorage.setItem("likelist", likelist);
          // this.getNotice();
          // this.$router.push('/main');
          //요청이 끝나면 버튼 활성화
          this.$router.push("/");
        },
        (error) => {
          this.password = "";
          Swal.fire({
            icon: "error",
            title: "로그인 실패",
            text: "아이디 혹은 비밀번호가 틀렸습니다",
          });
          console.log(error);
        }
      );
    },
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
    },
  },
};
</script>
