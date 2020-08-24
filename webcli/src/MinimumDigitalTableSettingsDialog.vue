<template>
    <v-dialog v-model="active" persistent scrollable max-width="600px">
        <v-card>
            <v-card-title>游戏设定</v-card-title>
            <v-card-text height="400px">
                <v-list>
                  <v-list-item-group>
                      <v-list-item>
                          <v-switch v-model="BgmOn" label="音乐" @change="escalate"></v-switch>
                      </v-list-item>
                      <v-list-item>
                          <v-switch v-model="SoundEffectOn" label="音效" @change="escalate"></v-switch>
                      </v-list-item>
                      <v-list-item>
                          <v-switch v-model="AutoSkip" label="无法响应对方舍牌/加杠时自动跳过" @change="escalate"></v-switch>
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
export default {
    name: 'MinimumDigitalTableSettingsDialog',
    props : {
        active:Boolean,
        InitialSettings:Object,
    },
    data: function(){
        window.console.log("[MinimumDigitalTableSettingsDialog].data()");
        return {
            BgmOn : this.InitialSettings.BgmOn,
            SoundEffectOn : this.InitialSettings.SoundEffectOn,
            AutoSkip : this.InitialSettings.AutoSkip,
        };
    },
    methods: {
        onNext : function(){
            this.$emit('done');
        },
        escalate: function(){
            window.console.log("[MinimumDigitalTableSettingsDialog].escalate()");
            this.$emit('updated', {
                BgmOn : this.BgmOn,
                SoundEffectOn : this.SoundEffectOn,
                AutoSkip : this.AutoSkip,
            });
        }
    }
}
</script>

<style>
</style>
