<template>
    <div class="MahjongTable">
        <player-area class="opposite-area player-area" :data="oppoAreaData" :gameStateView="gameStateView" :seatID="oppoSeat" :width="304" :height="200" @UserAction="onOppoAction($event)" />
        <player-area class="left-area player-area" :data="leftAreaData" :gameStateView="gameStateView" :seatID="leftSeat" :width="304" :height="200" @UserAction="onLeftAction($event)" />
        <player-area class="right-area player-area" :data="rightAreaData" :gameStateView="gameStateView" :seatID="rightSeat" :width="304" :height="200" @UserAction="onRightAction($event)" />
        <player-area class="my-area player-area" :data="myAreaData" :gameStateView="gameStateView" :seatID="mySeat" selfseat :width="304" :height="200" @UserAction="onSelfAction($event)" />
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
            window.console.log(`mySeat=${this.mySeat}`)
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
        rightSeat : function() {
            return (this.mySeat+1)%4
        },
        oppoSeat : function() {
            return (this.mySeat+2)%4
        },
        leftSeat : function() {
            return (this.mySeat+3)%4
        },
    },
    methods: {
        onSelfAction: function(action){
            window.console.log('Self action!')
            window.console.log(action)
            this.$emit('UserAction', {
                Area: 'Self',
                Action: action,
            })
        },
        onOppoAction: function(action){
            window.console.log('Oppo action!')
            window.console.log(action)
            this.$emit('UserAction', {
                Area: 'Oppo',
                Action: action,
            })
        },
        onLeftAction: function(action){
            window.console.log('Left action!')
            window.console.log(action)
            this.$emit('UserAction', {
                Area: 'Left',
                Action: action,
            })
        },
        onRightAction: function(action){
            window.console.log('Right action!')
            window.console.log(action)
            this.$emit('UserAction', {
                Area: 'Right',
                Action: action,
            })
        },
    },
}
</script>

<style>
.player-area {
    position: absolute;
    top: 500px;
    left: 300px;
}
.left-area {
    transform-origin: 152px -70px;
    transform: rotate(90deg);
}
.opposite-area {
    transform-origin: 152px -70px;
    transform: rotate(180deg);
}
.right-area {
    transform-origin: 152px -70px;
    transform: rotate(-90deg);
}
.MahjongTable {
    /* font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji"; */
}
.actionable:nth-child(10n+0) {
    animation-name: blink;
    animation-duration: 5s;
    animation-delay: 0s;
    animation-iteration-count: infinite;
}
.actionable:nth-child(10n+1) {
    animation-name: blink;
    animation-duration: 5s;
    animation-delay: 0.1s;
    animation-iteration-count: infinite;
}
.actionable:nth-child(10n+2) {
    animation-name: blink;
    animation-duration: 5s;
    animation-delay: 0.2s;
    animation-iteration-count: infinite;
}
.actionable:nth-child(10n+3) {
    animation-name: blink;
    animation-duration: 5s;
    animation-delay: 0.3s;
    animation-iteration-count: infinite;
}
.actionable:nth-child(10n+4) {
    animation-name: blink;
    animation-duration: 5s;
    animation-delay: 0.4s;
    animation-iteration-count: infinite;
}
.actionable:nth-child(10n+5) {
    animation-name: blink;
    animation-duration: 5s;
    animation-delay: 0.5s;
    animation-iteration-count: infinite;
}
.actionable:nth-child(10n+6) {
    animation-name: blink;
    animation-duration: 5s;
    animation-delay: 0.6s;
    animation-iteration-count: infinite;
}
.actionable:nth-child(10n+7) {
    animation-name: blink;
    animation-duration: 5s;
    animation-delay: 0.7s;
    animation-iteration-count: infinite;
}
.actionable:nth-child(10n+8) {
    animation-name: blink;
    animation-duration: 5s;
    animation-delay: 0.8s;
    animation-iteration-count: infinite;
}
.actionable:nth-child(10n+9) {
    animation-name: blink;
    animation-duration: 5s;
    animation-delay: 0.9s;
    animation-iteration-count: infinite;
}

.actionable:hover {
    opacity: 0.5;
    transform: translateX(0.1px) translateY(0.1px);
}
@keyframes blink {
    20% {
      opacity: 0.5;
    }
    40% {
        opacity: 1.0;
    }
}
@keyframes shake {
  10%, 90% {
    transform: translate3d(-1px, 0, 0);
  }

  20%, 80% {
    transform: translate3d(2px, 0, 0);
  }

  30%, 50%, 70% {
    transform: translate3d(-4px, 0, 0);
  }

  40%, 60% {
    transform: translate3d(4px, 0, 0);
  }
}
</style>
