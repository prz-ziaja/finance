<template>
  <div id="app">
    <div class='d-flex align-center justify-center'>
      <v-btn @click="getMessage(), dialog = true" size="x-large" color="deep-purple">
        Start Offline Scrapper star
      </v-btn>
    </div>

    <v-fade-transition hide-on-leave>
      <v-card v-if="dialogWindow" class="mx-auto" elevation="16" max-width="500" title="Command sent">

        <template v-slot:append>
          <v-btn icon="$close" variant="text" @click="dialogWindow = false"></v-btn>
        </template>

        <v-divider></v-divider>

        <div v-if="returnInfo['success']" class="py-3 text-center">
          <v-icon class="mb-6" color="success" icon="mdi-check-circle-outline" size="128"></v-icon>
          <div class="text-h5 font-weight-bold">Information was sent to server</div>
          <div class="pt-8 font-weight-bold">Response from server<br> {{ returnInfo['success'] }}</div>
        </div>
        <div v-else-if="returnInfo['error']" class="py-3 text-center">
          <v-icon class="mb-6" color="error" icon="mdi-alert-circle" size="128"></v-icon>
          <div class="text-h5 font-weight-bold">Information was sent to server,<br> but crashed occured on server side.</div>
          <div class="pt-8 font-weight-bold">Response from server<br> {{ returnInfo['error'] }}</div>
        </div>

        <v-divider></v-divider>

        <div class="pa-4 text-end">
          <v-btn class="text-none" color="medium-emphasis" min-width="92" rounded variant="outlined"
            @click="dialogWindow = false">
            Close
          </v-btn>
        </div>

      </v-card>
    </v-fade-transition>


    <div class="align-center pt-12 justify-center mt-10">
      <h4 v-if="returnInfo['success']">
        Information was sent to start a Offline Scraper! <br>
        Operation starting...
      </h4>
    </div>
  </div>

</template>
  
<script>
import axios from 'axios';
import { ref } from 'vue';

export default {
  name: 'StartView',
  data() {
    return {
      returnInfo: {},
      dialogWindow: ref(false),
    };
  },
  methods: {
    getMessage() {
      this.dialogWindow = true;
      axios.get('/offline-scraper')
        .then((res) => {
          this.returnInfo = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
}
</script>
  