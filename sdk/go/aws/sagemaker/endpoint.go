// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sagemaker

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a SageMaker Endpoint resource.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sagemaker_endpoint.html.markdown.
type Endpoint struct {
	s *pulumi.ResourceState
}

// NewEndpoint registers a new resource with the given unique name, arguments, and options.
func NewEndpoint(ctx *pulumi.Context,
	name string, args *EndpointArgs, opts ...pulumi.ResourceOpt) (*Endpoint, error) {
	if args == nil || args.EndpointConfigName == nil {
		return nil, errors.New("missing required argument 'EndpointConfigName'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["endpointConfigName"] = nil
		inputs["name"] = nil
		inputs["tags"] = nil
	} else {
		inputs["endpointConfigName"] = args.EndpointConfigName
		inputs["name"] = args.Name
		inputs["tags"] = args.Tags
	}
	inputs["arn"] = nil
	s, err := ctx.RegisterResource("aws:sagemaker/endpoint:Endpoint", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Endpoint{s: s}, nil
}

// GetEndpoint gets an existing Endpoint resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEndpoint(ctx *pulumi.Context,
	name string, id pulumi.ID, state *EndpointState, opts ...pulumi.ResourceOpt) (*Endpoint, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["arn"] = state.Arn
		inputs["endpointConfigName"] = state.EndpointConfigName
		inputs["name"] = state.Name
		inputs["tags"] = state.Tags
	}
	s, err := ctx.ReadResource("aws:sagemaker/endpoint:Endpoint", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Endpoint{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Endpoint) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Endpoint) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The Amazon Resource Name (ARN) assigned by AWS to this endpoint.
func (r *Endpoint) Arn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["arn"])
}

// The name of the endpoint configuration to use.
func (r *Endpoint) EndpointConfigName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["endpointConfigName"])
}

// The name of the endpoint.
func (r *Endpoint) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// A mapping of tags to assign to the resource.
func (r *Endpoint) Tags() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["tags"])
}

// Input properties used for looking up and filtering Endpoint resources.
type EndpointState struct {
	// The Amazon Resource Name (ARN) assigned by AWS to this endpoint.
	Arn interface{}
	// The name of the endpoint configuration to use.
	EndpointConfigName interface{}
	// The name of the endpoint.
	Name interface{}
	// A mapping of tags to assign to the resource.
	Tags interface{}
}

// The set of arguments for constructing a Endpoint resource.
type EndpointArgs struct {
	// The name of the endpoint configuration to use.
	EndpointConfigName interface{}
	// The name of the endpoint.
	Name interface{}
	// A mapping of tags to assign to the resource.
	Tags interface{}
}
