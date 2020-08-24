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
                    <HandAndSetView :OldHand="OppoOldHand" :NewHand="OppoNewHand" :Set0="OppoSet0" :Set1="OppoSet1" :Set2="OppoSet2" :Set3="OppoSet3" />
                </div>
                <v-card outlined>
                    <v-card-text class='GameStateMetadata'>{{BadgeText}}</v-card-text>
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
                    <HandAndSetView :OldHand="SelfOldHand" :NewHand="SelfNewHand" :Set0="SelfSet0" :Set1="SelfSet1" :Set2="SelfSet2" :Set3="SelfSet3" />
                </div>
            </v-col>
            <v-col cols='12' md='6' class='PlayerActions'>
                <v-list two-line v-if='IsGameActive' max-height=300>
                    <v-subheader class="typewriter">{{ActionListTitle}}</v-subheader>
                    <v-list-item v-for='(action,idx) in ActionUiData' :key='idx' @click="onActionSelected(action.Data)">
                        <v-list-item-content>
                            <div class='d-flex PreviewContainer'>
                                <TileViewRow v-for='(row,idx) in action.Preview' :key='`preview-${idx}`' :TileViews='row' />
                            </div>
                            <v-list-item-subtitle>{{action.Type}}</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-list-item>
                </v-list>
            </v-col>
        </v-row>
        <div v-else id='PendingView'>
            <div class="lds-ring"><div></div><div></div><div></div><div></div></div>
        </div>
        <v-footer dark color="primary lighten-1" padless fixed class='ActionPanel'>
            <v-btn text small :disabled='!IsGameResultAvailable' @click='onClickReturnToLobby'>返回大厅</v-btn>
            <v-spacer/>
            <v-btn text small :disabled='!IsGameResultAvailable' @click='onClickGameResultButton'>本局得点</v-btn>
            <v-spacer/>
            <v-btn text small @click="onRuleBook">番种表</v-btn>
            <v-btn text small @click="onOpeningSettings">设置</v-btn>
        </v-footer>
        <result-dialog :active="ShowingResultDialog" :gameStateView='gameStateView' @done="onResultDialogClosing"></result-dialog>
        <rulebook-dialog :active="ShowingRuleBook" :content="ruleBookContent" @done="onExitFromRuleBook"></rulebook-dialog>
        <settings-dialog :active="ShowingSettingsDialog" :InitialSettings='Settings' @updated="onNewSettings" @done="onExitFromSettingsDialog"></settings-dialog>
        <audio src="" id="BGM"></audio>
    </v-container>
</template>

<script>
import axios from 'axios';
import * as Game2Utils from './game2.js';
import * as styling from './PlayerAreaStyling.js';
import GameResultDialog from './GameResultDialog.vue';
import RuleBookDialog from './RuleBookDialog.vue';
import MinimumDigitalTableSettingsDialog from './MinimumDigitalTableSettingsDialog.vue';
import TileViewRow from './TileViewRow.vue';
import HandAndSetView from './HandAndSetView.vue';
import * as SoundPlayer from './SoundPlayer.js';
import BGM from './assets/sound/pinball.mp3';

