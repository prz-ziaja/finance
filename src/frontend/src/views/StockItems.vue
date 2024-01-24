<template>
    <div id="app">
        <v-row align="center" justify="center">
            <v-col cols="auto">
                <v-card title="Stock Items">
                    <template v-slot:text>
                        <v-text-field v-model="search" label="Search" prepend-inner-icon="mdi-magnify" single-line
                            variant="outlined" hide-details></v-text-field>
                    </template>
                    <v-data-table :headers="headers" :items="tableItems" :search="search" :loading="loading">

                    </v-data-table>
                </v-card>
            </v-col>
        </v-row>
    </div>
</template>
    
<script>
import axios from 'axios';

export default {
    name: 'StockItems',
    data() {
        return {
            search: '',
            loading: false,
            headers: [
                {
                    align: 'start',
                    key: 'company_symbol',
                    title: 'Company Symbol',
                },
                { key: 'datatime', title: 'Timestamp'},
                { key: 'open_price', title: "Opening Price" },
                { key: 'high_price', title: "High Price" },
                { key: 'low_price', title: "Low Price" },
                { key: 'close_price', title: "Close Price" },
                { key: 'volume', title: "Volume" }
            ],
            items: [],
            tableItems: [],
        };
    },
    methods: {
        getItems() {
            this.loading = true
            axios.get('/stock/items')
                .then((res) => {
                    this.items = res.data;
                    this.itemsToTable()
                    this.loading = false
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        itemsToTable() {
            this.tableItems = []
            for (let item of this.items) {
                this.tableItems.push({
                    "company_symbol": item[1],
                    "datatime": (new Date(item[2])).toLocaleString(),
                    "open_price": item[5].toFixed(2),
                    'high_price': item[6].toFixed(2),
                    'low_price': item[7].toFixed(2),
                    "close_price": item[8].toFixed(2),
                    "volume": item[10],
                })
            }
        }
    },
    mounted() {
        this.getItems();
    }
}
</script>