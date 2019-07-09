// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package directconnect

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a Direct Connect hosted private virtual interface resource. This resource represents the allocator's side of the hosted virtual interface.
// A hosted virtual interface is a virtual interface that is owned by another AWS account.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dx_hosted_private_virtual_interface.html.markdown.
type HostedPrivateVirtualInterface struct {
	s *pulumi.ResourceState
}

// NewHostedPrivateVirtualInterface registers a new resource with the given unique name, arguments, and options.
func NewHostedPrivateVirtualInterface(ctx *pulumi.Context,
	name string, args *HostedPrivateVirtualInterfaceArgs, opts ...pulumi.ResourceOpt) (*HostedPrivateVirtualInterface, error) {
	if args == nil || args.AddressFamily == nil {
		return nil, errors.New("missing required argument 'AddressFamily'")
	}
	if args == nil || args.BgpAsn == nil {
		return nil, errors.New("missing required argument 'BgpAsn'")
	}
	if args == nil || args.ConnectionId == nil {
		return nil, errors.New("missing required argument 'ConnectionId'")
	}
	if args == nil || args.OwnerAccountId == nil {
		return nil, errors.New("missing required argument 'OwnerAccountId'")
	}
	if args == nil || args.Vlan == nil {
		return nil, errors.New("missing required argument 'Vlan'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["addressFamily"] = nil
		inputs["amazonAddress"] = nil
		inputs["bgpAsn"] = nil
		inputs["bgpAuthKey"] = nil
		inputs["connectionId"] = nil
		inputs["customerAddress"] = nil
		inputs["mtu"] = nil
		inputs["name"] = nil
		inputs["ownerAccountId"] = nil
		inputs["vlan"] = nil
	} else {
		inputs["addressFamily"] = args.AddressFamily
		inputs["amazonAddress"] = args.AmazonAddress
		inputs["bgpAsn"] = args.BgpAsn
		inputs["bgpAuthKey"] = args.BgpAuthKey
		inputs["connectionId"] = args.ConnectionId
		inputs["customerAddress"] = args.CustomerAddress
		inputs["mtu"] = args.Mtu
		inputs["name"] = args.Name
		inputs["ownerAccountId"] = args.OwnerAccountId
		inputs["vlan"] = args.Vlan
	}
	inputs["arn"] = nil
	inputs["awsDevice"] = nil
	inputs["jumboFrameCapable"] = nil
	s, err := ctx.RegisterResource("aws:directconnect/hostedPrivateVirtualInterface:HostedPrivateVirtualInterface", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &HostedPrivateVirtualInterface{s: s}, nil
}

// GetHostedPrivateVirtualInterface gets an existing HostedPrivateVirtualInterface resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetHostedPrivateVirtualInterface(ctx *pulumi.Context,
	name string, id pulumi.ID, state *HostedPrivateVirtualInterfaceState, opts ...pulumi.ResourceOpt) (*HostedPrivateVirtualInterface, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["addressFamily"] = state.AddressFamily
		inputs["amazonAddress"] = state.AmazonAddress
		inputs["arn"] = state.Arn
		inputs["awsDevice"] = state.AwsDevice
		inputs["bgpAsn"] = state.BgpAsn
		inputs["bgpAuthKey"] = state.BgpAuthKey
		inputs["connectionId"] = state.ConnectionId
		inputs["customerAddress"] = state.CustomerAddress
		inputs["jumboFrameCapable"] = state.JumboFrameCapable
		inputs["mtu"] = state.Mtu
		inputs["name"] = state.Name
		inputs["ownerAccountId"] = state.OwnerAccountId
		inputs["vlan"] = state.Vlan
	}
	s, err := ctx.ReadResource("aws:directconnect/hostedPrivateVirtualInterface:HostedPrivateVirtualInterface", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &HostedPrivateVirtualInterface{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *HostedPrivateVirtualInterface) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *HostedPrivateVirtualInterface) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The address family for the BGP peer. `ipv4 ` or `ipv6`.
func (r *HostedPrivateVirtualInterface) AddressFamily() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["addressFamily"])
}

