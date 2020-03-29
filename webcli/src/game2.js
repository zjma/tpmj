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

export function getRandomTriplet(){
    var victimTid = randTid()
    var gid = Math.floor(victimTid/4)
    return {
        TileViews: [gid*4,gid*4+1,gid*4+2,gid*4+3].filter((tid) => tid!=victimTid).map((tid) => ({IsValueVisible : true, Value : tid}))
    }
}

export function getRandomSequence(){
    var candidates = [...Array(27).keys()].filter(gid => gid%9<=6)
    var gid = candidates[Utils.randInt(0, candidates.length)]
    var tids = [gid,gid+1,gid+2].map(gid => gid*4+Utils.randInt(0,4))
    var tileViews = tids.map((tid) => ({IsValueVisible : true, Value : tid}))
    Utils.shuffleArray(tileViews)
    tileViews[Utils.randInt(0,3)].Rotated = true
    return {
        TileViews: tileViews
    }
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

export function randAreaData() {
    // var setCount = Utils.randInt(0, 5)
    return {
        // River       : getRandomTileViewList(Math.floor(Math.random()*17)+5),
        River       : [
            {IsValueVisible : true, Value : 4,},
            {IsValueVisible : true, Value : 121,},
            {IsValueVisible : true, Value : 133,},
        ],
        Mountain    : getRandomMountain(),
        OldHand     : [
            {IsValueVisible : true, Value : 34},
        ],
        NewHand     : [
            {IsValueVisible : true, Value : 35},
        ],
        // BuiltSets   : [...Array(setCount).keys()].map(getRandomSet),
        BuiltSets   : [
            {
                'TileViews': [
                    {IsValueVisible : true, Value : 0,},
                    {IsValueVisible : true, Value : 1,},
                    {IsValueVisible : true, Value : 2,},
                    {IsValueVisible : true, Value : 3,},
                ],
            },
            {
                'TileViews': [
                    {IsValueVisible : true, Value : 20,},
                    {IsValueVisible : true, Value : 21,},
                    {IsValueVisible : true, Value : 22,},
                    {IsValueVisible : true, Value : 23,},
                ],
            },
            {
                'TileViews': [
                    {IsValueVisible : true, Value : 40,},
                    {IsValueVisible : true, Value : 41,},
                    {IsValueVisible : true, Value : 42,},
                    {IsValueVisible : true, Value : 43,},
                ],
            },
            {
                'TileViews': [
                    {IsValueVisible : true, Value : 60,},
                    {IsValueVisible : true, Value : 61,},
                    {IsValueVisible : true, Value : 62,},
                    {IsValueVisible : true, Value : 63,},
                ],
            },
        ],
    }

}

export function randGameStateView() {
    var obj = {
        AreaViews : [
            randAreaData(),
            randAreaData(),
            randAreaData(),
            randAreaData(),
        ],
        State : {
            Main: 'PlayerXWon',
            X: 0,
            WinningTileFromPlayer: 0,
        },
        PlayerNames : [
            'Player0',
            'Player11111111111111111111111111111111111',
        ],
        PatternValues : {
            OneQuad : 1,
            WhiteDragonTriplet : 1,
            GreenDragonTriplet : 1,
            RedDragonTriplet : 1,
        },
        MatchedPatterns: [
            [
                'RedDragonTriplet',
                'OneQuad',
                'GreenDragonTriplet',
            ],
            [],
            [],
            [],
        ],
    }

    return obj;
}

export function getRoleBySeatID(seatID) {
    return (seatID == 0) ? 0 : (seatID == 2) ? 1 : undefined
}

export function getTidFromTileView(view) {
    if (view && view.IsValueVisible) {
        return view.Value
    }
    return undefined
}

export function getTileGroupID(tid) {
    if (tid==undefined) return undefined
    return Math.floor(tid/4)
}

export function getSeatByRole(role) {
    return role*2
}

var minfinder = function(accumulated, toProcess){
    return Math.min(accumulated, toProcess)
}

function get3XSolutions(tgids, allowTgid0Triplet) {
    if (tgids.length==0) return [[]]
    if (tgids.length%3!=0) return []

    var result = []
    var tgid0 = tgids.reduce(minfinder, 999)
    var tgid0Count = tgids.filter(tgid => tgid==tgid0).length

    if (tgid0Count>=3 && allowTgid0Triplet) {
        var tmqTgids = tgids.slice(0)
        tmqTgids.splice(tmqTgids.indexOf(tgid0),1)
        tmqTgids.splice(tmqTgids.indexOf(tgid0),1)
        tmqTgids.splice(tmqTgids.indexOf(tgid0),1)

        var allowed = (tgid0Count == 3)

        for (const subSol of get3XSolutions(tmqTgids, allowed)) {
            result.push([[tgid0,tgid0,tgid0]].concat(subSol))
        }
    }

    if (tgid0>=0 && tgid0<=6 || tgid0>=9 && tgid0<=15 || tgid0>=18 && tgid0<=24) {
        var tgid1Count = tgids.filter(tgid => tgid==tgid0+1).length
        var tgid2Count = tgids.filter(tgid => tgid==tgid0+2).length
        if (tgid1Count>=1 && tgid2Count>=1) {
            var tmpTgids = tgids.slice(0)
            tmpTgids.splice(tmpTgids.indexOf(tgid0),1)
            tmpTgids.splice(tmpTgids.indexOf(tgid0+1),1)
            tmpTgids.splice(tmpTgids.indexOf(tgid0+2),1)

            var allowed2 = (tgid0Count == 1)

            for (const subSol of get3XSolutions(tmpTgids, allowed2)) {
                result.push([[tgid0,tgid0+1,tgid0+2]].concat(subSol))
            }
        }
    }

    return result
}

export function get3Xn2Solutions(tgids) {
    if (tgids.length%3!=2) {
        return []
    }

    var result = []

    var tg2c = Array(34).fill(0)
    for (const x of tgids) tg2c[x]++

    for (var tgid=0; tgid<34; tgid++) {
        if (tg2c[tgid]>=2) {
            var tmpTgids = tgids.slice(0)
            tmpTgids.splice(tmpTgids.indexOf(tgid), 1)
            tmpTgids.splice(tmpTgids.indexOf(tgid), 1)
            for (const subSol of get3XSolutions(tmpTgids, true)) {
                result.push(subSol.concat([[tgid,tgid]]))
            }
        }
    }

    return result
}

function getTidSolution(tids, gtidsol) {
    var tg2tids = [...Array(34).keys()].map(() => ([]))

    for (const tid of tids) {
        var tgid = getTileGroupID(tid)
        tg2tids[tgid].push(tid)
    }

    var result = []

    for (const part of gtidsol) {
        var subresult = []

        for (const tgid of part) {
            subresult.push(tg2tids[tgid].pop())
        }

        result.push(subresult)
    }

    return result
}

export function getTidListFromTileViewList(tvlist) {
    return tvlist.map(v => getTidFromTileView(v))
}

export function getTripletTileGroupID(tids) {
    if (tids.length != 3) return undefined
    var tgid0 = getTileGroupID(tids[0])
    var tgid1 = getTileGroupID(tids[1])
    var tgid2 = getTileGroupID(tids[2])
    if (tgid0 == tgid1 && tgid0==tgid2) return tgid0
    return undefined
}

export function getTsumoActions(gameStateView, role) {
    var seat = getSeatByRole(role)
    var oldTids = gameStateView.AreaViews[seat].OldHand.map(v => getTidFromTileView(v)).filter(v => v!=undefined)
    var newTids = gameStateView.AreaViews[seat].NewHand.map(v => getTidFromTileView(v)).filter(v => v!=undefined)
    var tids = oldTids.concat(newTids)
    tids.sort((a, b) => a - b)
    var tgids = tids.map(tid => getTileGroupID(tid))
    var result = get3Xn2Solutions(tgids).map(gtidsol => ({Type:'Tsumo',Value:getTidSolution(tids, gtidsol)}))
    return result
}

export function getRonActions(gameStateView, role) {
    var seat = getSeatByRole(role)
    var opposeat = getSeatByRole(1-role)
    var oldTids = gameStateView.AreaViews[seat].OldHand.map(v => getTidFromTileView(v)).filter(v => v!=undefined)
    var oppoRiver = gameStateView.AreaViews[opposeat].River
    var discardedTid = getTidFromTileView(oppoRiver[oppoRiver.length-1])
    var tids = oldTids.concat([discardedTid]).filter(x => x!=undefined)
    tids.sort((a, b) => a - b)
    var tgids = tids.map(tid => getTileGroupID(tid))
    var result = get3Xn2Solutions(tgids).map(gtidsol => ({Type:'Ron',Value:getTidSolution(tids, gtidsol)}))
    return result
}

export function getPonActions(gameStateView, role) {
    var seat = getSeatByRole(role)
    var opposeat = getSeatByRole(1-role)
    var oldTids = gameStateView.AreaViews[seat].OldHand.map(v => getTidFromTileView(v)).filter(v => v!=undefined)
    var oppoRiver = gameStateView.AreaViews[opposeat].River
    var discardedTid = getTidFromTileView(oppoRiver[oppoRiver.length-1])
    var discardedTgid = getTileGroupID(discardedTid)

    var ponCandTids = oldTids.filter(tid => getTileGroupID(tid)==discardedTgid)
    if (ponCandTids.length >= 2) {
        return [
            {
                Type : 'Pon',
                Value : ponCandTids.slice(0,2).concat([discardedTid]),
            }
        ]
    }

    return []
}

export function getChiActions(gameStateView, role) {
    var seat = getSeatByRole(role)
    var opposeat = getSeatByRole(1-role)
    var oldTids = gameStateView.AreaViews[seat].OldHand.map(v => getTidFromTileView(v)).filter(v => v!=undefined)
    var oppoRiver = gameStateView.AreaViews[opposeat].River
    var discardedTid = getTidFromTileView(oppoRiver[oppoRiver.length-1])
    var discardedTgid = getTileGroupID(discardedTid)
    if (discardedTgid == undefined) return []

    var result = []

    var candm1s = oldTids.filter(tid => getTileGroupID(tid)==discardedTgid-1)
    var candm2s = oldTids.filter(tid => getTileGroupID(tid)==discardedTgid-2)
    var candp1s = oldTids.filter(tid => getTileGroupID(tid)==discardedTgid+1)
    var candp2s = oldTids.filter(tid => getTileGroupID(tid)==discardedTgid+2)

    window.console.log('Chi analyzing.')
    window.console.log(candm2s)
    window.console.log(candm1s)
    window.console.log(candp1s)
    window.console.log(candp2s)

    if ((discardedTgid>=2 && discardedTgid<=8 || discardedTgid>=11 && discardedTgid<=17 || discardedTgid>=20 && discardedTgid<26) && candm2s.length>=1 && candm1s.length>=1) {
        result.push({
            Type:'Chi',
            Value:[candm2s[0],candm1s[0],discardedTid],
        })
    }

    if ((discardedTgid>=1 && discardedTgid<=7 || discardedTgid>=10 && discardedTgid<=16 || discardedTgid>=19 && discardedTgid<25) && candm1s.length>=1 && candp1s.length>=1) {
        result.push({
            Type:'Chi',
            Value:[candm1s[0],discardedTid,candp1s[0]],
        })
    }

    if ((discardedTgid>=0 && discardedTgid<=6 || discardedTgid>=9 && discardedTgid<=15 || discardedTgid>=18 && discardedTgid<24) && candp1s.length>=1 && candp2s.length>=1) {
        result.push({
            Type:'Chi',
            Value:[discardedTid,candp1s[0],candp2s[0]],
        })
    }

    window.console.log('Chi analyzed.')
    window.console.log(result)
    return result
}

export function getKan0Actions(gameStateView, role) {
    var seatID = getSeatByRole(role)
    var oldHandTids = gameStateView.AreaViews[seatID].OldHand.map(v => getTidFromTileView(v))
    var newHandTids = gameStateView.AreaViews[seatID].NewHand.map(v => getTidFromTileView(v))
    var tids = oldHandTids.concat(newHandTids)
    var tg2c = Array(34).fill(0)
    for (const tid of tids) tg2c[getTileGroupID(tid)]++
    var result = [...tg2c.keys()].map(idx => ({TileGroupID:idx,TileCount:tg2c[idx]})).filter(x => x.TileCount>=4).map(x => ({Type:'Kan0',Value:[x.TileGroupID*4,x.TileGroupID*4+1,x.TileGroupID*4+2,x.TileGroupID*4+3]}))
    return result
}

export function getKan1Actions(gameStateView, role) {
    var seat = getSeatByRole(role)
    var opposeat = getSeatByRole(1-role)
    var oldTids = gameStateView.AreaViews[seat].OldHand.map(v => getTidFromTileView(v)).filter(v => v!=undefined)
    var oppoRiver = gameStateView.AreaViews[opposeat].River
    var discardedTid = getTidFromTileView(oppoRiver[oppoRiver.length-1])
    var discardedTgid = getTileGroupID(discardedTid)

    if (oldTids.filter(tid => getTileGroupID(tid)==discardedTgid).length >= 3) {
        return [
            {
                Type : 'Kan1',
                Value : [discardedTgid*4,discardedTgid*4+1,discardedTgid*4+2,discardedTgid*4+3,],
            }
        ]
    }

    return []
}

export function getKan2Actions(gameStateView, role) {
    var seatID = getSeatByRole(role)
    var oldHandTids = gameStateView.AreaViews[seatID].OldHand.map(v => getTidFromTileView(v))
    var newHandTids = gameStateView.AreaViews[seatID].NewHand.map(v => getTidFromTileView(v))
    var tids = oldHandTids.concat(newHandTids)
    var handTgids = tids.map(tid => getTileGroupID(tid))

    return gameStateView.AreaViews[seatID].BuiltSets.map(function(setview){
        var tids = getTidListFromTileViewList(setview.TileViews)
        var tgid = getTripletTileGroupID(tids)
        return {
            Tiles : tids,
            TripletTileGroupID: tgid,
        }
    }).filter(
        o => o.TripletTileGroupID!=undefined && handTgids.indexOf(o.TripletTileGroupID)>=0
    ).map(function(o){
        return {
            Type : 'Kan2',
            Value: [o.TripletTileGroupID*4,o.TripletTileGroupID*4+1,o.TripletTileGroupID*4+2,o.TripletTileGroupID*4+3],
        }
    })
}

function tgDuplicatingTidRemover(accumulated, toProcess) {
    var tgid = getTileGroupID(toProcess)

    if (accumulated.filter(tid => getTileGroupID(tid) == tgid).length >= 1) {
        return accumulated
    } else {
        return accumulated.concat([toProcess])
    }
}

export function getDiscardNewActions(gameStateView, role) {
    var seat = getSeatByRole(role)
    return gameStateView.AreaViews[seat].NewHand.map(v => getTidFromTileView(v)).filter(v => v!=undefined).reduce(tgDuplicatingTidRemover, []).map(tid => ({Type:'Discard', Source:'NewHand', Value:tid}))
}

export function getDiscardOldActions(gameStateView, role) {
    var seat = getSeatByRole(role)
    return gameStateView.AreaViews[seat].OldHand.map(v => getTidFromTileView(v)).filter(v => v!=undefined).reduce(tgDuplicatingTidRemover, []).map(tid => ({Type:'Discard', Source:'OldHand', Value:tid}))
}

export function getDrawActions() {
    return {
        Type: 'Draw',
    }
}

export function getAction(gameStateView, role) {
    var result = []

    if (gameStateView.State.Main == 'PlayerXHandleDraw' && gameStateView.State.X == role) {
        result = result.concat(getTsumoActions(gameStateView, role))
        result = result.concat(getKan0Actions(gameStateView, role))
        result = result.concat(getKan2Actions(gameStateView, role))
        result = result.concat(getDiscardNewActions(gameStateView, role))
        result = result.concat(getDiscardOldActions(gameStateView, role))
        return result
    }

    if (gameStateView.State.Main == 'PlayerXToRespondToDiscard' && gameStateView.State.X == role) {
        result = result.concat(getDrawActions())
        result = result.concat(getRonActions(gameStateView, role))
        result = result.concat(getKan1Actions(gameStateView, role))
        result = result.concat(getPonActions(gameStateView, role))
        result = result.concat(getChiActions(gameStateView, role))
        return result
    }

    return []
}

export function getTotalPatternValue(gameStateView, seatID) {
    var result = 0;

    for (var pattern of gameStateView.MatchedPatterns[seatID]) {
        window.console.log(`Pattern=${pattern}`);
        result += gameStateView.PatternValues[pattern];
    }

    return result;
}
