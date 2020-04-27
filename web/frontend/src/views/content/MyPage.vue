<template>
  <div>
    <v-container>
      <!-- 내 프로필 카드 -->
      <v-layout my-5 row wrap>
        <v-flex xs12>
          <MyProfile></MyProfile>
        </v-flex>
      </v-layout>
      <!-- 내 관심 차량 -->
      <v-layout my-5>
        <v-flex lg12 md12 xs12>
          <v-divider />
          <div class="text-center display-1">My Car!!</div>
          <MyLike></MyLike>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import MyProfile from "@/components/MyProfile.vue";
import MyLike from "@/components/MyLike.vue";
export default {
  name: "MyPage",
  components: {
    MyProfile,
    MyLike
  },
  data() {
    return {};
  }
};
</script>

<style>
</style>