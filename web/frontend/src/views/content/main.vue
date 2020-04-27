<template>
  <div>
    <Carousels></Carousels>
    <div class="md-6 xs12">
      <imageUpload></imageUpload>
    </div>
  </div>
</template>

<script>
import imageUpload from "../../components/imageUpload";
import Carousels from "../../components/Carousels";

export default {
  components: {
    imageUpload,
    Carousels
  }
};
</script>


