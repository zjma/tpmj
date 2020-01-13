<template>
  <v-app>
      <login-dialog :active="IsLoginDialogActive" :default-user-name="UserName" @finished="onLoginFinished" />
      <mode-dialog :active="IsModeDialogActive" :default-mode="mode" @play-selected="onPlayModeSelected" @observe-selected="onObserveModeSelected" @cancelled="onModeSelectionCancelled" />
      <!-- <observer-waiting-dialog :active="IsObserverWaitingDialogActive" @cancelled="onObserverWaitingCancelled" /> -->
      <v-dialog v-model="ShowObserverWaitingDialog" persistent max-width="600px">
        <v-card>
          <v-card-title>
            <span class="headline"></span>
          </v-card-title>
          <v-container>
            Searching...
          </v-container>
          <v-card-actions>
            <v-btn color="blue darken-1" text @click="onObserverWaitingCanceled()">Back</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    <v-app-bar app color="primary" dark>
      <div class="d-flex align-center">
        <v-img
          src="@/assets/logo.png"
          alt="Miku Logo"
          class="shrink mr-2"
          contain
          transition="scale-transition"
          width="40"
        />

        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"
          width="100"
        />
      </div>

      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
        text
      >
        <span class="mr-2">Latest Release</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-content>
      <HelloWorld :username="this.UserName"/>
    </v-content>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld';
import LoginDialog from './LoginDialog.vue';
import ModeDialog from './ModeDialog.vue';
// import ObserverWaitingDialog from './ObserverWaitingDialog.vue';
export default {
  name: 'App',

  components: {
    'login-dialog'              : LoginDialog,
    'mode-dialog'               : ModeDialog,
    // 'observer-waiting-dialog'   : ObserverWaitingDialog,
    HelloWorld
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

    ShowObserverWaitingDialog: function(){
        return this.State == 'ObserverWaitingForGame'
    }
  },
    methods: {
        onPlayModeSelected : function(){
            this.mode = 'Play';
            this.State = 'PlayerWaitingForMatch';
        },
        onObserveModeSelected : function(){
            this.mode = 'Observe';
            this.State = 'ObserverWaitingForGame';
        },
        onModeSelectionCancelled : function(){
            this.State = 'UserLoggingIn';
        },
        onModeChosen(){
            if (this.Mode == 'Observe') {
                this.State = 'ObserverWaitingForGame'
                setInterval(function(){
                    // this.$http.post('/tpmj',{Action:'GetObservableGameID'}).then(function(res){
                    //     window.console.log(res.json);
                    // },function(){
                    //     window.console.log('Failed');
                    // });
                    window.console.log('Working.');
                }, 1000)
            } else {
                this.State = 'UserSelectingMode'
            }
        },
        onObserverWaitingCanceled(){
            this.State = 'UserSelectingMode'
        },
        onLoginFinished(userName){
            window.console.log(userName);
            this.UserName = userName
            this.State = 'UserSelectingMode'
        }
    }
};
</script>
