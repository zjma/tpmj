import { expect } from "chai"
import * as Game2Utils from "../src/game2.js"

describe('Game2Utils', function(){
    describe('function get3Xn2Solutions', function(){
        it('should return 1 solution for 334455mEE', function(){
            expect(Game2Utils.get3Xn2Solutions([2,2,3,3,4,4,27,27]))
            .to.be.an('Array')
            .that.deep.have.members([[[2,3,4],[2,3,4],[27,27]]])
        })
        it('should return 1 solution for 11s', () => {
            expect(Game2Utils.get3Xn2Solutions([9,9]))
            .to.be.an('Array')
            .that.deep.have.members([[[9,9]]])
        })
        it('should return 2 solutions for 33445566m', () => {
            expect(Game2Utils.get3Xn2Solutions([2,2,3,3,4,4,5,5]))
            .to.be.an('Array')
            .that.deep.have.members([
                [[2,3,4],[2,3,4],[5,5]],
                [[3,4,5],[3,4,5],[2,2]],
            ])
        })
        it('should return 0 solutions for 6789m1s', ()=>{
            expect(Game2Utils.get3Xn2Solutions([5,6,7,8,9]))
            .to.be.an('Array')
            .that.deep.have.members([])
        })
        it('should return 0 solutions for empty hand', ()=>{
            expect(Game2Utils.get3Xn2Solutions([]))
            .to.be.an('Array')
            .that.deep.have.members([])
        })
        it('should return 3 solutions for 22223333444455m', ()=>{
            expect(Game2Utils.get3Xn2Solutions([1,1,1,1,2,2,2,2,3,3,3,3,4,4]))
            .to.be.an('Array')
            .that.deep.have.members([
                [[1,1,1],[1,2,3],[2,2,2],[3,3,3],[4,4]],
                [[1,2,3],[1,2,3],[1,2,3],[1,2,3],[4,4]],
                [[1,2,3],[1,2,3],[2,3,4],[2,3,4],[1,1]],
            ])
        })
        it('should return 3 solutions for 44455566677m', ()=>{
            expect(Game2Utils.get3Xn2Solutions([3,3,3,4,4,4,5,5,5,6,6]))
            .to.be.an('Array')
            .that.deep.have.members([
                [[3,3,3],[4,4,4],[5,5,5],[6,6]],
                [[3,4,5],[3,4,5],[3,4,5],[6,6]],
                [[3,4,5],[4,5,6],[4,5,6],[3,3]],
            ])
        })
        it('should return 1 solution for 888999m11122s', ()=>{
            expect(Game2Utils.get3Xn2Solutions([7,7,7,8,8,8,9,9,9,10,10]))
            .to.be.an('Array')
            .that.deep.have.members([
                [[7,7,7],[8,8,8],[9,9,9],[10,10]],
            ])
        })
        it('should return 1 solution for 888999s11122p', ()=>{
            expect(Game2Utils.get3Xn2Solutions([16,16,16,17,17,17,18,18,18,19,19]))
            .to.be.an('Array')
            .that.deep.have.members([
                [[16,16,16],[17,17,17],[18,18,18],[19,19]],
            ])
        })
        it('should return 1 solution for 888999pEEESS', ()=>{
            expect(Game2Utils.get3Xn2Solutions([16,16,16,17,17,17,18,18,18,19,19]))
            .to.be.an('Array')
            .that.deep.have.members([
                [[16,16,16],[17,17,17],[18,18,18],[19,19]],
            ])
        })
        it('should return 0 solutions for ESWNN', ()=>{
            expect(Game2Utils.get3Xn2Solutions([27,28,29,30,30]))
            .to.be.an('Array')
            .that.deep.have.members([])
        })
        it('should return 1 solution for NNwwwgggrrr', ()=>{
            expect(Game2Utils.get3Xn2Solutions([30,30,31,31,31,32,32,32,33,33,33]))
            .to.be.an('Array')
            .that.deep.have.members([
                [[31,31,31],[32,32,32],[33,33,33],[30,30]],
            ])
        })
        it('should fail', ()=>{
            expect('asb').to.be.an('Array')
        })
    })
})
