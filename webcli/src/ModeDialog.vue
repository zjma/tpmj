<template>
    <v-dialog v-model="active" persistent max-width="600px">
        <v-card>
            <v-container>
                <v-btn text outlined width="100%" min-height=100 class="ModeButton" @click="onPlay">匹配</v-btn>
                <v-btn text outlined width="100%" min-height=100 disabled class="ModeButton">{{ObserveButtonText}}</v-btn>
            </v-container>
            <v-card-actions>
                <v-btn color="blue darken-1" text large @click="onBack()"><v-icon>mdi-arrow-left</v-icon></v-btn>
                <v-spacer></v-spacer>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script>
import * as styling from './PlayerAreaStyling.js';

export default {
    name: 'ModeDialog',
    props : {
        active:Boolean,
        defaultMode:String
    },
    computed:{
        ObserveButtonText:function(){
            return styling.ObserveButtonText;
        },
        PlayButtonText:function(){
            return styling.PlayButtonText;
        }
    },
    methods: {
        onBack : function(){
            this.$emit('cancelled');
        },
        onPlay: function(){
            this.$emit('play-selected');
        },
        onObserve: function(){
            this.$emit('observe-selected');
        },
    }
}
</script>

<style scoped>

.DialogTitle {
    text-align: center;
}
</style>
