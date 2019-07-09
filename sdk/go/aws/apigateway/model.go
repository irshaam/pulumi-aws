// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package apigateway

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a Model for a API Gateway.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_model.html.markdown.
type Model struct {
	s *pulumi.ResourceState
}

// NewModel registers a new resource with the given unique name, arguments, and options.
func NewModel(ctx *pulumi.Context,
	name string, args *ModelArgs, opts ...pulumi.ResourceOpt) (*Model, error) {
	if args == nil || args.ContentType == nil {
		return nil, errors.New("missing required argument 'ContentType'")
	}
	if args == nil || args.RestApi == nil {
		return nil, errors.New("missing required argument 'RestApi'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["contentType"] = nil
		inputs["description"] = nil
		inputs["name"] = nil
		inputs["restApi"] = nil
		inputs["schema"] = nil
	} else {
		inputs["contentType"] = args.ContentType
		inputs["description"] = args.Description
		inputs["name"] = args.Name
		inputs["restApi"] = args.RestApi
		inputs["schema"] = args.Schema
	}
	s, err := ctx.RegisterResource("aws:apigateway/model:Model", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Model{s: s}, nil
}

// GetModel gets an existing Model resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetModel(ctx *pulumi.Context,
	name string, id pulumi.ID, state *ModelState, opts ...pulumi.ResourceOpt) (*Model, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["contentType"] = state.ContentType
		inputs["description"] = state.Description
		inputs["name"] = state.Name
		inputs["restApi"] = state.RestApi
		inputs["schema"] = state.Schema
	}
	s, err := ctx.ReadResource("aws:apigateway/model:Model", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Model{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Model) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Model) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The content type of the model
func (r *Model) ContentType() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["contentType"])
}

// The description of the model
func (r *Model) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

// The name of the model
func (r *Model) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The ID of the associated REST API
func (r *Model) RestApi() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["restApi"])
}

// The schema of the model in a JSON form
func (r *Model) Schema() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["schema"])
}

// Input properties used for looking up and filtering Model resources.
type ModelState struct {
	// The content type of the model
	ContentType interface{}
	// The description of the model
	Description interface{}
	// The name of the model
	Name interface{}
	// The ID of the associated REST API
	RestApi interface{}
	// The schema of the model in a JSON form
	Schema interface{}
}

// The set of arguments for constructing a Model resource.
type ModelArgs struct {
	// The content type of the model
	ContentType interface{}
	// The description of the model
	Description interface{}
	// The name of the model
	Name interface{}
	// The ID of the associated REST API
	RestApi interface{}
	// The schema of the model in a JSON form
	Schema interface{}
}
