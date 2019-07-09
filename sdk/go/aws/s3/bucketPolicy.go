// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package s3

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Attaches a policy to an S3 bucket resource.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_policy.html.markdown.
type BucketPolicy struct {
	s *pulumi.ResourceState
}

// NewBucketPolicy registers a new resource with the given unique name, arguments, and options.
func NewBucketPolicy(ctx *pulumi.Context,
	name string, args *BucketPolicyArgs, opts ...pulumi.ResourceOpt) (*BucketPolicy, error) {
	if args == nil || args.Bucket == nil {
		return nil, errors.New("missing required argument 'Bucket'")
	}
	if args == nil || args.Policy == nil {
		return nil, errors.New("missing required argument 'Policy'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["bucket"] = nil
		inputs["policy"] = nil
	} else {
		inputs["bucket"] = args.Bucket
		inputs["policy"] = args.Policy
	}
	s, err := ctx.RegisterResource("aws:s3/bucketPolicy:BucketPolicy", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &BucketPolicy{s: s}, nil
}

// GetBucketPolicy gets an existing BucketPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetBucketPolicy(ctx *pulumi.Context,
	name string, id pulumi.ID, state *BucketPolicyState, opts ...pulumi.ResourceOpt) (*BucketPolicy, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["bucket"] = state.Bucket
		inputs["policy"] = state.Policy
	}
	s, err := ctx.ReadResource("aws:s3/bucketPolicy:BucketPolicy", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &BucketPolicy{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *BucketPolicy) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *BucketPolicy) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The name of the bucket to which to apply the policy.
func (r *BucketPolicy) Bucket() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["bucket"])
}

func (r *BucketPolicy) Policy() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["policy"])
}

// Input properties used for looking up and filtering BucketPolicy resources.
type BucketPolicyState struct {
	// The name of the bucket to which to apply the policy.
	Bucket interface{}
	Policy interface{}
}

// The set of arguments for constructing a BucketPolicy resource.
type BucketPolicyArgs struct {
	// The name of the bucket to which to apply the policy.
	Bucket interface{}
	Policy interface{}
}
