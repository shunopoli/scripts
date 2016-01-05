import boto;
ec2=boto.connect_ec2()
instances= ec2.get_only_instances()
for instance in instances:
      print instance.tags['Name'] , " is ", instance.state
