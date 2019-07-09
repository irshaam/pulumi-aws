// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package directconnect

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a Connection of Direct Connect.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dx_connection.html.markdown.
type Connection struct {
	s *pulumi.ResourceState
}

// NewConnection registers a new resource with the given unique name, arguments, and options.
func NewConnection(ctx *pulumi.Context,
	name string, args *ConnectionArgs, opts ...pulumi.ResourceOpt) (*Connection, error) {
	if args == nil || args.Bandwidth == nil {
		return nil, errors.New("missing required argument 'Bandwidth'")
	}
	if args == nil || args.Location == nil {
		return nil, errors.New("missing required argument 'Location'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["bandwidth"] = nil
		inputs["location"] = nil
		inputs["name"] = nil
		inputs["tags"] = nil
	} else {
		inputs["bandwidth"] = args.Bandwidth
		inputs["location"] = args.Location
		inputs["name"] = args.Name
		inputs["tags"] = args.Tags
	}
	inputs["arn"] = nil
	inputs["awsDevice"] = nil
	inputs["hasLogicalRedundancy"] = nil
	inputs["jumboFrameCapable"] = nil
	s, err := ctx.RegisterResource("aws:directconnect/connection:Connection", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Connection{s: s}, nil
}

// GetConnection gets an existing Connection resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetConnection(ctx *pulumi.Context,
	name string, id pulumi.ID, state *ConnectionState, opts ...pulumi.ResourceOpt) (*Connection, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["arn"] = state.Arn
		inputs["awsDevice"] = state.AwsDevice
		inputs["bandwidth"] = state.Bandwidth
		inputs["hasLogicalRedundancy"] = state.HasLogicalRedundancy
		inputs["jumboFrameCapable"] = state.JumboFrameCapable
		inputs["location"] = state.Location
		inputs["name"] = state.Name
		inputs["tags"] = state.Tags
	}
	s, err := ctx.ReadResource("aws:directconnect/connection:Connection", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Connection{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Connection) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Connection) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The ARN of the connection.
func (r *Connection) Arn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["arn"])
}

// The Direct Connect endpoint on which the physical connection terminates.
func (r *Connection) AwsDevice() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["awsDevice"])
}

// The bandwidth of the connection. Available values: 1Gbps, 10Gbps. Case sensitive.
func (r *Connection) Bandwidth() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["bandwidth"])
}

// Indicates whether the connection supports a secondary BGP peer in the same address family (IPv4/IPv6).
func (r *Connection) HasLogicalRedundancy() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["hasLogicalRedundancy"])
}

// Boolean value representing if jumbo frames have been enabled for this connection.
func (r *Connection) JumboFrameCapable() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["jumboFrameCapable"])
}

// The AWS Direct Connect location where the connection is located. See [DescribeLocations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html) for the list of AWS Direct Connect locations. Use `locationCode`.
func (r *Connection) Location() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["location"])
}

// The name of the connection.
func (r *Connection) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// A mapping of tags to assign to the resource.
func (r *Connection) Tags() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["tags"])
}

// Input properties used for looking up and filtering Connection resources.
type ConnectionState struct {
	// The ARN of the connection.
	Arn interface{}
	// The Direct Connect endpoint on which the physical connection terminates.
	AwsDevice interface{}
	// The bandwidth of the connection. Available values: 1Gbps, 10Gbps. Case sensitive.
	Bandwidth interface{}
	// Indicates whether the connection supports a secondary BGP peer in the same address family (IPv4/IPv6).
	HasLogicalRedundancy interface{}
	// Boolean value representing if jumbo frames have been enabled for this connection.
	JumboFrameCapable interface{}
	// The AWS Direct Connect location where the connection is located. See [DescribeLocations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html) for the list of AWS Direct Connect locations. Use `locationCode`.
	Location interface{}
	// The name of the connection.
	Name interface{}
	// A mapping of tags to assign to the resource.
	Tags interface{}
}

// The set of arguments for constructing a Connection resource.
type ConnectionArgs struct {
	// The bandwidth of the connection. Available values: 1Gbps, 10Gbps. Case sensitive.
	Bandwidth interface{}
	// The AWS Direct Connect location where the connection is located. See [DescribeLocations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html) for the list of AWS Direct Connect locations. Use `locationCode`.
	Location interface{}
	// The name of the connection.
	Name interface{}
	// A mapping of tags to assign to the resource.
	Tags interface{}
}
