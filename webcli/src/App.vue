<template>
    <v-app>
        <div class='Version'>WebCliVersion={{WebCliVersion}}, ApiServerVersion={{ApiServerVersion}}</div>
        <login-dialog :active="IsLoginDialogActive" :default-user-name="UserName" @finished="onLoginFinished" />
        <choose-game-dialog :active="IsGameListDialogActive" @cancelled="onGameSelectionCancelled" @selected="onGameSelected($event)"/>
        <mode-dialog :active="IsModeDialogActive" :default-mode="mode" @play-selected="onPlayModeSelected" @observe-selected="onObserveModeSelected" @cancelled="onModeSelectionCancelled" />
        <player-waiting-dialog :active="IsPlayerWaitingDialogActive" @cancelled="onPlayerWaitingCancelled" @selected="onPlayerGameSelected"/>
        <observer-waiting-dialog :active="IsObserverWaitingDialogActive" @cancelled="onObserverWaitingCancelled" @selected="onObservedGameSelected"/>
        <admin-monitoring-table v-if="IsAdminMonitoring" :active="IsAdminMonitoring" :GameID="MonitoringGameID"/>
        <minimum-digital-table v-if="State=='Playing'" :active="State=='Playing'" :GameID="GameID" :RoleID="MyRole" @Exit="onPlayerLeavingGameRoom"/>
    </v-app>
</template>

<script>
import {uuid} from 'vue-uuid'
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)

import * as Game2Util from './game2.js';
import LoginDialog from './LoginDialog.vue';
import ModeDialog from './ModeDialog.vue';
import ObserverWaitingDialog from './ObserverWaitingDialog.vue';
import PlayerWaitingDialog from './PlayerWaitingDialog.vue';
import MinimumDigitalTable from './MinimumDigitalTable.vue';
import AdminMonitoringTable from './AdminMonitoringTable.vue';
import ChooseGameDialog from './ChooseGameDialog.vue';

export default {
    name: 'App',

    components: {
        'login-dialog'              : LoginDialog,
        'mode-dialog'               : ModeDialog,
        'observer-waiting-dialog'   : ObserverWaitingDialog,
        'player-waiting-dialog'     : PlayerWaitingDialog,
        'minimum-digital-table'     : MinimumDigitalTable,
        'admin-monitoring-table'    : AdminMonitoringTable,
        'choose-game-dialog'        : ChooseGameDialog,
    },
    data: function() {
        var result = {
            UserName            : 'NoName',
            mode                : 'Play',
            State               : 'UserLoggingIn',
            MySeat              : 0,
            gameStateView       : Game2Util.randGameStateView(),
            counter             : 0,
            GameID              : uuid.v4(),
            RoleID              : null,
            MyRole              : 0,
            PlayerWaitingQueryPending : false,
            PlayingQueryPending: false,
            WebCliVersion       : process.env.VUE_APP_WEBCLI_VERSION,
            ApiServerVersion    : 'Connecting...',
            ApiServerAboutUrl   : `${process.env.VUE_APP_API_SERVER_URL}/about`,
            ApiServerPlayUrl    : `${process.env.VUE_APP_API_SERVER_URL}/tpmj`,
            AboutQueryPending   : false,
            MonitoringGameID    : undefined,
        };

        return result;
    },

    mounted: function() {
        window.console.log("App mounted.");
        const self = this

        //'Thread' for polling api server.
        setInterval(function(){
            if (!self.AboutQueryPending) {
                self.AboutQueryPending = true
                axios.get(self.ApiServerAboutUrl).then(response => {
                    self.AboutQueryPending = false
                    var sub = response.data
                    if (sub.Version) {
                        self.ApiServerVersion = sub.Version
                    } else {
                        self.ApiServerVersion = 'Connecting...'
                    }
                }).catch(function(error){
                    self.AboutQueryPending = false
                    window.console.log(error)
                    self.ApiServerVersion = 'Connecting...'
                })
            }
        }, 2000)

        //Thread for polling backend for waiting state.
        setInterval(function(){
            if (self.State == 'PlayerWaitingForGame' && !self.PlayerWaitingQueryPending) {
                self.PlayerWaitingQueryPending = true
                axios.post(self.ApiServerPlayUrl, {
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
                        self.MyRole = sub.Role;
                        self.RoleID = sub.Role;
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
        IsGameListDialogActive: function(){
            return this.State == 'AdminChoosingGameToMonitor';
        },
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
        IsResultDialogActive: function(){
            return this.State == 'GameFinished'
        },
        IsAdminMonitoring: function(){
            return this.State == 'AdminMonitoring'
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
            if (userName=='admin') {
                this.State = 'AdminChoosingGameToMonitor';
            } else {
                this.State = 'UserSelectingMode'
            }
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
        onGameResultConfirmed(){
            window.console.log("Game result confirmed.");
            this.State = 'UserSelectingMode';
        },
        onGameSelectionCancelled(){
            window.console.log("Game selection cancelled.");
            this.State = 'UserLoggingIn';
        },
        onGameSelected(gameID){
            window.console.log(`Game ${gameID} selected.`);
            this.MonitoringGameID = gameID;
            this.State = 'AdminMonitoring';
        },
        onPlayerLeavingGameRoom(){
            window.console.log(`onPlayerLeavingGameRoom`);
            this.State = 'UserSelectingMode';
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
