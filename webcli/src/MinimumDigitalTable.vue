<template>
    <v-container id='TheContainer' fluid>
        <v-row id='GameView' align='end'>
            <v-col md='6' cols='12'>
                <div class='OppoArea'>
                    <v-row>
                        <v-col cols='3'>
                            <v-card outlined>
                                <v-card-title>
                                    <div class='SeatIndicator'>
                                        南
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
                    <v-card-text class='GameMetadata'>索子麻雀练习赛·牌山剩余12</v-card-text>
                </v-card>
                <div>
                    <v-row>
                        <v-col cols='3'>
                            <v-card outlined>
                                <v-card-title>
                                    <div class='SeatIndicator'>
                                        東
                                    </div>
                                </v-card-title>
                                <v-card-text class='PlayerName'>
                                    Nyamaadwwfa
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
            </v-col>
            <v-col md='6' cols='12' class='PlayerActions'>
                <v-list two-line>
                    <v-list-item-group v-for='x in 33' :key='x'>
                        <v-list-item @click="onAction('yo')">
                            <v-list-item-content>
                                <v-list-item-title style="font-size: 1em;">🀉🀉🀉 🀉🀉🀉 🀉🀉🀉 🀉🀉🀉 🀉🀉</v-list-item-title>
                                <v-list-item-subtitle>Tsumo</v-list-item-subtitle>
                            </v-list-item-content>
                        </v-list-item>
                    </v-list-item-group>
                </v-list>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
export default {
    name : 'MinimumDigitalTable',
    components : {
    },
    props: {
        gameStateView   : Object,
        mySeat          : Number,
    },
    computed: {
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
    height: 50vh;
    overflow-y: scroll;
}

.ActionPreview {
    font-size: 2rem;
}
</style>
