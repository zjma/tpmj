<template>
    <v-dialog v-model="active" persistent max-width="600px">
        <v-card>
            <v-card-title></v-card-title>
            <v-card-text>
                <v-list v-if="AllGames">
                    <v-list-item v-for='game in AllGames' :key='`game-${game.GameID}`' @click="onSelect(game.GameID)">
                        <v-list-item-content>
                            <v-list-item-title>{{game.GameID}}</v-list-item-title>
                            <v-list-item-subtitle>Players: {{game.Players.join(',')}}</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-list-item>
                </v-list>
                <div v-else>
                    Loading all games...
                </div>
            </v-card-text>
            <v-card-actions>
                <v-btn color="blue darken-1" text @click="onBack">Back</v-btn>
                <v-spacer></v-spacer>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script>
import axios from 'axios';

export default {
    name: 'ChooseGameDialog',
    props: {
        active          : Boolean,
    },
    data : function(){
        window.console.log("ChooseGameDialog initing data.");
        return {
            AllGames : null,
            QueryPending : false,
            ApiServerPlayUrl : `${process.env.VUE_APP_API_SERVER_URL}/tpmj`,
        };
    },
    mounted: function(){
        const self = this;

        setInterval(function(){
            if (self.active && !self.QueryPending) {
                self.QueryPending = true;
                axios.post(self.ApiServerPlayUrl, {
                    Action:'GetGameList',
                }).then(response => {
                    self.QueryPending = false;
                    var sub = response.data;
                    if (self.active) {
                        window.console.log(sub);
                        if (sub.AllGames) {
                            self.AllGames = sub.AllGames;
                        } else {
                            window.console.log('GetGameList rsponded with some shit.');
                        }
                    } else {
                        window.console.log('GetGameList responded, but ChooseGameDialog is not active any more.');
                    }
                }).catch(function(error){
                    self.QueryPending = false;
                    window.console.log(error);
                })
            }
        }, 1000);
    },
    methods: {
        onBack() {
            this.$emit('cancelled');
        },
        onSelect(gameID) {
            this.$emit('selected', gameID);
        },
    },

};
</script>
