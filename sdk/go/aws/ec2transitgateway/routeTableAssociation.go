// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2transitgateway

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages an EC2 Transit Gateway Route Table association.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ec2_transit_gateway_route_table_association.html.markdown.
type RouteTableAssociation struct {
	s *pulumi.ResourceState
}

// NewRouteTableAssociation registers a new resource with the given unique name, arguments, and options.
func NewRouteTableAssociation(ctx *pulumi.Context,
	name string, args *RouteTableAssociationArgs, opts ...pulumi.ResourceOpt) (*RouteTableAssociation, error) {
	if args == nil || args.TransitGatewayAttachmentId == nil {
		return nil, errors.New("missing required argument 'TransitGatewayAttachmentId'")
	}
	if args == nil || args.TransitGatewayRouteTableId == nil {
		return nil, errors.New("missing required argument 'TransitGatewayRouteTableId'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["transitGatewayAttachmentId"] = nil
		inputs["transitGatewayRouteTableId"] = nil
	} else {
		inputs["transitGatewayAttachmentId"] = args.TransitGatewayAttachmentId
		inputs["transitGatewayRouteTableId"] = args.TransitGatewayRouteTableId
	}
	inputs["resourceId"] = nil
	inputs["resourceType"] = nil
	s, err := ctx.RegisterResource("aws:ec2transitgateway/routeTableAssociation:RouteTableAssociation", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &RouteTableAssociation{s: s}, nil
}

// GetRouteTableAssociation gets an existing RouteTableAssociation resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRouteTableAssociation(ctx *pulumi.Context,
	name string, id pulumi.ID, state *RouteTableAssociationState, opts ...pulumi.ResourceOpt) (*RouteTableAssociation, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["resourceId"] = state.ResourceId
		inputs["resourceType"] = state.ResourceType
		inputs["transitGatewayAttachmentId"] = state.TransitGatewayAttachmentId
		inputs["transitGatewayRouteTableId"] = state.TransitGatewayRouteTableId
	}
	s, err := ctx.ReadResource("aws:ec2transitgateway/routeTableAssociation:RouteTableAssociation", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &RouteTableAssociation{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *RouteTableAssociation) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *RouteTableAssociation) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// Identifier of the resource
func (r *RouteTableAssociation) ResourceId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["resourceId"])
}

// Type of the resource
func (r *RouteTableAssociation) ResourceType() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["resourceType"])
}

// Identifier of EC2 Transit Gateway Attachment.
func (r *RouteTableAssociation) TransitGatewayAttachmentId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["transitGatewayAttachmentId"])
}

// Identifier of EC2 Transit Gateway Route Table.
func (r *RouteTableAssociation) TransitGatewayRouteTableId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["transitGatewayRouteTableId"])
}

// Input properties used for looking up and filtering RouteTableAssociation resources.
type RouteTableAssociationState struct {
	// Identifier of the resource
	ResourceId interface{}
	// Type of the resource
	ResourceType interface{}
	// Identifier of EC2 Transit Gateway Attachment.
	TransitGatewayAttachmentId interface{}
	// Identifier of EC2 Transit Gateway Route Table.
	TransitGatewayRouteTableId interface{}
}

// The set of arguments for constructing a RouteTableAssociation resource.
type RouteTableAssociationArgs struct {
	// Identifier of EC2 Transit Gateway Attachment.
	TransitGatewayAttachmentId interface{}
	// Identifier of EC2 Transit Gateway Route Table.
	TransitGatewayRouteTableId interface{}
}
