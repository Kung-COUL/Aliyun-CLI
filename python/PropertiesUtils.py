import json
with open('properties.json') as json_data:
    data = json.load(json_data)

    def keyPairName():
        return data['KeyPairName']

    def accessKeyId():
        return data['AccessKeyId']

    def accessSecret():
        return data['AccessSecret']

    def regionId():
        return data['RegionId']

    def outputFormat():
        return data['OutputFormat']

    def instanceId():
        return data['InstanceId']

    def allocationId():
        return data['AllocationId']

    def diskId():
        return data['DiskId']
