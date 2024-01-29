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

            <v-select
                v-model="companyName"
                label="Select"
                :items="companyNames">
            </v-select>
            


        </v-card>
    </div>
</template>

<script>
import axios from 'axios';

export default{
    name: "CompanyView",
    data() {
        return{
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
        getCompanyItems(){
            axios.get('/company/' + this.companyName)
            .then((res) => {
                this.companyData = res.data
                console.log(this.companyData)
            })
        },
    },
    mounted(){
        this.getCompanyNames()
    },
    watch:{
        companyName: {
            handler(){
                this.getCompanyItems()
            }
        }
    }
}

</script>