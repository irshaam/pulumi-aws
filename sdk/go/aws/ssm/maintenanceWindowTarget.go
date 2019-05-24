// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ssm

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides an SSM Maintenance Window Target resource
type MaintenanceWindowTarget struct {
	s *pulumi.ResourceState
}

// NewMaintenanceWindowTarget registers a new resource with the given unique name, arguments, and options.
func NewMaintenanceWindowTarget(ctx *pulumi.Context,
	name string, args *MaintenanceWindowTargetArgs, opts ...pulumi.ResourceOpt) (*MaintenanceWindowTarget, error) {
	if args == nil || args.ResourceType == nil {
		return nil, errors.New("missing required argument 'ResourceType'")
	}
	if args == nil || args.Targets == nil {
		return nil, errors.New("missing required argument 'Targets'")
	}
	if args == nil || args.WindowId == nil {
		return nil, errors.New("missing required argument 'WindowId'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["description"] = nil
		inputs["name"] = nil
		inputs["ownerInformation"] = nil
		inputs["resourceType"] = nil
		inputs["targets"] = nil
		inputs["windowId"] = nil
	} else {
		inputs["description"] = args.Description
		inputs["name"] = args.Name
		inputs["ownerInformation"] = args.OwnerInformation
		inputs["resourceType"] = args.ResourceType
		inputs["targets"] = args.Targets
		inputs["windowId"] = args.WindowId
	}
	s, err := ctx.RegisterResource("aws:ssm/maintenanceWindowTarget:MaintenanceWindowTarget", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &MaintenanceWindowTarget{s: s}, nil
}

// GetMaintenanceWindowTarget gets an existing MaintenanceWindowTarget resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetMaintenanceWindowTarget(ctx *pulumi.Context,
	name string, id pulumi.ID, state *MaintenanceWindowTargetState, opts ...pulumi.ResourceOpt) (*MaintenanceWindowTarget, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["description"] = state.Description
		inputs["name"] = state.Name
		inputs["ownerInformation"] = state.OwnerInformation
		inputs["resourceType"] = state.ResourceType
		inputs["targets"] = state.Targets
		inputs["windowId"] = state.WindowId
	}
	s, err := ctx.ReadResource("aws:ssm/maintenanceWindowTarget:MaintenanceWindowTarget", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &MaintenanceWindowTarget{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *MaintenanceWindowTarget) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *MaintenanceWindowTarget) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The description of the maintenance window target.
func (r *MaintenanceWindowTarget) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

// The name of the maintenance window target.
func (r *MaintenanceWindowTarget) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.
func (r *MaintenanceWindowTarget) OwnerInformation() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["ownerInformation"])
}

// The type of target being registered with the Maintenance Window. Possible values `INSTANCE`.
func (r *MaintenanceWindowTarget) ResourceType() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["resourceType"])
}

// The targets (either instances or tags). Instances are specified using Key=instanceids,Values=instanceid1,instanceid2. Tags are specified using Key=tag name,Values=tag value.
func (r *MaintenanceWindowTarget) Targets() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["targets"])
}

// The Id of the maintenance window to register the target with.
func (r *MaintenanceWindowTarget) WindowId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["windowId"])
}

// Input properties used for looking up and filtering MaintenanceWindowTarget resources.
type MaintenanceWindowTargetState struct {
	// The description of the maintenance window target.
	Description interface{}
	// The name of the maintenance window target.
	Name interface{}
	// User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.
	OwnerInformation interface{}
	// The type of target being registered with the Maintenance Window. Possible values `INSTANCE`.
	ResourceType interface{}
	// The targets (either instances or tags). Instances are specified using Key=instanceids,Values=instanceid1,instanceid2. Tags are specified using Key=tag name,Values=tag value.
	Targets interface{}
	// The Id of the maintenance window to register the target with.
	WindowId interface{}
}

// The set of arguments for constructing a MaintenanceWindowTarget resource.
type MaintenanceWindowTargetArgs struct {
	// The description of the maintenance window target.
	Description interface{}
	// The name of the maintenance window target.
	Name interface{}
	// User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.
	OwnerInformation interface{}
	// The type of target being registered with the Maintenance Window. Possible values `INSTANCE`.
	ResourceType interface{}
	// The targets (either instances or tags). Instances are specified using Key=instanceids,Values=instanceid1,instanceid2. Tags are specified using Key=tag name,Values=tag value.
	Targets interface{}
	// The Id of the maintenance window to register the target with.
	WindowId interface{}
}
