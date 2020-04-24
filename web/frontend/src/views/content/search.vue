<template>
  <v-container fluid>
    <p>검색어: {{ this.$route.query.keyword }}</p>
    <v-row>
      <v-col cols="6" sm="4" v-for="item in carItems" :key="item.name">
        <carCard
          :name="item.name"
          :brand="item.brand"
          :price="item.price"
          :fuel_eff="item.fuel_eff"
          :engine="item.engine"
        ></carCard>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ContentsApi from "../../apis/ContentsApi";
import carCard from "../../components/carCard";
export default {
  name: "search",
  components: {
    carCard
  },
  created() {
    console.log("load search");
    console.log("query:", this.$route.query.keyword);
    this.getSearchResult(this.$route.query.keyword);
  },
  data: () => ({
    carItems: [
      {
        brand: "횬다이",
        name: "2020 아반떼",
        price: "1,531~2392",
        fuel_eff: "10.5~15.4km/ℓ",
        engine: "가솔린,LPG"
      },
      {
        brand: "횬다이",
        name: "2020 아반떼2",
        price: "1,531~2392",
        fuel_eff: "10.5~15.4km/ℓ",
        engine: "가솔린,LPG"
      },
      {
        brand: "횬다이",
        name: "2020 아반떼3",
        price: "1,531~2392",
        fuel_eff: "10.5~15.4km/ℓ",
        engine: "가솔린,LPG"
      },
      {
        brand: "횬다이",
        name: "2020 아반떼4",
        price: "1,531~2392",
        fuel_eff: "10.5~15.4km/ℓ",
        engine: "가솔린,LPG"
      },
      {
        brand: "횬다이",
        name: "2020 아반떼5",
        price: "1,531~2392",
        fuel_eff: "10.5~15.4km/ℓ",
        engine: "가솔린,LPG"
      }
    ]
  }),
  methods: {
    getSearchResult(keyword) {
      console.log("function query:", keyword);
      ContentsApi.search(
        keyword,
        res => {
          console.log(res);
        },
        error => {
          console.log(error);
        }
      );
    }
  },
  mounted() {}
};
</script>

<style scoped>
</style>
