<template>
    <div>
        <div v-for="(item,rowIdx) in Array(4)" :key="`riverrow-${rowIdx}`">
            <span v-for="(item,idx) in Array(6)" :key="`riverrow-${rowIdx}-leftgap-${idx}`"></span>
            <span v-for="(item,colIdx) in Array(7)" :key="`riverrow-${rowIdx}-content-${colIdx}`">{{RiverRow[rowIdx][colIdx]}}</span>
            <span v-for="(item,idx) in Array(6)" :key="`riverrow-${rowIdx}-rightgap-${idx}`"></span>
        </div>
        <div v-for="(item,rowIdx) in Array(2)" :key="`mountainrow-${rowIdx}`">
            <span v-for="(item,colIdx) in Array(19)" :key="`mountainrow-${rowIdx}-content-${colIdx}`">{{MountainRow[rowIdx][colIdx]}}</span>
        </div>
        <div class='gap-tile-row'>
            <span></span>
        </div>
        <div id='hand'>
            <span v-for="(item,idx) in HandRow" :key="`handrow-${idx}`">{{item}}</span>
        </div>
          <div class='gap-tile-row'>
              <span></span>
          </div>
          <div class='built-sets-row'>
              <span v-for="(item,idx) in SetRow" :key="`setrow-${idx}`">{{item}}</span>
          </div>
    </div>
</template>

<script>
export default {
    name : 'PlayerArea',
    props: {
        data: Object,
    },
    computed: {
        RiverRow : function() {
            return [...Array(4).keys()].map(rowID => this.getRiverRow(rowID))
        },
        MountainRow : function() {
            return [...Array(2).keys()].map(rowIdx => this.getMountainRow(rowIdx))
        },
        HandRow : function() {
            var leftGapCount = 2
            var rightGapCount = 19-(2+this.data.OldHand.length+1+this.data.NewHand.length)
            var sortedOldHand = [...this.data.OldHand]
            sortedOldHand.sort(function(v0,v1){
                var x0 = (v0.IsValueVisible) ? v0.Value : -1
                var x1 = (v1.IsValueVisible) ? v1.Value : -1
                if (x0<x1) return -1
                if (x0>x1) return 1
                return 0
            })
            var tileViews = Array(leftGapCount).concat(sortedOldHand).concat([undefined]).concat(this.data.NewHand).concat(Array(rightGapCount))
            var viewStrs = tileViews.map(this.getViewString)
            return viewStrs
        },
        SetRow : function() {
            var ret = Array(19)
            var idx = 18

            for (const [sid,builtSet] of this.data.BuiltSets.entries()) {
                var sortedSetTileViews = [...builtSet]

                sortedSetTileViews.sort(function(v0,v1){
                    var x0 = (v0.IsValueVisible) ? v0.Value : -1
                    var x1 = (v1.IsValueVisible) ? v1.Value : -1
                    if (x0<x1) return -1
                    if (x0>x1) return 1
                    return 0
                })

                for (const tileView of sortedSetTileViews.reverse()) {
                    if (idx>=0) {
                        ret[idx--] = this.getViewString(tileView)
                    }
                }

                if (sid < this.data.BuiltSets.length - 1) {
                    if (idx>=0) {
                        idx--;
                    }
                }
            }
            return ret
        }
    },
    data: function(){
        return {
            TileGroupChars : ['🀇','🀈','🀉','🀊','🀋','🀌','🀍','🀎','🀏','🀐','🀑','🀒','🀓','🀔','🀕','🀖','🀗','🀘','🀙','🀚','🀛','🀜','🀝','🀞','🀟','🀠','🀡','🀀','🀁','🀂','🀃','🀆','🀅','🀄']
        }
    },
    methods: {
        getUCharByTid(tid){
            var gid = Math.floor(tid/4)
            return this.TileGroupChars[gid]
        },
        getRiverRow(rowID){
            return [...Array(7).keys()].map(colID => this.getViewString(this.data.River[rowID*7+colID]))
        },
        getMountainRow(rowIdx){
            return [...Array(19).keys()].map(colIdx => this.getViewString(this.data.Mountain[colIdx*2+rowIdx]))
        },
        getViewString(tileView) {
            if (tileView) {
                if (tileView.IsValueVisible) {
                    return this.getUCharByTid(tileView.Value)
                } else {
                    return '🀫'
                }
            } else {
                return undefined;
            }
        },
    }
}
</script>

<style>
span {
    display: inline-block;
    font-size: 16px;
    width: 16px;
    max-width: 16px;
}
.rotate {
    display: inline-block;
    transform: rotate(-90deg);
    -webkit-transform: rotate(-90deg);
    -moz-transform: rotate(-90deg);
    -ms-transform: rotate(-90deg);
    -o-transform: rotate(-90deg);
    filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=3);
}

.NonExistingTile {
    visibility: hidden;
}

.foo {
    font-size: 99px
}

</style>
