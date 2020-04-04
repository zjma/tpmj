<template>
    <v-dialog v-model="active" persistent max-width="600px">
        <v-card>
            <v-card-title>
                <span class="headline"></span>
            </v-card-title>
            <v-card-text>{{StatusText}}</v-card-text>
            <v-card-actions>
                <v-btn color="blue darken-1" text @click="onBack"><v-icon>mdi-arrow-left</v-icon></v-btn>
                <v-spacer/>
                <v-btn color="blue darken-1" :disabled="!Nextable" text @click="onNext"><v-icon>mdi-arrow-right</v-icon>{{NextCountdown}}</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script>
import axios from 'axios';
import * as styling from './PlayerAreaStyling.js';

export default {
    name: 'PlayerWaitingDialog',
    props : {
        active:Boolean,
        PlayerName:String,
    },
    computed: {
        NextCountdown: function(){
            if (this.GameID==null){
                return '';
            } else {
                return `(${this.Countdown})`;
            }
        },
        StatusText:function(){
            if (this.GameID==null){
                return styling.MatchingText;
            } else {
                return styling.MatchedText;
            }
        }
    },
    data : function(){
        return {
            QueryPending:false,
            ApiServerPlayUrl    : `${process.env.VUE_APP_API_SERVER_URL}/tpmj`,
            GameID : null,
            RoleID : null,
            Nextable : false,
            Countdown : 9,
        };
    },
    mounted: function(){
        const self = this;

        //Thread for polling backend for waiting state.
        setInterval(function(){
            if (self.active && self.GameID==null && !self.QueryPending) {
                self.QueryPending = true;
                axios.post(self.ApiServerPlayUrl, {
                    Action:'RequestMatch',
                    PlayerName:self.PlayerName,
                }).then(response => {
                    self.QueryPending = false;
                    var sub = response.data;
                    if (self.active && sub.GameID) {
                        self.GameID = sub.GameID;
                        self.RoleID = sub.Role;
                        self.Nextable = true;
                        self.Countdown = 9;
                    }
                }).catch(function(error){
                    self.QueryPending = false;
                    window.console.log(error);
                })
            }
        },1000);

        setInterval(function(){
            if (self.active && self.GameID!=null){
                if (self.Countdown<=0){
                    self.onNext();
                }else{
                    self.Countdown--;
                }
            }
        }, 1000);
    },
    methods: {
        onBack : function(){
            this.$emit('cancelled');
        },
        onNext(){
            this.$emit("selected", {GameID:this.GameID,RoleID:this.RoleID});
        },
    }
}
</script>

<style scoped>

#IconContainer {
    width: 80px;
    height: 80px;
    margin-left: auto;
    margin-right: auto;
}

.lds-grid {
  display: inline-block;
  position: relative;
  width: 80px;
  height: 80px;
}
.lds-grid div {
  position: absolute;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: #82b1ff;
  animation: lds-grid 1.2s linear infinite;
}
.lds-grid div:nth-child(1) {
  top: 8px;
  left: 8px;
  animation-delay: 0s;
}
.lds-grid div:nth-child(2) {
  top: 8px;
  left: 32px;
  animation-delay: -0.4s;
}
.lds-grid div:nth-child(3) {
  top: 8px;
  left: 56px;
  animation-delay: -0.8s;
}
.lds-grid div:nth-child(4) {
  top: 32px;
  left: 8px;
  animation-delay: -0.4s;
}
.lds-grid div:nth-child(5) {
  top: 32px;
  left: 32px;
  animation-delay: -0.8s;
}
.lds-grid div:nth-child(6) {
  top: 32px;
  left: 56px;
  animation-delay: -1.2s;
}
.lds-grid div:nth-child(7) {
  top: 56px;
  left: 8px;
  animation-delay: -0.8s;
}
.lds-grid div:nth-child(8) {
  top: 56px;
  left: 32px;
  animation-delay: -1.2s;
}
.lds-grid div:nth-child(9) {
  top: 56px;
  left: 56px;
  animation-delay: -1.6s;
}
@keyframes lds-grid {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
}

</style>
