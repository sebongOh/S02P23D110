<template>
  <div>
    <v-layout wrap>
      <!-- 차량 리스트 -->
      <v-col v-for="mylikecar in mylikecars" :key="mylikecar.id" :cols="12" :md="3">
        <v-card>
          <v-img
            :src="mylikecar.imagelink"
            class="white--text align-end"
            gradient="to bottom, rgba(0,0,0,.1), rgba(1,2,2,.3)"
            height="300px"
          >
            <v-card-text>
              <!-- <h3 class="title font-weight-bold mb-1">{{ car.company }}</h3> -->
              <br />
              <div class="subtitle-1 font-weight-bold">
                {{mylikecar.company}}
                <br />
                {{ mylikecar.price }}만원
                <br />
                {{mylikecar.fuel_eff}}
              </div>
            </v-card-text>
            <v-card-actions>
              <v-chip
                label
                class="mx-1 mb-3"
                color="grey darken-3"
                text-color="white"
                @click="carDetail(car.id)"
              >{{ mylikecar.name }}</v-chip>
              <v-spacer></v-spacer>
              <v-btn icon @click="deletelike(car.id)">
                <v-icon>mdi-heart-broken</v-icon>
              </v-btn>
            </v-card-actions>
          </v-img>
        </v-card>
      </v-col>
    </v-layout>
  </div>
</template>

<script>
import UserApi from "../apis/UserApi";
export default {
  name: "MyLike",
  data() {
    return {
      mylikecars: [
        {
          id: "",
          imagelink: "",
          name: "",
          price: "",
          company: "",
          fuel_eff: "",
          size: "",
          engine: ""
        }
      ]
    };
  },
  mounted() {
    UserApi.requestLike(sessionStorage.getItem("id"), res => {
      this.mylikecars = res.data;
      console.log(this.mylikecars);
    }),
      error => {
        console.log(error);
      };
  },
  methods: {}
};
</script>

<style>
</style>