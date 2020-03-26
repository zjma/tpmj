<template>
    <v-dialog v-model="active" persistent max-width="600px">
        <v-card>
            <v-card-title class="ResultTitle">
                <span class="headline">{{ResultTitle}}</span>
            </v-card-title>
            <v-container>
                <v-row class="pl-10 pr-10 ResultHandShow">{{WinnderHand}}</v-row>
                <v-row class="pl-10 pr-10 pb-5 ResultSetShow">🀐🀐🀐🀐 🀆🀆🀆🀆 🀔🀔🀔🀔 🀀🀀🀀🀀</v-row>
                <v-row><v-col class="PatternName">清一色</v-col><v-col class="PatternValue">2番</v-col></v-row>
                <v-divider class="ma-4"/>
                <v-row class="TotalValue">9番</v-row>
            </v-container>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="onNext()">Next</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script>
import * as styling from './PlayerAreaStyling.js';
import * as Game2Utils from './game2.js';

export default {
    name: 'GameResultDialog',
    props : {
        active:Boolean,
        gameStateView:Object
    },
    computed: {
        ResultTitle : function() {
            var gsv = this.gameStateView;
            switch (gsv.State.Main) {
                case 'PlayerXWin':
                    var roleID = gsv.State.X;
                    var action = (gsv.State.WinningTileFromPlayer == roleID) ? "Tsumo" : "Ron";
                    var result = `${gsv.PlayerNames[roleID]} ${action}`;
                    return result;
                default:
                    throw `Unimplemented for ${gsv.State.Main}`
            }
        },
        WinnderHand : function() {
                var gsv = this.gameStateView;
                var roleID = gsv.State.X;
                var seatID = Game2Utils.getSeatByRole(roleID);
                return styling.getHandStr(gsv, seatID);
        },
    },
    methods: {
        onNext : function(){
            this.$emit('finished');
        }
    }
}
</script>

<style>
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
