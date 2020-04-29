<template>
  <div class="text-center">
    <h1>회원 가입</h1>

    <v-card class="mx-auto" max-width="500">
      <v-card-title class="title font-weight-regular justify-space-between">
        <span>{{ currentTitle }}</span>
        <v-avatar color="primary lighten-2" class="subheading white--text" size="24"></v-avatar>
      </v-card-title>

      <v-window>
        <v-card-text>
          <v-text-field label="아이디" v-model="id" value></v-text-field>
          <v-text-field label="비밀번호" type="password" v-model="password"></v-text-field>
          <v-text-field label="비밀번호 확인" type="password" v-model="passwordConfirm"></v-text-field>
          <v-text-field label="e-mail" value v-model="email"></v-text-field>
        </v-card-text>
        <div class="pa-4 text-center">
          <v-img
            class="mb-4"
            contain
            height="128"
            src="https://post-phinf.pstatic.net/MjAxOTAzMjBfMjY5/MDAxNTUzMDQ4MzgwMzgy.NdWfUZlmPgEr6I_MPh_OiDo9z2ewjX0dTvFz6Pc-ZBEg.Luu3cMmPBUTndKLJe5FGAaz1SiR9hCLbisWYCDIybg0g.JPEG/335790_17345_2048.jpg?type=w1200"
          ></v-img>
          <h3 class="title font-weight-light mb-2">Welcome to AutoSearch</h3>
          <span class="caption grey--text">Thanks for signing up!</span>
        </div>
      </v-window>

      <v-divider></v-divider>

      <v-card-actions>
        <router-link :to="{ name: 'main' }">
          <v-btn>Back</v-btn>
        </router-link>
        <v-spacer></v-spacer>
        <router-link :to="{ name: 'login' }">
          <v-btn>Next</v-btn>
        </router-link>
      </v-card-actions>
    </v-card>

    <v-btn color="blue" dark @click="sheet = !sheet">회원 가입 약관 보기</v-btn>
    <v-bottom-sheet v-model="sheet">
      <v-sheet class="text-center" height="200px">
        <v-btn class="mt-6" text color="red" @click="sheet = !sheet">close</v-btn>
        <div class="py-3">
          회원가입 정보는 가입일로부터 3년간 보관됩니다. 아이디는 9자리 이상, 비밀번호는 특수문자+숫자+영어의 조합으로 10자리 이상 만들어주십시오.
        </div>
      </v-sheet>
    </v-bottom-sheet>
  </div>
</template>

<script>
export default {
  data: () => ({
    sheet: false,
    id: "",
    password: "",
    passwordConfirm: "",
    email: "",
    passwordValid: false,
    idValid: false,
    signUpValid: false,
  }),
  methods: {
    checkId() {
      if (16 >= this.id.length >= 8) {
        this.idValid = true;
      } else {
        this.idValid = false;
      }
    },
    checkPwd() {
      if (this.password == this.passwordConfirm) {
        this.passwordValid = true;
      }
    },
    signUp() {
      if (this.id) {
      }
    },
  },
};
</script>
