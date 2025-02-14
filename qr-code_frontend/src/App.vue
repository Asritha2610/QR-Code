<template>
  <div id="app">
  <h1>QR Code Generator</h1>
   <form @submit.prevent="generateQR">
      <input type="text" v-model="url" placeholder="Enter URL" required />
      <button type="submit">Generate QR Code</button>
    </form>
     <div v-if="qrCode">
      <h2>Generated QR Code:</h2>
      <img :src="'data:image/png;base64,' + qrCode" alt="QR Code" />
    </div>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<script>
import axios from "axios";
export default {
data() {
    return {
      url: "",
      qrCode: "",
      error: "",
    };
  },

  methods: {
    async generateQR() {
      this.error = "";
      if (!this.url.startsWith("http")){
      this.error="Invalid URL format";
      return;
      }
      try {
        const response = await axios.post("http://127.0.0.1:8000/generate_qr", { url: this.url });
        this.qrCode = response.data.qr_code;
      } catch (error) {
        this.error = "Error generating QR Code";
      }
    },
  },
};
</script>

<style>
#app {
  text-align: center;
  max-width: 400px;
  margin: 50px auto;
}

input {
  width: 80%;
  padding: 8px;
  margin: 10px 0;
}

button {
  padding: 10px;
  background-color: blue;
  color: white;
  border: none;
  cursor: pointer;
}

.error {
  color: red;
}
</style>
