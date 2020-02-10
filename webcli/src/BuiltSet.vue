<template>
    <div @mouseover="$emit('mouseover')" @click="onClick()">
        <div v-if="setData.TileViews.length == 3">
            <div style="position:absolute; top:12px; left:20px; width:16px; max-width:16px; height:20px">{{getTileViewChar(setData.TileViews[0])}}</div>
            <div style="position:absolute; top:12px; left:36px; width:16px; max-width:16px; height:20px">{{getTileViewChar(setData.TileViews[1])}}</div>
            <div style="position:absolute; top:12px; left:52px; width:16px; max-width:16px; height:20px">{{getTileViewChar(setData.TileViews[2])}}</div>
        </div>
        <div v-if="setData.TileViews.length == 4">
            <div class='tile' style="position:absolute; top:12px; left:4px; width:16px; max-width:16px; height:20px">{{getTileViewChar(setData.TileViews[0])}}</div>
            <div class='tile' style="position:absolute; top:12px; left:20px; width:16px; max-width:16px; height:20px">{{getTileViewChar(setData.TileViews[1])}}</div>
            <div class='tile' style="position:absolute; top:12px; left:36px; width:16px; max-width:16px; height:20px">{{getTileViewChar(setData.TileViews[2])}}</div>
            <div class='tile' style="position:absolute; top:12px; left:52px; width:16px; max-width:16px; height:20px">{{getTileViewChar(setData.TileViews[3])}}</div>
        </div>
    </div>
</template>

<script>
import * as Styling from './PlayerAreaStyling.js'
export default {
    name : 'BuiltSet',
    props : {
        setData : Object,
        tileWidth : Number,
        tileHeight : Number,
    },
    computed : {
        shape : function() {
            var ret = undefined
            switch (this.setData.TileViews.length) {
                case 3:
                    if (this.setData.TileViews[0].Rotated) {
                        ret = '_||'
                    } else if (this.setData.TileViews[1].Rotated) {
                        ret = '|_|'
                    } else if (this.setData.TileViews[2].Rotated) {
                        ret = '||_'
                    } else {
                        ret = '|||'
                    }
                    break
                case 4:
                    if (this.setData.TileViews[0].Rotated && this.setData.TileViews[1].Rotated) {
                        ret = '=||'
                    } else if (this.setData.TileViews[1].Rotated && this.setData.TileViews[2].Rotated) {
                        ret = '|=|'
                    } else if (this.setData.TileViews[2].Rotated && this.setData.TileViews[3].Rotated) {
                        ret = '||='
                    } else if (this.setData.TileViews[0].Rotated) {
                        ret = '_|||'
                    } else if (this.setData.TileViews[1].Rotated) {
                        ret = '|_||'
                    } else if (this.setData.TileViews[3].Rotated) {
                        ret = '|||_'
                    } else {
                        ret = '||||'
                    }
                    break
                default:
                    ret = '|'
            }
            window.console.log(`ret=${ret}`)
            return ret
        },
    },
    methods : {
        getTileViewChar : function(tileView){
            return Styling.getTileViewChar(tileView)
        },
        onClick : function(){
            this.$emit('SetClick')
        }
    },
}
</script>
