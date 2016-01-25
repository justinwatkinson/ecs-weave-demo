# ecs-weave-demo
A demo environment using Ansible to deploy an Amazon ECS Cluster using a Weave Overlay Network

# Credit where credit is due
Lots of help/ideas from here:

- Docker install.sh:  https://get.docker.com/
- Weave script:  https://github.com/weaveworks/weave

# Disclaimer
This is just some random hacking and was meant for me to learn Ansible in the context of a project.  I make no guarantees for it's effectivenss in your environment, and you'll likely need to make changes yourself.

# Usage
## ECS with Weave
```
sudo ansible-playbook -i inventory.py ecs-ubuntu-weave.yaml --private-key ~/ec2-keypair.pem
```
## ECS only
```
sudo ansible-playbook -i inventory.py ecs-ubuntu.yaml --private-key ~/ec2-keypair.pem
```
# Assumptions
- The inventory.py assumes that the EC2 instances are tagged with the key of "role" and the value of "ecs-cluster".  You can change this to suit your needs, as the output is just the ipv4 addresses.
- The docker install.sh file is slightly modified to pass in the correct parameter for the version and be consumed from the install.sh.  I've had some success rolling back to 1.8 using this technique.  It's a little strange since the package repos don't necessarily handle everything top-to-bottom (as of this writing).
- The IAM role of the EC2 instance needs to have enough permissions to run the ecs-peers.py in the weave role.  Looks like describe_tags and describe_instances at a minimum.

# Required Software
- boto3 (python) on ansible host
