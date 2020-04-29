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
        <CarImages :aiItems="aiItems"></CarImages>
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
    aiItems: {},
  }),
  methods: {
    getItemDetail(id) {
      ContentsApi.requestCarDetail(
        id,
        async (res) => {
          console.log(res.data);
          this.item = res.data;
          console.log("itemcheck:", this.item);
          const link = this.item.imagelink;
          console.log("AI image link:", this.item.imagelink);
          await ContentsApi.requestCarAI(
            link,
            (res) => {
              console.log("AI request response");
              console.log(res.data);
              this.aiItems = res.data;
            },
            (error) => {
              console.log(error);
            }
          );
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
