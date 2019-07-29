import json
jsonData = {"queryType": 0, "accountNo": "1101040160000484013", "inOutFlag": "2",
					"amountLowerLmt": "", "amountUpperLmt": "", "queryBeginDate": "20181218",
					"queryEndDate": "20181218", "turnPageBeginPos": 1, "turnPageShowNum": "99999", "pageFlag": "1",
					"flag": "0", "businessCode": "001002", "anotherAccountNo": "", "sortType": "0"}
					
print(json.dumps(jsonData))