<template>
  <v-card max-width="344" class="mx-auto">
    <v-img :src="imagelink" height="194"></v-img>

    <v-list-item>
      <v-list-item-content>
        <v-list-item-title class="headline">{{ name }}</v-list-item-title>
      </v-list-item-content>
    </v-list-item>
    <v-card-text>
      <p>제조사: {{ company }}</p>
      <p>공인연비: {{ fuel_eff }}</p>
      <p>연료: {{ engine }}</p>
    </v-card-text>
    <v-card-actions>
      <v-btn text color="deep-purple accent-4" @click="goDetail(id)">상세정보</v-btn>
      <v-spacer></v-spacer>
      <v-btn @click="like">
        <v-icon>{{ icon }}</v-icon>
        <v-icon>mdi-heart-outline</v-icon>
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import UserApi from "../apis/UserApi";
export default {
  name: "carCard",
  props: ["id", "imagelink", "name", "company", "price", "fuel_eff", "engine"],
  created() {
    this.getLikeInfo();
  },
  data: () => ({
    isLike: false,
    icon: "mdi-heart-outline",
  }),
  methods: {
    goDetail(idx) {
      this.$router.push({ path: "/detail", query: { id: idx } });
    },
    getLikeInfo() {
      const likList = sessionStorage.getItem("likeList");

      if (this.id in likList) {
        this.isLike = true;
      } else {
        this.isLike = false;
      }
    },
    like() {
      this.isLike = !this.isLike;
      const data = {
        carId: this.id,
        userId: sessionStorage.getItem("id"),
      };
      if (this.isLike) {
        this.icon = "mdi-heart";
        UserApi.requestLike(
          data,
          (res) => {
            const carItemList = res.data;
            for (const idx in carItemList) {
              const carItem = carItemList[idx];
              this.carItems.push(carItem);
              console.log(carItem);
            }
          },
          (error) => {
            console.log(error);
          }
        );
      } else {
        this.icon = "mdi-heart-outline";
      }
    },
  },
  watch: {
    iconWatch: function() {
      this.isLike;
    },
  },
};
</script>

<style>
.bottom-gradient {
  background-image: linear-gradient(to top, rgba(0, 0, 0, 0.4) 0%, transparent 72px);
}

.repeating-gradient {
  background-image: repeating-linear-gradient(-45deg, rgba(255, 0, 0, 0.25), rgba(255, 0, 0, 0.25) 5px, rgba(0, 0, 255, 0.25) 5px, rgba(0, 0, 255, 0.25) 10px);
}
</style>
