
const makeCounter = () => {
    let count = 0

    return (function () {
        return {
            increament: () => {
                count+=1
                return count
            },
            decreament: () => {
                count-=1
                return count
            }
        }
    })()
}

const counter = makeCounter()

console.log('increament', counter.increament())

console.log('increament', counter.increament())

console.log('decreament', counter.decreament())

console.log('increament', counter.increament())

console.log('decreament', counter.decreament())

console.log('increament', counter.increament())

console.log('increament', counter.increament())

console.log('increament', counter.increament())