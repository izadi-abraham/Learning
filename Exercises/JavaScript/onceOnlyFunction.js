
const once = (fn) => {
    let called = false
    let result;
    
    return (...args) => {
        if(!called) {
            result = fn.apply(this, args)
            called = true
        }

        return result
    }
}


const init = once(() => console.log('Initialized'))

init()
init()
init()
