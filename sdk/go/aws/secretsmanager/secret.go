// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package secretsmanager

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a resource to manage AWS Secrets Manager secret metadata. To manage a secret value, see the [`aws_secretsmanager_secret_version` resource](https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_version.html).
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/secretsmanager_secret.html.markdown.
type Secret struct {
	s *pulumi.ResourceState
}

// NewSecret registers a new resource with the given unique name, arguments, and options.
func NewSecret(ctx *pulumi.Context,
	name string, args *SecretArgs, opts ...pulumi.ResourceOpt) (*Secret, error) {
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["description"] = nil
		inputs["kmsKeyId"] = nil
		inputs["name"] = nil
		inputs["namePrefix"] = nil
		inputs["policy"] = nil
		inputs["recoveryWindowInDays"] = nil
		inputs["rotationLambdaArn"] = nil
		inputs["rotationRules"] = nil
		inputs["tags"] = nil
	} else {
		inputs["description"] = args.Description
		inputs["kmsKeyId"] = args.KmsKeyId
		inputs["name"] = args.Name
		inputs["namePrefix"] = args.NamePrefix
		inputs["policy"] = args.Policy
		inputs["recoveryWindowInDays"] = args.RecoveryWindowInDays
		inputs["rotationLambdaArn"] = args.RotationLambdaArn
		inputs["rotationRules"] = args.RotationRules
		inputs["tags"] = args.Tags
	}
	inputs["arn"] = nil
	inputs["rotationEnabled"] = nil
	s, err := ctx.RegisterResource("aws:secretsmanager/secret:Secret", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Secret{s: s}, nil
}

// GetSecret gets an existing Secret resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSecret(ctx *pulumi.Context,
	name string, id pulumi.ID, state *SecretState, opts ...pulumi.ResourceOpt) (*Secret, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["arn"] = state.Arn
		inputs["description"] = state.Description
		inputs["kmsKeyId"] = state.KmsKeyId
		inputs["name"] = state.Name
		inputs["namePrefix"] = state.NamePrefix
		inputs["policy"] = state.Policy
		inputs["recoveryWindowInDays"] = state.RecoveryWindowInDays
		inputs["rotationEnabled"] = state.RotationEnabled
		inputs["rotationLambdaArn"] = state.RotationLambdaArn
		inputs["rotationRules"] = state.RotationRules
		inputs["tags"] = state.Tags
	}
	s, err := ctx.ReadResource("aws:secretsmanager/secret:Secret", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Secret{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Secret) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Secret) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// Amazon Resource Name (ARN) of the secret.
func (r *Secret) Arn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["arn"])
}

// A description of the secret.
func (r *Secret) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

// Specifies the ARN or alias of the AWS KMS customer master key (CMK) to be used to encrypt the secret values in the versions stored in this secret. If you don't specify this value, then Secrets Manager defaults to using the AWS account's default CMK (the one named `aws/secretsmanager`). If the default KMS CMK with that name doesn't yet exist, then AWS Secrets Manager creates it for you automatically the first time.
func (r *Secret) KmsKeyId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["kmsKeyId"])
}

// Specifies the friendly name of the new secret. The secret name can consist of uppercase letters, lowercase letters, digits, and any of the following characters: `/_+=.@-` Conflicts with `name_prefix`.
func (r *Secret) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
func (r *Secret) NamePrefix() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["namePrefix"])
}

func (r *Secret) Policy() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["policy"])
}

// Specifies the number of days that AWS Secrets Manager waits before it can delete the secret. This value can be `0` to force deletion without recovery or range from `7` to `30` days. The default value is `30`.
func (r *Secret) RecoveryWindowInDays() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["recoveryWindowInDays"])
}

// Specifies whether automatic rotation is enabled for this secret.
func (r *Secret) RotationEnabled() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["rotationEnabled"])
}

// Specifies the ARN of the Lambda function that can rotate the secret.
func (r *Secret) RotationLambdaArn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["rotationLambdaArn"])
}

// A structure that defines the rotation configuration for this secret. Defined below.
func (r *Secret) RotationRules() *pulumi.Output {
	return r.s.State["rotationRules"]
}

// Specifies a key-value map of user-defined tags that are attached to the secret.
func (r *Secret) Tags() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["tags"])
}

// Input properties used for looking up and filtering Secret resources.
type SecretState struct {
	// Amazon Resource Name (ARN) of the secret.
	Arn interface{}
	// A description of the secret.
	Description interface{}
	// Specifies the ARN or alias of the AWS KMS customer master key (CMK) to be used to encrypt the secret values in the versions stored in this secret. If you don't specify this value, then Secrets Manager defaults to using the AWS account's default CMK (the one named `aws/secretsmanager`). If the default KMS CMK with that name doesn't yet exist, then AWS Secrets Manager creates it for you automatically the first time.
	KmsKeyId interface{}
	// Specifies the friendly name of the new secret. The secret name can consist of uppercase letters, lowercase letters, digits, and any of the following characters: `/_+=.@-` Conflicts with `name_prefix`.
	Name interface{}
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
	NamePrefix interface{}
	Policy interface{}
	// Specifies the number of days that AWS Secrets Manager waits before it can delete the secret. This value can be `0` to force deletion without recovery or range from `7` to `30` days. The default value is `30`.
	RecoveryWindowInDays interface{}
	// Specifies whether automatic rotation is enabled for this secret.
	RotationEnabled interface{}
	// Specifies the ARN of the Lambda function that can rotate the secret.
	RotationLambdaArn interface{}
	// A structure that defines the rotation configuration for this secret. Defined below.
	RotationRules interface{}
	// Specifies a key-value map of user-defined tags that are attached to the secret.
	Tags interface{}
}

// The set of arguments for constructing a Secret resource.
type SecretArgs struct {
	// A description of the secret.
	Description interface{}
	// Specifies the ARN or alias of the AWS KMS customer master key (CMK) to be used to encrypt the secret values in the versions stored in this secret. If you don't specify this value, then Secrets Manager defaults to using the AWS account's default CMK (the one named `aws/secretsmanager`). If the default KMS CMK with that name doesn't yet exist, then AWS Secrets Manager creates it for you automatically the first time.
	KmsKeyId interface{}
	// Specifies the friendly name of the new secret. The secret name can consist of uppercase letters, lowercase letters, digits, and any of the following characters: `/_+=.@-` Conflicts with `name_prefix`.
	Name interface{}
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
	NamePrefix interface{}
	Policy interface{}
	// Specifies the number of days that AWS Secrets Manager waits before it can delete the secret. This value can be `0` to force deletion without recovery or range from `7` to `30` days. The default value is `30`.
	RecoveryWindowInDays interface{}
	// Specifies the ARN of the Lambda function that can rotate the secret.
	RotationLambdaArn interface{}
	// A structure that defines the rotation configuration for this secret. Defined below.
	RotationRules interface{}
	// Specifies a key-value map of user-defined tags that are attached to the secret.
	Tags interface{}
}
