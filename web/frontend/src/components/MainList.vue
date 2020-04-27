<template>
  <v-container>
    <v-content>
      <h1 class="display-2 font-weight-light">The Art Of Travel</h1>
      <div class="subheading text-uppercase pl-4 mb-6">Finding Beauty, One flight at a time</div>
    </v-content>
    <v-row>
      <v-col v-for="car in cars" :key="car.id" :cols="12" :md="3">
        <v-card>
          <v-img
            :src="car.imagelink"
            class="white--text align-end"
            gradient="to bottom, rgba(0,0,0,.1), rgba(1,2,2,.3)"
            height="300px"
          >
            <v-card-text>
              <!-- <h3 class="title font-weight-bold mb-1">{{ car.company }}</h3> -->
              <br />
              <div class="subtitle-1 font-weight-bold">
                {{car.company}}
                <br />
                {{ car.price }}만원
                <br />
                {{car.fuel_eff}}
              </div>
            </v-card-text>
            <v-card-actions>
              <v-chip
                label
                class="mx-1 mb-3"
                color="grey darken-3"
                text-color="white"
                @click.stop
              >{{ car.name }}</v-chip>
              <v-spacer></v-spacer>
              <v-btn icon>
                <v-icon>mdi-heart</v-icon>
              </v-btn>
            </v-card-actions>
          </v-img>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ContentsApi from "../apis/ContentsApi";
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
        engine: ""
      }
    ],
    cards: [
      {
        title: "Pre-fab homes",
        src: "https://cdn.vuetifyjs.com/images/cards/house.jpg",
        flex: 4
      }
    ]
  }),
  mounted() {
    ContentsApi.requestCars(res => {
      console.log("데이터 넘어어어어어온다다다다다");
      console.log(res.data);
      this.cars = res.data;
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