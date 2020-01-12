<template>
  <v-app>
      <v-dialog v-model="ShowUserNameDialog" persistent max-width="600px">
          <UserNameForm v-bind:DefaultUserName="UserName" v-on:UserNameCollected="onUserNameCollected" />
      </v-dialog>
      <v-dialog v-model="ShowModeDialog" persistent max-width="600px">
        <v-card>
          <v-card-title>
            <span class="headline">Choose Mode</span>
          </v-card-title>

          <v-container>
              <v-radio-group v-model="Mode">
                  <v-radio label="Play" value="Play"></v-radio>
                  <v-radio label="Observe" value="Observe"></v-radio>
              </v-radio-group>
          </v-container>
          <v-card-actions>
            <v-btn color="blue darken-1" text @click="onBackPressed()">Back</v-btn>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="onModeChosen()">Next</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
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
    <v-app-bar
      app
      color="primary"
      dark
    >
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
import UserNameForm from './UserNameForm.vue';
export default {
  name: 'App',

  components: {
    HelloWorld,
    UserNameForm
  },

  data: () => ({
    UserName: 'NoName',
    Mode    : 'Play',
    State   : 'UserChoosingName'
  }),
  computed: {
    ShowUserNameDialog: function(){
        return this.State == 'UserChoosingName'
    },

    ShowModeDialog: function(){
        return this.State == 'UserSelectingMode'
    },

    ShowObserverWaitingDialog: function(){
        return this.State == 'ObserverWaitingForGame'
    }
  },
  methods: {
    onBackPressed(){
        this.State = 'UserChoosingName'
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
    onUserNameCollected(arg){
        window.console.log(arg);
        this.UserName = arg
        this.State = 'UserSelectingMode'
    }
  }
};
</script>
