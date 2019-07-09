// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iam

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides an IAM role policy.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_role_policy.html.markdown.
type RolePolicy struct {
	s *pulumi.ResourceState
}

// NewRolePolicy registers a new resource with the given unique name, arguments, and options.
func NewRolePolicy(ctx *pulumi.Context,
	name string, args *RolePolicyArgs, opts ...pulumi.ResourceOpt) (*RolePolicy, error) {
	if args == nil || args.Policy == nil {
		return nil, errors.New("missing required argument 'Policy'")
	}
	if args == nil || args.Role == nil {
		return nil, errors.New("missing required argument 'Role'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["name"] = nil
		inputs["namePrefix"] = nil
		inputs["policy"] = nil
		inputs["role"] = nil
	} else {
		inputs["name"] = args.Name
		inputs["namePrefix"] = args.NamePrefix
		inputs["policy"] = args.Policy
		inputs["role"] = args.Role
	}
	s, err := ctx.RegisterResource("aws:iam/rolePolicy:RolePolicy", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &RolePolicy{s: s}, nil
}

// GetRolePolicy gets an existing RolePolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRolePolicy(ctx *pulumi.Context,
	name string, id pulumi.ID, state *RolePolicyState, opts ...pulumi.ResourceOpt) (*RolePolicy, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["name"] = state.Name
		inputs["namePrefix"] = state.NamePrefix
		inputs["policy"] = state.Policy
		inputs["role"] = state.Role
	}
	s, err := ctx.ReadResource("aws:iam/rolePolicy:RolePolicy", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &RolePolicy{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *RolePolicy) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *RolePolicy) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The name of the policy.
func (r *RolePolicy) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// Creates a unique name beginning with the specified
// prefix. Conflicts with `name`.
func (r *RolePolicy) NamePrefix() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["namePrefix"])
}

// The policy document attached to the role.
func (r *RolePolicy) Policy() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["policy"])
}

// The IAM role to attach to the policy.
func (r *RolePolicy) Role() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["role"])
}

// Input properties used for looking up and filtering RolePolicy resources.
type RolePolicyState struct {
	// The name of the policy.
	Name interface{}
	// Creates a unique name beginning with the specified
	// prefix. Conflicts with `name`.
	NamePrefix interface{}
	// The policy document attached to the role.
	Policy interface{}
	// The IAM role to attach to the policy.
	Role interface{}
}

// The set of arguments for constructing a RolePolicy resource.
type RolePolicyArgs struct {
	// The name of the policy.
	Name interface{}
	// Creates a unique name beginning with the specified
	// prefix. Conflicts with `name`.
	NamePrefix interface{}
	// The policy document attached to the role.
	Policy interface{}
	// The IAM role to attach to the policy.
	Role interface{}
}
