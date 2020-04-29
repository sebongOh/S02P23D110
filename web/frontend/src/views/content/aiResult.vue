<template>
<<<<<<< HEAD
  <v-container fluid>
    <v-row>
      <v-col cols="6" sm="4" v-for="item in carItems" :key="item.name">
        <carCard :name="item.name" :company="item.company" :price="item.price" :fuel_eff="item.fuel_eff" :engine="item.engine"></carCard>
      </v-col>
    </v-row>
=======
  <v-container>
    <v-layout wrap justify-center>
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
    <v-layout my-5>
      <v-flex lg12 md12 xs12>
        <v-divider />
        <p></p>
        <div class="text-center display-1">아니면 혹시 이들 중 하나인가요?</div>
        <CarImages></CarImages>
      </v-flex>
    </v-layout>
>>>>>>> 449d0db5d99de9c7454c7595a152d0c2fee996ec
  </v-container>
</template>

<script>
import ContentsApi from "../../apis/ContentsApi";
import CarImages from "../../components/CarImages";
export default {
  name: "detail",
  components: {
<<<<<<< HEAD
    carCard,
  },
  data: () => ({
    carItems: [
      {
        company: "횬다이",
        name: "2020 아반떼",
        price: "1,531~2392",
        fuel_eff: "10.5~15.4km/ℓ",
        engine: "가솔린,LPG",
      },
      {
        company: "횬다이",
        name: "2020 아반떼2",
        price: "1,531~2392",
        fuel_eff: "10.5~15.4km/ℓ",
        engine: "가솔린,LPG",
      },
      {
        company: "횬다이",
        name: "2020 아반떼3",
        price: "1,531~2392",
        fuel_eff: "10.5~15.4km/ℓ",
        engine: "가솔린,LPG",
      },
      {
        company: "횬다이",
        name: "2020 아반떼4",
        price: "1,531~2392",
        fuel_eff: "10.5~15.4km/ℓ",
        engine: "가솔린,LPG",
      },
      {
        company: "횬다이",
        name: "2020 아반떼5",
        price: "1,531~2392",
        fuel_eff: "10.5~15.4km/ℓ",
        engine: "가솔린,LPG",
      },
    ],
  }),
};
</script>

<style scoped></style>
=======
    CarImages,
  },
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
>>>>>>> 449d0db5d99de9c7454c7595a152d0c2fee996ec
