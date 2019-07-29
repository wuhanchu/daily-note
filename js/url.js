/**
 * get the url anchor
 * @param url
 * @returns {string}
 */
const getUrlAnchor = (url)=>{
	const index1 = url.indexOf("#")
	const index2 = url.indexOf("?")
	if(index2 && index1 < index2){
		return url.substring(index1+1,index2)
	}else{
		return url.substring(index1+1)
	}
}

var getUrlParam = (url,name) => {
		var reg = new RegExp("(/?|&)" + name + "=([^&#/?]*)(&|#|/?|$)", "i");
		var r = url.substr(1).match(reg);
		if (r != null) return unescape(r[2]);
		return null;
	}
console.log('getUrlParam',getUrlParam('http://localhost:8080/?expires_in=7200&access_token=3531313133443841354534257F0C1EC2DB13F0E2714C3ADB8B2F?/evidence?sign=Y2lkcmo4Q2lDSnRVd1ZYNnpmSnNpNm9RdHlQVzNXaW5xdVhmUUJPTHVJdXZySnQ2aDlmcEtxSjZOd1BGNXFmYW5FTnlYbFpWQnRFcWcvQnlqN0ZCUTlaTzhraTVRUUN6V0l3cVFhdWYvTXlPOEsvTjltZE4vdE10czZBT0puTHM4QmJlQ0ZUbEVFMlA0M01XQVZXNzdNN1VvcDU3aWZuYnFxSnFzbnIydVAwPQ==','access_token'))
console.log('anchor',getUrlAnchor('http://localhost:8000/#/dashboard?_k=a6f1k7'))