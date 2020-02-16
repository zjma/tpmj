<template>
    <v-container id='TheContainer' fluid>
        <v-row id='GameView' align='end'>
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
                                <v-card-text>
                                    Miku
                                </v-card-text>
                            </v-card>
                        </v-col>
                        <v-col>
                            <div class='RiverRow'>
                                🀟🀟🀟🀟🀟🀟🀟🀟🀟🀟🀟🀟🀟🀟🀟🀟🀟🀟🀟🀟🀟🀟🀟🀟
                            </div>
                        </v-col>
                    </v-row>
                    <div class='Hand'>
                        🀟🀟🀟🀟🀟🀟🀟🀟🀟🀟🀟🀟🀟 🀟
                    </div>
                    <v-row>
                        <v-col>🀟🀟🀟🀟</v-col>
                        <v-col>🀟🀟🀟🀟</v-col>
                        <v-col>🀟🀟🀟🀟</v-col>
                        <v-col>🀟🀟🀟🀟</v-col>
                    </v-row>
                </div>
                <v-card>
                    <v-card-text class='GameMetadata'>索子麻雀练习 · 牌山剩余:{{MountainRemaining}}</v-card-text>
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
                            <div class='RiverRow'>
                                {{SelfRiver}}
                            </div>
                        </v-col>
                    </v-row>
                    <div class='Hand'>
                        {{SelfHand}}
                    </div>
                    <v-row>
                        <v-col>{{SelfSet3}}</v-col>
                        <v-col>{{SelfSet2}}</v-col>
                        <v-col>{{SelfSet1}}</v-col>
                        <v-col>{{SelfSet0}}</v-col>
                    </v-row>
                </div>
            </v-col>
            <v-col md='6' cols='12' class='PlayerActions'>
                <v-list two-line>
                    <v-list-item-group v-for='(action,idx) in ActionUiData' :key='idx'>
                        <v-list-item @click="onAction('yo')">
                            <v-list-item-content>
                                <v-list-item-title style="font-size: 1em;">{{action.Value}}</v-list-item-title>
                                <v-list-item-subtitle>{{action.Type}}</v-list-item-subtitle>
                            </v-list-item-content>
                        </v-list-item>
                    </v-list-item-group>
                </v-list>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import * as Game2Utils from './game2.js'
import * as styling from './PlayerAreaStyling.js'
export default {
    name : 'MinimumDigitalTable',
    components : {
    },
    props: {
        gameStateView   : Object,
        myRole          : Number,
    },
    computed: {
        mySeat: function() {
            return Game2Utils.getSeatByRole(this.myRole)
        },
        oppoSeat: function() {
            return Game2Utils.getSeatByRole(1-this.myRole)
        },
        OppoRoleLabel: function(){
            return styling.getSeatChar(1-this.myRole)
        },
        SelfRoleLabel: function(){
            return styling.getSeatChar(this.myRole)
        },
        MountainRemaining: function(){
            var accumulator = (accumulated, toProcess) => toProcess.Mountain.filter(v => v!=undefined).length + accumulated
            return this.gameStateView.AreaViews.reduce(accumulator, 0)
        },
        SelfName: function(){
            return this.gameStateView.PlayerNames[this.myRole]
        },
        SelfRiver: function(){
            return this.gameStateView.AreaViews[this.mySeat].River.map(v => styling.getTileViewChar(v)).join('')
        },
        SelfHand: function(){
            var oldHandStr = this.gameStateView.AreaViews[this.mySeat].OldHand.map(v => styling.getTileViewChar(v)).join('')
            var newHandStr = this.gameStateView.AreaViews[this.mySeat].NewHand.map(v => styling.getTileViewChar(v)).join('')
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
        ActionUiData: function(){
            var actions = Game2Utils.getAction(this.gameStateView, this.myRole)
            return actions.map(a => styling.getActionUIData(a))
        },

    },
    methods: {
        onAction: function(){
            window.console.log('kaykay')
        },
        onSelfAction: function(action){
            window.console.log('Self action!')
            window.console.log(action)
            this.$emit('UserAction', {
                Area: 'Self',
                Action: action,
            })
        },
        onOppoAction: function(action){
            window.console.log('Oppo action!')
            window.console.log(action)
            this.$emit('UserAction', {
                Area: 'Oppo',
                Action: action,
            })
        },
        onLeftAction: function(action){
            window.console.log('Left action!')
            window.console.log(action)
            this.$emit('UserAction', {
                Area: 'Left',
                Action: action,
            })
        },
        onRightAction: function(action){
            window.console.log('Right action!')
            window.console.log(action)
            this.$emit('UserAction', {
                Area: 'Right',
                Action: action,
            })
        },
    },
}
</script>

<style>
.ActionCard {
    width: 100%;
}

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

.OldHand {
    justify-content: right;
    display: grid;
    font-family: 'Segoe UI Symbol';
}

.Hand {
}
#TheRow {
    height: 250px;
}
.PlayerActions {
    height: 30vh;
    overflow-y: scroll;
}

.ActionPreview {
    font-size: 2rem;
}
</style>