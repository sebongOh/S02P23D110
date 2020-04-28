<template>
  <v-container fluid>
    <p>검색어: {{ this.$route.query.keyword }}</p>
    <v-row>
      <v-col cols="6" sm="4" v-for="item in carItems" :key="item.id">
        <carCard
          :id="item.id"
          :imagelink="item.imagelink"
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
    carItems: []
  }),
  methods: {
    getSearchResult(keyword) {
      console.log("function query:", keyword);
      ContentsApi.search(
        keyword,
        res => {
          // console.log(res);
          const carItemList = res.data;
          for (const idx in carItemList) {
            const carItem = carItemList[idx];
            this.carItems.push(carItem);
            console.log(carItem);
          }
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

<style scoped></style>
