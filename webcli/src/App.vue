<template>
    <v-app>
        <div class='Version'>WebCliVersion={{WebCliVersion}}</div>
        <login-dialog :active="IsLoginDialogActive" :default-user-name="UserName" @finished="onLoginFinished" />
        <mode-dialog :active="IsModeDialogActive" :default-mode="mode" @play-selected="onPlayModeSelected" @observe-selected="onObserveModeSelected" @cancelled="onModeSelectionCancelled" />
        <player-waiting-dialog :active="IsPlayerWaitingDialogActive" @cancelled="onPlayerWaitingCancelled" @selected="onPlayerGameSelected"/>
        <observer-waiting-dialog :active="IsObserverWaitingDialogActive" @cancelled="onObserverWaitingCancelled" @selected="onObservedGameSelected"/>
        <minimum-digital-table :gameStateView="gameStateView" :myRole="MyRole" @UserAction="onUserAction"/>
    </v-app>
</template>

<script>
import Vue from 'vue'
import {uuid} from 'vue-uuid'
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)

import * as Game2Util from './game2.js'
import LoginDialog from './LoginDialog.vue'
import ModeDialog from './ModeDialog.vue'
import ObserverWaitingDialog from './ObserverWaitingDialog.vue'
import PlayerWaitingDialog from './PlayerWaitingDialog.vue'
import MinimumDigitalTable from './MinimumDigitalTable.vue'

export default {
    name: 'App',

    components: {
        'login-dialog'              : LoginDialog,
        'mode-dialog'               : ModeDialog,
        'observer-waiting-dialog'   : ObserverWaitingDialog,
        'player-waiting-dialog'     : PlayerWaitingDialog,
        'minimum-digital-table'     : MinimumDigitalTable,
    },
    data: function() {
        return {
            UserName            : 'NoName',
            mode                : 'Play',
            State               : 'UserLoggingIn',
            MySeat              : 0,
            gameStateView       : Game2Util.randGameStateView(),
            counter             : 0,
            GameID              : uuid.v4(),
            MyRole              : 0,
            PlayerWaitingQueryPending : false,
            PlayingQueryPending: false,
            WebCliVersion       : process.env.VUE_APP_WEBCLI_VERSION,
        }
    },

    mounted: function() {
        const self = this
        setInterval(function(){
            if (self.State == 'Playing' && !self.PlayingQueryPending) {
                self.PlayingQueryPending = true
                axios.post(process.env.VUE_APP_API_SERVER_URL, {
                    Action:'GetGameState',
                    GameID:self.GameID,
                    RoleID:self.MyRole,
                }).then(response => {
                    self.PlayingQueryPending = false
                    var sub = response.data
                    if (self.State == 'Playing') {
                        self.gameStateView = sub
                        if (sub.State.Main == 'PlayerXWon' || sub.State.Main == 'Finished') {
                            window.console.log(sub.State)
                            self.State = 'UserSelectingMode'
                        }
                    }
                }).catch(function(error){
                    self.PlayingQueryPending = false
                    window.console.log(error)
                })
            }
        }, 1000)

        setInterval(function(){
            if (self.State == 'PlayerWaitingForGame' && !self.PlayerWaitingQueryPending) {
                self.PlayerWaitingQueryPending = true
                axios.post(process.env.VUE_APP_API_SERVER_URL, {
                    Action:'RequestMatch',
                    PlayerName:self.UserName,
                }).then(response => {
                    self.PlayerWaitingQueryPending = false
                    var sub = response.data
                    if (self.State == 'PlayerWaitingForGame' && sub.GameID) {
                        window.console.log('Switching to playing view.')
                        window.console.log(sub)
                        self.State = 'Playing'
                        self.GameID = sub.GameID
                        self.MyRole = sub.Role
                        self.MySeat = (sub.Role==0)?0:2
                    }
                }).catch(function(error){
                    self.PlayerWaitingQueryPending = false
                    window.console.log(error)
                })

            }
        },2000)
    },

    computed: {
        IsLoginDialogActive: function(){
            return this.State == 'UserLoggingIn'
        },

        IsModeDialogActive: function(){
            return this.State == 'UserSelectingMode'
        },

        IsObserverWaitingDialogActive: function(){
            return this.State == 'ObserverWaitingForGame'
        },

        IsPlayerWaitingDialogActive: function(){
            return this.State == 'PlayerWaitingForGame'
        },
    },
    methods: {
        onPlayModeSelected : function(){
            this.mode = 'Play'
            this.State = 'PlayerWaitingForGame'
        },
        onObserveModeSelected : function(){
            this.mode = 'Observe'
            this.State = 'ObserverWaitingForGame'
        },
        onModeSelectionCancelled : function(){
            this.State = 'UserLoggingIn'
        },
        onLoginFinished(userName){
            window.console.log(userName)
            this.UserName = userName
            this.State = 'UserSelectingMode'
        },
        onObserverWaitingCancelled(){
            this.State = 'UserSelectingMode'
        },
        onObservedGameSelected(gameID){
            window.console.log("Starting to observe " + gameID + ".")
            this.State = 'Observing'
        },
        onPlayerWaitingCancelled(){
            this.State = 'UserSelectingMode'
        },
        onPlayerGameSelected(gameID){
            window.console.log("Starting to observe " + gameID + ".")
            this.State = 'Playing'
        },
        onUserAction(action){
            window.console.log("User action!")
            window.console.log(action)
            axios.post(process.env.VUE_APP_API_SERVER_URL, {
                Action:'PerformGameAction',
                GameID:this.GameID,
                RoleID: this.MyRole,
                Payload:action,
            })
        }
    },
};
</script>

<style>
.Version {
    font-family: monospace;
    text-align: right;
    font-size: 1em;
}
</style>
