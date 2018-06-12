// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iam

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// -> **Note:** There is only a single account alias per AWS account.
// 
// Manages the account alias for the AWS Account.
type AccountAlias struct {
	s *pulumi.ResourceState
}

// NewAccountAlias registers a new resource with the given unique name, arguments, and options.
func NewAccountAlias(ctx *pulumi.Context,
	name string, args *AccountAliasArgs, opts ...pulumi.ResourceOpt) (*AccountAlias, error) {
	if args == nil || args.AccountAlias == nil {
		return nil, errors.New("missing required argument 'AccountAlias'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["accountAlias"] = nil
	} else {
		inputs["accountAlias"] = args.AccountAlias
	}
	s, err := ctx.RegisterResource("aws:iam/accountAlias:AccountAlias", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &AccountAlias{s: s}, nil
}

// GetAccountAlias gets an existing AccountAlias resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAccountAlias(ctx *pulumi.Context,
	name string, id pulumi.ID, state *AccountAliasState, opts ...pulumi.ResourceOpt) (*AccountAlias, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["accountAlias"] = state.AccountAlias
	}
	s, err := ctx.ReadResource("aws:iam/accountAlias:AccountAlias", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &AccountAlias{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *AccountAlias) URN() *pulumi.URNOutput {
	return r.s.URN
}

// ID is this resource's unique identifier assigned by its provider.
func (r *AccountAlias) ID() *pulumi.IDOutput {
	return r.s.ID
}

// The account alias
func (r *AccountAlias) AccountAlias() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["accountAlias"])
}

// Input properties used for looking up and filtering AccountAlias resources.
type AccountAliasState struct {
	// The account alias
	AccountAlias interface{}
}

// The set of arguments for constructing a AccountAlias resource.
type AccountAliasArgs struct {
	// The account alias
	AccountAlias interface{}
}