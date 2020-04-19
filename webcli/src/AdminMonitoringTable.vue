<template>
    <v-container id='TheContainer' fluid>
        <div v-if="gameStateView">
            <div v-for="seatID in seatIDs" :key="`PlayerArea-${seatID}`">
                <v-divider/>
                <label>SeatID={{seatID}}</label>
                <div class="Mountain">
                    <label>Mountain</label>
                    <span v-for="(tileChar,idx) in getChars(seatID,'Mountain')" :key="`${seatID}-OldHand-${idx}`" :class="{selected:isSelected(seatID,'Mountain',idx)}" @click="onClick(seatID,'Mountain',idx)">{{tileChar}}</span>
                </div>
                <div class="River">
                    <label>River</label>
                    <span v-for="(tileChar,idx) in getChars(seatID,'River')" :key="`${seatID}-River-${idx}`" :class="{selected:isSelected(seatID,'River',idx)}" @click="onClick(seatID,'River',idx)">{{tileChar}}</span>
                </div>
                <div class="OldHand">
                    <label>OldHand</label>
                    <span v-for="(tileChar,idx) in getChars(seatID,'OldHand')" :key="`${seatID}-OldHand-${idx}`" :class="{selected:isSelected(seatID,'OldHand',idx)}" @click="onClick(seatID,'OldHand',idx)">{{tileChar}}</span>
                </div>
                <div class="NewHand">
                    <label>NewHand</label>
                    <span v-for="(tileChar,idx) in getChars(seatID,'NewHand')" :key="`${seatID}-NewHand-${idx}`" :class="{selected:isSelected(seatID,'NewHand',idx)}" @click="onClick(seatID,'NewHand',idx)">{{tileChar}}</span>
                </div>
                <div class="BuiltSet0">
                    <label>BuiltSet0</label>
                    <span v-for="(tileChar,idx) in getChars(seatID,`BuiltSet0`)" :key="`${seatID}-BuiltSet0-${idx}`" :class="{selected:isSelected(seatID,'BuiltSet0',idx)}" @click="onClick(seatID,'BuiltSet0',idx)">{{tileChar}}</span>
                </div>
                <div class="BuiltSet1">
                    <label>BuiltSet1</label>
                    <span v-for="(tileChar,idx) in getChars(seatID,`BuiltSet1`)" :key="`${seatID}-BuiltSet1-${idx}`" :class="{selected:isSelected(seatID,'BuiltSet1',idx)}" @click="onClick(seatID,'BuiltSet1',idx)">{{tileChar}}</span>
                </div>
                <div class="BuiltSet2">
                    <label>BuiltSet2</label>
                    <span v-for="(tileChar,idx) in getChars(seatID,`BuiltSet2`)" :key="`${seatID}-BuiltSet2-${idx}`" :class="{selected:isSelected(seatID,'BuiltSet2',idx)}" @click="onClick(seatID,'BuiltSet2',idx)">{{tileChar}}</span>
                </div>
                <div class="BuiltSet3">
                    <label>BuiltSet3</label>
                    <span v-for="(tileChar,idx) in getChars(seatID,`BuiltSet3`)" :key="`${seatID}-BuiltSet3-${idx}`" :class="{selected:isSelected(seatID,'BuiltSet3',idx)}" @click="onClick(seatID,'BuiltSet3',idx)">{{tileChar}}</span>
                </div>
            </div>
        </div>
        <div v-else>Loading game state...</div>
    </v-container>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)

import * as styling from './PlayerAreaStyling.js';

export default {
    name : 'AdminMonitoringTable',
    props: {
        active: Boolean,
        GameID : String,
    },
    data: function(){
        return {
            gameStateView : undefined,
            selectedLocIds : [],
            QueryPending: false,
            ApiServerPlayUrl:`${process.env.VUE_APP_API_SERVER_URL}/tpmj`,
        };
    },
    computed: {
        seatIDs: function() {
            return [0,1,2,3];
        },
    },
    mounted: function(){
        const self = this;

        //Thread for polling backend for game state.
        setInterval(function(){
            if (self.active && !self.QueryPending) {
                self.QueryPending = true;
                axios.post(self.ApiServerPlayUrl, {
                    Action:'GetGameState',
                    GameID:self.GameID,
                    RoleID:-1,
                }).then(response => {
                    self.QueryPending = false;
                    var sub = response.data;
                    if (self.active) {
                        self.gameStateView = sub;
                    }
                }).catch(function(error){
                    self.QueryPending = false
                    window.console.log(error)
                });
            }
        }, 1000);

    },
    methods: {
        getChars: function(seatID, area) {
            var tileviews = [];
            if (area.includes('BuiltSet')) {
                var setidx = parseInt(area.substring(8));
                if (setidx >= this.gameStateView.AreaViews[seatID].BuiltSets.length) {
                    tileviews = [];
                } else {
                    tileviews = this.gameStateView.AreaViews[seatID].BuiltSets[setidx].TileViews;
                }
            } else {
                tileviews = this.gameStateView.AreaViews[seatID][area];
            }
            return tileviews.map(tv => styling.getTileViewChar(tv));
        },
        onClick: function(seatID, area, idx) {
            var locID = this.getLocId(seatID, area, idx);
            if (this.selectedLocIds.includes(locID)) {
                this.selectedLocIds = this.selectedLocIds.filter(lid => lid!=locID);
            } else {
                this.selectedLocIds.push(locID);
            }

            if (this.selectedLocIds.length >= 2) {
                window.console.log("2 tiles selected. Request a swap.");
                var payload = {
                    Action:'EditGame',
                    GameID:this.GameID,
                    Command:'Swap',
                    Locations:this.selectedLocIds.map(locid => this.getLocationFromLID(locid)),
                    RoleID:-1,
                };
                window.console.log(payload);
                axios.post(this.ApiServerPlayUrl, payload);

                this.selectedLocIds = this.selectedLocIds.slice(2);
            }
        },
        isSelected: function(seatID, area, idx) {
            var locID = this.getLocId(seatID, area, idx);
            return this.selectedLocIds.includes(locID);
        },
        getLocId: function(seatID, area, idx) {
            return `${seatID}-${area}-${idx}`;
        },
        getLocationFromLID: function(locID){
            var items = locID.split('-');
            return {
                SeatID:parseInt(items[0]),
                Area:items[1],
                'Index':parseInt(items[2]),
            }
        }
    },
}
</script>

<style scoped>
.selected {
    animation: blinker 1s linear infinite;
}

@keyframes blinker {
  50% {
    opacity: 0;
  }
}

.TileOnlyContainer {
    font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";
}


</style>
