<template>
  <v-carousel cycle height="20%" hide-delimiter-background show-arrows-on-hove class="text-center align-center">
  <LoadingBar
  v-if="ImageOn"
  />
    <v-carousel-item v-for="(item, i) in items" :key="i" :src="item.src">
      <v-row class="fill-height" align="center" justify="center">
        <v-row class="fill-height pa-3" align="center">
          <v-col cols="12" md="7" offset-md="5">
            <h1 class="display-3 font-weight-light white--text">The Art Of Travel</h1>
            <div class="subheading text-uppercase pl-4 mb-6 white--text">Finding Beauty, One flight at a time</div>
            <v-btn large color="orange" class="ma-2 white--text" dark @click="dialog = true">
              Upload
              <v-icon right dark>mdi-cloud-upload</v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </v-row>
    </v-carousel-item>
    <!-- ###########################upload modal 창-->
    <v-dialog v-model="dialog" max-width="700px">
      <v-card>
        <v-card-title>UploadImage</v-card-title>
        <v-card v-model="imageSrc" class="upload-image">
          <v-img :src="imageSrc"></v-img>
        </v-card>
        <v-card-subtitle>
          <input type="text" class="form-control" placeholder="Input Image URL or Drag & Drop or Select" v-model="filename" @dragover.prevent @dragenter.prevent @drop.prevent="onDrop" />
        </v-card-subtitle>
        <v-card-subtitle>
          <input type="file" class="file-input" accept="image/*" ref="fileInput" @change="onFileChange" />
        </v-card-subtitle>
        <v-card-actions>
          <v-btn color="orange" class="ma-2 white--text" dark @click="onClickUpload">Upload</v-btn>
          <v-btn color="grey" class="ma-2 white--text" dark @click="dialogfalse()">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <!--########################## -->
  </v-carousel>
</template>

<script>
import ContentsApi from "../apis/ContentsApi";
import LoadingBar from "./LoadingBar";

export default {
  components:{
    LoadingBar,
  },
  data() {
    return {
      uploadImage: "",
      filename: "",
      imageSrc: "",
      dialog: false,
      result: {},
      ImageOn: false,
      items: [
        {
          src: "https://images.unsplash.com/photo-1542362567-b07e54358753?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80",
        },
        {
          src: "https://images.unsplash.com/photo-1532581140115-3e355d1ed1de?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80",
        },
        {
          src: "https://images.unsplash.com/photo-1503376780353-7e6692767b70?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80",
        },
        {
          src: "https://images.unsplash.com/photo-1522037576655-7a93ce0f4d10?ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80",
        },
      ],
    };
  },
  methods: {
    dialogfalse() {
      this.dialog = false;
      this.uploadImage = "";
      this.filename = "";
      this.imageSrc = "";
    },
    onDrop(event) {
      this.inputImageFile(event.dataTransfer.files);
      this.uploadImage = event.dataTransfer.files[0];
      console.log(event.dataTransfer.files[0]);
    },
    onClickFile(event) {
      console.log(event);
      this.$refs.fileInput.click();
    },
    onFileChange(event) {
      console.log(event);
      this.inputImageFile(event.target.files);
    },
    inputImageFile(files) {
      if (files.length) {
        let file = files[0];
        if (!/^image\//.test(file.type)) {
          alert("이미지 파일만 등록이 가능합니다");
          return false;
        }
        this.filename = file.name;
        this.uploadImage = file;
        this.preview(file);
      }
    },
    onClickUpload() {
      this.preview(this.filename);
      this.ImageOn = !this.ImageOn;
      const formData = new FormData();
      formData.append("file", this.uploadImage);
      console.log("imageSrc", this.imageSrc);

      for (let key of formData.entries()) {
        console.log(`${key}`);
      }

      ContentsApi.imgupload(
        formData,
        (res) => {
          console.log(res);
          this.imageSrc = "";
          this.result = res.data;
        },
        (error) => {
          console.log(error);
        }
      );
      this.$router.push({ path: "/result", query: { carList: this.result } });
    },
    preview(file) {
      if (typeof file === "string") {
        this.imageSrc = file;
      } else {
        let vm = this;
        let reader = new FileReader();
        reader.onload = () => {
          vm.imageSrc = reader.result;
        };
        reader.readAsDataURL(file);
      }
    },
  },
};
</script>

<style>
.form-control {
  border: 3px solid black;
  width: 100%;
}
</style>
