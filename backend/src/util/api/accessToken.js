var CryptoJS = require('crypto-js');

const bsp_organization = "test-drive-d2525f33ae1741398399d";
const bsp_site_id = "34f1bad383af4825a242554708c31585";
const bsp_shared_key = "8a4914a9f08b4a45916012763aafe24a";
const bsp_secret_key = "9ccb738734ee4b2f92916abbb7547748";
const request = {};
request.url = process.argv[2];
request.method = process.argv[3];
request.headers = {};
request.headers['nep_organization'] = "test-drive-d2525f33ae1741398399d";


const convertVariables = function(templateContent) {
    const regexPattern = /({{(.*?)}})/g;
    let convertedContent = templateContent;
    let matchedVar = new RegExp(regexPattern).exec(convertedContent);
    while (matchedVar !== null) {
        const variableReplacement = matchedVar[1];
        const variableName = matchedVar[2];
        const variableValue = postman.getEnvironmentVariable(variableName) || postman.getGlobalVariable(variableName);
        convertedContent = convertedContent.replace(variableReplacement, variableValue);
        matchedVar = new RegExp(regexPattern).exec(convertedContent);
    }
    return convertedContent;
}
// Extracts the signable content from the request
const signableContent = function() {
    const requestPath = convertVariables(request.url.trim()).replace(/^https?:\/\/[^\/]+\//, '/');
    const params = [
        request.method,
        requestPath,
        "application/json",
        convertVariables(request.headers['nep-organization'])
    ];
    return params.filter(p => p && p.length > 0).join('\n');
}
// Generates a unique date-based signing key
const uniqueKey = function(date) {
    const nonce = date.toISOString().slice(0, 19) + '.000Z';
    return bsp_secret_key + nonce;
}
// Calculates the HMAC signature
const calculateSignature = function() {
    const date = new Date();
    //postman.setEnvironmentVariable('date', date.toGMTString());
    const key = uniqueKey(date);
    const sc = signableContent();
    const hmac = CryptoJS.HmacSHA512(sc, key);
    return CryptoJS.enc.Base64.stringify(hmac);
}
// Stores the generated HMAC signature under the access key
const signature = calculateSignature();
let bsp_access_key = `AccessKey ${bsp_shared_key}:${signature}`;
console.log(bsp_access_key);