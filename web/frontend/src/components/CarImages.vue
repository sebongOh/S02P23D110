<template>
  <v-layout wrap>
    <v-flex v-for="item in aiItems" :key="item.id" lg2 sm2 md2 xs12>
      <v-hover v-slot:default="{ hover }">
        <v-card elevation="0" max-width="344" class="ma-auto">
          <v-img :src="item.imagelink" class="white--text" height="200px">
            <v-expand-transition>
              <div
                v-if="hover"
                class="d-flex transition-fast-in-fast-out grey display-3 white--text justify-center"
                style="height: 100%;"
              >
                <v-card-title
                  v-text="item.name"
                  @click="getDetail(item.id)"
                ></v-card-title>
              </div>
            </v-expand-transition>
          </v-img>
        </v-card>
      </v-hover>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  name: "CarImages",
  props: ["aiItems"],
  data() {
    return {};
  },
  methods: {
    getDetail(id) {
      // this.$router.go({ name: "detail", query: { id: id } });
      this.$router.push({ path: "/detail", query: { id: id } });
    },
  },
};
</script>

<style></style>
