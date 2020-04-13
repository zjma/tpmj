<template>
    <v-app>
        <v-app-bar app color="indigo" dark>
            索子麻雀练习
            <v-spacer/>
            <v-bottom-sheet>
                <template v-slot:activator="{ on }">
                    <v-btn dark v-on="on" text>
                        版本与运行状态
                        <!-- <v-icon>mdi-access-point</v-icon> -->
                    </v-btn>
              </template>
              <v-sheet height="200px">
                  <div>WebCliVersion={{WebCliVersion}}</div>
                  <div>ApiServerVersion={{ApiServerVersion}}</div>
              </v-sheet>
            </v-bottom-sheet>
        </v-app-bar>
        <v-content>
            <login-dialog :active="IsLoginDialogActive" :default-user-name="UserName" @finished="onLoginFinished" />
            <choose-game-dialog :active="IsGameListDialogActive" @cancelled="onGameSelectionCancelled" @selected="onGameSelected($event)"/>
            <mode-dialog :active="IsModeDialogActive" :default-mode="mode" @play-selected="onPlayModeSelected" @observe-selected="onObserveModeSelected" @cancelled="onModeSelectionCancelled" />
            <player-waiting-dialog :active="IsPlayerWaitingDialogActive" :PlayerName="UserName" @cancelled="onPlayerWaitingCancelled" @selected="onPlayerGameSelected"/>
            <observer-waiting-dialog :active="IsObserverWaitingDialogActive" @cancelled="onObserverWaitingCancelled" @selected="onObservedGameSelected"/>
            <admin-monitoring-table v-if="IsAdminMonitoring" :active="IsAdminMonitoring" :GameID="MonitoringGameID"/>
            <minimum-digital-table v-if="State=='Playing'" :active="State=='Playing'" :GameID="GameID" :RoleID="MyRole" @Exit="onPlayerLeavingGameRoom"/>
        </v-content>
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
            UserName            : uuid.v4().substring(0,8),
            mode                : 'Play',
            State               : 'Playing',
            MySeat              : 0,
            gameStateView       : Game2Util.randGameStateView(),
            counter             : 0,
            GameID              : null,
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
        onPlayerGameSelected(params){
            this.GameID = params.GameID;
            this.RoleID = params.RoleID;
            this.MyRole = params.RoleID;
            this.State = 'Playing';
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
    font-size: 1em;
}
</style>
