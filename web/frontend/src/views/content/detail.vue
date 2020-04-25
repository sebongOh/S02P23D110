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
          <v-card-subtitle>{{ item.company }}</v-card-subtitle>
          <v-card-text>
            <p>분류: {{ item.size }}</p>
            <p>출시가: {{ item.price }}</p>
            <p>연비: {{ item.fuel_eff }}</p>
            <p>연료: {{ item.engine }}</p>
          </v-card-text>
        </v-card>
      </v-col>
      <!-- <template v-for="n in 4">
        <v-col :key="n">
          <v-card class="pa-2" outlined tile>
            Column
          </v-card>
        </v-col>
        <v-responsive v-if="n === 2" :key="`width-${n}`" width="100%"></v-responsive>
      </template> -->
    </v-row>
  </v-container>
</template>

<script>
// import carCard from "../../components/carCard";
export default {
  name: "detail",
  //   components: {
  //     carCard,
  //   },
  data: () => ({
    item: {
      id: 1,
      imagelink: "https://imgauto-phinf.pstatic.net/20200330_142/auto_1585547248870fGwBQ_PNG/20200330144726_jJxZhNkX.png?type=f160_116",
      name: "2021 G80",
      price: "5,247~6,187",
      company: "제네시스",
      fuel_eff: "8.4~14.6km/ℓ",
      size: "준대형",
      engine: "디젤, 가솔린",
    },
  }),
};
</script>

<style></style>
