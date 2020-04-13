<template>
    <v-container fluid>

        <v-row v-if="isGameStateViewValid" id='GameView' align='end' no-gutters>
            <v-col cols='12' md='6' class="GameStateView">
                <div class='OppoArea Area'>
                    <v-row>
                        <v-col class='SeatIndiContainer'>
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
                            <TileViewRow :TileViews="OppoRiver"/>
                        </v-col>
                    </v-row>
                    <div class="d-flex">
                        <div class='HandRowContainer'>
                            <TileViewRow :TileViews="OppoOldHand"/>
                        </div>
                        <div class='HandRowContainer'>
                            <TileViewRow :TileViews="OppoNewHand"/>
                        </div>
                    </div>
                    <div class='BuiltSetContainer'>
                        <TileViewRow :TileViews="OppoSet0"/>
                        <TileViewRow :TileViews="OppoSet1"/>
                        <TileViewRow :TileViews="OppoSet2"/>
                        <TileViewRow :TileViews="OppoSet3"/>
                    </div>
                </div>
                <v-card outlined>
                    <v-card-text>{{BadgeText}}</v-card-text>
                    <!-- <v-btn text large @click="onRuleBook">番种表</v-btn>
                    <v-btn text large @click="onContrlSettings">设置</v-btn>
                    <v-btn text large :disabled='IsGameResultAvailable' @click="onClickShowScore">本局得分</v-btn> -->
                </v-card>
                <div class='Area'>
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
                            <TileViewRow :TileViews="SelfRiver" />
                        </v-col>
                    </v-row>
                    <div class="d-flex">
                        <div class='HandRowContainer'>
                            <TileViewRow :TileViews="SelfOldHand"/>
                        </div>
                        <div class='HandRowContainer'>
                            <TileViewRow :TileViews="SelfNewHand"/>
                        </div>
                    </div>
                    <div class='BuiltSetContainer'>
                        <TileViewRow :TileViews="SelfSet0"/>
                        <TileViewRow :TileViews="SelfSet1"/>
                        <TileViewRow :TileViews="SelfSet2"/>
                        <TileViewRow :TileViews="SelfSet3"/>
                    </div>
                </div>
            </v-col>
            <v-col cols='12' md='6' class='PlayerActions'>
                <!-- <v-card>
                    <v-container>
                        <v-btn text outlined width="100%" min-height=100 class="ModeButton">匹配</v-btn>
                        <v-btn text outlined width="100%" min-height=100 disabled class="ModeButton">something</v-btn>
                    </v-container>
                </v-card> -->


                <!-- <v-list two-line>
                    <v-list-item v-for='(action,idx) in ActionUiData' :key='idx' @click="onAction(action.Data)">
                        <v-list-item-content>
                            <div class='d-flex PreviewContainer'>
                                <TileViewRow v-for='(row,idx) in action.Preview' :key='`preview-${idx}`' :TileViews='row' />
                            </div>
                            <v-list-item-subtitle>{{action.Type}}</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-list-item>
                </v-list> -->
            </v-col>
        </v-row>
        <div v-else id='PendingView'>
            <div class="lds-ring"><div></div><div></div><div></div><div></div></div>
        </div>
        <v-footer color="primary lighten-1" padless absolute class='ActionPanel'>
            <v-btn color="white" text outlined>你的回合(5)</v-btn>
            <v-btn color="white" text outlined>你的回合(5)</v-btn>
            <v-btn color="white" text outlined>你的回合(5)</v-btn>
            <v-btn color="white" text outlined>你的回合(5)</v-btn>
            <v-switch v-model="AutoPass" dark label="自动Pass"></v-switch>
        </v-footer>
        <result-dialog :active="ShowingResultDialog" :gameStateView='gameStateView' @done="onResultDialogClosing"></result-dialog>
        <rulebook-dialog :active="ShowingRuleBook" :content="ruleBookContent" @done="onExitFromRuleBook"></rulebook-dialog>
    </v-container>
</template>

<script>
import axios from 'axios';
import * as Game2Utils from './game2.js';
import * as styling from './PlayerAreaStyling.js';
import GameResultDialog from './GameResultDialog.vue';
import RuleBookDialog from './RuleBookDialog.vue';
import TileViewRow from './TileViewRow.vue';

