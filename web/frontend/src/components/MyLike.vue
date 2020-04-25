<template>
  <div>
    <v-layout wrap>
      <v-flex v-for="card in cards" :key="card.title" lg4 sm6 md6 xs12>
        <v-hover v-slot:default="{ hover }">
          <v-card elevation="0" max-width="344" style="border: 1px solid;" class="ma-auto">
            <v-img :src="card.src" class="white--text" height="200px">
              <v-expand-transition>
                <div
                  v-if="hover"
                  class="d-flex transition-fast-in-fast-out grey display-3 white--text justify-center"
                  style="height: 100%;"
                >
                  <v-card-title v-text="card.title"></v-card-title>
                </div>
              </v-expand-transition>
            </v-img>
          </v-card>
        </v-hover>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
export default {
  name: "MyLike",
  data() {
    return {
      cards: [
        {
          title: "Pre-fab homes",
          src:
            "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTaN-ujXAbXuBt9dV8akS1Mgu2_L-nadEpxGUPsvPs_V4ObLIfj&usqp=CAU"
        },
        {
          title: "Favorite road trips",
          src:
            "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRL-i91N289RHesU25SR38igUY9MQ_deDJtt_ROcfvpV6ilekzC&usqp=CAU"
        },
        {
          title: "Best airlines",
          src:
            "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQWNxFt2_bMG73tliJic1dW6l4xQLmQXcM7lVxlk2niwnD-BoAA&usqp=CAU"
        },
        {
          title: "Best airlines",
          src:
            "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSpnNJjKe86ZKuHHLaBt2Awm-GkXRm3y6afgxGney8rCXwyHh1_&usqp=CAU"
        },
        {
          title: "Best airlines",
          src:
            "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQhB5OPB1UFzmvLEq7nhOFaORSLEQdWwGYwbs4nBvisUDTr0wsT&usqp=CAU"
        }
      ]
    };
  }
};
</script>

<style>
</style>