package com.coul.aliyun;

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

	public static void main(String[] args) {
		stopInstance();
	}

	private static void createInstanceResponse() {
		// 初始化
		DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou",
				"LTAIwtHOAIIRbgWJ", "qH4pNNH5yYatzMgcxKQBCGJu5lei6e");
		IAcsClient client = new DefaultAcsClient(profile);

		// 设置参数
		CreateInstanceRequest createInstance = new CreateInstanceRequest();
		createInstance.setInstanceType("ecs.n4.small");
		createInstance.setImageId("centos_7_02_64_20G_alibase_20170818.vhd");
		createInstance.setRegionId("cn-shanghai");
		createInstance.setInstanceChargeType("PostPaid");

		// 发起请求
		try {
			CreateInstanceResponse response = client
					.getAcsResponse(createInstance);
			System.out.println(response.getRequestId());
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	private static void deleteInstance() {
		// 初始化
		DefaultProfile profile = DefaultProfile.getProfile("cn-shanghai",
				"LTAIwtHOAIIRbgWJ", "qH4pNNH5yYatzMgcxKQBCGJu5lei6e");
		IAcsClient client = new DefaultAcsClient(profile);

		// 设置参数
		DeleteInstanceRequest deleteInstance = new DeleteInstanceRequest();
		deleteInstance.setInstanceId("i-uf633n67cx27b12kytym");

		// 发起请求
		try {
			DeleteInstanceResponse response = client
					.getAcsResponse(deleteInstance);
			System.out.println(response.getRequestId());
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	private static void startInstance() {
		// 初始化
		DefaultProfile profile = DefaultProfile.getProfile("cn-shanghai",
				"LTAIwtHOAIIRbgWJ", "qH4pNNH5yYatzMgcxKQBCGJu5lei6e");
		IAcsClient client = new DefaultAcsClient(profile);

		// 设置参数
		StartInstanceRequest startInstance = new StartInstanceRequest();
		startInstance.setInstanceId("i-uf633n67cx27b12kytym");

		// 发起请求
		try {
			StartInstanceResponse response = client
					.getAcsResponse(startInstance);
			System.out.println(response.getRequestId());
		} catch (Exception e) {
			System.out.println(e.getMessage());
			e.printStackTrace();
		}
	}

	private static void stopInstance() {
		// 初始化
		DefaultProfile profile = DefaultProfile.getProfile("cn-shanghai",
				"LTAIwtHOAIIRbgWJ", "qH4pNNH5yYatzMgcxKQBCGJu5lei6e");
		IAcsClient client = new DefaultAcsClient(profile);

		// 设置参数
		StopInstanceRequest stopInstance = new StopInstanceRequest();
		stopInstance.setInstanceId("i-uf633n67cx27b12kytym");

		// 发起请求
		try {
			StopInstanceResponse response = client.getAcsResponse(stopInstance);
			
			System.out.println("RequestId:"+response.getRequestId());
		} catch (Exception e) {
			System.out.println(e.getMessage());
			e.printStackTrace();
		}
	}
	
	private static void describeInstanceTypes(){
		// 初始化
	    DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou", "<accessKeyId>","<accessSecret>");
	    IAcsClient client = new DefaultAcsClient(profile);
	  
	    //设置参数
	    DescribeInstanceTypesRequest describeInstanceTypes = new DescribeInstanceTypesRequest();
	    describeInstanceTypes.setInstanceTypeFamily("ecs.n4");
	  
	    // 发起请求
	    try {
	      DescribeInstanceTypesResponse response = client.getAcsResponse(describeInstanceTypes);
	    }catch (Exception e) {
	      e.printStackTrace();
	    }
	}
	

}
