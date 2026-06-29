
const multiplier = (factor) => {
    return function (numberInput) {
        return numberInput * factor
    }
}


const double = multiplier(2)

console.log(double(5))