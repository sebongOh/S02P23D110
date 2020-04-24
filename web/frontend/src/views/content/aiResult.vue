<template>
  <v-container fluid>
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
import carCard from "../../components/carCard";
export default {
  name: "aiResult",
  components: {
    carCard
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
  })
};
</script>

<style scoped>
</style>
