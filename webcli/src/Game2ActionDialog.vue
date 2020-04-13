<template>
    <v-dialog v-model="active" overlay-opacity=0.5 max-width="600px">
        <v-card>
            <v-card-text>
                <v-list two-line>
                    <v-list-item v-for='(action,idx) in actions' :key='idx' @click="onAction(action.Data)">
                        <v-list-item-content>
                            <div class='d-flex PreviewContainer'>
                                <TileViewRow v-for='(row,idx) in action.Preview' :key='`preview-${idx}`' :TileViews='row' />
                            </div>
                            <v-list-item-subtitle>{{action.Type}}</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-list-item>
                </v-list>
            </v-card-text>
            <v-card-actions>
                <v-btn color="blue darken-1" text @click="onBack">Back</v-btn>
                <v-spacer></v-spacer>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script>
import TileViewRow from './TileViewRow.vue';
export default {
    name: 'Game2ActionDialog',
    props: {
        active:Boolean,
        actions:Array,
    },
    components:{
        'TileViewRow':TileViewRow,
    },
    data : function(){
        window.console.log("[Game2ActionDialog] initing data.");
        return {};
    },
    methods: {
        onBack() {
            window.console.log('[Game2ActionDialog] onBack.');
            this.$emit('cancelled');
        },
        onAction(actionPayload) {
            window.console.log('[Game2ActionDialog] onAction.');
            window.console.log(actionPayload);
            this.$emit('selected', actionPayload);
        },
    },
};
</script>

<style scoped>
.PreviewContainer {
    flex-wrap: wrap;
}
</style>
