<template>
  <v-container>
    <v-layout my-5 row wrap>
      <v-flex xs12 md12 lg4>
        <v-card>
          <img :src="item.imagelink" alt="" width="340vw" />
        </v-card>
      </v-flex>
      <v-flex xs12 md12 lg4>
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
    <v-divider></v-divider>
    <p><b>비슷한 차를 찾으시나요?</b></p>
    <v-layout my-3 xs row>
      <v-flex v-for="similItem in cards" lg4 sm4 md4 xs12 :key="similItem.src">
        <v-layout wrap>
          <v-flex>
            <v-card>
              <img :src="similItem.src" alt="" />
            </v-card>
          </v-flex>
        </v-layout>
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
    similarItems: {},
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
    getSimilar(imgLink) {
      console.log("get AI result");
      let file = document.querySelector("#getfile");
      console.log("queryselector:", file);
      const formData = new FormData();

      console.log("file: ", imgLink);
      // console.log("append formData:", formData.append("file", imgLink));
      // console.log("formData:", formData);
      ContentsApi.imgupload(
        formData,
        (res) => {
          console.log(res);
        },
        (error) => {
          console.log(error);
        }
      );
    },
    getItemDetail(id) {
      console.log("--get detail start--");
      ContentsApi.requestCarDetail(
        id,
        (res) => {
          // console.log(res.data);
          this.item = res.data;
          // console.log("image link check:", res.data.imagelink);
          // console.log("check:", this.item);
          this.getSimilar(res.data.imagelink);
        },
        (error) => {
          console.log(error);
        }
      );
      console.log("--get detail end--");
    },
  },
  mounted() {
    this.getSimilar();
  },
};
</script>

<style></style>
