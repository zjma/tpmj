<template>
    <div class="mahjong-table">
        <player-area class="opposite-area" :data="oppoAreaData" />
        <player-area class="left-area" :data="leftAreaData" />
        <player-area class="right-area" :data="rightAreaData" />
        <player-area class="my-area" :data="myAreaData" />
    </div>
</template>

<script>
import * as Utils from './util.js'
import * as Game2Util from './game2.js'
import PlayerArea from './PlayerArea.vue'
export default {
    name : 'MahjongTable',
    components : {
        'player-area'   :   PlayerArea,
    },
    props: {
        data: Object
    },
    computed: {
        oppoAreaData : function() {
            return this.randAreaData()
        },
        leftAreaData : function() {
            return this.randAreaData()
        },
        rightAreaData : function() {
            return this.randAreaData()
        },
        myAreaData : function() {
            return this.randAreaData()
        },
    },
    methods: {
        randAreaData() {
            var setCount = Utils.randInt(0, 5)
            return {
                River       : Game2Util.getRandomTileViewList(Math.floor(Math.random()*17)+5),
                Mountain    : Game2Util.getRandomMountain(),
                OldHand     : Game2Util.getRandomTileViewList((4-setCount)*3+1),
                NewHand     : Game2Util.getRandomTileViewList(Math.floor(Math.random()*2)),
                BuiltSets   : [...Array(setCount).keys()].map(Game2Util.getRandomSet),
            }
        }
    }
}
</script>

<style>
.my-area {
    position: absolute;
    top: 352px;
    left: 144px;
}
.opposite-area {
    position: absolute;
    top: 0px;
    left: 144px;
    transform: rotate(-180deg);
    -webkit-transform: rotate(-180deg);
    -moz-transform: rotate(-180deg);
    -ms-transform: rotate(-180deg);
    -o-transform: rotate(-180deg);
    filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=2);
}
.left-area {
    position: absolute;
    top: 176px;
    left: -32px;
    transform: rotate(90deg);
    -webkit-transform: rotate(90deg);
    -moz-transform: rotate(90deg);
    -ms-transform: rotate(90deg);
    -o-transform: rotate(90deg);
    filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=1);
}
.right-area {
    position: absolute;
    top: 176px;
    left: 320px;
    transform: rotate(-90deg);
    -webkit-transform: rotate(-90deg);
    -moz-transform: rotate(-90deg);
    -ms-transform: rotate(-90deg);
    -o-transform: rotate(-90deg);
    filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=1);
}
.player {
    font-size: 0;
    width: 314px;
    max-width: 314px;
    height: 240px;
    max-height: 240px;
    text-align: center;
}

.mahjong-table {
    font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";
    line-height: 1.5;
}
</style>
