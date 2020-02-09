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


function getUCharByTid(tid) {
    var gid = Math.floor(tid/4)
    return TileGroupChars[gid]
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
