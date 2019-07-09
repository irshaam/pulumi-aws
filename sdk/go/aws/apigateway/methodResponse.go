// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package apigateway

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides an HTTP Method Response for an API Gateway Resource.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_method_response.html.markdown.
type MethodResponse struct {
	s *pulumi.ResourceState
}

// NewMethodResponse registers a new resource with the given unique name, arguments, and options.
func NewMethodResponse(ctx *pulumi.Context,
	name string, args *MethodResponseArgs, opts ...pulumi.ResourceOpt) (*MethodResponse, error) {
	if args == nil || args.HttpMethod == nil {
		return nil, errors.New("missing required argument 'HttpMethod'")
	}
	if args == nil || args.ResourceId == nil {
		return nil, errors.New("missing required argument 'ResourceId'")
	}
	if args == nil || args.RestApi == nil {
		return nil, errors.New("missing required argument 'RestApi'")
	}
	if args == nil || args.StatusCode == nil {
		return nil, errors.New("missing required argument 'StatusCode'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["httpMethod"] = nil
		inputs["resourceId"] = nil
		inputs["responseModels"] = nil
		inputs["responseParameters"] = nil
		inputs["restApi"] = nil
		inputs["statusCode"] = nil
	} else {
		inputs["httpMethod"] = args.HttpMethod
		inputs["resourceId"] = args.ResourceId
		inputs["responseModels"] = args.ResponseModels
		inputs["responseParameters"] = args.ResponseParameters
		inputs["restApi"] = args.RestApi
		inputs["statusCode"] = args.StatusCode
	}
	s, err := ctx.RegisterResource("aws:apigateway/methodResponse:MethodResponse", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &MethodResponse{s: s}, nil
}

// GetMethodResponse gets an existing MethodResponse resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetMethodResponse(ctx *pulumi.Context,
	name string, id pulumi.ID, state *MethodResponseState, opts ...pulumi.ResourceOpt) (*MethodResponse, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["httpMethod"] = state.HttpMethod
		inputs["resourceId"] = state.ResourceId
		inputs["responseModels"] = state.ResponseModels
		inputs["responseParameters"] = state.ResponseParameters
		inputs["restApi"] = state.RestApi
		inputs["statusCode"] = state.StatusCode
	}
	s, err := ctx.ReadResource("aws:apigateway/methodResponse:MethodResponse", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &MethodResponse{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *MethodResponse) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *MethodResponse) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)
func (r *MethodResponse) HttpMethod() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["httpMethod"])
}

// The API resource ID
func (r *MethodResponse) ResourceId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["resourceId"])
}

// A map of the API models used for the response's content type
func (r *MethodResponse) ResponseModels() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["responseModels"])
}

// A map of response parameters that can be sent to the caller.
// For example: `response_parameters = { "method.response.header.X-Some-Header" = true }`
// would define that the header `X-Some-Header` can be provided on the response.
func (r *MethodResponse) ResponseParameters() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["responseParameters"])
}

// The ID of the associated REST API
func (r *MethodResponse) RestApi() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["restApi"])
}

// The HTTP status code
func (r *MethodResponse) StatusCode() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["statusCode"])
}

// Input properties used for looking up and filtering MethodResponse resources.
type MethodResponseState struct {
	// The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)
	HttpMethod interface{}
	// The API resource ID
	ResourceId interface{}
	// A map of the API models used for the response's content type
	ResponseModels interface{}
	// A map of response parameters that can be sent to the caller.
	// For example: `response_parameters = { "method.response.header.X-Some-Header" = true }`
	// would define that the header `X-Some-Header` can be provided on the response.
	ResponseParameters interface{}
	// The ID of the associated REST API
	RestApi interface{}
	// The HTTP status code
	StatusCode interface{}
}

// The set of arguments for constructing a MethodResponse resource.
type MethodResponseArgs struct {
	// The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)
	HttpMethod interface{}
	// The API resource ID
	ResourceId interface{}
	// A map of the API models used for the response's content type
	ResponseModels interface{}
	// A map of response parameters that can be sent to the caller.
	// For example: `response_parameters = { "method.response.header.X-Some-Header" = true }`
	// would define that the header `X-Some-Header` can be provided on the response.
	ResponseParameters interface{}
	// The ID of the associated REST API
	RestApi interface{}
	// The HTTP status code
	StatusCode interface{}
}
