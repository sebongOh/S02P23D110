<template>
  <div class="text-center">
    <h1>로그인</h1>

    <v-card class="mx-auto" max-width="500">
      <v-card-title class="title font-weight-regular justify-space-between">
        <span>{{ currentTitle }}</span>
        <v-avatar color="primary lighten-2" class="subheading white--text" size="24" v-text="step"></v-avatar>
      </v-card-title>

      <v-window v-model="step">
        <v-card-text>
          <v-text-field label="아이디" value></v-text-field>
          <span
            class="caption grey--text text--darken-1"
          >This is the id you will use to login to your account</span>
        </v-card-text>
        <v-card-text>
          <v-text-field label="비밀번호" type="password"></v-text-field>
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
        <router-link :to="{name: 'main'}">
          <v-btn :disabled="step === 1" text @click="step--">Back</v-btn>
        </router-link>
        <v-spacer></v-spacer>
        <router-link :to="{name: 'myInformation'}">
          <v-btn :disabled="step === 3" color="primary" depressed @click="step++">Next</v-btn>
        </router-link>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
export default {
  data: () => ({
    sheet: false,
    tiles: [
      { img: "keep.png", title: "Keep" },
      { img: "inbox.png", title: "Inbox" },
      { img: "hangouts.png", title: "Hangouts" },
      { img: "messenger.png", title: "Messenger" },
      { img: "google.png", title: "Google+" }
    ],
    computed: {
      currentTitle() {
        switch (this.step) {
          case 1:
            return "Sign-up";
          case 2:
            return "Create a password";
          default:
            return "Account created";
        }
      }
    }
  })
};
</script>