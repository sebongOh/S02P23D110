<template>
  <div>
    <v-layout row wrap>
      <v-flex xs12 lg4 class="text-center">
        <v-avatar class="profile" color="grey" size="164">
          <v-img contain src="https://cdn.vuetifyjs.com/images/cards/store.jpg"></v-img>
        </v-avatar>
      </v-flex>

      <v-flex xs12 lg8>
        <v-list>
          <v-list-item>
            <v-list-item-icon>
              <v-icon color="indigo">mdi-human</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>SungUk Hong</v-list-item-title>
              <v-list-item-subtitle>name</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-icon>
              <v-icon color="indigo">mdi-phone</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>(650) 555-1234</v-list-item-title>
              <v-list-item-subtitle>Mobile</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list>
        <v-list>
          <v-list-item>
            <v-btn @click="MyInfoBtnClick()">내 정보 수정</v-btn>
          </v-list-item>
        </v-list>
      </v-flex>
    </v-layout>
    <v-dialog
      v-model="MyInfoVisible"
      hide-overlay
      transition="dialog-bottom-transition"
      width="50vh"
    >
      <v-card>
        <v-toolbar color="transparent">
          <v-btn icon>
            <v-icon @click="MyInfoVisible=false">mdi-close</v-icon>
          </v-btn>
          <v-spacer></v-spacer>
        </v-toolbar>
        <v-card-text>
          <v-text-field label="아이디" value></v-text-field>
          <v-text-field label="비밀번호" type="password"></v-text-field>
          <v-text-field label="비밀번호 확인" type="password"></v-text-field>
          <v-text-field label="e-mail" value></v-text-field>
          <v-text-field label="주소" value></v-text-field>
          <v-text-field label="생년월일" value></v-text-field>
        </v-card-text>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
// import MyInfoDialog from "../components/MyInfoDialog";
export default {
  name: "MyProfile",
  components: {
    // MyInfoDialog
  },
  data() {
    return {
      MyInfoVisible: false
    };
  },
  mounted() {},
  methods: {
    MyInfoBtnClick() {
      this.MyInfoVisible = !this.MyInfoVisible;
    }
  }
};
</script>

<style>
</style>