<template>
    <v-dialog v-model="active" persistent max-width="600px">
        <v-card>
            <v-card-title class="ResultTitle">
                <span class="headline">{{ResultTitle}}</span>
            </v-card-title>
            <v-container v-if="HasWinner">
                <HandAndSetView :ScaleRatio="0.8" :OldHand='OldHand' :NewHand='LastHand' :Set0='Set0' :Set1='Set1' :Set2='Set2' :Set3='Set3' />
                <v-row v-for='(pattern,idx) in PatternUIData' :key='idx'>
                    <v-col class="PatternName">{{pattern.DisplayName}}</v-col>
                    <v-col class="PatternValue">{{pattern.DisplayValue}}</v-col>
                </v-row>
                <v-divider class="ma-4"/>
                <v-row class="TotalValue">{{WinnerTotalValue}}</v-row>
            </v-container>
            <v-container v-else>
            </v-container>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text large @click="onNext"><v-icon>mdi-check</v-icon></v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script>
import * as styling from './PlayerAreaStyling.js';
import * as Game2Utils from './game2.js';
import HandAndSetView from './HandAndSetView.vue';

export default {
    name: 'GameResultDialog',
    props : {
        active:Boolean,
        gameStateView:Object,
    },
    components:{
        'HandAndSetView':HandAndSetView,
    },
    computed: {
        HasWinner:function(){
            return this.gameStateView.State.Main=='PlayerXWon';
        },
        NextButtonText:function(){
            return styling.DialogNextButtonText;
        },
        ResultTitle : function() {
            var gsv = this.gameStateView;
            switch (gsv.State.Main) {
                case 'PlayerXWon':
                    var roleID = gsv.State.X;
                    var seatID = Game2Utils.getSeatByRole(roleID);
                    var action = (gsv.AreaViews[seatID].NewHand.length>=1) ? styling.TsumoResultTitleText : styling.RonResultTitleText;
                    var result = `${gsv.PlayerNames[roleID]} ${action}`;
                    return result;
                case 'Finished':
                    return styling.DrawResultTitleText;
                default:
                    return 'Unexpected result';
            }
        },
        OldHand:function(){
            var gsv = this.gameStateView;
            var roleID = gsv.State.X;
            var seatID = Game2Utils.getSeatByRole(roleID);
            var result = gsv.AreaViews[seatID].OldHand;
            window.console.log(result);
            return result;
        },
        LastHand:function(){
            var gsv = this.gameStateView;
            var lastTileView = {
                IsValueVisible : true,
                Value : gsv.State.LastTile,
            };
            return [lastTileView];
        },

        WinnderHand : function() {
            var gsv = this.gameStateView;
            var roleID = gsv.State.X;
            var seatID = Game2Utils.getSeatByRole(roleID);
            var lastTileView = {
                IsValueVisible : true,
                Value : gsv.State.LastTile,
            };
            return styling.getTileViewListStr(gsv.AreaViews[seatID].OldHand)+' '+styling.getTileViewChar(lastTileView);
        },
        WinnerSetRow : function() {
            var gsv = this.gameStateView;
            var roleID = gsv.State.X;
            var seatID = Game2Utils.getSeatByRole(roleID);
            return styling.getSetRowStr(gsv, seatID);
        },
        PatternUIData : function() {
            window.console.log('PatternUIData calculating.');
            var gsv = this.gameStateView;
            var roleID = gsv.State.X;
            var seatID = Game2Utils.getSeatByRole(roleID);
            return this.gameStateView.MatchedPatterns[seatID].map(function(pid){
                var val = gsv.PatternValues[pid];
                return {
                    DisplayName:Game2Utils.PatternLibrary[pid].Name,
                    DisplayValue:`${val}番`,
                };
            });
        },
        WinnerTotalValue : function() {
            var gsv = this.gameStateView;
            var roleID = gsv.State.X;
            var seatID = Game2Utils.getSeatByRole(roleID);
            var total = Game2Utils.getTotalPatternValue(gsv, seatID);
            return styling.getPatternValueStr(total);
        },
        Set3: function(){
            var gsv = this.gameStateView;
            var roleID = gsv.State.X;
            var seatID = Game2Utils.getSeatByRole(roleID);
            var set = gsv.AreaViews[seatID].BuiltSets[3];
            return (set) ? set.TileViews : [];
        },
        Set0: function(){
            var gsv = this.gameStateView;
            var roleID = gsv.State.X;
            var seatID = Game2Utils.getSeatByRole(roleID);
            var set = gsv.AreaViews[seatID].BuiltSets[0];
            return (set) ? set.TileViews : [];
        },
        Set1: function(){
            var gsv = this.gameStateView;
            var roleID = gsv.State.X;
            var seatID = Game2Utils.getSeatByRole(roleID);
            var set = gsv.AreaViews[seatID].BuiltSets[1];
            return (set) ? set.TileViews : [];
        },
        Set2: function(){
            var gsv = this.gameStateView;
            var roleID = gsv.State.X;
            var seatID = Game2Utils.getSeatByRole(roleID);
            var set = gsv.AreaViews[seatID].BuiltSets[2];
            return (set) ? set.TileViews : [];
        },
    },
    methods: {
        onNext : function(){
            this.$emit('done');
        }
    }
}
</script>

<style>
.BuiltSetContainer {
    display: flex;
    flex-direction: row-row-reverse;
    justify-content: flex-end;
    flex-wrap: wrap;
}

.ResultHandShow {
    font-size: 1.5em;
    justify-content: flex-start;
}
.ResultSetShow {
    font-size: 1.5em;
    justify-content: flex-end;
}

.PatternName {
    text-align: right;
    padding-top: 0px;
    padding-bottom: 0px;
}

.PatternValue {
    justify-content: flex-start;
    padding-top: 0px;
    padding-bottom: 0px;
}

.ResultTitle {
    justify-content: center;
}

.TotalValue {
    font-size: 1.5em;
    justify-content: center;
}
</style>
