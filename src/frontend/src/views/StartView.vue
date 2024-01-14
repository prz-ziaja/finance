<template>
  <div id="app">
    <v-card></v-card>
    <v-btn size="large" color="primary" @click="getMessage()">
      START BUTTON
    </v-btn>
    {{ returnInfo }}
  </div>
</template>
  
<script>
import axios from 'axios';

export default {
  name: 'StartView',
  data() {
    return {
      returnInfo: {},
    };
  },
  methods: {
    getMessage() {
      axios.get('/offline-scraper')
        .then((res) => {
          this.returnInfo = res.data;
          console.log(this.returnInfo)
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
}
</script>
  