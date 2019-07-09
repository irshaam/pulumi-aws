// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type VpcEndpointServiceAllowedPrinciple struct {
	s *pulumi.ResourceState
}

// NewVpcEndpointServiceAllowedPrinciple registers a new resource with the given unique name, arguments, and options.
func NewVpcEndpointServiceAllowedPrinciple(ctx *pulumi.Context,
	name string, args *VpcEndpointServiceAllowedPrincipleArgs, opts ...pulumi.ResourceOpt) (*VpcEndpointServiceAllowedPrinciple, error) {
	if args == nil || args.PrincipalArn == nil {
		return nil, errors.New("missing required argument 'PrincipalArn'")
	}
	if args == nil || args.VpcEndpointServiceId == nil {
		return nil, errors.New("missing required argument 'VpcEndpointServiceId'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["principalArn"] = nil
		inputs["vpcEndpointServiceId"] = nil
	} else {
		inputs["principalArn"] = args.PrincipalArn
		inputs["vpcEndpointServiceId"] = args.VpcEndpointServiceId
	}
	s, err := ctx.RegisterResource("aws:ec2/vpcEndpointServiceAllowedPrinciple:VpcEndpointServiceAllowedPrinciple", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &VpcEndpointServiceAllowedPrinciple{s: s}, nil
}

// GetVpcEndpointServiceAllowedPrinciple gets an existing VpcEndpointServiceAllowedPrinciple resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVpcEndpointServiceAllowedPrinciple(ctx *pulumi.Context,
	name string, id pulumi.ID, state *VpcEndpointServiceAllowedPrincipleState, opts ...pulumi.ResourceOpt) (*VpcEndpointServiceAllowedPrinciple, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["principalArn"] = state.PrincipalArn
		inputs["vpcEndpointServiceId"] = state.VpcEndpointServiceId
	}
	s, err := ctx.ReadResource("aws:ec2/vpcEndpointServiceAllowedPrinciple:VpcEndpointServiceAllowedPrinciple", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &VpcEndpointServiceAllowedPrinciple{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *VpcEndpointServiceAllowedPrinciple) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *VpcEndpointServiceAllowedPrinciple) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The ARN of the principal to allow permissions.
func (r *VpcEndpointServiceAllowedPrinciple) PrincipalArn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["principalArn"])
}

// The ID of the VPC endpoint service to allow permission.
func (r *VpcEndpointServiceAllowedPrinciple) VpcEndpointServiceId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["vpcEndpointServiceId"])
}

// Input properties used for looking up and filtering VpcEndpointServiceAllowedPrinciple resources.
type VpcEndpointServiceAllowedPrincipleState struct {
	// The ARN of the principal to allow permissions.
	PrincipalArn interface{}
	// The ID of the VPC endpoint service to allow permission.
	VpcEndpointServiceId interface{}
}

// The set of arguments for constructing a VpcEndpointServiceAllowedPrinciple resource.
type VpcEndpointServiceAllowedPrincipleArgs struct {
	// The ARN of the principal to allow permissions.
	PrincipalArn interface{}
	// The ID of the VPC endpoint service to allow permission.
	VpcEndpointServiceId interface{}
}
