import org.json.simple.JSONObject;

public class Json {  
	public static void main(String[] args) throws Exception { 
		HashMap<String,String> map = new HashMap<String,String>();
			map.put("姓名", "张三");
			map.put("年龄","18");
			map.put("学号","10");
			JSONObject json = new JSONObject();
			json = JSONObject.fromObject(map);
			System.out.println(json);
	}
}