export function getDimensions(width, height) {
    var ret = Object()
    ret.tileHeight = height / 10
    ret.tileWidth = width / 19
    ret.riverTop = 0
    ret.riverLeft = ret.tileWidth*6.5
    ret.MountainTop = ret.tileHeight*4
    ret.MountainLeft = 0
    ret.HandTop = ret.tileHeight*7
    ret.HandLeft = ret.tileWidth*2
    ret.SetTop = ret.tileHeight*9
    ret.SetWidth = ret.tileWidth*3+ret.tileHeight
    ret.SetHeight = ret.tileWidth*2
    return ret
}

var TileGroupChars = ['🀇','🀈','🀉','🀊','🀋','🀌','🀍','🀎','🀏','🀐','🀑','🀒','🀓','🀔','🀕','🀖','🀗','🀘','🀙','🀚','🀛','🀜','🀝','🀞','🀟','🀠','🀡','🀀','🀁','🀂','🀃','🀆','🀅','🀄']
var SeatChars = ['東','南','西','北']

function getUCharByTid(tid) {
    var gid = Math.floor(tid/4)
    return TileGroupChars[gid]
}

function getTidListStr(tids) {
    return tids.map(tid => getUCharByTid(tid)).join('')
}

export function getSeatChar(seat){
    return SeatChars[seat]
}
export function getTileViewChar(tileView) {
    if (tileView) {
        if (tileView.IsValueVisible) {
            return getUCharByTid(tileView.Value)
        } else {
            return '🀫'
        }
    } else {
        return undefined;
    }
}

export function getActionUIData(action) {
    switch (action.Type) {
        case 'Draw':
            return {
                Type: 'Pass',
                Data: action,
            }
        case 'Discard':
            switch (action.Source) {
                case 'NewHand':
                    return {
                        Type: 'Discard New',
                        Value: getUCharByTid(action.Value),
                        Data: action,
                    }
                case 'OldHand':
                    return {
                        Type: 'Discard Old',
                        Value: getUCharByTid(action.Value),
                        Data: action,
                    }
                default:
                    return undefined
            }
        case 'Tsumo':
            return {
                Type: 'Tsumo',
                Value: action.Value.map(tids => getTidListStr(tids)).join(' '),
                Data: action,
            }
        case 'Ron':
            return {
                Type: 'Ron',
                Value: action.Value.map(tids => getTidListStr(tids)).join(' '),
                Data: action,
            }
        case 'Chi':
            return {
                Type: 'Chi',
                Value: action.Value.map(tid => getUCharByTid(tid)).join(''),
                Data: action,
            }
        case 'Pon':
            return {
                Type: 'Pon',
                Value: action.Value.map(tid => getUCharByTid(tid)).join(''),
                Data: action,
            }
        case 'Kan0':
            return {
                Type: 'Kan',
                Value: action.Value.map(tid => getUCharByTid(tid)).join(''),
                Data: action,
            }
        case 'Kan1':
            return {
                Type: 'Kan',
                Value: action.Value.map(tid => getUCharByTid(tid)).join(''),
                Data: action,
            }
        case 'Kan2':
            return {
                Type: 'Kan+',
                Value: action.Value.map(tid => getUCharByTid(tid)).join(''),
                Data: action,
            }
        default:
            return undefined
    }
}
