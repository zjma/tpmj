<template>
    <v-container id='TheContainer' class="fill-height" fluid>
        <v-row v-if="isGameStateViewValid" id='GameView' align='end'>
            <v-col md='6' cols='12'>
                <div class='OppoArea'>
                    <v-row>
                        <v-col cols='4'>
                            <v-card outlined>
                                <v-card-title>
                                    <div class='SeatIndicator'>
                                        {{OppoRoleLabel}}
                                    </div>
                                </v-card-title>
                                <v-card-text class='PlayerName'>
                                    {{OppoName}}
                                </v-card-text>
                            </v-card>
                        </v-col>
                        <v-col>
                            <div class='RiverRow TileOnlyContainer'>
                                {{OppoRiver}}
                            </div>
                        </v-col>
                    </v-row>
                    <div class='Hand TileOnlyContainer'>
                        {{OppoHand}}
                    </div>
                    <v-row class='TileOnlyContainer BuiltSet'>
                        <v-col>{{OppoSet3}}</v-col>
                        <v-col>{{OppoSet2}}</v-col>
                        <v-col>{{OppoSet1}}</v-col>
                        <v-col>{{OppoSet0}}</v-col>
                    </v-row>
                </div>
                <v-card>
                    <v-card-text class='GameMetadata'>{{BadgeText}}</v-card-text>
                </v-card>
                <div>
                    <v-row>
                        <v-col cols='4'>
                            <v-card outlined>
                                <v-card-title>
                                    <div class='SeatIndicator'>
                                        {{SelfRoleLabel}}
                                    </div>
                                </v-card-title>
                                <v-card-text class='PlayerName'>
                                    {{SelfName}}
                                </v-card-text>
                            </v-card>
                        </v-col>
                        <v-col>
                            <div class='RiverRow TileOnlyContainer'>
                                {{SelfRiver}}
                            </div>
                        </v-col>
                    </v-row>
                    <div class='Hand TileOnlyContainer'>
                        {{SelfHand}}
                    </div>
                    <v-row class='TileOnlyContainer BuiltSet'>
                        <v-col>{{SelfSet3}}</v-col>
                        <v-col>{{SelfSet2}}</v-col>
                        <v-col>{{SelfSet1}}</v-col>
                        <v-col>{{SelfSet0}}</v-col>
                    </v-row>
                </div>
            </v-col>
            <v-col md='6' cols='12' class='PlayerActions'>
                <v-list two-line>
                    <v-list-item v-for='(action,idx) in ActionUiData' :key='idx' @click="onAction(action.Data)">
                        <v-list-item-content>
                            <v-list-item-title class='TileOnlyContainer' style="font-size: 1em;">{{action.Value}}</v-list-item-title>
                            <v-list-item-subtitle>{{action.Type}}</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-list-item>
                </v-list>
            </v-col>
        </v-row>
        <div v-else id='PendingView'>
            <div class="lds-ring"><div></div><div></div><div></div><div></div></div>
        </div>
        <result-dialog :active="ShowingResultDialog" :gameStateView='gameStateView' @done="onResultDialogClosing"></result-dialog>
    </v-container>
</template>

<script>
import axios from 'axios';
import * as Game2Utils from './game2.js';
import * as styling from './PlayerAreaStyling.js';
import GameResultDialog from './GameResultDialog.vue';

