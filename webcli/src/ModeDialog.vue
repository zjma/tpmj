<template>
    <v-dialog v-model="active" persistent max-width="600px">
        <v-card>
            <v-card-title>
                <span class="headline">Choose Mode</span>
            </v-card-title>
            <v-container>
                <v-radio-group v-model="mode">
                    <v-radio label="Play" value="Play"></v-radio>
                    <v-radio label="Observe" value="Observe"></v-radio>
                </v-radio-group>
            </v-container>
            <v-card-actions>
                <v-btn color="blue darken-1" text @click="onBack()">Back</v-btn>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="onNext()">Next</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script>
export default {
    name: 'ModeDialog',
    props : {
        active:Boolean,
        defaultMode:String
    },
    data : function(){
        return {
            mode : this.defaultMode
        };
    },
    methods: {
        onBack : function(){
            this.$emit('cancelled');
        },
        onNext : function(){
            if (this.mode == 'Play') {
                this.$emit('play-selected');
            } else {
                this.$emit('observe-selected');
            }
        }
    }
}
</script>
