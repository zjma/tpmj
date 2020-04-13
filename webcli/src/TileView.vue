<template>
    <div :class="BorderHelperClasses" id="DimCalc">
        <div class="Scaler">
            <div :class="RotatorClasses">
                <Back v-if="!TileView.IsValueVisible"/>
                <Man1 v-else-if="TileCategoryID==0"/>
                <Man2 v-else-if="TileCategoryID==1"/>
                <Man3 v-else-if="TileCategoryID==2"/>
                <Man4 v-else-if="TileCategoryID==3"/>
                <Man5 v-else-if="TileCategoryID==4"/>
                <Man6 v-else-if="TileCategoryID==5"/>
                <Man7 v-else-if="TileCategoryID==6"/>
                <Man8 v-else-if="TileCategoryID==7"/>
                <Man9 v-else-if="TileCategoryID==8"/>
                <Sou1 v-else-if="TileCategoryID==9"/>
                <Sou2 v-else-if="TileCategoryID==10"/>
                <Sou3 v-else-if="TileCategoryID==11"/>
                <Sou4 v-else-if="TileCategoryID==12"/>
                <Sou5 v-else-if="TileCategoryID==13"/>
                <Sou6 v-else-if="TileCategoryID==14"/>
                <Sou7 v-else-if="TileCategoryID==15"/>
                <Sou8 v-else-if="TileCategoryID==16"/>
                <Sou9 v-else-if="TileCategoryID==17"/>
                <Pin1 v-else-if="TileCategoryID==18"/>
                <Pin2 v-else-if="TileCategoryID==19"/>
                <Pin3 v-else-if="TileCategoryID==20"/>
                <Pin4 v-else-if="TileCategoryID==21"/>
                <Pin5 v-else-if="TileCategoryID==22"/>
                <Pin6 v-else-if="TileCategoryID==23"/>
                <Pin7 v-else-if="TileCategoryID==24"/>
                <Pin8 v-else-if="TileCategoryID==25"/>
                <Pin9 v-else-if="TileCategoryID==26"/>
                <Ton v-else-if="TileCategoryID==27"/>
                <Nan v-else-if="TileCategoryID==28"/>
                <Shaa v-else-if="TileCategoryID==29"/>
                <Pei v-else-if="TileCategoryID==30"/>
                <Blank v-else-if="TileCategoryID==31"/>
                <Hatsu v-else-if="TileCategoryID==32"/>
                <Chun v-else-if="TileCategoryID==33"/>
            </div>
        </div>
    </div>
</template>

<script>
import Back from './assets/Regular/Back.svg';
import Man1 from './assets/Regular/Man1.svg';
import Man2 from './assets/Regular/Man2.svg';
import Man3 from './assets/Regular/Man3.svg';
import Man4 from './assets/Regular/Man4.svg';
import Man5 from './assets/Regular/Man5.svg';
import Man6 from './assets/Regular/Man6.svg';
import Man7 from './assets/Regular/Man7.svg';
import Man8 from './assets/Regular/Man8.svg';
import Man9 from './assets/Regular/Man9.svg';
import Pin1 from './assets/Regular/Pin1.svg';
import Pin2 from './assets/Regular/Pin2.svg';
import Pin3 from './assets/Regular/Pin3.svg';
import Pin4 from './assets/Regular/Pin4.svg';
import Pin5 from './assets/Regular/Pin5.svg';
import Pin6 from './assets/Regular/Pin6.svg';
import Pin7 from './assets/Regular/Pin7.svg';
import Pin8 from './assets/Regular/Pin8.svg';
import Pin9 from './assets/Regular/Pin9.svg';
import Sou1 from './assets/Regular/Sou1.svg';
import Sou2 from './assets/Regular/Sou2.svg';
import Sou3 from './assets/Regular/Sou3.svg';
import Sou4 from './assets/Regular/Sou4.svg';
import Sou5 from './assets/Regular/Sou5.svg';
import Sou6 from './assets/Regular/Sou6.svg';
import Sou7 from './assets/Regular/Sou7.svg';
import Sou8 from './assets/Regular/Sou8.svg';
import Sou9 from './assets/Regular/Sou9.svg';
import Ton from './assets/Regular/Ton.svg';
import Nan from './assets/Regular/Nan.svg';
import Shaa from './assets/Regular/Shaa.svg';
import Pei from './assets/Regular/Pei.svg';
import Blank from './assets/Regular/Blank.svg';
import Hatsu from './assets/Regular/Hatsu.svg';
import Chun from './assets/Regular/Chun.svg';

export default {
    name : 'TileView',
    props: {
        TileView : Object,
    },
    components:{
        Back,
        Man1,
        Man2,
        Man3,
        Man4,
        Man5,
        Man6,
        Man7,
        Man8,
        Man9,
        Pin1,
        Pin2,
        Pin3,
        Pin4,
        Pin5,
        Pin6,
        Pin7,
        Pin8,
        Pin9,
        Sou1,
        Sou2,
        Sou3,
        Sou4,
        Sou5,
        Sou6,
        Sou7,
        Sou8,
        Sou9,
        Ton,
        Nan,
        Shaa,
        Pei,
        Blank,
        Hatsu,
        Chun,
    },
    computed: {
        TileCategoryID:function(){
            return Math.floor(this.TileView.Value/4);
        },
        BorderHelperClasses:function(){
            switch(this.TileView.Rotation){
                case 90:
                    return ['C90BorderHelper'];
                case -90:
                    return ['AC90BorderHelper'];
                default:
                    return ['C00BorderHelper'];
            }
        },
        RotatorClasses:function(){
            switch(this.TileView.Rotation){
                case 90:
                    return ['C90Rotator'];
                case -90:
                    return ['AC90Rotator'];
                default:
                    return ['C00Rotator'];
            }
        },
    }
}
</script>

<style scoped>
#DimCalc {
    --ratio: 0.06;
    --tile-border-width: 1.5px;
    --tile-border-radius: 3px;
    --tile-net-width: calc(300px * var(--ratio));
    --tile-net-height: calc(400px * var(--ratio));
    --tile-bordered-width: calc(var(--tile-net-width) + var(--tile-border-width) * 2);
    --tile-bordered-height: calc(var(--tile-net-height) + var(--tile-border-width) * 2);
}

.Scaler {
    display: inline-block;
    width: var(--tile-net-width);
    height: var(--tile-net-height);
    transform-origin: 0px 0px;
    transform: scale(var(--ratio));
}

.C00BorderHelper {
    display: inline-block;
    width:var(--tile-bordered-width);
    height:var(--tile-bordered-height);
    border: solid;
    border-width: var(--tile-border-width);
    border-radius: var(--tile-border-radius);
}

.C00Rotator {
}

.C90BorderHelper {
    display: inline-block;
    width:var(--tile-bordered-height);
    height:var(--tile-bordered-width);
    border: solid;
    border-width: var(--tile-border-width);
    border-radius: var(--tile-border-radius);
}

.C90Rotator {
    transform-origin: 200px 200px;
    transform: rotate(90deg);
}

.AC90BorderHelper {
    display: inline-block;
    width:var(--tile-bordered-height);
    height:var(--tile-bordered-width);
    border: solid;
    border-width: var(--tile-border-width);
    border-radius: var(--tile-border-radius);
}

.AC90Rotator {
    transform-origin: 150px 150px;
    transform: rotate(-90deg);
}

</style>