export default {
    name : 'MinimumDigitalTable',
    components : {
        'result-dialog' : GameResultDialog,
    },
    props: {
        active : Boolean,
        GameID : String,
        RoleID : Number,
    },
    data: function(){
        window.console.log("[MinimumDigitalTable] initing data.");
        return {
            QueryPending : false,
            ApiServerPlayUrl : `${process.env.VUE_APP_API_SERVER_URL}/tpmj`,
            gameStateView : Game2Utils.randGameStateView(),
            isGameStateViewValid : false,
            ShowingResultDialog : false,
            ResultPrompted : false,
        };
    },
    computed: {
        BadgeText:function(){
            return `${styling.GameNameText} · ${styling.MountainRemainingLabelText}:${this.MountainRemaining}`;
        },
        mySeat: function() {
            return Game2Utils.getSeatByRole(this.RoleID)
        },
        oppoSeat: function() {
            return Game2Utils.getSeatByRole(1-this.RoleID)
        },
        OppoRoleLabel: function(){
            return styling.getSeatChar(1-this.RoleID)
        },
        SelfRoleLabel: function(){
            return styling.getSeatChar(this.RoleID)
        },
        MountainRemaining: function(){
            var accumulator = (accumulated, toProcess) => toProcess.Mountain.filter(v => v!=undefined).length + accumulated
            return this.gameStateView.AreaViews.reduce(accumulator, 0)
        },
        SelfName: function(){
            return this.gameStateView.PlayerNames[this.RoleID]
        },
        OppoName: function(){
            return this.gameStateView.PlayerNames[1-this.RoleID]
        },
        SelfRiver: function(){
            return this.gameStateView.AreaViews[this.mySeat].River.map(v => styling.getTileViewChar(v)).join('')
        },
        OppoRiver: function(){
            return this.gameStateView.AreaViews[this.oppoSeat].River.map(v => styling.getTileViewChar(v)).join('')
        },
        SelfHand: function(){
            return styling.getHandStr(this.gameStateView, this.mySeat);
        },
        OppoHand: function(){
            var oldHandStr = this.gameStateView.AreaViews[this.oppoSeat].OldHand.map(v => styling.getTileViewChar(v)).join('')
            var newHandStr = this.gameStateView.AreaViews[this.oppoSeat].NewHand.map(v => styling.getTileViewChar(v)).join('')
            return oldHandStr+' '+newHandStr
        },
        SelfSet0: function(){
            var set = this.gameStateView.AreaViews[this.mySeat].BuiltSets[0]
            return (set) ? set.TileViews.map(v => styling.getTileViewChar(v)).join('') : undefined
        },
        SelfSet1: function(){
            var set = this.gameStateView.AreaViews[this.mySeat].BuiltSets[1]
            return (set) ? set.TileViews.map(v => styling.getTileViewChar(v)).join('') : undefined
        },
        SelfSet2: function(){
            var set = this.gameStateView.AreaViews[this.mySeat].BuiltSets[2]
            return (set) ? set.TileViews.map(v => styling.getTileViewChar(v)).join('') : undefined
        },
        SelfSet3: function(){
            var set = this.gameStateView.AreaViews[this.mySeat].BuiltSets[3]
            return (set) ? set.TileViews.map(v => styling.getTileViewChar(v)).join('') : undefined
        },
        OppoSet0: function(){
            var set = this.gameStateView.AreaViews[this.oppoSeat].BuiltSets[0]
            return (set) ? set.TileViews.map(v => styling.getTileViewChar(v)).join('') : undefined
        },
        OppoSet1: function(){
            var set = this.gameStateView.AreaViews[this.oppoSeat].BuiltSets[1]
            return (set) ? set.TileViews.map(v => styling.getTileViewChar(v)).join('') : undefined
        },
        OppoSet2: function(){
            var set = this.gameStateView.AreaViews[this.oppoSeat].BuiltSets[2]
            return (set) ? set.TileViews.map(v => styling.getTileViewChar(v)).join('') : undefined
        },
        OppoSet3: function(){
            var set = this.gameStateView.AreaViews[this.oppoSeat].BuiltSets[3]
            return (set) ? set.TileViews.map(v => styling.getTileViewChar(v)).join('') : undefined
        },
        ActionUiData: function(){
            var actions = Game2Utils.getAction(this.gameStateView, this.RoleID);
            var result = actions.map(a => styling.getActionUIData(a));

            //Special actions: show score & continue after game finishes.
            if (this.gameStateView.State.Main == 'PlayerXWon' || this.gameStateView.State.Main == 'Finished') {
                result.push({
                    Type: '',
                    Value: 'Show Score',
                    Data: 'ShowScore',
                });
                result.push({
                    Type: '',
                    Value: 'Continue',
                    Data: 'Exit',
                });
            }

            return result;
        },
    },
    mounted: function(){
        const self = this;

        setInterval(function(){
            if (self.active && !self.QueryPending) {
                self.QueryPending = true;
                axios.post(self.ApiServerPlayUrl, {
                    Action:'GetGameState',
                    GameID:self.GameID,
                    RoleID:self.RoleID,
                }).then(response => {
                    self.QueryPending = false;
                    var sub = response.data;
                    if (self.active) {
                        self.gameStateView = sub;
                        self.isGameStateViewValid = true;
                        if (sub.State.Main=='PlayerXWon' || sub.State.Main=='Finished') {
                            self.onGameResultAvailable();
                        }
                    }
                }).catch(function(error){
                    self.QueryPending = false;
                    window.console.log(error);
                })
            }
        },1000)
    },
    methods: {
        onGameResultAvailable:function(){
            if (!this.ResultPrompted) {
                this.ShowingResultDialog = true;
                this.ResultPrompted = true;
            }
        },
        onAction(action){
            window.console.log("User action!");
            window.console.log(action);
            if (action=='Exit'){
                this.$emit('Exit');
            } else if (action=='ShowScore'){
                this.ShowingResultDialog = true;
            } else {
                axios.post(this.ApiServerPlayUrl, {
                    Action:'PerformGameAction',
                    GameID:this.GameID,
                    RoleID: this.RoleID,
                    Payload:action,
                });
            }
        },
        onResultDialogClosing: function(){
            this.ShowingResultDialog = false;
        },
    },
}
</script>

<style scoped>
.PlayerName {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.GameMetadata {
    text-align: center;
}

.OppoArea {
    transform: rotate(180deg);
}

.SeatIndicator {
    font-size: 2em;
    text-align: center;
}

#GameView {
    font-size: 2rem;
}

.hand {
    font-size: 1em;
}

.PlayerActions {
    height: 30vh;
    overflow-y: scroll;
}

.ActionPreview {
    font-size: 2rem;
}
/*
@font-face {
  font-family: "color-emoji";
  src: local("Apple Color Emoji"),
       local("Segoe UI Emoji"),
       local("Segoe UI Symbol"),
       local("Noto Color Emoji");
} */

.TileOnlyContainer {
    font-size: 1.5rem;
    /* font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji"; */
    font-family: "Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";
}

.BuiltSet {
}

.lds-ring {
    width: 100px;
    height: 100px;
    margin-left: auto;
    margin-right: auto;
}

.lds-ring div {
    box-sizing: border-box;
    display: block;
    position: absolute;
    width: 100px;
    height: 100px;
    margin: 8px;
    border: 8px solid #fff;
    border-radius: 50%;
    animation: lds-ring 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
    border-color: #82b1ff transparent transparent transparent;
}
.lds-ring div:nth-child(1) {
    animation-delay: -0.45s;
}
.lds-ring div:nth-child(2) {
    animation-delay: -0.3s;
}
.lds-ring div:nth-child(3) {
    animation-delay: -0.15s;
}
@keyframes lds-ring {
    0% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(360deg);
    }
}

#PendingView {
    width:100%;
}

</style>
