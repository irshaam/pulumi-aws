// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a resource to create a VPC NAT Gateway.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/nat_gateway.html.markdown.
type NatGateway struct {
	s *pulumi.ResourceState
}

// NewNatGateway registers a new resource with the given unique name, arguments, and options.
func NewNatGateway(ctx *pulumi.Context,
	name string, args *NatGatewayArgs, opts ...pulumi.ResourceOpt) (*NatGateway, error) {
	if args == nil || args.AllocationId == nil {
		return nil, errors.New("missing required argument 'AllocationId'")
	}
	if args == nil || args.SubnetId == nil {
		return nil, errors.New("missing required argument 'SubnetId'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["allocationId"] = nil
		inputs["subnetId"] = nil
		inputs["tags"] = nil
	} else {
		inputs["allocationId"] = args.AllocationId
		inputs["subnetId"] = args.SubnetId
		inputs["tags"] = args.Tags
	}
	inputs["networkInterfaceId"] = nil
	inputs["privateIp"] = nil
	inputs["publicIp"] = nil
	s, err := ctx.RegisterResource("aws:ec2/natGateway:NatGateway", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &NatGateway{s: s}, nil
}

// GetNatGateway gets an existing NatGateway resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNatGateway(ctx *pulumi.Context,
	name string, id pulumi.ID, state *NatGatewayState, opts ...pulumi.ResourceOpt) (*NatGateway, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["allocationId"] = state.AllocationId
		inputs["networkInterfaceId"] = state.NetworkInterfaceId
		inputs["privateIp"] = state.PrivateIp
		inputs["publicIp"] = state.PublicIp
		inputs["subnetId"] = state.SubnetId
		inputs["tags"] = state.Tags
	}
	s, err := ctx.ReadResource("aws:ec2/natGateway:NatGateway", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &NatGateway{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *NatGateway) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *NatGateway) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The Allocation ID of the Elastic IP address for the gateway.
func (r *NatGateway) AllocationId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["allocationId"])
}

// The ENI ID of the network interface created by the NAT gateway.
func (r *NatGateway) NetworkInterfaceId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["networkInterfaceId"])
}

// The private IP address of the NAT Gateway.
func (r *NatGateway) PrivateIp() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["privateIp"])
}

// The public IP address of the NAT Gateway.
func (r *NatGateway) PublicIp() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["publicIp"])
}

// The Subnet ID of the subnet in which to place the gateway.
func (r *NatGateway) SubnetId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["subnetId"])
}

// A mapping of tags to assign to the resource.
func (r *NatGateway) Tags() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["tags"])
}

// Input properties used for looking up and filtering NatGateway resources.
type NatGatewayState struct {
	// The Allocation ID of the Elastic IP address for the gateway.
	AllocationId interface{}
	// The ENI ID of the network interface created by the NAT gateway.
	NetworkInterfaceId interface{}
	// The private IP address of the NAT Gateway.
	PrivateIp interface{}
	// The public IP address of the NAT Gateway.
	PublicIp interface{}
	// The Subnet ID of the subnet in which to place the gateway.
	SubnetId interface{}
	// A mapping of tags to assign to the resource.
	Tags interface{}
}

// The set of arguments for constructing a NatGateway resource.
type NatGatewayArgs struct {
	// The Allocation ID of the Elastic IP address for the gateway.
	AllocationId interface{}
	// The Subnet ID of the subnet in which to place the gateway.
	SubnetId interface{}
	// A mapping of tags to assign to the resource.
	Tags interface{}
}
