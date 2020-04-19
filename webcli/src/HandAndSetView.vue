<template>
    <div>
        <div class="d-flex">
            <TileViewRow :TileViews="OldHand"/>
            <TileViewRow :TileViews="NewHand"/>
        </div>
        <div class='BuiltSetContainer'>
            <TileViewRow :TileViews="Set0"/>
            <TileViewRow :TileViews="Set1"/>
            <TileViewRow :TileViews="Set2"/>
            <TileViewRow :TileViews="Set3"/>
        </div>
    </div>
</template>

<script>
import TileViewRow from './TileViewRow.vue';

export default {
    name : 'HandAndSetView',
    components : {
        'TileViewRow' : TileViewRow,
    },
    props: {
        OldHand : Array,
        NewHand : Array,
        Set0 : Array,
        Set1 : Array,
        Set2 : Array,
        Set3 : Array,
    },
}
</script>

<style scoped>
.BuiltSetContainer {
    display: flex;
    flex-direction: row-reverse;
    justify-content: flex-start;
    flex-wrap: wrap-reverse;
}
</style>
