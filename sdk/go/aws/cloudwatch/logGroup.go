// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package cloudwatch

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a CloudWatch Log Group resource.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudwatch_log_group.html.markdown.
type LogGroup struct {
	s *pulumi.ResourceState
}

// NewLogGroup registers a new resource with the given unique name, arguments, and options.
func NewLogGroup(ctx *pulumi.Context,
	name string, args *LogGroupArgs, opts ...pulumi.ResourceOpt) (*LogGroup, error) {
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["kmsKeyId"] = nil
		inputs["name"] = nil
		inputs["namePrefix"] = nil
		inputs["retentionInDays"] = nil
		inputs["tags"] = nil
	} else {
		inputs["kmsKeyId"] = args.KmsKeyId
		inputs["name"] = args.Name
		inputs["namePrefix"] = args.NamePrefix
		inputs["retentionInDays"] = args.RetentionInDays
		inputs["tags"] = args.Tags
	}
	inputs["arn"] = nil
	s, err := ctx.RegisterResource("aws:cloudwatch/logGroup:LogGroup", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &LogGroup{s: s}, nil
}

// GetLogGroup gets an existing LogGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLogGroup(ctx *pulumi.Context,
	name string, id pulumi.ID, state *LogGroupState, opts ...pulumi.ResourceOpt) (*LogGroup, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["arn"] = state.Arn
		inputs["kmsKeyId"] = state.KmsKeyId
		inputs["name"] = state.Name
		inputs["namePrefix"] = state.NamePrefix
		inputs["retentionInDays"] = state.RetentionInDays
		inputs["tags"] = state.Tags
	}
	s, err := ctx.ReadResource("aws:cloudwatch/logGroup:LogGroup", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &LogGroup{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *LogGroup) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *LogGroup) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The Amazon Resource Name (ARN) specifying the log group.
func (r *LogGroup) Arn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["arn"])
}

// The ARN of the KMS Key to use when encrypting log data. Please note, after the AWS KMS CMK is disassociated from the log group,
// AWS CloudWatch Logs stops encrypting newly ingested data for the log group. All previously ingested data remains encrypted, and AWS CloudWatch Logs requires
// permissions for the CMK whenever the encrypted data is requested.
func (r *LogGroup) KmsKeyId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["kmsKeyId"])
}

func (r *LogGroup) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
func (r *LogGroup) NamePrefix() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["namePrefix"])
}

// Specifies the number of days
// you want to retain log events in the specified log group.
func (r *LogGroup) RetentionInDays() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["retentionInDays"])
}

// A mapping of tags to assign to the resource.
func (r *LogGroup) Tags() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["tags"])
}

// Input properties used for looking up and filtering LogGroup resources.
type LogGroupState struct {
	// The Amazon Resource Name (ARN) specifying the log group.
	Arn interface{}
	// The ARN of the KMS Key to use when encrypting log data. Please note, after the AWS KMS CMK is disassociated from the log group,
	// AWS CloudWatch Logs stops encrypting newly ingested data for the log group. All previously ingested data remains encrypted, and AWS CloudWatch Logs requires
	// permissions for the CMK whenever the encrypted data is requested.
	KmsKeyId interface{}
	Name interface{}
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
	NamePrefix interface{}
	// Specifies the number of days
	// you want to retain log events in the specified log group.
	RetentionInDays interface{}
	// A mapping of tags to assign to the resource.
	Tags interface{}
}

// The set of arguments for constructing a LogGroup resource.
type LogGroupArgs struct {
	// The ARN of the KMS Key to use when encrypting log data. Please note, after the AWS KMS CMK is disassociated from the log group,
	// AWS CloudWatch Logs stops encrypting newly ingested data for the log group. All previously ingested data remains encrypted, and AWS CloudWatch Logs requires
	// permissions for the CMK whenever the encrypted data is requested.
	KmsKeyId interface{}
	Name interface{}
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
	NamePrefix interface{}
	// Specifies the number of days
	// you want to retain log events in the specified log group.
	RetentionInDays interface{}
	// A mapping of tags to assign to the resource.
	Tags interface{}
}
