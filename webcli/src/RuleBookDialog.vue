<template>
    <v-dialog v-model="active" persistent scrollable max-width="600px">
        <v-card>
            <v-card-title>番种表</v-card-title>
            <v-card-text height="400px">
                <v-list>
                  <v-list-item-group>
                    <v-list-item>
                        <v-container>
                            <v-row>
                                <v-col>清一色</v-col>
                                <v-col>1番</v-col>
                            </v-row>
                            <v-row><v-col>你的所有牌都是索子牌。</v-col></v-row>
                            <HandAndSetView :ScaleRatio="0.7" :OldHand="OldHand" :NewHand="NewHand" :Set0="Set0" :Set1="Set1" :Set2="Set2" :Set3="Set3" />
                        </v-container>
                    </v-list-item>
                    <v-list-item>
                        <v-container>
                            <v-row>
                                <v-col>清一色</v-col>
                                <v-col>1番</v-col>
                            </v-row>
                            <v-row><v-col>你的所有牌都是索子牌。</v-col></v-row>
                            <v-row>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                            </v-row>
                        </v-container>
                    </v-list-item>
                    <v-list-item>
                        <v-container>
                            <v-divider/>
                            <v-row>
                                <v-col>清一色</v-col>
                                <v-col>1番</v-col>
                            </v-row>
                            <v-row><v-col>你的所有牌都是索子牌。</v-col></v-row>
                            <v-row>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                            </v-row>
                        </v-container>
                    </v-list-item>
                    <v-list-item>
                        <v-container>
                            <v-row>
                                <v-col>清一色</v-col>
                                <v-col>1番</v-col>
                            </v-row>
                            <v-row><v-col>你的所有牌都是索子牌。</v-col></v-row>
                            <v-row>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                            </v-row>
                        </v-container>
                    </v-list-item>
                    <v-list-item>
                        <v-container>
                            <v-row>
                                <v-col>清一色</v-col>
                                <v-col>1番</v-col>
                            </v-row>
                            <v-row><v-col>你的所有牌都是索子牌。</v-col></v-row>
                            <v-row>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                            </v-row>
                        </v-container>
                    </v-list-item>
                    <v-list-item>
                        <v-container>
                            <v-row>
                                <v-col>清一色</v-col>
                                <v-col>1番</v-col>
                            </v-row>
                            <v-row><v-col>你的所有牌都是索子牌。</v-col></v-row>
                            <v-row>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                                <span>🀕</span>
                            </v-row>
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
        ruleBookContent:Object,
    },
    components:{
        'HandAndSetView':HandAndSetView,
    },
    computed: {
        OldHand:function(){
            return [
                {IsValueVisible:true,Value:99},
                {IsValueVisible:true,Value:99},
                {IsValueVisible:true,Value:99},
                {IsValueVisible:true,Value:99},
                {IsValueVisible:true,Value:99},
                {IsValueVisible:true,Value:99},
                {IsValueVisible:true,Value:99},
                {IsValueVisible:true,Value:99},
                {IsValueVisible:true,Value:99},
                {IsValueVisible:true,Value:99},
                {IsValueVisible:true,Value:99},
                {IsValueVisible:true,Value:99},
                {IsValueVisible:true,Value:99},
            ];
        },
        NewHand:function(){
            return [
                {IsValueVisible:true,Value:33},
            ];
        },
        Set0:function(){
            return [
                {IsValueVisible:true,Value:66},
                {IsValueVisible:true,Value:66},
                {IsValueVisible:true,Value:66},
                {IsValueVisible:true,Value:66},
            ];
        },
        Set1:function(){
            return [
                {IsValueVisible:true,Value:66},
                {IsValueVisible:true,Value:66},
                {IsValueVisible:true,Value:66},
                {IsValueVisible:true,Value:66},
            ];
        },
        Set2:function(){
            return [
                {IsValueVisible:true,Value:66},
                {IsValueVisible:true,Value:66},
                {IsValueVisible:true,Value:66},
                {IsValueVisible:true,Value:66},
            ];
        },
        Set3:function(){
            return [
                {IsValueVisible:true,Value:66},
                {IsValueVisible:true,Value:66},
                {IsValueVisible:true,Value:66},
                {IsValueVisible:true,Value:66},
            ];
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
