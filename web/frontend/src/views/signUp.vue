<template>
  <div class="text-center">
    <h1>회원 가입</h1>

    <v-card class="mx-auto" max-width="500">
      <v-card-title class="title font-weight-regular justify-space-between">
        <span>{{ message }}</span>
      </v-card-title>

      <v-window>
        <v-card-text>
          <v-text-field label="아이디" v-model="userId" value></v-text-field>
          <v-text-field label="비밀번호" type="password" v-model="password"></v-text-field>
          <v-text-field label="비밀번호 확인" type="password" v-model="passwordConfirm"></v-text-field>
          <v-text-field label="이름" v-model="userName" value></v-text-field>
          <v-text-field label="닉네임" v-model="nickName" value></v-text-field>
        </v-card-text>
        <div class="pa-4 text-center">
          <!-- <v-img
            class="mb-4"
            contain
            height="128"
            src="https://post-phinf.pstatic.net/MjAxOTAzMjBfMjY5/MDAxNTUzMDQ4MzgwMzgy.NdWfUZlmPgEr6I_MPh_OiDo9z2ewjX0dTvFz6Pc-ZBEg.Luu3cMmPBUTndKLJe5FGAaz1SiR9hCLbisWYCDIybg0g.JPEG/335790_17345_2048.jpg?type=w1200"
          ></v-img>-->
          <h3 class="title font-weight-light mb-2">Welcome to AutoSearch</h3>
          <span class="caption grey--text">Thanks for signing up!</span>
        </div>
      </v-window>

      <v-divider></v-divider>

      <v-card-actions>
        <v-btn @click="goBack">Back</v-btn>
        <v-spacer></v-spacer>
        <v-btn @click="signUp">SignUp</v-btn>
      </v-card-actions>
    </v-card>

    <v-btn color="blue" dark @click="sheet = !sheet">회원 가입 가이드</v-btn>
    <v-bottom-sheet v-model="sheet">
      <v-sheet class="text-center" height="200px">
        <v-btn class="mt-6" text color="red" @click="sheet = !sheet">close</v-btn>
        <div class="py-3">아이디는 영문 기준 6자리 이상 20자리 이하, 비밀번호는 8자리 이상으로 만들어주십시오.</div>
      </v-sheet>
    </v-bottom-sheet>
  </div>
</template>

<script>
import UserApi from "../apis/UserApi";
import Swal from "sweetalert2";
export default {
  data: () => ({
    sheet: false,
    userId: "",
    password: "",
    passwordConfirm: "",
    userName: "",
    nickName: "",
    passwordValid: false,
    idValid: false,
    isSubmit: false,
    message: ""
  }),
  methods: {
    goBack() {
      this.$router.go(-1);
    },
    checkId() {
      if (20 >= this.userId.length && this.userId.length >= 6) {
        this.idValid = true;
      } else {
        this.idValid = false;
      }
    },
    checkPwd() {
      if (this.password == this.passwordConfirm) {
        this.passwordValid = true;
      } else {
        this.passwordValid = false;
        this.message = "비밀번호가 다릅니다";
      }

      if (this.password.length < 8) {
        this.message = "비밀번호를 8자리 이상으로 작성해주세요";
        this.passwordValid = false;
      } else if (this.passwordConfirm.length == 0) {
        this.message = "비밀번호를 한번 더 입력해주세요";
        this.passwordValid = false;
      }
    },
    checkForm() {
      this.isSubmit = true;
      this.checkId();
      this.checkPwd();

      // console.log("Input:");
      // console.log("ID:", this.userId);
      // console.log("PASSWORD:", this.password);
      // console.log("PASSWORD CONFRIM", this.passwordConfirm);
      // console.log("USERNAME", this.userName);
      // console.log("NICKNAME", this.nickName);
      // console.log("Id check:", this.idValid);
      // console.log("pwd check:", this.passwordValid);

      if (this.idValid == false) {
        this.isSubmit = false;
      }
      if (this.passwordValid == false) {
        this.isSubmit = false;
      }
      if (this.nickName.length == 0) {
        this.message = "닉네임을 입력해주세요";
        this.isSubmit = false;
      }
      if (this.userName.length == 0) {
        (this.message = "이름을 입력해주세요"), (this.isSubmit = false);
      }
      if (this.passwordConfirm.length == 0) {
        this.message = "비밀번호를 한번 더 입력해주세요";
        this.isSubmit = false;
      }
      if (this.password.length == 0) {
        this.message = "비밀번호를 입력해주세요";
        this.isSubmit = false;
      }
      if (this.userId.length == 0) {
        this.message = "아이디를 입력해주세요";
        this.isSubmit = false;
      }
      console.log("Valid Check:", this.isSubmit);
    },
    signUp() {
      this.checkForm();
      if (this.isSubmit == true) {
        let signUpInfo = {
          userId: this.userId,
          password: this.password,
          userName: this.userName,
          nickName: this.nickName
        };
        UserApi.join(signUpInfo);
        this.$router.push("login");
      } else {
        Swal.fire({
          icon: "error",
          title: "회원가입 양식이 올바르지 않습니다"
        });
        return;
      }
    }
  },
  watch: {
    checkValid: function() {
      this.checkForm();
    }
  }
};
</script>
