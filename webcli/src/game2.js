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
    var setCount = Utils.randInt(0, 5)
    return {
        River       : getRandomTileViewList(Math.floor(Math.random()*17)+5),
        Mountain    : getRandomMountain(),
        // OldHand     : getRandomTileViewList((4-setCount)*3+1),
        // NewHand     : getRandomTileViewList(1),
        OldHand     : [
            {IsValueVisible : true, Value : 0,},
            {IsValueVisible : true, Value : 1,},
            {IsValueVisible : true, Value : 3,},
            {IsValueVisible : true, Value : 4,},
            {IsValueVisible : true, Value : 8,},
            {IsValueVisible : true, Value : 12,},
            {IsValueVisible : true, Value : 16,},
            {IsValueVisible : true, Value : 20,},
            {IsValueVisible : true, Value : 24,},
            {IsValueVisible : true, Value : 28,},
            {IsValueVisible : true, Value : 32,},
            {IsValueVisible : true, Value : 33,},
            {IsValueVisible : true, Value : 34,},
        ],
        NewHand     : [
            {IsValueVisible : true, Value : 16,},
        ],
        BuiltSets   : [...Array(setCount).keys()].map(getRandomSet),
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
            Main: 'PlayerXHandleDraw',
            X: 0,
        },
        PlayerNames : [
            'Player0',
            'Player11111111111111111111111111111111111',
        ],
    }

    return obj
}

export function getRoleFromArea(area) {
    switch (area) {
        case 'Self': return 0
        case 'Oppo': return 1
        default: return undefined
    }
}

export function getActionPayload(userAction) {
    switch (userAction.Type) {
        case 'OldHandClick':
            return {
                Type : 'DiscardFromHand',
                'FromOldHand': true,
                'Index': userAction.Idx,
            }
        case 'NewHandClick':
            return {
                Type : 'DiscardFromHand',
                'FromOldHand': false,
                'Index': userAction.Idx,
            }
        case 'SetClick':
            return {
                Type : 'Kan2',
            }
        case 'PassClick':
            return {
                Type : 'Pass',
            }
        case 'PonClick':
            return {
                Type : 'Pon',
            }
        case 'WinClick':
            return {
                Type : 'Win',
            }
        case 'Chi0Click':
            return {
                Type : 'Chi',
                ChiMode : '_YZ',
            }
        case 'Chi1Click':
            return {
                Type : 'Chi',
                ChiMode : 'X_Z',
            }
        case 'Chi2Click':
            return {
                Type : 'Chi',
                ChiMode : 'XY_',
            }
        case 'KanOptionClick':
            return {
                Type : 'Kan',
                Value: userAction.KanOption,
            }
    }
}

export function getRoleBySeatID(seatID) {
    return (seatID == 0) ? 0 : (seatID == 2) ? 1 : undefined
}

export function getTidsFromViews() {
    //TODO
}

export function getTidFromTileView(view) {
    if (view && view.IsValueVisible) {
        return view.Value
    }
    return undefined
}

export function getTileGroupID(tid) {
    return Math.floor(tid/4)
}

export function getKanOptions(gameStateView, role) {
    var seatID = 0 //TODO
    var oldHandTids = getTidsFromViews(gameStateView.AreaViews[seatID].OldHand)
    var newHandTids = getTidsFromViews(gameStateView.AreaViews[seatID].NewHand)
    var handTids = oldHandTids.concat(newHandTids)
    handTids.sort()
    if (gameStateView.State.Main == 'PlayerXHandleDraw' && gameStateView.State.X == role) {
        for (var tgid=0; tgid<34; tgid++) {
            if (handTids.filter(tid => (getTileGroupID(tid)==tgid)).length == 4) {
                //TODO
            }
        }
    }
    return []
}

export function getSeatByRole(role) {
    return role*2
}

