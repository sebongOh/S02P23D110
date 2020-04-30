<template>
  <v-container fluid>
    <NavBar />
    <!-- 검색어 확인용, 배포시 삭제 -->
    <p>검색어: {{ this.$route.query.keyword }}</p>
    <v-row>
      <v-col cols="6" sm="4" v-for="item in carItems" :key="item.id">
        <carCard :id="item.id" :company="item.company" :imagelink="item.imagelink" :name="item.name" :brand="item.brand" :price="item.price" :fuel_eff="item.fuel_eff" :engine="item.engine"></carCard>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import NavBar from "../../components/NavBar";
import ContentsApi from "../../apis/ContentsApi";
import carCard from "../../components/carCard";
export default {
  name: "search",
  components: {
    NavBar,
    carCard,
  },
  created() {
    console.log("load search");
    console.log("query:", this.$route.query.keyword);
    console.log("filter:", this.$route.query.filter);
    this.getSearchResult(this.$route.query.keyword, this.$route.query.filter);
  },
  data: () => ({
    carItems: [],
  }),
  methods: {
    getSearchResult(keyword, filter) {
      console.log("function query:", keyword);
      if (filter == "이름") {
        ContentsApi.searchName(
          keyword,
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
        if (filter == "제조사") {
          ContentsApi.searchCompany(
            keyword,
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
        }
      }
    },
  },
  mounted() {},
};
</script>

<style scoped></style>
