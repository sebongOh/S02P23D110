<template>
  <v-container>
    <v-content>
      <h1 class="display-2 font-weight-light">The Art Of Travel</h1>
      <div class="subheading text-uppercase pl-4 mb-6">Finding Beauty, One flight at a time</div>
    </v-content>

    <v-row>
      <!-- 차량 리스트 -->
      <v-col v-for="car in calData" :key="car.id" :cols="12" :md="3">
        <v-card>
          <v-img :src="car.imagelink" class="white--text align-end" gradient="to bottom, rgba(0,0,0,.1), rgba(1,2,2,.3)" height="300px">
            <v-card-text>
              <!-- <h3 class="title font-weight-bold mb-1">{{ car.company }}</h3> -->
              <br />
              <div class="subtitle-1 font-weight-bold">
                {{ car.company }}
                <br />
                {{ car.price }}만원
                <br />
                {{ car.fuel_eff }}
              </div>
            </v-card-text>
            <v-card-actions>
              <v-chip label class="mx-1 mb-3" color="grey darken-3" text-color="white" @click="carDetail(car.id)">{{ car.name }}</v-chip>
              <v-spacer></v-spacer>
              <v-btn icon @click="heart(car.id)">
                <v-icon>mdi-heart</v-icon>
              </v-btn>
            </v-card-actions>
          </v-img>
        </v-card>
      </v-col>
    </v-row>
    <v-container class="text-center">
      <v-btn class="ma-2" color=" darken-2" dark @click="previous()"> <v-icon dark left>mdi-arrow-left</v-icon>Back </v-btn>
      <v-chip label class="ma-1 font-weight-bold" color="black darken-2" text-color="white">{{ curPageNum }}</v-chip>
      <v-btn class="ma-2" color=" darken-2" dark @click="next()"> <v-icon dark left>mdi-arrow-right</v-icon>Next </v-btn>
    </v-container>
  </v-container>
</template>

<script>
import ContentsApi from "../apis/ContentsApi";
// import UserApi from "../apis/UserApi";
export default {
  data: () => ({
    cars: [
      {
        id: "",
        imagelink: "",
        name: "",
        price: "",
        company: "",
        fuel_eff: "",
        size: "",
        engine: "",
      },
    ],
    dataPerpage: 16,
    curPageNum: 1,
  }),
  mounted() {
    ContentsApi.requestCars((res) => {
      this.cars = res.data;
    }),
      (error) => {
        console.log(error);
      };
  },
  methods: {
    heart(car_id) {
      console.log("좋아요 :: " + car_id);
    },
    carDetail(car_id) {
      console.log("디테일 :: " + car_id);
      this.$router.push({ path: "/detail", query: { id: car_id } });
    },
    previous() {
      if (1 < this.curPageNum) {
        return (this.curPageNum -= 1);
      }
      return this.curPageNum;
    },
    next() {
      if (this.numOfpages > this.curPageNum) {
        return (this.curPageNum += 1);
      }
      return this.curPageNum;
    },
  },
  computed: {
    startOffset() {
      return (this.curPageNum - 1) * this.dataPerpage;
    },
    endOffset() {
      return this.startOffset + this.dataPerpage;
    },
    numOfpages() {
      return Math.ceil(this.cars.length / this.dataPerpage);
    },
    calData() {
      return this.cars.slice(this.startOffset, this.endOffset);
    },
  },
};
</script>

<style></style>
