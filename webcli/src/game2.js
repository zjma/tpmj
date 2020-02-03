import * as Utils from "./util.js"

export function randTid() {
    return Utils.randInt(0, 136)
}

export function getRandomTileView() {
    if (Utils.randInt(0,2)==0) {
        return {
            IsValueVisible  : false,
        }
    } else {
        return {
            IsValueVisible  : true,
            Value           : randTid(),
        }
    }
}

export function getRandomVisibleTileView(){
    return {
        IsValueVisible  : true,
        Value           : randTid(),
    }
}

export function getRandomTileViewList(len){
    return [...Array(len).keys()].map(getRandomVisibleTileView)
}

export function getRandomHand(){
    var candidates = [1, 4, 7, 10, 13]
    var x = candidates[Utils.randInt(0, candidates.length)]
    return [...Array(x).keys()].map(getRandomVisibleTileView)
}

export function getRandomTriplet(){
    var victimTid = randTid()
    var gid = Math.floor(victimTid/4)
    return [gid*4,gid*4+1,gid*4+2,gid*4+3].filter((tid) => tid!=victimTid).map((tid) => ({IsValueVisible : true, Value : tid}))
}

export function getRandomSequence(){
    var candidates = [...Array(27).keys()].filter(gid => gid%9<=6)
    var gid = candidates[Utils.randInt(0, candidates.length)]
    return [gid,gid+1,gid+2].map(gid => gid*4+Utils.randInt(0,4)).map((tid) => ({IsValueVisible : true, Value : tid}))
}

export function getRandomSet(){
    if (Utils.randInt(0,2)==0) {
        return getRandomTriplet()
    } else {
        return getRandomSequence()
    }
}

export function getRandomSetList(){
    var x = Utils.randInt(0, 5)
    return [...Array(x).keys()].map(getRandomSet)
}

export function getRandomMountain(){
    var f0 = Utils.randInt(0, 11)
    var f1 = 38 - Utils.randInt(0, 11)
    if (f0 > f1) {
        var tmp = f0
        f0 = f1
        f1 = tmp
    }

    var leftGapCount = f0
    var rightGapCount = 38-f1
    var tileCount = f1-f0
    var tileViews = [...Array(tileCount).keys()].map(() => ({IsValueVisible : false}))
    return Array(leftGapCount).concat(tileViews).concat(Array(rightGapCount))
}
