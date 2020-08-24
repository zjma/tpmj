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

export function getTileViewListByTids(tids){
    return tids.map(tid => ({IsValueVisible:true,Value:tid}));
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

export function getMountainRemainingCount(gameStateView) {
    var accumulator = (accumulated, toProcess) => toProcess.Mountain.filter(v => v!=undefined).length + accumulated;
    return gameStateView.AreaViews.reduce(accumulator, 0);
}

export function randAreaData() {
    // var setCount = Utils.randInt(0, 5)
    return {
        // River       : getRandomTileViewList(Math.floor(Math.random()*17)+5),
        River       : [
            {IsValueVisible : true, Value : 121,},
            {IsValueVisible : true, Value : 121,},
            {IsValueVisible : true, Value : 121,},
            {IsValueVisible : true, Value : 121,},
            {IsValueVisible : true, Value : 121,},
            {IsValueVisible : true, Value : 121,},
            {IsValueVisible : true, Value : 121,},
            {IsValueVisible : true, Value : 121,},
            {IsValueVisible : true, Value : 121,},
            {IsValueVisible : true, Value : 121,},
            {IsValueVisible : true, Value : 121,},
            {IsValueVisible : true, Value : 121,},
            {IsValueVisible : true, Value : 121,},
            {IsValueVisible : true, Value : 121,},
            {IsValueVisible : true, Value : 121,},
            {IsValueVisible : false},
            {IsValueVisible : false},
            {IsValueVisible : false},
            {IsValueVisible : false},
            {IsValueVisible : false},
            {IsValueVisible : false},
            {IsValueVisible : false},
            {IsValueVisible : false},
            {IsValueVisible : false},
            {IsValueVisible : true, Value : 3},
        ],
        Mountain    : getRandomMountain(),
        OldHand     : [
            {IsValueVisible : true, Value : 0},
            {IsValueVisible : true, Value : 1},
            {IsValueVisible : true, Value : 2},
            {IsValueVisible : true, Value : 4},
            {IsValueVisible : true, Value : 8},
            {IsValueVisible : true, Value : 12},
            {IsValueVisible : true, Value : 16},
            {IsValueVisible : true, Value : 20},
            {IsValueVisible : true, Value : 24},
            {IsValueVisible : true, Value : 28},
            {IsValueVisible : true, Value : 32},
            {IsValueVisible : true, Value : 33},
            {IsValueVisible : true, Value : 34},
        ],
        NewHand     : [
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
            Main: 'PlayerXToRespondToDiscard',
            X: 0,
            // WinningTileFromPlayer: 0,
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
    var seat = getSeatByRole(role);
    var oldTids = gameStateView.AreaViews[seat].OldHand.map(v => getTidFromTileView(v)).filter(v => v!=undefined);
    var newTids = gameStateView.AreaViews[seat].NewHand.map(v => getTidFromTileView(v)).filter(v => v!=undefined);
    var tids = oldTids.concat(newTids);
    tids.sort((a, b) => a - b);
    var tgids = tids.map(tid => getTileGroupID(tid));
    var result = get3Xn2Solutions(tgids).map(function(gtidsol){
        var sol = getTidSolution(tids, gtidsol);
        return {
            Type:'Tsumo',
            Value:sol,
            Preview:sol.map(tids => getTileViewListByTids(tids)),
        };
    });
    return result;
}

export function getRonActions(gameStateView, role, ronTid) {
    var seat = getSeatByRole(role);
    var oldTids = gameStateView.AreaViews[seat].OldHand.map(v => getTidFromTileView(v)).filter(v => v!=undefined);
    var tids = oldTids.concat([ronTid]).filter(x => x!=undefined);
    tids.sort((a, b) => a - b);
    var tgids = tids.map(tid => getTileGroupID(tid));
    var result = get3Xn2Solutions(tgids).map(function(gtidsol){
        var sol = getTidSolution(tids, gtidsol);
        return {
            Type:'Ron',
            Value:sol,
            Preview:sol.map(tids => getTileViewListByTids(tids)),
        };
    });
    return result;
}

export function getPonActions(gameStateView, role) {
    var seat = getSeatByRole(role);
    var opposeat = getSeatByRole(1-role);
    var oldTids = gameStateView.AreaViews[seat].OldHand.map(v => getTidFromTileView(v)).filter(v => v!=undefined);
    var oppoRiver = gameStateView.AreaViews[opposeat].River;
    var discardedTid = getTidFromTileView(oppoRiver[oppoRiver.length-1]);
    var discardedTgid = getTileGroupID(discardedTid);

    var ponCandTids = oldTids.filter(tid => getTileGroupID(tid)==discardedTgid);
    if (ponCandTids.length >= 2) {
        var tids = [ponCandTids[0],discardedTid,ponCandTids[1]];
        return [
            {
                Type : 'Pon',
                Value : tids,
                Preview: [getTileViewListByTids(tids)],
            }
        ];
    }

    return [];
}

export function getChiActions(gameStateView, role) {
    var seat = getSeatByRole(role);
    var opposeat = getSeatByRole(1-role);
    var oldTids = gameStateView.AreaViews[seat].OldHand.map(v => getTidFromTileView(v)).filter(v => v!=undefined);
    var oppoRiver = gameStateView.AreaViews[opposeat].River;
    var discardedTid = getTidFromTileView(oppoRiver[oppoRiver.length-1]);
    var discardedTgid = getTileGroupID(discardedTid);
    if (discardedTgid == undefined) return [];

    var result = [];

    var candm1s = oldTids.filter(tid => getTileGroupID(tid)==discardedTgid-1);
    var candm2s = oldTids.filter(tid => getTileGroupID(tid)==discardedTgid-2);
    var candp1s = oldTids.filter(tid => getTileGroupID(tid)==discardedTgid+1);
    var candp2s = oldTids.filter(tid => getTileGroupID(tid)==discardedTgid+2);

    if ((discardedTgid>=2 && discardedTgid<=8 || discardedTgid>=11 && discardedTgid<=17 || discardedTgid>=20 && discardedTgid<26) && candm2s.length>=1 && candm1s.length>=1) {
        result.push({
            Type:'Chi',
            Value:[candm2s[0],candm1s[0],discardedTid],
            Preview:[getTileViewListByTids([candm2s[0],candm1s[0],discardedTid])],
        });
    }

    if ((discardedTgid>=1 && discardedTgid<=7 || discardedTgid>=10 && discardedTgid<=16 || discardedTgid>=19 && discardedTgid<25) && candm1s.length>=1 && candp1s.length>=1) {
        result.push({
            Type:'Chi',
            Value:[candm1s[0],discardedTid,candp1s[0]],
            Preview:[getTileViewListByTids([candm1s[0],discardedTid,candp1s[0]])],
        });
    }

    if ((discardedTgid>=0 && discardedTgid<=6 || discardedTgid>=9 && discardedTgid<=15 || discardedTgid>=18 && discardedTgid<24) && candp1s.length>=1 && candp2s.length>=1) {
        var tids = [discardedTid,candp1s[0],candp2s[0]];
        result.push({
            Type:'Chi',
            Value:tids,
            Preview:[getTileViewListByTids(tids)],
        });
    }

    return result;
}

export function getKan0Actions(gameStateView, role) {
    if (getMountainRemainingCount(gameStateView)==0) return [];
    var seatID = getSeatByRole(role);
    var oldHandTids = gameStateView.AreaViews[seatID].OldHand.map(v => getTidFromTileView(v));
    var newHandTids = gameStateView.AreaViews[seatID].NewHand.map(v => getTidFromTileView(v));
    var tids = oldHandTids.concat(newHandTids);
    var tg2c = Array(34).fill(0);
    for (const tid of tids) tg2c[getTileGroupID(tid)]++;
    var result = [...tg2c.keys()].map(idx => ({
        TileGroupID:idx,
        TileCount:tg2c[idx]
    })).filter(x => x.TileCount>=4).map(function(x){
        var tids = [x.TileGroupID*4,x.TileGroupID*4+1,x.TileGroupID*4+2,x.TileGroupID*4+3];
        return {
            Type:'Kan0',
            Value:tids,
            Preview:[getTileViewListByTids(tids)],
        };
    });
    return result;
}

export function getKan1Actions(gameStateView, role) {
    if (getMountainRemainingCount(gameStateView)==0) return [];
    var seat = getSeatByRole(role);
    var opposeat = getSeatByRole(1-role);
    var oldTids = gameStateView.AreaViews[seat].OldHand.map(v => getTidFromTileView(v)).filter(v => v!=undefined);
    var oppoRiver = gameStateView.AreaViews[opposeat].River;
    var discardedTid = getTidFromTileView(oppoRiver[oppoRiver.length-1]);
    var discardedTgid = getTileGroupID(discardedTid);

    if (oldTids.filter(tid => getTileGroupID(tid)==discardedTgid).length >= 3) {
        var tids = [discardedTgid*4,discardedTgid*4+1,discardedTgid*4+2,discardedTgid*4+3,];
        return [
            {
                Type : 'Kan1',
                Value : tids,
                Preview: [getTileViewListByTids(tids)],
            }
        ]
    }

    return []
}

export function getKan2Actions(gameStateView, role) {
    if (getMountainRemainingCount(gameStateView)==0) return [];
    var seatID = getSeatByRole(role);
    var oldHandTids = gameStateView.AreaViews[seatID].OldHand.map(v => getTidFromTileView(v));
    var newHandTids = gameStateView.AreaViews[seatID].NewHand.map(v => getTidFromTileView(v));
    var tids = oldHandTids.concat(newHandTids);
    var handTgids = tids.map(tid => getTileGroupID(tid));
    return gameStateView.AreaViews[seatID].BuiltSets.map(function(setview){
        var tids = getTidListFromTileViewList(setview.TileViews);
        var tgid = getTripletTileGroupID(tids);
        return {
            Tiles : tids,
            TripletTileGroupID: tgid,
        };
    }).filter(o => o.TripletTileGroupID!=undefined && handTgids.indexOf(o.TripletTileGroupID)>=0).map(function(o){
        var tids = [o.TripletTileGroupID*4,o.TripletTileGroupID*4+1,o.TripletTileGroupID*4+2,o.TripletTileGroupID*4+3];
        return {
            Type : 'Kan2',
            Value: tids,
            Preview: [getTileViewListByTids(tids)],
        };
    });
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
    return gameStateView.AreaViews[seat].NewHand.map(v => getTidFromTileView(v)).filter(v => v!=undefined).reduce(tgDuplicatingTidRemover, []).map(tid => ({Type:'Discard', Source:'NewHand', Value:tid, Preview:[getTileViewListByTids([tid])]}))
}

export function getDiscardOldActions(gameStateView, role) {
    var seat = getSeatByRole(role)
    return gameStateView.AreaViews[seat].OldHand.map(v => getTidFromTileView(v)).filter(v => v!=undefined).reduce(tgDuplicatingTidRemover, []).map(tid => ({Type:'Discard', Source:'OldHand', Value:tid, Preview:[getTileViewListByTids([tid])]}))
}

export function getDrawActions() {
    return {
        Type: 'Draw',
    }
}

export function getPassActions() {
    return {
        Type: 'Pass',
    }
}

export function getAction(gameStateView, role) {
    var result = [];

    if (gameStateView.State.Main == 'PlayerXHandleDraw' && gameStateView.State.X == role) {
        result = result.concat(getTsumoActions(gameStateView, role));
        result = result.concat(getKan0Actions(gameStateView, role));
        result = result.concat(getKan2Actions(gameStateView, role));
        result = result.concat(getDiscardNewActions(gameStateView, role));
        result = result.concat(getDiscardOldActions(gameStateView, role));
        window.console.log(result);
        return result;
    }

    if (gameStateView.State.Main == 'PlayerXToRespondToDiscard' && gameStateView.State.X == role) {
        var opposeat = getSeatByRole(1-role);
        var oppoRiver = gameStateView.AreaViews[opposeat].River;
        var discardedTid = getTidFromTileView(oppoRiver[oppoRiver.length-1]);
        result = result.concat(getDrawActions());
        result = result.concat(getRonActions(gameStateView, role, discardedTid));
        result = result.concat(getKan1Actions(gameStateView, role));
        result = result.concat(getPonActions(gameStateView, role));
        result = result.concat(getChiActions(gameStateView, role));
        window.console.log(result);
        return result;
    }

    if (gameStateView.State.Main == 'PlayerXToRespondToKan2' && gameStateView.State.X == role) {
        result = result.concat(getPassActions());
        result = result.concat(getRonActions(gameStateView, role, gameStateView.State.Kan2Tile));
        window.console.log(result);
        return result;
    }

    return [];
}

export function getTotalPatternValue(gameStateView, seatID) {
    var result = 0;

    for (var pattern of gameStateView.MatchedPatterns[seatID]) {
        window.console.log(`Pattern=${pattern}`);
        result += gameStateView.PatternValues[pattern];
    }

    return result;
}

export const PatternLibrary = {
    WhiteDragonTriplet : {
        Name:'役牌·白',
        Value:1,
        Desc:'和牌时，有白板的刻/杠。',
        Example:{
            OldHand:[
                {IsValueVisible:true,Value:4},
                {IsValueVisible:true,Value:5},
                {IsValueVisible:true,Value:6},
                {IsValueVisible:true,Value:40},
                {IsValueVisible:true,Value:44},
                {IsValueVisible:true,Value:48},
                {IsValueVisible:true,Value:127},
                {IsValueVisible:true,Value:126},
                {IsValueVisible:true,Value:125},
                {IsValueVisible:true,Value:135},
            ],
            NewHand:[
                {IsValueVisible:true,Value:134},
            ],
            Set0:[
                {IsValueVisible:true,Value:7},
                {IsValueVisible:true,Value:11},
                {IsValueVisible:true,Value:15},
            ],
            Set1:[
            ],
            Set2:[
            ],
            Set3:[
            ],
        },
    },
    GreenDragonTriplet : {
        Name:'役牌·发',
        Value:1,
        Desc:'和牌时，有发财的刻/杠。',
        Example:{
            OldHand:[
                {IsValueVisible:true,Value:40},
                {IsValueVisible:true,Value:44},
                {IsValueVisible:true,Value:48},
                {IsValueVisible:true,Value:56},
                {IsValueVisible:true,Value:60},
                {IsValueVisible:true,Value:64},
                {IsValueVisible:true,Value:68},
            ],
            NewHand:[
                {IsValueVisible:true,Value:69},
            ],
            Set0:[
                {IsValueVisible:true,Value:131},
                {IsValueVisible:true,Value:130},
                {IsValueVisible:true,Value:129},
            ],
            Set1:[
                {IsValueVisible:true,Value:4},
                {IsValueVisible:true,Value:5},
                {IsValueVisible:true,Value:6},
            ],
            Set2:[
            ],
            Set3:[
            ],
        },
    },
    RedDragonTriplet : {
        Name:'役牌·中',
        Value:1,
        Desc:'和牌时，有红中的刻/杠。',
        Example:{
            OldHand:[
                {IsValueVisible:true,Value:40},
                {IsValueVisible:true,Value:44},
                {IsValueVisible:true,Value:48},
                {IsValueVisible:true,Value:56},
                {IsValueVisible:true,Value:60},
                {IsValueVisible:true,Value:64},
                {IsValueVisible:true,Value:68},
            ],
            NewHand:[
                {IsValueVisible:true,Value:69},
            ],
            Set0:[
                {IsValueVisible:true,Value:135},
                {IsValueVisible:true,Value:134},
                {IsValueVisible:true,Value:133},
            ],
            Set1:[
                {IsValueVisible:true,Value:4},
                {IsValueVisible:true,Value:5},
                {IsValueVisible:true,Value:6},
            ],
            Set2:[
            ],
            Set3:[
            ],
        },
    },
    EastWindTriplet : {
        Name:'门风·东',
        Value:1,
        Desc:'和牌时，身为东家，且有东风的刻/杠。',
        Example:{
            OldHand:[
                {IsValueVisible:true,Value:40},
                {IsValueVisible:true,Value:44},
                {IsValueVisible:true,Value:48},
                {IsValueVisible:true,Value:56},
                {IsValueVisible:true,Value:60},
                {IsValueVisible:true,Value:64},
                {IsValueVisible:true,Value:68},
            ],
            NewHand:[
                {IsValueVisible:true,Value:69},
            ],
            Set0:[
                {IsValueVisible:true,Value:108},
                {IsValueVisible:true,Value:109},
                {IsValueVisible:true,Value:110},
            ],
            Set1:[
                {IsValueVisible:true,Value:4},
                {IsValueVisible:true,Value:5},
                {IsValueVisible:true,Value:6},
            ],
            Set2:[
            ],
            Set3:[
            ],
        },
    },
    SouthWindTriplet : {
        Name:'门风·南',
        Value:1,
        Desc:'和牌时，身为南家，且有南风的刻/杠。',
        Example:{
            OldHand:[
                {IsValueVisible:true,Value:56},
                {IsValueVisible:true,Value:60},
                {IsValueVisible:true,Value:64},
                {IsValueVisible:true,Value:68},
                {IsValueVisible:true,Value:112},
                {IsValueVisible:true,Value:113},
                {IsValueVisible:true,Value:114},
            ],
            NewHand:[
                {IsValueVisible:true,Value:69},
            ],
            Set0:[
                {IsValueVisible:true,Value:40},
                {IsValueVisible:true,Value:44},
                {IsValueVisible:true,Value:48},
            ],
            Set1:[
                {IsValueVisible:true,Value:4},
                {IsValueVisible:true,Value:5},
                {IsValueVisible:true,Value:6},
            ],
            Set2:[
            ],
            Set3:[
            ],
        },
    },
    OneQuad : {
        Name:'单杠',
        Value:1,
        Desc:'和牌时，有1个杠。',
        Example:{
            OldHand:[
                {IsValueVisible:true,Value:40},
                {IsValueVisible:true,Value:44},
                {IsValueVisible:true,Value:48},
                {IsValueVisible:true,Value:56},
                {IsValueVisible:true,Value:60},
                {IsValueVisible:true,Value:64},
                {IsValueVisible:true,Value:68},
            ],
            NewHand:[
                {IsValueVisible:true,Value:69},
            ],
            Set0:[
                {IsValueVisible:true,Value:1},
                {IsValueVisible:true,Value:2},
                {IsValueVisible:true,Value:3},
                {IsValueVisible:true,Value:0},
            ],
            Set1:[
                {IsValueVisible:true,Value:120},
                {IsValueVisible:true,Value:121},
                {IsValueVisible:true,Value:122},
            ],
            Set2:[
            ],
            Set3:[
            ],
        },
    },
    IdenticalSequencesI : {
        Name:'一般高',
        Value:1,
        Desc:'和牌时，有2个一样的顺子。',
        Example:{
            OldHand:[
                {IsValueVisible:true,Value:56},
                {IsValueVisible:true,Value:60},
                {IsValueVisible:true,Value:64},
                {IsValueVisible:true,Value:68},
                {IsValueVisible:true,Value:72},
                {IsValueVisible:true,Value:76},
                {IsValueVisible:true,Value:80},
            ],
            NewHand:[
                {IsValueVisible:true,Value:69},
            ],
            Set0:[
                {IsValueVisible:true,Value:5},
                {IsValueVisible:true,Value:6},
                {IsValueVisible:true,Value:7},
            ],
            Set1:[
                {IsValueVisible:true,Value:73},
                {IsValueVisible:true,Value:77},
                {IsValueVisible:true,Value:81},
            ],
            Set2:[
            ],
            Set3:[
            ],
        },
    },
    Rinshan : {
        Name:'杠上开花',
        Value:1,
        Desc:'开杠后从牌山尾部补的牌形成自摸。',
        Example:{
            OldHand:[
            ],
            NewHand:[
            ],
            Set0:[
            ],
            Set1:[
            ],
            Set2:[
            ],
            Set3:[
            ],
        },
    },
    RobKan : {
        Name:'抢杠',
        Value:1,
        Desc:'和他人开小明杠的牌。',
        Example:{
            OldHand:[
            ],
            NewHand:[
            ],
            Set0:[
            ],
            Set1:[
            ],
            Set2:[
            ],
            Set3:[
            ],
        },
    },
    LastTileTsumo : {
        Name:'海底捞月',
        Value:1,
        Desc:'以牌山最后一张牌自摸和牌。',
        Example:{
            OldHand:[
            ],
            NewHand:[
            ],
            Set0:[
            ],
            Set1:[
            ],
            Set2:[
            ],
            Set3:[
            ],
        },
    },
    LastTileRon : {
        Name:'河底捞鱼',
        Value:1,
        Desc:'在牌山已耗尽时，由他人点炮和牌。',
        Example:{
            OldHand:[
            ],
            NewHand:[
            ],
            Set0:[
            ],
            Set1:[
            ],
            Set2:[
            ],
            Set3:[
            ],
        },
    },
    NoMelding: {
        Name:'不求人',
        Value:1,
        Desc:'没有吃/碰/开大明杠/加杠，自摸和牌。（注：可以暗杠。）',
        Example:{
            OldHand:[
            ],
            NewHand:[
            ],
            Set0:[
            ],
            Set1:[
            ],
            Set2:[
            ],
            Set3:[
            ],
        },
    },
    AllMelding: {
        Name:'全求人',
        Value:1,
        Desc:'4副面子都靠吃/碰/大明杠/加杠完成，由他人点炮和牌。（注：不能暗杠。）',
        Example:{
            OldHand:[
            ],
            NewHand:[
            ],
            Set0:[
            ],
            Set1:[
            ],
            Set2:[
            ],
            Set3:[
            ],
        },
    },
    TwoQuads : {
        Name:'双杠',
        Value:2,
        Desc:'和牌时，有2个杠。',
        Example:{
            OldHand:[
                {IsValueVisible:true,Value:40},
                {IsValueVisible:true,Value:44},
                {IsValueVisible:true,Value:48},
                {IsValueVisible:true,Value:56},
                {IsValueVisible:true,Value:60},
                {IsValueVisible:true,Value:64},
                {IsValueVisible:true,Value:68},
            ],
            NewHand:[
                {IsValueVisible:true,Value:69},
            ],
            Set0:[
                {IsValueVisible:true,Value:0},
                {IsValueVisible:true,Value:1},
                {IsValueVisible:true,Value:2},
                {IsValueVisible:true,Value:3},
            ],
            Set1:[
                {IsValueVisible:true,Value:120},
                {IsValueVisible:true,Value:121},
                {IsValueVisible:true,Value:122},
                {IsValueVisible:true,Value:123},
            ],
            Set2:[
            ],
            Set3:[
            ],
        },
    },
    AllTriplets : {
        Name:'对对和',
        Value:2,
        Desc:'和牌时，有4个刻/杠。',
        Example:{
            OldHand:[
                {IsValueVisible:true,Value:40},
                {IsValueVisible:true,Value:41},
                {IsValueVisible:true,Value:42},
                {IsValueVisible:true,Value:80},
            ],
            NewHand:[
                {IsValueVisible:true,Value:81},
            ],
            Set0:[
                {IsValueVisible:true,Value:0},
                {IsValueVisible:true,Value:1},
                {IsValueVisible:true,Value:2},
            ],
            Set1:[
                {IsValueVisible:true,Value:60},
                {IsValueVisible:true,Value:61},
                {IsValueVisible:true,Value:62},
            ],
            Set2:[],
            Set3:[],
        },
    },
    FullFlush : {
        Name:'清一色',
        Value:2,
        Desc:'和牌时，所有牌都是万子/索子/筒子。',
        Example:{
            OldHand:[
                {IsValueVisible:true,Value:36},
                {IsValueVisible:true,Value:37},
                {IsValueVisible:true,Value:38},
                {IsValueVisible:true,Value:40},
                {IsValueVisible:true,Value:41},
                {IsValueVisible:true,Value:42},
                {IsValueVisible:true,Value:48},
            ],
            NewHand:[
                {IsValueVisible:true,Value:49},
            ],
            Set0:[
                {IsValueVisible:true,Value:50},
                {IsValueVisible:true,Value:52},
                {IsValueVisible:true,Value:56},
            ],
            Set1:[
                {IsValueVisible:true,Value:57},
                {IsValueVisible:true,Value:60},
                {IsValueVisible:true,Value:64},
            ],
            Set2:[
            ],
            Set3:[
            ],
        },
    },
    IdenticalSequencesII : {
        Name:'两般高',
        Value:2,
        Desc:'和牌时，有4个顺子，其中2个顺子一样，另外2个顺子也一样。不加计『一般高』。',
        Example:{
            OldHand:[
                {IsValueVisible:true,Value:4},
                {IsValueVisible:true,Value:8},
                {IsValueVisible:true,Value:12},
                {IsValueVisible:true,Value:68},
                {IsValueVisible:true,Value:72},
                {IsValueVisible:true,Value:76},
                {IsValueVisible:true,Value:80},
            ],
            NewHand:[
                {IsValueVisible:true,Value:69},
            ],
            Set0:[
                {IsValueVisible:true,Value:5},
                {IsValueVisible:true,Value:9},
                {IsValueVisible:true,Value:13},
            ],
            Set1:[
                {IsValueVisible:true,Value:73},
                {IsValueVisible:true,Value:77},
                {IsValueVisible:true,Value:81},
            ],
            Set2:[
            ],
            Set3:[
            ],
        },
    },
    Straight : {
        Name:'一气通贯',
        Value:2,
        Desc:'和牌时，有同种花色的123,456,789的顺子。',
        Example:{
            OldHand:[
                {IsValueVisible:true,Value:0},
                {IsValueVisible:true,Value:1},
                {IsValueVisible:true,Value:4},
                {IsValueVisible:true,Value:5},
                {IsValueVisible:true,Value:6},
                {IsValueVisible:true,Value:48},
                {IsValueVisible:true,Value:52},
                {IsValueVisible:true,Value:56},
                {IsValueVisible:true,Value:60},
                {IsValueVisible:true,Value:68},
            ],
            NewHand:[
                {IsValueVisible:true,Value:64},
            ],
            Set0:[
                {IsValueVisible:true,Value:36},
                {IsValueVisible:true,Value:40},
                {IsValueVisible:true,Value:44},
            ],
            Set1:[
            ],
            Set2:[
            ],
            Set3:[
            ],
        },
    },
    ThreeQuads : {
        Name:'三杠子',
        Value:3,
        Desc:'和牌时，有3个杠。',
        Example:{
            OldHand:[
                {IsValueVisible:true,Value:56},
                {IsValueVisible:true,Value:60},
                {IsValueVisible:true,Value:64},
                {IsValueVisible:true,Value:68},
            ],
            NewHand:[
                {IsValueVisible:true,Value:69},
            ],
            Set0:[
                {IsValueVisible:true,Value:0},
                {IsValueVisible:true,Value:1},
                {IsValueVisible:true,Value:2},
                {IsValueVisible:true,Value:3},
            ],
            Set1:[
                {IsValueVisible:true,Value:120},
                {IsValueVisible:true,Value:121},
                {IsValueVisible:true,Value:122},
                {IsValueVisible:true,Value:123},
            ],
            Set2:[
                {IsValueVisible:true,Value:40},
                {IsValueVisible:true,Value:41},
                {IsValueVisible:true,Value:42},
                {IsValueVisible:true,Value:43},
            ],
            Set3:[
            ],
        },
    },
    IdenticalSequencesIII : {
        Name:'一色三同顺',
        Value:3,
        Desc:'和牌时，有3个一样的顺子。不加计『一般高』。',
        Example:{
            OldHand:[
                {IsValueVisible:true,Value:4},
                {IsValueVisible:true,Value:8},
                {IsValueVisible:true,Value:12},
                {IsValueVisible:true,Value:68},
                {IsValueVisible:true,Value:72},
                {IsValueVisible:true,Value:76},
                {IsValueVisible:true,Value:80},
            ],
            NewHand:[
                {IsValueVisible:true,Value:69},
            ],
            Set0:[
                {IsValueVisible:true,Value:74},
                {IsValueVisible:true,Value:78},
                {IsValueVisible:true,Value:82},
            ],
            Set1:[
                {IsValueVisible:true,Value:73},
                {IsValueVisible:true,Value:77},
                {IsValueVisible:true,Value:81},
            ],
            Set2:[
            ],
            Set3:[
            ],
        },
    },
    AllHonors : {
        Name:'字一色',
        Value:3,
        Desc:'和牌时，所有手牌都是字牌（东/南/西/北/白/发/中）。',
        Example:{
            OldHand:[
                {IsValueVisible:true,Value:108},
                {IsValueVisible:true,Value:109},
                {IsValueVisible:true,Value:110},
                {IsValueVisible:true,Value:112},
                {IsValueVisible:true,Value:113},
                {IsValueVisible:true,Value:114},
                {IsValueVisible:true,Value:116},
            ],
            NewHand:[
                {IsValueVisible:true,Value:117},
            ],
            Set0:[
                {IsValueVisible:true,Value:124},
                {IsValueVisible:true,Value:125},
                {IsValueVisible:true,Value:126},
            ],
            Set1:[
                {IsValueVisible:true,Value:128},
                {IsValueVisible:true,Value:129},
                {IsValueVisible:true,Value:130},
            ],
            Set2:[
            ],
            Set3:[
            ],
        },
    },
    FourQuads : {
        Name:'四杠子',
        Value:4,
        Desc:'和牌时，有4个杠。注：此时一定满足对对和。',
        Example:{
            OldHand:[
                {IsValueVisible:true,Value:68},
            ],
            NewHand:[
                {IsValueVisible:true,Value:69},
            ],
            Set0:[
                {IsValueVisible:true,Value:0},
                {IsValueVisible:true,Value:1},
                {IsValueVisible:true,Value:2},
                {IsValueVisible:true,Value:3},
            ],
            Set1:[
                {IsValueVisible:true,Value:120},
                {IsValueVisible:true,Value:121},
                {IsValueVisible:true,Value:122},
                {IsValueVisible:true,Value:123},
            ],
            Set2:[
                {IsValueVisible:true,Value:40},
                {IsValueVisible:true,Value:41},
                {IsValueVisible:true,Value:42},
                {IsValueVisible:true,Value:43},
            ],
            Set3:[
                {IsValueVisible:true,Value:61},
                {IsValueVisible:true,Value:60},
                {IsValueVisible:true,Value:62},
                {IsValueVisible:true,Value:63},
            ],
        },
    },
    IdenticalSequencesIV : {
        Name:'一色四同顺',
        Value:6,
        Desc:'和牌时，有4个一样的顺子。不加计『一般高』『两般高』『一色三同顺』。',
        Example:{
            OldHand:[
                {IsValueVisible:true,Value:0},
                {IsValueVisible:true,Value:72},
                {IsValueVisible:true,Value:75},
                {IsValueVisible:true,Value:76},
                {IsValueVisible:true,Value:79},
                {IsValueVisible:true,Value:80},
                {IsValueVisible:true,Value:83},
            ],
            NewHand:[
                {IsValueVisible:true,Value:1},
            ],
            Set0:[
                {IsValueVisible:true,Value:74},
                {IsValueVisible:true,Value:78},
                {IsValueVisible:true,Value:82},
            ],
            Set1:[
                {IsValueVisible:true,Value:73},
                {IsValueVisible:true,Value:77},
                {IsValueVisible:true,Value:81},
            ],
            Set2:[
            ],
            Set3:[
            ],
        },
    },
};
