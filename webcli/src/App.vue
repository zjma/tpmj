<template>
  <v-app>
      <login-dialog :active="IsLoginDialogActive" :default-user-name="UserName" @finished="onLoginFinished" />
      <mode-dialog :active="IsModeDialogActive" :default-mode="mode" @play-selected="onPlayModeSelected" @observe-selected="onObserveModeSelected" @cancelled="onModeSelectionCancelled" />
      <observer-waiting-dialog :active="IsObserverWaitingDialogActive" @cancelled="onObserverWaitingCancelled" @selected="onObservedGameSelected"/>
      <mahjong-table />
  </v-app>
</template>

<script>
import LoginDialog from './LoginDialog.vue';
import ModeDialog from './ModeDialog.vue';
import ObserverWaitingDialog from './ObserverWaitingDialog.vue';
import MahjongTable from './MahjongTable.vue';
export default {
  name: 'App',

  components: {
    'login-dialog'              : LoginDialog,
    'mode-dialog'               : ModeDialog,
    'observer-waiting-dialog'   : ObserverWaitingDialog,
    'mahjong-table'             : MahjongTable
  },

  data: () => ({
    UserName: 'NoName',
    mode    : 'Play',
    State   : 'UserLoggingIn'
  }),
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