// The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.
func (r *HostedPrivateVirtualInterface) AmazonAddress() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["amazonAddress"])
}

// The ARN of the virtual interface.
func (r *HostedPrivateVirtualInterface) Arn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["arn"])
}

// The Direct Connect endpoint on which the virtual interface terminates.
func (r *HostedPrivateVirtualInterface) AwsDevice() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["awsDevice"])
}

// The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
func (r *HostedPrivateVirtualInterface) BgpAsn() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["bgpAsn"])
}

// The authentication key for BGP configuration.
func (r *HostedPrivateVirtualInterface) BgpAuthKey() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["bgpAuthKey"])
}

// The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.
func (r *HostedPrivateVirtualInterface) ConnectionId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["connectionId"])
}

// The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.
func (r *HostedPrivateVirtualInterface) CustomerAddress() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["customerAddress"])
}

// Indicates whether jumbo frames (9001 MTU) are supported.
func (r *HostedPrivateVirtualInterface) JumboFrameCapable() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["jumboFrameCapable"])
}

// The maximum transmission unit (MTU) is the size, in bytes, of the largest permissible packet that can be passed over the connection. The MTU of a virtual private interface can be either `1500` or `9001` (jumbo frames). Default is `1500`.
func (r *HostedPrivateVirtualInterface) Mtu() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["mtu"])
}

// The name for the virtual interface.
func (r *HostedPrivateVirtualInterface) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The AWS account that will own the new virtual interface.
func (r *HostedPrivateVirtualInterface) OwnerAccountId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["ownerAccountId"])
}

// The VLAN ID.
func (r *HostedPrivateVirtualInterface) Vlan() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["vlan"])
}

// Input properties used for looking up and filtering HostedPrivateVirtualInterface resources.
type HostedPrivateVirtualInterfaceState struct {
	// The address family for the BGP peer. `ipv4 ` or `ipv6`.
	AddressFamily interface{}
	// The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.
	AmazonAddress interface{}
	// The ARN of the virtual interface.
	Arn interface{}
	// The Direct Connect endpoint on which the virtual interface terminates.
	AwsDevice interface{}
	// The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
	BgpAsn interface{}
	// The authentication key for BGP configuration.
	BgpAuthKey interface{}
	// The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.
	ConnectionId interface{}
	// The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.
	CustomerAddress interface{}
	// Indicates whether jumbo frames (9001 MTU) are supported.
	JumboFrameCapable interface{}
	// The maximum transmission unit (MTU) is the size, in bytes, of the largest permissible packet that can be passed over the connection. The MTU of a virtual private interface can be either `1500` or `9001` (jumbo frames). Default is `1500`.
	Mtu interface{}
	// The name for the virtual interface.
	Name interface{}
	// The AWS account that will own the new virtual interface.
	OwnerAccountId interface{}
	// The VLAN ID.
	Vlan interface{}
}

// The set of arguments for constructing a HostedPrivateVirtualInterface resource.
type HostedPrivateVirtualInterfaceArgs struct {
	// The address family for the BGP peer. `ipv4 ` or `ipv6`.
	AddressFamily interface{}
	// The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.
	AmazonAddress interface{}
	// The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
	BgpAsn interface{}
	// The authentication key for BGP configuration.
	BgpAuthKey interface{}
	// The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.
	ConnectionId interface{}
	// The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.
	CustomerAddress interface{}
	// The maximum transmission unit (MTU) is the size, in bytes, of the largest permissible packet that can be passed over the connection. The MTU of a virtual private interface can be either `1500` or `9001` (jumbo frames). Default is `1500`.
	Mtu interface{}
	// The name for the virtual interface.
	Name interface{}
	// The AWS account that will own the new virtual interface.
	OwnerAccountId interface{}
	// The VLAN ID.
	Vlan interface{}
}
