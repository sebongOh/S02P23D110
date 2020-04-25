<template>
  <v-card max-width="344" class="mx-auto">
    <v-img src="https://cdn.vuetifyjs.com/images/cards/mountain.jpg" height="194"></v-img>

    <v-list-item>
      <v-list-item-content>
        <v-list-item-title class="headline">{{ name }}</v-list-item-title>
      </v-list-item-content>
    </v-list-item>
    <v-card-text>
      <p>제조사: {{ company }}</p>
      <p>공인연비: {{ fuel_eff }}</p>
      <p>연료: {{ engine }}</p>
    </v-card-text>
    <v-card-actions>
      <v-btn text color="deep-purple accent-4">Read</v-btn>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "carCard",

  props: ["name", "company", "price", "fuel_eff", "engine"],
};
</script>

<style>
.bottom-gradient {
  background-image: linear-gradient(to top, rgba(0, 0, 0, 0.4) 0%, transparent 72px);
}

.repeating-gradient {
  background-image: repeating-linear-gradient(-45deg, rgba(255, 0, 0, 0.25), rgba(255, 0, 0, 0.25) 5px, rgba(0, 0, 255, 0.25) 5px, rgba(0, 0, 255, 0.25) 10px);
}
</style>
