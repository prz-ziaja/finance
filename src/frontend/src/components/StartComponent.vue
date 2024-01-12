<template>
    <div>
      <p>{{ data }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'PingComponent',

    data() {
      return {
        data: {},
      };
    },

    methods: {
      getMessage() {
        axios.get('/items')
          .then((res) => {
            this.data = res.data;
            console.log(this.data)
          })
          .catch((error) => {
            console.error(error);
          });
      },
    },

    mounted() {
      this.getMessage();
    },

  };
  </script>
  