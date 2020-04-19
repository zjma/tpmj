<template>
    <v-dialog v-model="active" persistent scrollable max-width="600px">
        <v-card>
            <v-card-title>番种表</v-card-title>
            <v-card-text height="400px">
                <v-list>
                  <v-list-item-group>
                    <v-list-item v-for='(pattern,idx) in patterns' :key='`PatternDesc-${idx}`'>
                        <v-container>
                            <v-row>
                                <v-col>{{pattern.Name}}</v-col>
                                <v-col>{{pattern.Value}}番</v-col>
                            </v-row>
                            <v-row><v-col>{{pattern.Desc}}</v-col></v-row>
                            <HandAndSetView :ScaleRatio="0.7" :OldHand="pattern.Example.OldHand" :NewHand="pattern.Example.NewHand" :Set0="pattern.Example.Set0" :Set1="pattern.Example.Set1" :Set2="pattern.Example.Set2" :Set3="pattern.Example.Set3" />
                        </v-container>
                    </v-list-item>
                  </v-list-item-group>
                </v-list>


            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text large @click="onNext"><v-icon>mdi-check</v-icon></v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script>
import HandAndSetView from './HandAndSetView.vue';

export default {
    name: 'RuleBookDialog',
    props : {
        active:Boolean,
        content:Object,
    },
    components:{
        'HandAndSetView':HandAndSetView,
    },
    computed: {
        patterns:function(){
            var result = Object.values(this.content);
            return result;
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
</style>
