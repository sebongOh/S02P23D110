<template>
  <div>
    <v-layout row wrap>
      <v-flex xs12 lg4 class="text-center">
        <v-avatar class="profile" color="grey" size="164">
          <v-img contain src="user.image"></v-img>
        </v-avatar>
      </v-flex>

      <v-flex xs12 lg8>
        <v-list>
          <v-list-item>
            <v-list-item-icon>
              <v-icon color="indigo">mdi-phone</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{user.identify}}</v-list-item-title>
              <v-list-item-subtitle>identify</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>

          <v-list-item>
            <v-list-item-icon>
              <v-icon color="indigo">mdi-human</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{user.name}}</v-list-item-title>
              <v-list-item-subtitle>name</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-icon>
              <v-icon color="indigo">mdi-phone</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{user.nickname}}</v-list-item-title>
              <v-list-item-subtitle>nickname</v-list-item-subtitle>
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
    <v-dialog v-model="MyInfoVisible" persistent max-width="600px">
      <v-card>
        <v-card-title>
          <span class="headline">User Profile</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field label="identify*" readonly="user.id" v-model="user.identify"></v-text-field>
              </v-col>

              <v-col cols="12">
                <v-text-field label="name*" required v-model="user.name"></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field label="Password*" type="password" required></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field label="nickname*" required v-model="user.nickname"></v-text-field>
              </v-col>
            </v-row>
          </v-container>
          <small>*indicates required field</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="MyInfoBtnClick() ">Close</v-btn>
          <v-btn color="blue darken-1" text @click="MyInfoBtnClick() ">Save</v-btn>
        </v-card-actions>
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
      user: {
        id: sessionStorage.getItem("id"),
        identify: sessionStorage.getItem("identify"),
        name: sessionStorage.getItem("name"),
        nickname: sessionStorage.getItem("nickname"),
        image: sessionStorage.getItem("image")
      },
      update: {
        identify: "",
        name: "",
        nickname: "",
        image: ""
      },

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