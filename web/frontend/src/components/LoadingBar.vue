<template>
  <v-overlay opacity="0.8">

  <div class="loading">로딩중 입니다..</div>

  <v-progress-circular
      :size="200"
      :width="15"
      color="white"
      indeterminate
    ></v-progress-circular>
  
  </v-overlay>
</template>

<script>

export default {
  components: {
  },
  data() {
    return {
    }
  },
 mounted() {

 }
}
</script>

<style lang="scss" scoped>
  .loading{
    font-size: 3rem;
  }
</style>
