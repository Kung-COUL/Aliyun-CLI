package com.coul.aliyun;

import java.io.FileInputStream;
import java.io.InputStream;
import java.util.Enumeration;
import java.util.Properties;

import com.aliyuncs.DefaultAcsClient;
import com.aliyuncs.IAcsClient;
import com.aliyuncs.ecs.model.v20140526.CreateInstanceRequest;
import com.aliyuncs.ecs.model.v20140526.CreateInstanceResponse;
import com.aliyuncs.ecs.model.v20140526.DeleteInstanceRequest;
import com.aliyuncs.ecs.model.v20140526.DeleteInstanceResponse;
import com.aliyuncs.ecs.model.v20140526.DescribeInstanceTypesRequest;
import com.aliyuncs.ecs.model.v20140526.DescribeInstanceTypesResponse;
import com.aliyuncs.ecs.model.v20140526.StartInstanceRequest;
import com.aliyuncs.ecs.model.v20140526.StartInstanceResponse;
import com.aliyuncs.ecs.model.v20140526.StopInstanceRequest;
import com.aliyuncs.ecs.model.v20140526.StopInstanceResponse;
import com.aliyuncs.profile.DefaultProfile;

public class EcsTest {

	public static void main(String[] args) throws Exception {
//		System.out.println(PropertiesUtils.getPropertiesByKey("Format"));
		startInstance();
		stopInstance();
	}

	private static IAcsClient getClient(){
		String accessKeyId = PropertiesUtils.getPropertiesByKey("AccessKeyId");
		String accessSecret = PropertiesUtils.getPropertiesByKey("Access_Key_Secret");
		String region = PropertiesUtils.getPropertiesByKey("Region");
		if(region==null)region = "cn-hangzhou";//Ĭ��ֵcn-hangzhou
		DefaultProfile profile = DefaultProfile.getProfile(region,
				accessKeyId, accessSecret);
		IAcsClient client = new DefaultAcsClient(profile);
		return client;
	}
	private static void createInstanceResponse() {
		CreateInstanceRequest createInstance = new CreateInstanceRequest();
		createInstance.setInstanceType("ecs.n4.small");
		createInstance.setImageId("centos_7_02_64_20G_alibase_20170818.vhd");
		createInstance.setRegionId("cn-shanghai");
		createInstance.setInstanceChargeType("PostPaid");

		try {
			CreateInstanceResponse response = getClient()
					.getAcsResponse(createInstance);
			System.out.println(response.getRequestId());
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	private static void deleteInstance() {
		DeleteInstanceRequest deleteInstance = new DeleteInstanceRequest();
		deleteInstance.setInstanceId("i-uf633n67cx27b12kytym");

		try {
			DeleteInstanceResponse response = getClient()
					.getAcsResponse(deleteInstance);
			System.out.println(response.getRequestId());
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	private static void startInstance() {
		StartInstanceRequest startInstance = new StartInstanceRequest();
		startInstance.setInstanceId("i-uf633n67cx27b12kytym");

		try {
			StartInstanceResponse response = getClient()
					.getAcsResponse(startInstance);
			System.out.println(response.getRequestId());
		} catch (Exception e) {
			System.out.println(e.getMessage());
			e.printStackTrace();
		}
	}

	private static void stopInstance() {
		StopInstanceRequest stopInstance = new StopInstanceRequest();
		stopInstance.setInstanceId("i-uf633n67cx27b12kytym");

		try {
			StopInstanceResponse response = getClient().getAcsResponse(stopInstance);

			System.out.println("RequestId:" + response.getRequestId());
		} catch (Exception e) {
			System.out.println(e.getMessage());
			e.printStackTrace();
		}
	}

	private static void describeInstanceTypes() {


		DescribeInstanceTypesRequest describeInstanceTypes = new DescribeInstanceTypesRequest();
		describeInstanceTypes.setInstanceTypeFamily("ecs.n4");

		try {
			DescribeInstanceTypesResponse response = getClient()
					.getAcsResponse(describeInstanceTypes);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

}
