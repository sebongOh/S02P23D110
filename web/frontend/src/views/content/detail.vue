<template>
  <v-container>
        <LoadingBar
        v-if="ImageOn"
        />
    <v-layout wrap justify-center>
      <v-flex lg6 sm12 md6 xs12>
        <v-card class="main_img">
          <img :src="item.imagelink" alt="" class="car_img" />
        </v-card>
      </v-flex>
      <v-flex lg6 sm12 md6 xs12>
        <v-card class="main_subs">
          <v-card-title style="font-size:2.5rem">{{ item.name }}</v-card-title>
          <hr />
          <v-card-subtitle style="font-size:1.5rem">제조사: {{ item.company }}</v-card-subtitle>
          <v-card-text style="font-size:1.2rem">
            <br />
            <p>분류: {{ item.size }}</p>
            <p>출시가: {{ item.price }}만</p>
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
import LoadingBar from "../../components/LoadingBar";

export default {
  name: "detail",
  components: {
    CarImages,
    LoadingBar,
  },
  created() {
    console.log("carId:", this.$route.query.id);
    this.getItemDetail(this.$route.query.id);
  },
  data: () => ({
    item: {},
    result: {},
    aiItems: {},
    ImageOn: true,
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
        async (res) => {
          console.log(res.data);
          this.item = res.data;
          console.log("itemcheck:", this.item);
          const link = this.item.imagelink;
          console.log("AI image link:", this.item.imagelink);
          this.ImageOn = true
          await ContentsApi.requestCarAI(
            link,
            (res) => {
              console.log("AI request response");
              console.log(res.data);
              this.aiItems = res.data;
              this.ImageOn = false
            },
            (error) => {
              console.log(error);
              this.ImageOn = false

            }
          );
          
        },
        (error) => {
          console.log(error);
              this.ImageOn = false

        }
      );
      console.log("--get detail end--");
      this.ImageOn = false

    },
  },
  mounted() {},
};
</script>

<style lang="scss" scoped>
.main_img {
  background: url("data:image/jpeg;base64,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");
  background-size: cover;
  height: 40vh;

  .car_img {
    display: block;
    margin: 0px auto;
    width: 500px;
    padding-top: 10px;
  }
  @media (max-width: 768px) {
    .car_img {
      width: 500px;
      padding-top: 10px;
    }
  }

  @media (min-width: 992px) {
    .car_img {
      padding-top: 10px;
      width: 400px;
    }
  }

  @media (min-width: 1200px) {
    .car_img {
      padding-top: 10px;
      width: 450px;
    }
  }
}
.main_subs {
  height: 40vh;
}
</style>
