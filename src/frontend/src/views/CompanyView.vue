<template>
    <div id="app">
        <v-card>
            <v-card-title>
                <h3>
                    Company Page
                </h3>
            </v-card-title>
            <v-card-subtitle>
                Select company name to see stock history
            </v-card-subtitle>

            <v-select v-model="companyName" label="Select" :items="companyNames">
            </v-select>

            <LineChart v-if="loaded" />

        </v-card>
    </div>
</template>

<script>
import LineChart from '@/components/LineChart.vue'
import axios from 'axios';

export default {
    name: "CompanyView",
    components: { LineChart },
    data() {
        return {
            loaded: false,
            companyName: '',
            companyNames: [],
            companyData: [],
        }
    },
    methods: {
        getCompanyNames() {
            axios.get('/companies')
                .then((res) => {
                    this.companyNames = res.data;
                })
        },
        getCompanyItems() {
            this.loaded = false;
            axios.get('/company/' + this.companyName)
                .then((res) => {
                    this.companyData = res.data;
                    this.loaded = true;
                    console.log(this.companyData)
                })
        },
    },
    mounted() {
        this.getCompanyNames()
    },
    watch: {
        companyName: {
            handler() {
                this.getCompanyItems()
            }
        }
    }
}

</script>