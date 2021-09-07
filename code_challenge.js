var crypto = require('crypto')


module.exports = function code_challenge(text){
    
    async function sha256(text,padding){
        const buffer = new TextEncoder().encode(text)

        const hash = crypto.subtle.digest('SHA-256',buffer)
        
        const hexstr = hash.map( b => toString(16).padStart(2))
        
        return hexstr 
    }

    

    

    return Buffer.from(text.toString('base64'))
}




