<template>
  <v-container>
    <v-row no-gutters flex>
      <v-col cols="4">
        <v-card>
          <img :src="item.imagelink" alt="" />
        </v-card>
      </v-col>
      <v-col cols="6">
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
      </v-col>
    </v-row>
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
