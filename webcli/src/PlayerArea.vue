<template>
    <div class="PlayerArea.vue" :style="containerStyle">
        <div v-for="(item,idx) in this.data.River" :key="`river-${idx}`" :style="getRiverTileStyle(idx)">{{getViewString(data.River[idx])}}</div>
        <div v-for="(item,idx) in this.data.Mountain" :key="`mountain-${idx}`" :style="getMountainTileStyle(idx)">{{getViewString(data.Mountain[idx])}}</div>
        <div v-for="(item,idx) in this.data.OldHand" :key="`oldhand-${idx}`" :style="getOldHandTileStyle(idx)" @click="onOldHandClick(idx)">{{getViewString(data.OldHand[idx])}}</div>
        <div v-for="(item,idx) in this.data.NewHand" :key="`newhand-${idx}`" :style="getNewHandTileStyle(idx)" @click="onNewHandClick(idx)" @mouseover="onMouseOverNewHand(idx)" @mouseout="onMouseOutNewHand(idx)">{{getViewString(data.NewHand[idx])}}</div>
        <built-set v-for="(item,idx) in this.data.BuiltSets" :key="`buildsets-${idx}`" :style="getBuiltSetStyle(idx)" @SetClick="onSetClick(idx)" @mouseover="onMouseOverSet(idx)" @mouseout="onMouseOutSet(idx)" :setData="item" :tileWidth="dims.tileWidth" :tileHeight="dims.tileHeight"/>
        <div style="position:absolute; top:200px; width:304px">
            <v-btn text small height="40px" @click="onPassClick">Pass</v-btn>
            <v-btn text small height="40px" @click="onPonClick">Pon</v-btn>
            <v-btn text small height="40px" @click="onWinClick">{{winButtonText}}</v-btn>
        </div>
    </div>
</template>

<script>
import * as Game2Utils from './game2.js'
import BuiltSet from './BuiltSet.vue'
import * as styling from './PlayerAreaStyling.js'
export default {
    name : 'PlayerArea',
    components: {
        'built-set' : BuiltSet
    },
    props: {
        data: Object,
        width: Number,
        height: Number,
        gameStateView : Object,
        seatID : Number,
    },
    computed: {
        containerStyle : function(){
            return {
                width : `${this.width}px`,
                'max-width' : `${this.width}px`,
                height : `${this.height}px`,
            }
        },
        dims: function(){
            return styling.getDimensions(this.width, this.height)
        },
        winButtonStatus : function(){
            if (this.gameStateView.State.Main == 'PlayerXHandleDraw' && this.gameStateView.State.X == Game2Utils.getRoleBySeatID(this.seatID)) {
                return {
                    ButtonText : 'Tsumo',
                    Enabled   : true,
                }
            } else if (this.gameStateView.State.Main == 'PlayerXToRespondToDiscard' && this.gameStateView.State.X == Game2Utils.getRoleBySeatID(this.seatID)) {
                return {
                    ButtonText: 'Ron',
                    Enabled   : true,
                }
            } else {
                return {
                    ButtonText: '',
                    Enabled   : false,
                }
            }
        },
        winButtonText : function() {
            return this.winButtonStatus.ButtonText
        }
    },
    methods: {
        getRiverTileStyle(idx) {
            var rowIdx = Math.floor(idx/6)
            var colIdx = idx%6
            return {
                position: 'absolute',
                top: `${this.dims.riverTop+this.dims.tileHeight*rowIdx}px`,
                left: `${this.dims.riverLeft+this.dims.tileWidth*colIdx}px`,
                width: `${this.dims.tileWidth}px`,
                'max-width': `${this.dims.tileWidth}px`,
                height: `${this.dims.tileHeight}px`,
            }
        },
        getMountainTileStyle(idx) {
            var rowIdx = idx%2
            var colIdx = 18-Math.floor(idx/2)
            return {
                position: 'absolute',
                top: `${this.dims.MountainTop+this.dims.tileHeight*rowIdx}px`,
                left: `${this.dims.MountainLeft+this.dims.tileWidth*colIdx}px`,
                width: `${this.dims.tileWidth}px`,
                'max-width': `${this.dims.tileWidth}px`,
                height: `${this.dims.tileHeight}px`,
            }
        },
        getOldHandTileStyle(idx) {
            return {
                position: 'absolute',
                top: `${this.dims.HandTop}px`,
                left: `${this.dims.HandLeft+this.dims.tileWidth*idx}px`,
                width: `${this.dims.tileWidth}px`,
                'max-width': `${this.dims.tileWidth}px`,
                height: `${this.dims.tileHeight}px`,
            }
        },
        getNewHandTileStyle(idx) {
            var left = this.dims.HandLeft + this.dims.tileWidth*(this.data.OldHand.length+1+idx)
            return {
                position: 'absolute',
                top: `${this.dims.HandTop}px`,
                left: `${left}px`,
                width: `${this.dims.tileWidth}px`,
                'max-width': `${this.dims.tileWidth}px`,
                height: `${this.dims.tileHeight}px`,
            }
        },
        getBuiltSetStyle(idx) {
            return {
                position: 'absolute',
                top: `${this.height-this.dims.SetHeight}px`,
                left: `${this.width-this.dims.SetWidth*(idx+1)-this.dims.tileWidth/2*(idx)}px`,
                width: `${this.dims.SetWidth}px`,
                'max-width': `${this.dims.SetWidth}px`,
                height: `${this.dims.SetHeight}px`,
            }
        },
        getViewString(tileView) {
            return styling.getTileViewChar(tileView)
        },
        IsRotatedTileView(tileView) {
            return tileView && tileView.Rotated
        },
        onMouseOverOldHand(idx){
            window.console.log(`MouseOverOldHand,idx=${idx}`)
        },
        onMouseOutOldHand(idx){
            window.console.log(`MouseOutOldHand,idx=${idx}`)
        },
        onMouseOverNewHand(idx){
            window.console.log(`MouseOverNewHand,idx=${idx}`)
        },
        onMouseOutNewHand(idx){
            window.console.log(`MouseOutNewHand,idx=${idx}`)
        },
        onMouseOverSet(idx){
            window.console.log(`MouseOverSet,idx=${idx}`)
        },
        onMouseOutSet(idx){
            window.console.log(`MouseOutSet,idx=${idx}`)
        },
        onOldHandClick(idx){
            window.console.log(`onOldHandClick,idx=${idx}`)
            this.$emit('UserAction', {
                Type: 'OldHandClick',
                Idx: idx,
            })
        },
        onNewHandClick(idx){
            window.console.log(`onNewHandClick,idx=${idx}`)
            this.$emit('UserAction', {
                Type: 'NewHandClick',
                Idx: idx,
            })
        },
        onSetClick(idx){
            window.console.log(`onSetClick,idx=${idx}`)
            this.$emit('UserAction', {
                Type: 'SetClick',
                Idx: idx,
            })
        },
        onPassClick(){
            window.console.log('onPassClick')
            this.$emit('UserAction', {
                Type: 'PassClick',
            })
        },
        onPonClick(){
            window.console.log('onPassClick')
            this.$emit('UserAction', {
                Type: 'PonClick',
            })
        },
        onWinClick(){
            window.console.log('onWinClick')
            this.$emit('UserAction', {
                Type: 'WinClick',
            })
        }
    }
}
</script>

<style>
.Skip {
    position: absolute;
    top: 200px;
    left: 350px;
}
.Tsumo {
    position: absolute;
    top: 150px;
    left: 350px;
}
.Ron {
    position: absolute;
    top: 100px;
    left: 350px;
}
</style>