export default {
    name : 'MinimumDigitalTable',
    components : {
        'result-dialog' : GameResultDialog,
        'rulebook-dialog': RuleBookDialog,
        'TileViewRow' : TileViewRow,
    },
    props: {
        active : Boolean,
        GameID : String,
        RoleID : Number,
    },
    data: function(){
        window.console.log("[MinimumDigitalTable].data()");
        return {
            QueryPending : false,
            ApiServerPlayUrl : `${process.env.VUE_APP_API_SERVER_URL}/tpmj`,
            gameStateView : Game2Utils.randGameStateView(),
            isGameStateViewValid : false,
            ShowingResultDialog : false,
            ResultPrompted : false,
            ShowingRuleBook : false,
            ruleBookContent : {},
            AutoPass: true,
        };
    },
    computed: {
        IsGameResultAvailable: function(){
            return this.gameStateView.State.Main == 'PlayerXWon' || this.gameStateView.State.Main == 'Finished';
        },
        BadgeText:function(){
            return `${styling.MountainRemainingLabelText}:${this.MountainRemaining}`;
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
            return this.gameStateView.AreaViews[this.mySeat].River;
        },
        OppoRiver: function(){
            return this.gameStateView.AreaViews[this.oppoSeat].River;
        },
        SelfHand: function(){
            return styling.getHandStr(this.gameStateView, this.mySeat);
        },
        OppoOldHand:function(){
            return this.gameStateView.AreaViews[this.oppoSeat].OldHand;
        },
        OppoNewHand:function(){
            return this.gameStateView.AreaViews[this.oppoSeat].NewHand;
        },
        SelfOldHand:function(){
            return this.gameStateView.AreaViews[this.mySeat].OldHand;
        },
        SelfNewHand:function(){
            return this.gameStateView.AreaViews[this.mySeat].NewHand;
        },
        SelfSet0: function(){
            var set = this.gameStateView.AreaViews[this.mySeat].BuiltSets[0];
            return (set) ? set.TileViews : [];
        },
        SelfSet1: function(){
            var set = this.gameStateView.AreaViews[this.mySeat].BuiltSets[1];
            return (set) ? set.TileViews : [];
        },
        SelfSet2: function(){
            var set = this.gameStateView.AreaViews[this.mySeat].BuiltSets[2];
            return (set) ? set.TileViews : [];
        },
        SelfSet3: function(){
            var set = this.gameStateView.AreaViews[this.mySeat].BuiltSets[3];
            return (set) ? set.TileViews : [];
        },
        OppoSet0: function(){
            var set = this.gameStateView.AreaViews[this.oppoSeat].BuiltSets[0];
            return (set) ? set.TileViews : [];
        },
        OppoSet1: function(){
            var set = this.gameStateView.AreaViews[this.oppoSeat].BuiltSets[1];
            return (set) ? set.TileViews : [];
        },
        OppoSet2: function(){
            var set = this.gameStateView.AreaViews[this.oppoSeat].BuiltSets[2];
            return (set) ? set.TileViews : [];
        },
        OppoSet3: function(){
            var set = this.gameStateView.AreaViews[this.oppoSeat].BuiltSets[3];
            return (set) ? set.TileViews : [];
        },
        ActionUiData: function(){
            var actions = Game2Utils.getAction(this.gameStateView, this.RoleID);
            var result = actions.map(a => styling.getActionUIData(a));

            //Special actions: show score & continue after game finishes.
            if (this.gameStateView.State.Main == 'PlayerXWon' || this.gameStateView.State.Main == 'Finished') {
                result.push({
                    Type: styling.GameEndShowResult,
                    Value: '',
                    Data: 'ShowScore',
                });
                result.push({
                    Type: styling.GameEndContinue,
                    Value: '',
                    Data: 'Exit',
                });
            }

            return result;
        },
    },
    mounted: function(){
        window.console.log("[MinimumDigitalTable].mounted()");
        const self = this;

        setInterval(function(){
            if (!self.active) return;

            //If valid GameID is not given, we are probably in development.
            //Just show the fake data.
            if (self.GameID==null || self.RoleID==null){
                self.isGameStateViewValid = true;
                return;
            }

            if (!self.QueryPending) {
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
        },1000);
    },
    methods: {
        onExitFromRuleBook:function(){
            this.ShowingRuleBook = false;
        },
        onRuleBook:function(){
            this.ShowingRuleBook = true;
        },
        onContrlSettings:function(){
            window.console.warn("onContrlSettings not implemented.");
        },
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
        onClickShowScore:function(){
            this.ShowingResultDialog = true;
        },
    },
}
</script>

<style scoped>
.ActionPanel {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}
.PreviewContainer {
    flex-wrap: wrap;
}

.BuiltSetContainer {
    display: flex;
    flex-direction: row-row-reverse;
    justify-content: flex-end;
}

.SeatIndiContainer{
    max-width:150px;
}

.PlayerName {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.OppoArea {
    transform: rotate(180deg);
}

.Area{
    max-height: 250px;
}

.SeatIndicator {
    font-size: 2em;
    text-align: center;
}

.PlayerActions {
    overflow-y: scroll;
}

.ActionPreview {
    font-size: 2rem;
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
