<template>
  <v-container>
    <v-layout my-5>
      <v-flex lg4 sm6 md4 xs12>
        <v-card>
          <img :src="item.imagelink" alt="" width="340vw" />
        </v-card>
      </v-flex>
      <v-flex lg4 sm6 md4 xs12>
        <v-card>
          <v-card-title>{{ item.name }}</v-card-title>
          <v-card-subtitle>제조사: {{ item.company }}</v-card-subtitle>
          <v-card-text>
            <p>분류: {{ item.size }}</p>
            <p>출시가: {{ item.price }}</p>
            <p>연비: {{ item.fuel_eff }}</p>
            <p>연료: {{ item.engine }}</p>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import ContentsApi from "../../apis/ContentsApi";
export default {
  name: "detail",
  //   components: {
  //     carCard,
  //   },
  created() {
    console.log("carId:", this.$route.query.id);
    this.getItemDetail(this.$route.query.id);
  },
  data: () => ({
    item: {},
  }),
  methods: {
    getItemDetail(id) {
      ContentsApi.requestCarDetail(
        id,
        (res) => {
          console.log(res.data);
          this.item = res.data;
        },
        (error) => {
          console.log(error);
        }
      );
    },
  },
};
</script>

<style></style>