export function has3XSolutions(tgids) {
    if (tgids.length==0) return true
    if (tgids.length%3!=0) return false

    var minfinder = function(accumulated, toProcess){
        return Math.min(accumulated, toProcess)
    }

    var tgid0 = tgids.reduce(minfinder, 999)
    var tgid0Count = tgids.filter(tgid => tgid==tgid0).length

    if (tgid0>=0 && tgid0<=6 || tgid0>=9 && tgid0<=15 || tgid0>=18 && tgid0<=24) {
        var tgid1Count = tgids.filter(tgid => tgid==tgid0+1).length
        var tgid2Count = tgids.filter(tgid => tgid==tgid0+2).length
        if (tgid1Count>=1 && tgid2Count>=1) {
            var tmpTgids = tgids.slice(0)
            tmpTgids.splice(tmpTgids.indexOf(tgid0),1)
            tmpTgids.splice(tmpTgids.indexOf(tgid0+1),1)
            tmpTgids.splice(tmpTgids.indexOf(tgid0+2),1)
            if (has3XSolutions(tmpTgids)) return true
        }
    }

    if (tgid0Count>=3) {
        var tmqTgids = tgids.slice(0)
        tmqTgids.splice(tmqTgids.indexOf(tgid0),1)
        tmqTgids.splice(tmqTgids.indexOf(tgid0),1)
        tmqTgids.splice(tmqTgids.indexOf(tgid0),1)
        if (has3XSolutions(tmqTgids)) return true
    }

    return false
}

export function has3Xn2Solutions(tgids) {
    window.console.log('Starting has3Xn2Solutions.')
    window.console.log(tgids)
    if (tgids.length%3!=2) {
        return false
    }
    window.console.log('Initing counter.')
    var tg2c = Array(34).fill(0)
    window.console.log(tg2c)
    for (const x of tgids) tg2c[x]++
    window.console.log(tg2c)
    for (var tgid=0; tgid<34; tgid++) {
        if (tg2c[tgid]>=2) {
            var tmpTgids = tgids.slice(0)
            tmpTgids.splice(tmpTgids.indexOf(tgid), 1)
            tmpTgids.splice(tmpTgids.indexOf(tgid), 1)
            window.console.log('Got a pair. Remaining:')
            window.console.log(tmpTgids)
            if (has3XSolutions(tmpTgids)) {
                return true
            }
        }
    }

    return false
}

export function getTsumoActions(gameStateView, role) {
    window.console.log(gameStateView, role)
    var seat = getSeatByRole(role)
    var oldTids = gameStateView.AreaViews[seat].OldHand.map(v => getTidFromTileView(v)).filter(v => v!=undefined)
    var newTids = gameStateView.AreaViews[seat].NewHand.map(v => getTidFromTileView(v)).filter(v => v!=undefined)
    var tids = oldTids.concat(newTids).sort()
    var tgids = tids.map(tid => getTileGroupID(tid))
    return has3Xn2Solutions(tgids) ? [{Type:'Tsumo'}] : []
}

export function getKan0Actions(gameStateView, role) {
    window.console.log(gameStateView, role)
    return [] //TODO
}

export function getKan2Actions(gameStateView, role) {
    window.console.log(gameStateView, role)
    return [] //TODO
}

export function getAction(gameStateView, role) {
    if (gameStateView.State.Main == 'PlayerXHandleDraw' && gameStateView.State.X == role) {
        var result = []
        result = result.concat(getTsumoActions(gameStateView, role))
        result = result.concat(getKan0Actions(gameStateView, role))
        result = result.concat(getKan2Actions(gameStateView, role))
        result = result.concat(gameStateView.AreaViews[role].NewHand.map(v => getTidFromTileView(v)).filter(v => v!=undefined).map(tid => ({Type:'Discard', Value:tid})))
        result = result.concat(gameStateView.AreaViews[role].OldHand.map(v => getTidFromTileView(v)).filter(v => v!=undefined).map(tid => ({Type:'Discard', Value:tid})))
        return result
    }
    return [
        {
            'Type':'Tsumo',
            'Value':[
                [0,0,0,],
                [10,10,10,],
                [20,20,20,],
                [30,30,30,],
                [40,40],
            ],
        },
        {
            'Type':'Kan',
            'Value':[0,0,0,0],
        },
    ]
}
