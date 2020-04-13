<template>
    <div id="TileViewRowContainer">
        <TileView class="TileView" v-for="(tileView,idx) in TileViews" :key="`TileView-${idx}`" :TileView="tileView" />
    </div>
</template>

<script>
import TileView from './TileView.vue';

export default {
    name : 'TileViewRow',
    components:{
        'TileView':TileView,
    },
    props: {
        TileViews : Array,
        RightToLeft : Boolean,
    },
    methods: {
        getTileView: function(idx){
            var jdx = (this.RightToLeft)?idx:(this.TileViews.length-1-idx);
            return this.TileViews[jdx];
        },
        getTileViewContainerClasses: function(tileView){
            if (tileView.Rotation==90){
                return ['C90Container'];
            }
            if (tileView.Rotation==-90){
                return ['AC90Container'];
            }
            return ['C00Container'];
        }
    }
}
</script>

<style scoped>
#TileViewRowContainer {
    display: flex;
    flex-wrap: wrap;
    align-items: flex-end;
    padding-left: 0.25rem;
    padding-right: 0.25rem;
    padding-top: 0.25rem;
    padding-bottom: 0.25rem;
}
</style>
