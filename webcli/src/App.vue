<template>
  <v-app>
      <login-dialog :active="IsLoginDialogActive" :default-user-name="UserName" @finished="onLoginFinished" />
      <mode-dialog :active="IsModeDialogActive" :default-mode="mode" @play-selected="onPlayModeSelected" @observe-selected="onObserveModeSelected" @cancelled="onModeSelectionCancelled" />
      <observer-waiting-dialog :active="IsObserverWaitingDialogActive" @cancelled="onObserverWaitingCancelled" @selected="onObservedGameSelected"/>
      <mahjong-table :gameStateView="gameStateView" :mySeat="mySeat" />
  </v-app>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)

import * as Utils from './util.js'
import * as Game2Util from './game2.js'
import LoginDialog from './LoginDialog.vue'
import ModeDialog from './ModeDialog.vue'
import ObserverWaitingDialog from './ObserverWaitingDialog.vue'
import MahjongTable from './MahjongTable.vue'

export default {
    name: 'App',

    components: {
        'login-dialog'              : LoginDialog,
        'mode-dialog'               : ModeDialog,
        'observer-waiting-dialog'   : ObserverWaitingDialog,
        'mahjong-table'             : MahjongTable,
    },
    data: function() {
        return {
            UserName            : 'NoName',
            mode                : 'Play',
            State               : 'Observing',
            mySeat              : Utils.randInt(0,4),
            gameStateView       : Game2Util.randGameStateView(),
            counter             : 0,
        }
    },

    mounted: function() {
        const self = this
        setInterval(function(){
            if (!self.inProgress) {
                self.inProgress = true
                axios.post(process.env.VUE_APP_API_SERVER_URL, {Action:'GetGameState2',GameID:'qwer',RoleID:-1,})
                .then(response => {
                    var sub = response.data
                    self.gameStateView = sub
                    self.inProgress = false
                })
                .catch(function(error){
                    window.console.log(error)
                    self.inProgress = false
                })
            }
        }, 1000)
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
        }
    },
    methods: {
        onPlayModeSelected : function(){
            window.console.warn('Not implemented')
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
        }
    },
};
</script>
