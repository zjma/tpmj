import { expect } from "chai"
import * as Foo from "../src/foo.js"

describe("heyhey", () => {
    it("should say Hello guys!", () => {
        expect(Foo.getFoo()).to.equal(99)
    })
})
