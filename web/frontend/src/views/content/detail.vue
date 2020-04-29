<template>
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
        <div class="text-center display-1">이런 차는 어떠신가요?</div>
        <CarImages></CarImages>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import ContentsApi from "../../apis/ContentsApi";
import CarImages from "../../components/CarImages";
export default {
  name: "detail",
  components: {
    CarImages,
  },
  created() {
    console.log("carId:", this.$route.query.id);
    this.getItemDetail(this.$route.query.id);
  },
  data: () => ({
    item: {},
    result: {},
    otherItems: {},
    cards: [
      {
        title: "Pre-fab homes",
        src: "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTaN-ujXAbXuBt9dV8akS1Mgu2_L-nadEpxGUPsvPs_V4ObLIfj&usqp=CAU",
      },
      {
        title: "Favorite road trips",
        src: "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRL-i91N289RHesU25SR38igUY9MQ_deDJtt_ROcfvpV6ilekzC&usqp=CAU",
      },
      {
        title: "Best airlines",
        src: "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQWNxFt2_bMG73tliJic1dW6l4xQLmQXcM7lVxlk2niwnD-BoAA&usqp=CAU",
      },
      {
        title: "Best airlines",
        src: "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSpnNJjKe86ZKuHHLaBt2Awm-GkXRm3y6afgxGney8rCXwyHh1_&usqp=CAU",
      },
    ],
  }),
  methods: {
    getItemDetail(id) {
      ContentsApi.requestCarDetail(
        id,
        (res) => {
          console.log(res.data);
          const carList = res.data;
          let otherList = [];
          for (let idx in carList) {
            if (idx == 0) {
              this.result = carList[idx];
            } else {
              otherList.push(carList[idx]);
            }
          }
        },
        (error) => {
          console.log(error);
        }
      );
    },
  },
  mounted() {},
};
</script>

<style></style>
