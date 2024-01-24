<template>
  <div class="hello pa-10 mb-20">
    <h1>{{ msg }}</h1>
  </div>
  <div>
    <v-container class="ma-20">
      <v-row align="center" justify="center">
        <v-col cols="auto">
          <v-card variant=outlined width="400" height="200" class="mx-auto pa-3">
            <v-card-title>
              <h2>
                Offline Scraper
              </h2>
            </v-card-title>
            <v-card-text class="py-5">
              <h5>
                Offline Scraper is currently not working
              </h5>
            </v-card-text>
            <v-card-actions class="pa-5 pb-10 justify-center align-center">
              <v-btn rounded="lg" elevated href="/scraper">
                <h3>
                  Route to Scraper
                </h3>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
        <v-col cols="auto">
          <v-card variant=outlined width="400" height="200" class="mx-auto pa-3">
            <v-card-title>
              <h2>
                Stock Items
              </h2>
            </v-card-title>
            <v-card-text class="py-5">
              <h5>
                Click to see current stock items.
              </h5>
            </v-card-text>
            <v-card-actions class="pa-5 pb-10 justify-center align-center">
              <v-btn rounded="lg" elevated href="/stock/items">
                <h3>
                  Route to Stock Items
                </h3>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<style scoped></style>
