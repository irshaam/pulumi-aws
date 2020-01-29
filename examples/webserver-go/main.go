// Copyright 2016-2017, Pulumi Corporation.  All rights reserved.

package main

import (
	awsconfig "github.com/pulumi/pulumi-aws/sdk/go/aws/config"
	"github.com/pulumi/pulumi-aws/sdk/go/aws/ec2"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

const size = "t2.micro"

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		group, err := ec2.NewSecurityGroup(ctx, "web-secgrp-2", &ec2.SecurityGroupArgs{
			Description: pulumi.String("Enable HTTP access"),
			Ingress: ec2.SecurityGroupIngressArray{
				&ec2.SecurityGroupIngressArgs{
					Protocol: pulumi.String("tcp"),
					FromPort: pulumi.Int(80),
					ToPort: pulumi.Int(80),
					CidrBlocks: pulumi.StringArray{
						pulumi.String("0.0.0.0/0"),
					},
				},
			},
		})
		if err != nil {
			return err
		}

		server, err := ec2.NewInstance(ctx, "web-server-www", &ec2.InstanceArgs{
			InstanceType: pulumi.String(size),
			SecurityGroups: pulumi.StringArray{
				group.Name,
			},
			Ami: pulumi.String(getLinuxAMI(awsconfig.GetRegion(ctx), size)),
		})
		if err != nil {
			return err
		}

		ctx.Export("publicIp", server.PublicIp)
		ctx.Export("publicDns", server.PublicDns)
		return nil
	})
}
