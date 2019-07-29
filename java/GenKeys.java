import java.io.FileOutputStream;   
import java.security.KeyPair;   
import java.security.KeyPairGenerator;   
import java.security.SecureRandom;   
import java.util.Date;  
import java.util.Base64;

  
public class GenKeys {  
	public static void main(String[] args) throws Exception {  
		KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance("RSA");   
		keyPairGenerator.initialize(1024);  
		KeyPair keyPair = keyPairGenerator.genKeyPair();  
		String publicKeyFilename = "./publicKeyFile";  
		byte[] publicKeyBytes = keyPair.getPublic().getEncoded();  
		FileOutputStream fos = new FileOutputStream(publicKeyFilename);   
		fos.write(Base64.encodeBase64String(publicKeyBytes));   
		fos.close();  
		String privateKeyFilename = "./privateKeyFile";   
		byte[] privateKeyBytes = keyPair.getPrivate().getEncoded();  
		fos = new FileOutputStream(privateKeyFilename);   
		fos.write(privateKeyBytes);   
		fos.close();  
	}  
}  