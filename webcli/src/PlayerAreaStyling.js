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
        case 'Discard':
            return {
                Type: 'Discard',
                Value: getUCharByTid(action.Value)
            }
        case 'Tsumo':
            return {
                Type: 'Tsumo',
                Value: 'Tsumo',
            }
        default:
            return {
                Type: 'Unknown',
                Value: '🀇🀈🀉 🀇🀈🀉 🀇🀈🀉 🀇🀈🀉 🀐🀐',
            }
    }
}