export default {
    name : 'MinimumDigitalTable',
    components : {
        'result-dialog' : GameResultDialog,
        'rulebook-dialog': RuleBookDialog,
        'settings-dialog': MinimumDigitalTableSettingsDialog,
        'TileViewRow' : TileViewRow,
        'HandAndSetView' : HandAndSetView,
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
            ShowingSettingsDialog : false,
            ruleBookContent : Game2Utils.PatternLibrary,
            Settings : {
                AutoSkip : true,//Auto-skip when current player needs to respond to other player's discard/Kan2 and the only possible move is to skip.
                BgmOn : true,
                SoundEffectOn : true,
            },
            ManualActionRequired : true,
        };
    },
    computed: {
        IsGameActive:function(){
            if (this.gameStateView.State.Main=='PlayerXWon') return false;
            if (this.gameStateView.State.Main=='Finished') return false;
            return true;
        },
        ActionListTitle:function(){
            switch(this.gameStateView.State.Main){
                case 'PlayerXHandleDraw':
                    if (this.gameStateView.State.X==this.RoleID){
                        return '要怎么做?';
                    }else{
                        return `${this.gameStateView.PlayerNames[this.gameStateView.State.X]}思考中...`;
                    }
                case 'PlayerXToRespondToDiscard':
                    if (this.gameStateView.State.X==this.RoleID){
                        if (this.ManualActionRequired) {
                            return '对手的弃牌! 要怎么做?';
                        } else {
                            return '对手的弃牌!';
                        }
                    }else{
                        return `${this.gameStateView.PlayerNames[this.gameStateView.State.X]}思考中...`;
                    }
                case 'PlayerXToRespondToKan2':
                    if (this.gameStateView.State.X==this.RoleID){
                        if (this.ManualActionRequired) {
                            return '啊! 这个加杠! 抢杠吗?'
                        } else {
                            return '啊! 这个加杠!'
                        }
                    }else{
                        return `${this.gameStateView.PlayerNames[this.gameStateView.State.X]}思考中...`;
                    }
                default:
                    return '';
            }
        },
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
            return Game2Utils.getMountainRemainingCount(this.gameStateView);
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
            window.console.log('MinimumDigitalTable.ActionUiData()');
            if (this.ManualActionRequired) {
                var actions = Game2Utils.getAction(this.gameStateView, this.RoleID);
                var result = actions.map(a => styling.getActionUIData(a));
                return result;
            } else {
                return [];
            }
        },
    },
    mounted: function(){
        window.console.log("[MinimumDigitalTable].mounted()");
        const self = this;

        document.getElementById('BGM').setAttribute('src', BGM);
        document.getElementById('BGM').setAttribute('loop', true);

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
                        window.console.log(`SequenceNumber=${sub.SequenceNumber},LastAction=${sub.LastAction.Main},CurrentState=${sub.State.Main}`);
                        if (self.gameStateView.SequenceNumber != sub.SequenceNumber) {
                            if (sub.LastAction.Main=='PlayerXDraw') {
                                SoundPlayer.play('DrewTile');
                            } else if (sub.LastAction.Main=='PlayerXDiscardNew') {
                                SoundPlayer.play('DiscardedNew');
                            } else if (sub.LastAction.Main=='PlayerXDiscardOld') {
                                SoundPlayer.play('DiscardedOld');
                            } else if (sub.LastAction.Main=='PlayerXPon') {
                                SoundPlayer.play('Pon');
                            } else if (sub.LastAction.Main=='PlayerXChi') {
                                SoundPlayer.play('Chi');
                            } else if (sub.LastAction.Main=='PlayerXKan0') {
                                SoundPlayer.play('Kan');
                            } else if (sub.LastAction.Main=='PlayerXKan1') {
                                SoundPlayer.play('Kan');
                            } else if (sub.LastAction.Main=='PlayerXKan2') {
                                SoundPlayer.play('Kan');
                            } else if (sub.LastAction.Main=='PlayerXTsumo') {
                                SoundPlayer.play('Tsumo');
                            } else if (sub.LastAction.Main=='PlayerXRon') {
                                SoundPlayer.play('Ron');
                            }
                            self.ManualActionRequired = true;
                            if (self.Settings.AutoSkip){
                                if ((sub.State.Main=='PlayerXToRespondToDiscard'||sub.State.Main=='PlayerXToRespondToKan2')&&sub.State.X==self.RoleID) {
                                    var actions = Game2Utils.getAction(sub, self.RoleID);
                                    if (actions.length==1 && (actions[0].Type=='Pass'||actions[0].Type=='Draw')) {
                                        self.onActionSelected(actions[0]);
                                        self.ManualActionRequired = false;
                                    }
                                }
                            }
                        }

                        self.gameStateView = sub;
                        if (!self.isGameStateViewValid) {
                            self.startBGM();
                        }
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
        onClickReturnToLobby(){
            window.console.log('MinimumDigitalTable.onClickReturnToLobby()');
            this.$emit('Exit');
            this.stopBGM();
            SoundPlayer.play('NormalAction');
        },
        onClickGameResultButton(){
            window.console.log('MinimumDigitalTable.onClickGameResultButton()');
            this.ShowingResultDialog = true;
            SoundPlayer.play('NormalAction');
        },
        onExitFromRuleBook:function(){
            window.console.log('MinimumDigitalTable.onExitFromRuleBook()');
            this.ShowingRuleBook = false;
            SoundPlayer.play('NormalAction');
        },
        onRuleBook:function(){
            window.console.log('MinimumDigitalTable.onRuleBook()');
            this.ShowingRuleBook = true;
            SoundPlayer.play('NormalAction');
        },
        onExitFromSettingsDialog:function(){
            window.console.log('MinimumDigitalTable.onExitFromSettingsDialog()');
            this.ShowingSettingsDialog = false;
            SoundPlayer.play('NormalAction');
        },
        onNewSettings:function(newSettings){
            window.console.log('MinimumDigitalTable.onNewSettings()');
            window.console.log(newSettings);
            if (newSettings.BgmOn==true&&this.Settings.BgmOn==false){
                this.startBGM();
            }
            if (newSettings.BgmOn==false&&this.Settings.BgmOn==true){
                this.stopBGM();
            }
            this.Settings = newSettings;
        },
        onOpeningSettings:function(){
            window.console.log('MinimumDigitalTable.onOpeningSettings()');
            this.ShowingSettingsDialog = true;
            SoundPlayer.play('NormalAction');
        },
        onGameResultAvailable:function(){
            window.console.log('MinimumDigitalTable.onGameResultAvailable()');
            if (!this.ResultPrompted) {
                this.ShowingResultDialog = true;
                this.ResultPrompted = true;
            }
        },
        onActionSelected:function(action){
            window.console.log('MinimumDigitalTable.onActionSelected()');
            window.console.log(action);

            axios.post(this.ApiServerPlayUrl, {
                Action:'PerformGameAction',
                GameID:this.GameID,
                RoleID: this.RoleID,
                Payload:action,
            });
        },
        onResultDialogClosing: function(){
            window.console.log('MinimumDigitalTable.onResultDialogClosing()');
            this.ShowingResultDialog = false;
        },
        onClickShowScore:function(){
            window.console.log('MinimumDigitalTable.onClickShowScore()');
            this.ShowingResultDialog = true;
        },
        startBGM:function(){
            document.getElementById('BGM').play();
        },
        stopBGM:function(){
            document.getElementById('BGM').pause();
        }
    },
}
</script>

<style scoped>
.GameStateMetadata {
    text-align: center;
}

.ActionPanel {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    font-size: 0.5rem;
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
