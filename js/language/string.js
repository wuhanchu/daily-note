var matches = "您好我是国盛证券见证工作人员工号是31506以下问题请回答是或否，您好！请问您是。".match(/\d+/g);
if (matches != null) {
	console.log('number',matches);
}