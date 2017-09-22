package com.coul.aliyun;

import java.io.InputStream;
import java.util.Properties;
//properties������
public class PropertiesUtils {

	private static  Properties pps = null; 
//	private static  Enumeration enum1=null; 
	
	public PropertiesUtils() {
		// TODO Auto-generated constructor stub

	}
	//���key��ȡvalue����ȡproperties�ļ��Ĳ���ֻ��ִ��һ��
	public static String getPropertiesByKey(String key)  {
		if(null==pps){
			pps = new Properties();
			String propertiesFilename = "aliyun.properties";
			InputStream in = PropertiesUtils.class.getResourceAsStream(propertiesFilename);
			try{
				pps.load(in);
//				enum1 = pps.propertyNames();// �õ������ļ��ı���
			}catch(Exception ex){
				ex.printStackTrace();
			}
		}
		return pps.getProperty(key);
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		while (enum1.hasMoreElements()) {
//			String strKey = (String) enum1.nextElement();
//			String strValue = pps.getProperty(strKey);
//			System.out.println(strKey + "=" + strValue);
//		}
		System.out.println(getPropertiesByKey("Format"));
	}

}
