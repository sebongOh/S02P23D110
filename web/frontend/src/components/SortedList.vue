<template>
  <v-card elevation="0" style="border:1px solid;">
    <v-list>
      <!--제목 -->
      <v-list-item>
        <v-list-item-content class="text-center">
          <v-list-item-title class="headline">Like Ranking</v-list-item-title>
          <!--<v-list-item-subtitle>사용자 좋아요순 정렬</v-list-item-subtitle>-->
        </v-list-item-content>
      </v-list-item>

      <!-- 아이템 -->
      <v-list-item v-for="likecar in likecars" :key="likecar.id">
        <!--<v-list-item-icon>
          <v-icon>{{icons[idx].path}}</v-icon>
        </v-list-item-icon>-->
        <v-list-item-avatar>
          <v-img :src="likecar.imagelink"></v-img>
        </v-list-item-avatar>

        <v-list-item-content class="mx-3">
          <v-list-item-title v-html="likecar.name"></v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-card>
</template>

<script>
import ContentsApi from "../apis/ContentsApi";
import {
  mdiNumeric1,
  mdiNumeric2,
  mdiNumeric3,
  mdiNumeric4,
  mdiNumeric5
} from "@mdi/js";
export default {
  name: "SortedList",
  data() {
    return {
      icons: [
        {
          index: 1,
          path: mdiNumeric1
        },
        {
          index: 2,
          path: mdiNumeric2
        },
        {
          index: 3,
          path: mdiNumeric3
        },
        {
          index: 4,
          path: mdiNumeric4
        },
        {
          index: 5,
          path: mdiNumeric5
        }
      ],
      likecars: [
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
          index: 1,
          title: "Pre-fab homes",
          src:
            "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTaN-ujXAbXuBt9dV8akS1Mgu2_L-nadEpxGUPsvPs_V4ObLIfj&usqp=CAU"
        },
        {
          index: 2,
          title: "Favorite road trips",
          src:
            "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRL-i91N289RHesU25SR38igUY9MQ_deDJtt_ROcfvpV6ilekzC&usqp=CAU"
        },
        {
          index: 3,
          title: "Best airlines",
          src:
            "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQWNxFt2_bMG73tliJic1dW6l4xQLmQXcM7lVxlk2niwnD-BoAA&usqp=CAU"
        },
        {
          index: 4,
          title: "Best airlines",
          src:
            "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSpnNJjKe86ZKuHHLaBt2Awm-GkXRm3y6afgxGney8rCXwyHh1_&usqp=CAU"
        },
        {
          index: 5,
          title: "Best airlines",
          src:
            "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQhB5OPB1UFzmvLEq7nhOFaORSLEQdWwGYwbs4nBvisUDTr0wsT&usqp=CAU"
        }
      ]
    };
  },
  mounted() {
    ContentsApi.likecarAll(res => {
      this.likecars = res.data;
      console.log(this.likecars);
    }),
      error => {
        console.log(error);
      };
  }
};
</script>

<style>
</style>