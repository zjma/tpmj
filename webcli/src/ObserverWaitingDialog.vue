<template>
    <v-dialog v-model="active" persistent max-width="600px">
        <v-card>
            <v-card-title>
                <span class="headline"></span>
            </v-card-title>
            <v-container>
                Searching...
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
    name: 'ModeDialog',
    props : {
        active:Boolean
    },
    watch: {
        active: function(newVal, oldVal){
            if (newVal == true && oldVal == false) {
                this.requestObservableGames()
            }
            if (newVal == false && oldVal == true) {
                //User cancelled the searching.
            }
        }
    },
    methods: {
        onBack : function(){
            this.$emit('cancelled');
        },
        onGameSelected(gameID){
            this.$emit('selected', gameID);
        },
        requestObservableGames(){
            this.axios
            .post('http://localhost:8080/tpmj', {Action:'GetObservableGame'})
            .then(response => {
                var sub = response.data
                window.console.log(sub)
                if (sub.GameID) {
                    this.$emit('selected',sub.gameID)
                } else {
                    if (this.active) {
                        setTimeout(this.requestObservableGames, 1000)
                    }
                }
            })
            .catch(function(error){
                window.console.log(error)
                if (this.active) {
                    setTimeout(this.requestObservableGames, 1000)
                }
            })
        },
    }
}
</script>
