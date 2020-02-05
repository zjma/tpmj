<template>
    <div class="mahjong-table">
        <player-area class="opposite-area" :data="oppoAreaData" />
        <player-area class="left-area" :data="leftAreaData" />
        <player-area class="right-area" :data="rightAreaData" />
        <player-area class="my-area" :data="myAreaData" />
    </div>
</template>

<script>
import PlayerArea from './PlayerArea.vue'
export default {
    name : 'MahjongTable',
    components : {
        'player-area'   :   PlayerArea,
    },
    props: {
        gameStateView   : Object,
        mySeat          : Number,
    },
    computed: {
        oppoAreaData : function() {
            return this.gameStateView.AreaViews[(this.mySeat+2)%4]
        },
        leftAreaData : function() {
            return this.gameStateView.AreaViews[(this.mySeat+3)%4]
        },
        rightAreaData : function() {
            return this.gameStateView.AreaViews[(this.mySeat+1)%4]
        },
        myAreaData : function() {
            return this.gameStateView.AreaViews[(this.mySeat+0)%4]
        },
    },
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
</style>
