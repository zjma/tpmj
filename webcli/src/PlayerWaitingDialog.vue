<template>
    <v-dialog v-model="active" persistent max-width="600px">
        <v-card>
            <v-card-title>
                <span class="headline"></span>
            </v-card-title>
            <v-container>
                Waiting for opponent...
            </v-container>
            <v-card-actions>
                <v-btn color="blue darken-1" text @click="onBack">Back</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)

export default {
    name: 'PlayerWaitingDialog',
    props : {
        active:Boolean
    },
    methods: {
        onBack : function(){
            this.$emit('cancelled');
        },
        onGameSelected(gameID){
            this.$emit('selected', gameID);
        },
    }
}
</script>
