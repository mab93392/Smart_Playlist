const char_bank = ['a','b','v','x','z','s','d','f','g','h','j','k','l','q','w','e','r','t','y','u','i','o','p','~','1','2','3','4','5','6','7','8','9','%','Q','W','E','R','T','Y','U','I','O','P','-','_','A','S','D','F','G','H','J','K','L']


module.exports = function rand_int_(){
    
    let out = ''

    for(let i = 0; i < char_bank.length * 2; i++){
        let deg = Math.round(Math.random() * char_bank.length - 1)
        out += char_bank[deg]
        
    }

    return out
}


